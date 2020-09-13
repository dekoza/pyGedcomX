import re
from datetime import datetime
from typing import List, Optional, Union

import language_tags
from pydantic import AnyUrl, BaseModel, HttpUrl

from .date import DateFormat
from .enums import (
    Confidence,
    DocumentType,
    EventType,
    FactType,
    GedcomXIdentifier,
    GenderType,
    IdentifierType,
    NamePartType,
    NameType,
    RelationshipType,
    ResourceType,
    RoleType,
)


class Hashtag(str):
    @classmethod
    def __get_validators__(cls, *args, **kwargs):
        yield cls.validate

    @classmethod
    def validate(cls, value: str):
        if value[0] != "#":
            ValueError("Hashtag must start with a '#' sign.")
        return value


GedURI = Union[Hashtag, AnyUrl]


class NetGedcomXURI(AnyUrl):
    @classmethod
    def __get_validators__(cls, *args, **kwargs):
        yield from super().__get_validators__(*args, **kwargs)
        yield cls.validate

    @classmethod
    def validate(cls, value: str):
        pattern = r"^https?://(www\.)?gedcomx\.org/"
        if re.match(pattern, value):
            ValueError("value must not use a base URI of http://gedcomx.org/")
        return value


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


class GedcomXElement(BaseModel):
    pass
    # preparing for xml support


class ResourceReference(GedcomXElement):
    resource: str


class Date(GedcomXElement):
    original: Optional[str]
    formal: Optional[DateFormat]


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
        return value


class Attribution(GedcomXElement):
    contributor: Optional[Union[ResourceReference, GedURI]]
    modified: Optional[datetime]
    changeMessage: Optional[str]
    creator: Optional[Union[ResourceReference, GedURI]]
    created: Optional[datetime]


class Qualifier(GedcomXElement):
    name: GedURI
    value: Optional[str]


class SourceReference(GedcomXElement):
    description: str
    descriptionId: Optional[str]
    attribution: Optional[Attribution]
    qualifiers: Optional[List[Qualifier]]


class Note(GedcomXElement):
    lang: Optional[Language]
    subject: Optional[str]
    text: str
    attribution: Optional[Attribution]


class Conclusion(GedcomXElement):
    id: Optional[str]
    lang: Optional[Language]
    sources: Optional[List[SourceReference]]
    analysis: Optional[Union[ResourceReference, GedURI]]
    notes: Optional[List[Note]]
    confidence: Optional[Confidence]
    attribution: Optional[Attribution]


class Identifier(GedcomXElement):
    value: GedURI
    type: IdentifierType


class EvidenceReference(GedcomXElement):
    resource: GedURI
    attribution: Optional[Attribution]


class Subject(Conclusion):
    extracted: Optional[bool] = False
    evidence: Optional[List[EvidenceReference]]
    media: Optional[List[SourceReference]]
    identifiers: Optional[List[Identifier]]


class Gender(Conclusion):
    type: GenderType


class PlaceReference(GedcomXElement):
    original: Optional[str]
    descriptionRef: Optional[HttpUrl]


class NamePart(GedcomXElement):
    type: Optional[NamePartType]
    value: str
    qualifiers: Optional[Qualifier]


class NameForm(GedcomXElement):
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
    person1: Union[ResourceReference, GedURI]
    person2: Union[ResourceReference, GedURI]
    facts: Optional[List[Fact]]


class SourceCitation(GedcomXElement):
    lang: Optional[Language]
    value: str


class TextValue(GedcomXElement):
    lang: Optional[Language]
    value: str


class OnlineAccount(GedcomXElement):
    serviceHomepage: Union[ResourceReference, HttpUrl]
    accountName: str


class Address(GedcomXElement):
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
    person: Union[ResourceReference, GedURI]
    type: Optional[RoleType]


class GroupRole(Conclusion):
    person: Union[ResourceReference, GedURI]
    type: Optional[RoleType]
    date: Optional[Date]
    details: Optional[str]


class Coverage(GedcomXElement):
    spatial: Optional[PlaceReference]
    temporal: Optional[Date]


class SourceDescription(GedcomXElement):
    id: Optional[str]
    resourceType: Optional[ResourceType]
    citations: Union[SourceCitation, List[SourceCitation]]
    mediaType: Optional[str]
    about: Optional[Union[ResourceReference, GedURI]]
    mediator: Optional[Union[ResourceReference, GedURI]]
    publisher: Optional[Union[ResourceReference, GedURI]]
    authors: Optional[List[Union[ResourceReference, GedURI]]]
    sources: Optional[List[SourceReference]]
    analysis: Optional[Union[ResourceReference, GedURI]]
    componentOf: Optional[SourceReference]
    titles: Optional[List[TextValue]]
    notes: Optional[List[Note]]
    attribution: Optional[Attribution]
    rights: Optional[List[GedURI]]
    coverage: Optional[List[Coverage]]
    descriptions: Optional[List[TextValue]]
    identifiers: Optional[List[Identifier]]
    created: Optional[datetime]
    modified: Optional[datetime]
    published: Optional[datetime]
    repository: Optional[Union[ResourceReference, GedURI]]


class Agent(GedcomXElement):
    id: Optional[str]
    identifiers: Optional[List[Identifier]]
    names: Optional[List[TextValue]]
    homepage: Optional[Union[ResourceReference, HttpUrl]]
    openid: Optional[Union[ResourceReference, HttpUrl]]
    accounts: Optional[OnlineAccount]
    emails: Optional[List[Union[ResourceReference, Email]]]
    phones: Optional[List[Union[ResourceReference, str]]]
    addresses: Optional[List[Address]]
    person: Optional[Union[ResourceReference, GedURI]]


class Event(Subject):
    type: Optional[EventType]
    date: Optional[Date]
    place: Optional[PlaceReference]
    roles: Optional[List[EventRole]]


class Document(Conclusion):
    type: Optional[DocumentType]
    extracted: Optional[bool] = False
    textType: Optional[str]
    text: str
    attribution: Optional[Attribution]


class PlaceDescription(Subject):
    names: List[TextValue]
    type: Optional[GedcomXIdentifier]
    place: Optional[Union[ResourceReference, NetGedcomXURI]]
    jurisdiction: Optional[Union[ResourceReference, GedURI]]
    latitude: Optional[float]
    longitude: Optional[float]
    temporalDescription: Optional[Date]
    spatialDescription: Optional[Union[ResourceReference, GedURI]]


class Group(Subject):
    names: List[TextValue]
    date: Optional[Date]
    place: Optional[PlaceReference]
    roles: Optional[GroupRole]


class GedcomXObject(GedcomXElement):
    """
    Main container used only to read/write files.
    """

    id: Optional[str]
    attribution: Optional[Attribution]
    persons: Optional[List[Person]]
    relationships: Optional[List[Relationship]]
    sourceDescriptions: Optional[List[SourceDescription]]
    agents: Optional[List[Agent]]
    events: Optional[List[Event]]
    documents: Optional[List[Document]]
    places: Optional[List[PlaceReference]]
    groups: Optional[List[Group]]
