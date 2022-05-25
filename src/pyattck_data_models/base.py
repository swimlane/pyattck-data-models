from datetime import datetime
from typing import (
    Any,
    AnyStr,
    List
)
from pydantic import (
    HttpUrl
)
from attr import (
    define,
    field,
    validators
)
from .types import (
    PATTERNS,
    Id,
    SemVersion
)


BASE_OBJECTS = []
RELATIONSHIP_MAP = {}


@define
class ExternalReferences:
    source_name: AnyStr = field(default=None)
    url: HttpUrl = field(default=None)
    external_id: AnyStr = field(default=None)
    description: AnyStr = field(default=None)
    source_name: AnyStr = field(default=None)

    @external_id.validator
    def validate_external_id(self, attribute, value):
        if value[0] not in ['T', 'G'] and value != 'enterprise-attack':
            raise ValueError("External ID must start with a known letter.")


@define
class BaseAttckModel:
    id: Id = field()


@define(eq=False)
class BaseModel(BaseAttckModel):
    id: Id = field()
    name: AnyStr = field()
    created: datetime = field()
    external_references: List[ExternalReferences] = field()
    modified: datetime = field()
    x_mitre_version: SemVersion = field()
    object_marking_refs: List[Id] = field()
    x_mitre_domains: List = field()

    def _get_relationship_objects(self, parent_id: str, parent_type: str) -> list:
        return_list = []
        if RELATIONSHIP_MAP.get(parent_id):
            for item in RELATIONSHIP_MAP[parent_id]:
                for x in BASE_OBJECTS:
                    if x.id == item and x.type == parent_type and x not in return_list:
                        return_list.append(x)
        return return_list

    def __attrs_post_init__(self):
        if self.external_references:
            return_list = []
            for item in self.external_references:
                return_list.append(ExternalReferences(**item))
            self.external_references = return_list
