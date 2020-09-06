import re
from datetime import datetime
from typing import List, Optional, Union

import language_tags
from pydantic import AnyUrl, BaseModel, HttpUrl

from .date import Date
from .enums import (
    Confidence,
    DocumentType,
    EventType,
    FactType,
    GenderType,
    IdentifierType,
    NamePartType,
    NameType,
    RelationshipType,
    ResourceType,
    RoleType,
)


class NetGedcomXURI(AnyUrl):
    @classmethod
    def __get_validators__(cls, *args, **kwargs):
        yield super(NetGedcomXURI, cls).__get_validators__(*args, **kwargs)
        yield cls.validate

    @classmethod
    def validate(cls, value: str):
        pattern = r"^https?://(www\.)?gedcomx\.org/"
        if re.match(pattern, value):
            ValueError("value must not use a base URI of http://gedcomx.org/")


class Language(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(description="Language tag conforming to BCP 47 (RFC 5646)")

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError("string required")
        if not language_tags.tags.check(value):
            raise ValueError("invalid language code")
        return value


class GedcomXIdentifier(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError("string required")
        pattern = r"^https?://(www\.)?gedcomx.org/"
        if not re.match(pattern, value):
            raise ValueError("invalid GEDCOM X identifier")


class Email(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not isinstance(value, str):
            raise TypeError("string required")
        pattern = r"^(mailto:)?[\w\.-]+@[\w\.-]+(?:\.[\w]+)+$"
        if not re.match(pattern, value):
            raise ValueError("invalid email")


class Attribution(BaseModel):
    contributor: Optional[AnyUrl]
    modified: Optional[datetime]
    changeMessage: Optional[str]
    creator: Optional[AnyUrl]
    created: Optional[datetime]


class Qualifier(BaseModel):
    name: AnyUrl
    value: Optional[str]


class SourceReference(BaseModel):
    description: AnyUrl
    descriptionId: Optional[str]
    attribution: Optional[Attribution]
    qualifiers: Optional[List[Qualifier]]


class Note(BaseModel):
    lang: Optional[Language]
    subject: Optional[str]
    text: str
    attribution: Optional[Attribution]


class Conclusion(BaseModel):
    id: Optional[str]
    lang: Optional[Language]
    sources: Optional[List[SourceReference]]
    analysis: Optional[AnyUrl]
    notes: Optional[List[Note]]
    confidence: Optional[Confidence]
    attribution: Optional[Attribution]


class Identifier(BaseModel):
    value: AnyUrl
    type: IdentifierType


class EvidenceReference(BaseModel):
    resource: AnyUrl
    attribution: Optional[Attribution]


class Subject(Conclusion):
    extracted: Optional[bool] = False
    evidence: Optional[List[EvidenceReference]]
    media: Optional[List[SourceReference]]
    identifiers: Optional[List[Identifier]]


class Gender(Conclusion):
    type: GenderType


class PlaceReference(BaseModel):
    original: Optional[str]
    descriptionRef: Optional[HttpUrl]


class NamePart(BaseModel):
    type: Optional[NamePartType]
    value: str
    qualifiers: Optional[Qualifier]


class NameForm(BaseModel):
    lang: Optional[Language]
    fullText: Optional[str]
    parts: Optional[List[NamePart]]


class Name(Conclusion):
    type: Optional[NameType]
    nameForms: List[NameForm]
    date: Optional[Date]


class Fact(Conclusion):
    type: FactType
    date: Optional[Date]
    place: Optional[PlaceReference]
    value: Optional[str]
    qualifiers: Optional[Qualifier]


class Person(Subject):
    private: Optional[bool]
    gender: Optional[Gender]
    names: Optional[List[Name]]
    facts: Optional[List[Fact]]


class Relationship(Subject):
    type: Optional[RelationshipType]
    person1: AnyUrl
    person2: AnyUrl
    facts: Optional[List[Fact]]


class SourceCitation(BaseModel):
    lang: Optional[Language]
    value: str


class TextValue(BaseModel):
    lang: Optional[Language]
    value: str


class OnlineAccount(BaseModel):
    serviceHomepage: HttpUrl
    accountName: str


class Address(BaseModel):
    value: Optional[str]
    city: Optional[str]
    country: Optional[str]
    postalCode: Optional[str]
    stateOrProvince: Optional[str]
    street: Optional[str]
    street2: Optional[str]
    street3: Optional[str]
    street4: Optional[str]
    street5: Optional[str]
    street6: Optional[str]


class EventRole(Conclusion):
    person: AnyUrl
    type: Optional[RoleType]


class Event(Subject):
    type: Optional[EventType]
    date: Optional[Date]
    place: Optional[PlaceReference]
    roles: Optional[List[EventRole]]


class Agent(BaseModel):
    id: Optional[str]
    identifiers: Optional[List[Identifier]]
    names: Optional[TextValue]
    homepage: Optional[HttpUrl]
    openid: Optional[HttpUrl]
    accounts: Optional[OnlineAccount]
    emails: Optional[List[Email]]
    phones: Optional[List[str]]
    addresses: Optional[List[Address]]
    person: Optional[Person]


class Document(Conclusion):
    type: Optional[DocumentType]
    extracted: Optional[bool] = False
    textType = Optional[str]
    text = str
    attribution = Optional[Attribution]


class PlaceDescription(Subject):
    names: List[TextValue]
    type: Optional[GedcomXIdentifier]
    place: Optional[NetGedcomXURI]
    jurisdiction: Optional[AnyUrl]
    latitude: Optional[float]
    longitude: Optional[float]
    temporalDescription: Optional[Date]
    spatialDescription: Optional[AnyUrl]


class GroupRole(Conclusion):
    person: AnyUrl
    type: Optional[RoleType]
    date: Optional[Date]
    details: Optional[str]


class Group(Subject):
    names: List[TextValue]
    date: Optional[Date]
    place: Optional[PlaceReference]
    roles: Optional[GroupRole]


class Coverage(BaseModel):
    spatial: Optional[PlaceReference]
    temporal: Optional[Date]


class SourceDescription(BaseModel):
    id: Optional[str]
    resourceType: Optional[ResourceType]
    citations: Union[SourceCitation, List[SourceCitation]]
    mediaType: Optional[str]
    about: Optional[AnyUrl]
    mediator: Optional[AnyUrl]
    publisher: Optional[AnyUrl]
    authors: Optional[List[AnyUrl]]
    sources: Optional[List[SourceReference]]
    analysis: Optional[AnyUrl]
    componentOf: Optional[SourceReference]
    titles: Optional[List[TextValue]]
    notes: Optional[List[Note]]
    attribution: Optional[Attribution]
    rights: Optional[List[AnyUrl]]
    coverage: Optional[List[Coverage]]
    descriptions: Optional[List[TextValue]]
    identifiers: Optional[List[Identifier]]
    created: Optional[datetime]
    modified: Optional[datetime]
    published: Optional[datetime]
    repository: Optional[AnyUrl]
