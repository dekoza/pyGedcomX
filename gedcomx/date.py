"""
Implementation of GEDCOM X Date Format Specification.
https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md
"""
from typing import Optional

import pendulum
from lark.exceptions import UnexpectedCharacters, UnexpectedEOF
from pydantic import BaseModel

from .utils import date_preparser


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


class DateFormat(str):
    """
    Please note that GEDCOM X uses ISO 8601:2004 (aka astronomical) notation
    which means that the year 1 BCE is written as "+0000".
    See: http://dotat.at/tmp/ISO_8601-2004_E.pdf
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @staticmethod
    def _check_with_pendulum(value: str) -> None:
        # Pendulum counts years from 1CE onward so we need this hack to
        # have proper handling of year 0000 (1BCE) which is a leap year
        # in proleptic Gregorian calendar.
        if value[1:5] == "0000":
            value = f"+2000{value[5:]}"
        pendulum.parse(value[1:])

    @classmethod
    def validate(cls, value: str):
        try:
            parse_tree = date_preparser.parse(value)
            for subtree in parse_tree.iter_subtrees():
                for node in subtree.children:
                    if getattr(node, "type", None) is not None:
                        # At this point lark has proven that duration is OK and
                        # the date looks kinda OK. Let's use pendulum to be sure.
                        if node.type == "SIMPLE_DATE":
                            cls._check_with_pendulum(node.value)
        except (UnexpectedCharacters, UnexpectedEOF, AssertionError, TypeError):
            raise ValueError("invalid date format")
        return cls(value)
