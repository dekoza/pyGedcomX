from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel

from gedcomx.enums import GedcomXIdentifier
from gedcomx.utils import CaseInsensitiveMapping

EXTENSION = "gedx"


class MainHeader(CaseInsensitiveMapping):
    X_DC_conformsTo: List[Union[GedcomXIdentifier, str]]
    User_Agent: Optional[str]
    X_DC_created: Optional[str]
    X_DC_creator: Optional[AnyUrl]


class ResourceHeader(CaseInsensitiveMapping):
    Name: str
    Content_Type: Optional[str]
    ETag: Optional[str]
    X_DC_modified: Optional[str]


class Manifest(BaseModel):
    main_header: MainHeader
    resource_headers: List[ResourceHeader]
