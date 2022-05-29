"""
Implementation of https://github.com/FamilySearch/gedcomx-record/
"""

from typing import Union

from .enums import EventTypes, FieldValueType
from .models import (
    Attribution,
    Conclusion,
    Coverage,
    Fact,
    GedcomXElement,
    GedcomXObject,
    GedURI,
    Language,
    Person,
    Qualifier,
    ResourceReference,
    SourceDescription,
    SourceReference,
    TextValue,
)


class CollectionContent(GedcomXElement):
    resourceType: GedURI
    count: Union[None, int]
    completeness: Union[None, float]


class Collection(GedcomXElement):
    id: Union[None, str]
    lang: Union[None, Language]
    content: Union[None, list[CollectionContent]]
    title: Union[None, str]
    size: Union[None, int]
    attribution: Union[None, Attribution]


class FieldValue(Conclusion):
    type: Union[None, FieldValueType]
    labelId: Union[None, str]
    text: Union[None, str]
    datatype: Union[None, EventTypes]  # TODO: Specs muddy here, check this
    resource: Union[None, GedURI]


class Field(GedcomXElement):
    id: Union[None, str]
    type: Union[None, GedURI]
    values: Union[None, list[FieldValue]]


class FieldValueDescriptor:
    id: Union[None, str]
    type: Union[None, FieldValueType]
    labelId: Union[None, str]
    optionsl: Union[None, bool]
    labels: Union[None, list[TextValue]]
    displaySortKey: Union[None, str]
    entrySortKey: Union[None, str]
    entryRequired: Union[None, bool]
    editable: Union[None, bool]
    parentLabelId: Union[None, str]


class FieldDesctiptor:
    id: Union[None, str]
    originalLabel: Union[None, str]
    descriptions: Union[None, list[TextValue]]
    values: Union[None, list[FieldValueDescriptor]]


class RecordDescriptor(GedcomXElement):
    id: Union[None, str]
    lang: Union[None, Language]
    fields: Union[None, list[FieldDesctiptor]]


# extensions to original types


class FactExt(Fact):
    primary: Union[None, bool]


class PersonExt(Person):
    principal: Union[None, bool]


class SourceDescriptionExt(SourceDescription):
    titleLabel: Union[None, str]
    sortKey: Union[None, str]
    descriptorRef: Union[None, ResourceReference]  # must resolve to RecordDescriptor


class SourceReferenceExt(SourceReference):
    qualifiers: Union[None, list[Qualifier]]


class CoverageExt(Coverage):
    recordType: GedURI


# originally defined as XML-only


class RecordSet(GedcomXElement):
    id: str
    lang: Union[None, Language]
    metadata: GedcomXObject
    records: list[GedcomXObject]
