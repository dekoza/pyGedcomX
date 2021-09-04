from typing import List, Optional, Union

from pydantic import AnyUrl, BaseModel

from gedcomx.enums import GedcomXIdentifier
from gedcomx.utils import CaseInsensitiveMapping

EXTENSION = "gedx"


class HeaderMixin:
    def __str__(self) -> str:
        return "\n".join(
            f"{key.replace('_', '-')}: {value}"
            for key, value in self.items()
            if value is not None
        )


class MainHeader(HeaderMixin, CaseInsensitiveMapping):
    X_DC_conformsTo: List[Union[GedcomXIdentifier, str]]
    User_Agent: Optional[str]
    X_DC_created: Optional[str]
    X_DC_creator: Optional[AnyUrl]


class ResourceHeader(HeaderMixin, CaseInsensitiveMapping):
    Name: str
    Content_Type: Optional[str]
    ETag: Optional[str]
    X_DC_modified: Optional[str]


class Manifest(BaseModel):
    main_header: MainHeader
    resource_headers: List[ResourceHeader]

    def __str__(self) -> str:
        resources = "\n\n".join(str(h) for h in self.resource_headers)

        return f"{self.main_header}\n\n{resources}"
