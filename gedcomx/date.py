"""
Implementation of GEDCOM X Date Format Specification.
https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md
"""
from datetime import datetime
from typing import Optional, Union

import pendulum
from lark.tree import Tree
from pydantic import BaseModel

from .parsers import date_pattern, date_preparser


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
    def __init__(self, value: Union[datetime, str, Tree]) -> None:
        if not isinstance(value, Tree):
            value = self.validate(value)

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        parse_tree = date_preparser(value)
        return value
