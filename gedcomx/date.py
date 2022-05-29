"""
Implementation of GEDCOM X Date Format Specification.
https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md
"""
import re
from typing import TYPE_CHECKING

import lark
import pendulum
from lark.exceptions import UnexpectedCharacters, UnexpectedEOF
from pendulum.parsing import ParserError

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator

date_pattern = re.compile(
    # slightly against specs core, but respects examples from specs (sic!)
    r"""
    ^
    (
        (?P<approx>A?)
        (?P<year>[-+]\d{4})
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
                        [-+]\d{2}
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
    ((?P<years>\d+)Y)?
    ((?P<months>\d+)M)?
    ((?P<days>\d+)D)?
    (
        T
        ((?P<hours>\d+)H)?
        ((?P<minutes>\d+)M)?
        ((?P<seconds>\d+)S)?
    )?
    $
    """,
    re.X,
)
date_grammar = r"""
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
date_preparser = lark.Lark(date_grammar)


class DateFormat(str):
    """
    At the moment it's only a validator. TODO: convert from datetime objects.
    """

    def __init__(self, value: str):
        try:
            # this makes most of the checks
            parse_tree = date_preparser.parse(value)
            # for dates, we need another sanity check
            token: lark.Token
            for token in parse_tree.scan_values(lambda v: v.type == "SIMPLE_DATE"):
                self._validate_date_format(token.value)
        except (
            UnexpectedCharacters,
            UnexpectedEOF,
            AssertionError,
            TypeError,
            ParserError,
        ):
            raise ValueError("invalid date format")

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        yield cls

    @staticmethod
    def _validate_date_format(value: str) -> None:
        # Pendulum counts years from 1CE onward, so we need this hack to
        # have proper handling of year 0000 (1BCE) which is a leap year
        # in proleptic Gregorian calendar.
        if value[1:5] == "0000":
            value = f"+2000{value[5:]}"
        pendulum.parse(value[1:])
