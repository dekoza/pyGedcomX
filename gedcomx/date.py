"""
Implementation of GEDCOM X Date Format Specification.
https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md
"""
from typing import Optional

import pendulum
from dateutil.rrule import rrule
from lark import Lark
from pydantic import BaseModel


class DateFormat:
    def __init__(self, value):
        self.validate(value)

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        return value


date_pattern = r"""
    ^
    (
        (?P<approx>A?)
        (?P<sign>[\+-])
        (?P<year>\d{4})
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
                    )?
                )?
            )?
        )?
    )?
    $"""


grammar = r"""

start: date_format

date_format: simple_date
           | approx
           | (closed_date_range|open_date_range)
           | recurring

simple_date: /[\+-]\d{4}(-\d{2}(-\d{2}(T\d{2}(:\d{2}(:\d{1,2})?)?([\+-]\d{2}(:\d{2})?)?)?)?)?/

duration: /P.+/

closed_date_range: simple_date "/" simple_date
                  | simple_date "/" duration
open_date_range: simple_date "/"
               | "/" simple_date

approx: "A" simple_date
      | "A" (closed_date_range|open_date_range)

recurring: "R" closed_date_range
         | "R" NUMBER closed_date_range

NUMBER: DIGIT+

%import common.DIGIT
"""
