"""
Implementation of GEDCOM X Date Format Specification.
https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md
"""
from typing import Optional

import pendulum
from dateutil.rrule import rrule
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
