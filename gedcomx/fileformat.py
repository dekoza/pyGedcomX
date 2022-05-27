from typing import Union

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
    X_DC_conformsTo: list[Union[GedcomXIdentifier, str]]
    User_Agent: Union[None, str]
    X_DC_created: Union[None, str]
    X_DC_creator: Union[None, AnyUrl]


class ResourceHeader(HeaderMixin, CaseInsensitiveMapping):
    Name: str
    Content_Type: Union[None, str]
    ETag: Union[None, str]
    X_DC_modified: Union[None, str]


class Manifest(BaseModel):
    main_header: MainHeader
    resource_headers: list[ResourceHeader]

    def __str__(self) -> str:
        resources = "\n\n".join(str(h) for h in self.resource_headers)

        return f"{self.main_header}\n\n{resources}"
