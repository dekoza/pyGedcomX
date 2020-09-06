"""
Implementation of GEDCOM X Date Format Specification.
https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md
"""
from typing import Optional

import pendulum
from dateutil.rrule import rrule
from pydantic import BaseModel


class DateFormat(BaseModel):
    pass


class Date(BaseModel):
    original: Optional[str]
    formal: Optional[DateFormat]
