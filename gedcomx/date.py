"""
Implementation of GEDCOM X Date Format Specification.
https://github.com/FamilySearch/gedcomx/blob/master/specifications/date-format-specification.md
"""
from typing import TYPE_CHECKING

import pendulum
from lark.exceptions import UnexpectedCharacters, UnexpectedEOF
from pendulum.parsing import ParserError

from .utils import date_preparser

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


class DateFormat(str):
    """
    At the moment it's only a validator. TODO: convert from datetime objects.
    """

    def __init__(self, value: str):
        try:
            # this makes most of the checks
            parse_tree = date_preparser.parse(value)
            # for dates, we need another sanity check
            for token in parse_tree.scan_values(lambda v: v.type == "SIMPLE_DATE"):
                self._check_with_pendulum(token.value)
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
    def _check_with_pendulum(value: str) -> None:
        # Pendulum counts years from 1CE onward, so we need this hack to
        # have proper handling of year 0000 (1BCE) which is a leap year
        # in proleptic Gregorian calendar.
        if value[1:5] == "0000":
            value = f"+2000{value[5:]}"
        pendulum.parse(value[1:])
