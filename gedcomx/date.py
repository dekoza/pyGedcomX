"""
Implementation of GEDCOM X Date Format Specification.
https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md
"""
import re
from typing import Optional

from lark.exceptions import UnexpectedCharacters, UnexpectedEOF
from pydantic import BaseModel

from .parsers import date_preparser, duration_pattern


class TimeZone(BaseModel):
    hours: int
    minutes: Optional[int] = 0


class SimpleDate(BaseModel):
    year: int
    month: Optional[int]
    day: Optional[int]
    hour: Optional[int]
    minute: Optional[int]
    second: Optional[int]
    timezone: Optional[TimeZone]


class Duration(BaseModel):
    years: Optional[int]
    months: Optional[int]
    days: Optional[int]
    hours: Optional[int]
    minutes: Optional[int]
    seconds: Optional[int]


class ApproxDate(SimpleDate):
    approx: Optional[bool] = False


class DateRange(BaseModel):
    approx: Optional[bool] = False
    start_date: Optional[SimpleDate]
    end_date: Optional[SimpleDate]
    # TODO: specs allow duration but it can be just used to calculate end_date
    duration: Optional[Duration]


class Recurrence(DateRange):
    repetitions: Optional[int]


class DateFormat:
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        try:
            parse_tree = date_preparser.parse(value)
            for subtree in parse_tree.iter_subtrees():
                for node in subtree.children:
                    if getattr(node, "type", None) is not None:
                        # TODO: check if pendulum accepts the date
                        if node.type == "DURATION":
                            assert re.match(duration_pattern, node.value)
        except (UnexpectedCharacters, UnexpectedEOF, AssertionError, TypeError):
            raise ValueError("invalid date format")
        return value
