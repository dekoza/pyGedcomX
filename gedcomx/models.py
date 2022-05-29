import re
from datetime import datetime
from typing import Union

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
    original: Union[str, None]
    formal: Union[DateFormat, None]


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
    contributor: Union[ResourceReference, GedURI, None]
    modified: Union[datetime, None]
    changeMessage: Union[str, None]
    creator: Union[ResourceReference, GedURI, None]
    created: Union[datetime, None]


class Qualifier(GedcomXElement):
    name: GedURI
    value: Union[str, None]


class SourceReference(GedcomXElement):
    description: str
    descriptionId: Union[str, None]
    attribution: Union[Attribution, None]
    qualifiers: Union[None, list[Qualifier]]


class Note(GedcomXElement):
    lang: Union[None, Language]
    subject: Union[None, str]
    text: str
    attribution: Union[None, Attribution]


class Conclusion(GedcomXElement):
    id: Union[None, str]
    lang: Union[None, Language]
    sources: Union[None, list[SourceReference]]
    analysis: Union[ResourceReference, GedURI, None]
    notes: Union[None, list[Note]]
    confidence: Union[None, Confidence]
    attribution: Union[None, Attribution]


class Identifier(GedcomXElement):
    value: GedURI
    type: IdentifierType


class EvidenceReference(GedcomXElement):
    resource: GedURI
    attribution: Union[None, Attribution]


class Subject(Conclusion):
    extracted: Union[None, bool] = False
    evidence: Union[None, list[EvidenceReference]]
    media: Union[None, list[SourceReference]]
    identifiers: Union[None, list[Identifier]]


class Gender(Conclusion):
    type: GenderType


class PlaceReference(GedcomXElement):
    original: Union[None, str]
    descriptionRef: Union[None, HttpUrl]


class NamePart(GedcomXElement):
    type: Union[None, NamePartType]
    value: str
    qualifiers: Union[None, Qualifier]


class NameForm(GedcomXElement):
    lang: Union[None, Language]
    fullText: Union[None, str]
    parts: Union[None, list[NamePart]]


class Name(Conclusion):
    type: Union[None, NameType]
    nameForms: list[NameForm]
    date: Union[None, Date]


class Fact(Conclusion):
    type: FactType
    date: Union[None, Date]
    place: Union[None, PlaceReference]
    value: Union[None, str]
    qualifiers: Union[None, Qualifier]


class Person(Subject):
    private: Union[None, bool]
    gender: Union[None, Gender]
    names: Union[None, list[Name]]
    facts: Union[None, list[Fact]]


class Relationship(Subject):
    type: Union[None, RelationshipType]
    person1: Union[ResourceReference, GedURI]
    person2: Union[ResourceReference, GedURI]
    facts: Union[None, list[Fact]]


class SourceCitation(GedcomXElement):
    lang: Union[None, Language]
    value: str


class TextValue(GedcomXElement):
    lang: Union[None, Language]
    value: str


class OnlineAccount(GedcomXElement):
    serviceHomepage: Union[ResourceReference, HttpUrl]
    accountName: str


class Address(GedcomXElement):
    value: Union[None, str]
    city: Union[None, str]
    country: Union[None, str]
    postalCode: Union[None, str]
    stateOrProvince: Union[None, str]
    street: Union[None, str]
    street2: Union[None, str]
    street3: Union[None, str]
    street4: Union[None, str]
    street5: Union[None, str]
    street6: Union[None, str]


class EventRole(Conclusion):
    person: Union[ResourceReference, GedURI]
    type: Union[None, RoleType]


class GroupRole(Conclusion):
    person: Union[ResourceReference, GedURI]
    type: Union[None, RoleType]
    date: Union[None, Date]
    details: Union[None, str]


class Coverage(GedcomXElement):
    spatial: Union[None, PlaceReference]
    temporal: Union[None, Date]


class SourceDescription(GedcomXElement):
    id: Union[None, str]
    resourceType: Union[None, ResourceType]
    citations: Union[SourceCitation, list[SourceCitation]]
    mediaType: Union[None, str]
    about: Union[ResourceReference, GedURI, None]
    mediator: Union[ResourceReference, GedURI, None]
    publisher: Union[ResourceReference, GedURI, None]
    authors: Union[None, list[Union[ResourceReference, GedURI]]]
    sources: Union[None, list[SourceReference]]
    analysis: Union[ResourceReference, GedURI, None]
    componentOf: Union[None, SourceReference]
    titles: Union[None, list[TextValue]]
    notes: Union[None, list[Note]]
    attribution: Union[None, Attribution]
    rights: Union[None, list[GedURI]]
    coverage: Union[None, list[Coverage]]
    descriptions: Union[None, list[TextValue]]
    identifiers: Union[None, list[Identifier]]
    created: Union[None, datetime]
    modified: Union[None, datetime]
    published: Union[None, datetime]
    repository: Union[ResourceReference, GedURI, None]


class Agent(GedcomXElement):
    id: Union[None, str]
    identifiers: Union[None, list[Identifier]]
    names: Union[None, list[TextValue]]
    homepage: Union[ResourceReference, HttpUrl, None]
    openid: Union[ResourceReference, HttpUrl, None]
    accounts: Union[None, OnlineAccount]
    emails: Union[None, list[Union[ResourceReference, Email]]]
    phones: Union[None, list[Union[ResourceReference, str]]]
    addresses: Union[None, list[Address]]
    person: Union[ResourceReference, GedURI, None]


class Event(Subject):
    type: Union[None, EventType]
    date: Union[None, Date]
    place: Union[None, PlaceReference]
    roles: Union[None, list[EventRole]]


class Document(Conclusion):
    type: Union[None, DocumentType]
    extracted: Union[None, bool] = False
    textType: Union[None, str]
    text: str
    attribution: Union[None, Attribution]


class PlaceDescription(Subject):
    names: list[TextValue]
    type: Union[None, GedcomXIdentifier]
    place: Union[ResourceReference, NetGedcomXURI, None]
    jurisdiction: Union[ResourceReference, GedURI, None]
    latitude: Union[None, float]
    longitude: Union[None, float]
    temporalDescription: Union[None, Date]
    spatialDescription: Union[ResourceReference, GedURI, None]


class Group(Subject):
    names: list[TextValue]
    date: Union[None, Date]
    place: Union[None, PlaceReference]
    roles: Union[None, GroupRole]


class GedcomXObject(GedcomXElement):
    """
    Main container used only to read/write files.
    """

    id: Union[None, str]
    lang: Union[None, Language]
    attribution: Union[None, Attribution]
    persons: Union[None, list[Person]]
    relationships: Union[None, list[Relationship]]
    sourceDescriptions: Union[None, list[SourceDescription]]
    agents: Union[None, list[Agent]]
    events: Union[None, list[Event]]
    documents: Union[None, list[Document]]
    places: Union[None, list[PlaceReference]]
    groups: Union[None, list[Group]]
    description: Union[None, GedURI]  # URI must resolve to SourceDescription

    placeDescriptions: Union[None, list[PlaceDescription]]
    notes: Union[None, Note]
    sourceReferences: Union[None, list[SourceReference]]
    genders: Union[None, list[Gender]]
    names: Union[None, list[Name]]
    facts: Union[None, list[Fact]]
