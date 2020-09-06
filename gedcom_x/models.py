from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Enum, HttpUrl

from .basetypes import Fact, Gender, Name
from .enums import RelationshipType


class Person(Subject):
    private: bool
    gender: Optional[Gender]
    names: Optional[List[Name]]
    facts: Optional[List[Fact]]


class Relationship(Subject):
    type: Optional[RelationshipType]
    person1: HttpUrl
    person2: HttpUrl
    facts = Optional[List[Fact]]
