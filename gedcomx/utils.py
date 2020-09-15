# flake8: noqa
import re
import xml.etree.ElementTree as ET
from collections.abc import Mapping

import lark


def xmlize(obj):
    if hasattr(obj, "xml"):
        return obj.xml()
    tag = obj.__class__.__name__
    e = ET.Element(tag)


date_pattern = re.compile(
    # against specs core, but respects examples from specs
    r"""
    ^
    (
        (?P<approx>A?)
        (?P<year>[\+-]\d{4})
        (
            -
            (?P<month>\d{2})
            (
                -
                (?P<day>\d{2})
                (
                    T
                    (?P<hour>\d{2})
                    (
                        :
                        (?P<minute>\d{2})
                        (
                            :
                            (?P<second>\d{1,2})
                        )?
                    )?
                    (?P<tz>
                        [\+-]\d{2}
                        (:\d{2})?
                        | Z
                    )?
                )?
            )?
        )?
    )?
    $""",
    re.X,
)

duration_pattern = re.compile(
    # This pattern is broader than original specification.
    # Values not conforming to specs (for example "1000 seconds")
    # should be recalculated during parsing (using pendulum)
    # and returned in canonical form.
    r"""
    ^
    P
    (?P<years>\d+Y)?
    (?P<months>\d+M)?
    (?P<days>\d+D)?
    (
        T
        (?P<hours>\d+H)?
        (?P<minutes>\d+M)?
        (?P<seconds>\d+S)?
    )?
    $
    """,
    re.X,
)

grammar = r"""
start: date_format
date_format: SIMPLE_DATE
           | approx
           | closed_date_range
           | open_date_range
           | recurring
SIMPLE_DATE: /[\+-]\d{4}(-\d{2}(-\d{2}(T\d{2}(:\d{2}(:\d{1,2})?)?([\+-]\d{2}(:\d{2})?|Z)?)?)?)?/
DURATION: /P(\d+Y)?(\d+M)?(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?)?/
closed_date_range: SIMPLE_DATE "/" SIMPLE_DATE
                  | SIMPLE_DATE "/" DURATION
open_date_range: SIMPLE_DATE "/"
               | "/" SIMPLE_DATE
approx: "A" (SIMPLE_DATE|closed_date_range|open_date_range)
recurring: "R/" closed_date_range
         | "R" COUNT "/" closed_date_range
COUNT: DIGIT+
%import common.DIGIT
"""

date_preparser = lark.Lark(grammar)


class MultiValueDictKeyError(KeyError):
    pass


class MultiValueDict(dict):
    """
    Ripped from Django.
    A subclass of dictionary customized to handle multiple values for the
    same key.

    >>> d = MultiValueDict({'name': ['Adrian', 'Simon'], 'position': ['Developer']})
    >>> d['name']
    'Simon'
    >>> d.getlist('name')
    ['Adrian', 'Simon']
    >>> d.getlist('doesnotexist')
    []
    >>> d.getlist('doesnotexist', ['Adrian', 'Simon'])
    ['Adrian', 'Simon']
    >>> d.get('lastname', 'nonexistent')
    'nonexistent'
    >>> d.setlist('lastname', ['Holovaty', 'Willison'])

    This class exists to solve the irritating problem raised by cgi.parse_qs,
    which returns a list for every key, even though most Web forms submit
    single name-value pairs.
    """

    def __init__(self, key_to_list_mapping=()):
        super().__init__(key_to_list_mapping)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__, super().__repr__())

    def __getitem__(self, key):
        """
        Return the last data value for this key, or [] if it's an empty list;
        raise KeyError if not found.
        """
        try:
            list_ = super().__getitem__(key)
        except KeyError:
            raise MultiValueDictKeyError(key)
        try:
            return list_[-1]
        except IndexError:
            return []

    def __setitem__(self, key, value):
        super().__setitem__(key, [value])

    def __copy__(self):
        return self.__class__([(k, v[:]) for k, v in self.lists()])

    def __deepcopy__(self, memo):
        result = self.__class__()
        memo[id(self)] = result
        for key, value in dict.items(self):
            dict.__setitem__(
                result, copy.deepcopy(key, memo), copy.deepcopy(value, memo)
            )
        return result

    def __getstate__(self):
        return {**self.__dict__, "_data": {k: self._getlist(k) for k in self}}

    def __setstate__(self, obj_dict):
        data = obj_dict.pop("_data", {})
        for k, v in data.items():
            self.setlist(k, v)
        self.__dict__.update(obj_dict)

    def get(self, key, default=None):
        """
        Return the last data value for the passed key. If key doesn't exist
        or value is an empty list, return `default`.
        """
        try:
            val = self[key]
        except KeyError:
            return default
        if val == []:
            return default
        return val

    def _getlist(self, key, default=None, force_list=False):
        """
        Return a list of values for the key.

        Used internally to manipulate values list. If force_list is True,
        return a new copy of values.
        """
        try:
            values = super().__getitem__(key)
        except KeyError:
            if default is None:
                return []
            return default
        else:
            if force_list:
                values = list(values) if values is not None else None
            return values

    def getlist(self, key, default=None):
        """
        Return the list of values for the key. If key doesn't exist, return a
        default value.
        """
        return self._getlist(key, default, force_list=True)

    def setlist(self, key, list_):
        super().__setitem__(key, list_)

    def setdefault(self, key, default=None):
        if key not in self:
            self[key] = default
            # Do not return default here because __setitem__() may store
            # another value -- QueryDict.__setitem__() does. Look it up.
        return self[key]

    def setlistdefault(self, key, default_list=None):
        if key not in self:
            if default_list is None:
                default_list = []
            self.setlist(key, default_list)
            # Do not return default_list here because setlist() may store
            # another value -- QueryDict.setlist() does. Look it up.
        return self._getlist(key)

    def appendlist(self, key, value):
        """Append an item to the internal list associated with key."""
        self.setlistdefault(key).append(value)

    def items(self):
        """
        Yield (key, value) pairs, where value is the last item in the list
        associated with the key.
        """
        for key in self:
            yield key, self[key]

    def lists(self):
        """Yield (key, list) pairs."""
        return iter(super().items())

    def values(self):
        """Yield the last value on every key list."""
        for key in self:
            yield self[key]

    def copy(self):
        """Return a shallow copy of this object."""
        return copy.copy(self)

    def update(self, *args, **kwargs):
        """Extend rather than replace existing key lists."""
        if len(args) > 1:
            raise TypeError("update expected at most 1 argument, got %d" % len(args))
        if args:
            other_dict = args[0]
            if isinstance(other_dict, MultiValueDict):
                for key, value_list in other_dict.lists():
                    self.setlistdefault(key).extend(value_list)
            else:
                try:
                    for key, value in other_dict.items():
                        self.setlistdefault(key).append(value)
                except TypeError:
                    raise ValueError(
                        "MultiValueDict.update() takes either a MultiValueDict or dictionary"
                    )
        for key, value in kwargs.items():
            self.setlistdefault(key).append(value)

    def dict(self):
        """Return current object as a dict with singular values."""
        return {key: self[key] for key in self}


def _destruct_iterable_mapping_values(data):
    for i, elem in enumerate(data):
        if len(elem) != 2:
            raise ValueError(
                "dictionary update sequence element #{} has "
                "length {}; 2 is required.".format(i, len(elem))
            )
        if not isinstance(elem[0], str):
            raise ValueError(
                "Element key %r invalid, only strings are allowed" % elem[0]
            )
        yield tuple(elem)


class CaseInsensitiveMapping(Mapping):
    """
    Ripped from Django.
    Mapping allowing case-insensitive key lookups. Original case of keys is
    preserved for iteration and string representation.

    Example::

        >>> ci_map = CaseInsensitiveMapping({'name': 'Jane'})
        >>> ci_map['Name']
        Jane
        >>> ci_map['NAME']
        Jane
        >>> ci_map['name']
        Jane
        >>> ci_map  # original case preserved
        {'name': 'Jane'}
    """

    def __init__(self, data):
        if not isinstance(data, Mapping):
            data = {k: v for k, v in _destruct_iterable_mapping_values(data)}
        self._store = {k.lower(): (k, v) for k, v in data.items()}

    def __getitem__(self, key):
        return self._store[key.lower()][1]

    def __len__(self):
        return len(self._store)

    def __eq__(self, other):
        return isinstance(other, Mapping) and {
            k.lower(): v for k, v in self.items()
        } == {k.lower(): v for k, v in other.items()}

    def __iter__(self):
        return (original_key for original_key, value in self._store.values())

    def __repr__(self):
        return repr({key: value for key, value in self._store.values()})

    def copy(self):
        return self
