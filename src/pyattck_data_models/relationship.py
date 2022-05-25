from datetime import datetime
from attr import validators
from .types import (
    Id,
    SemVersion
)
from .base import (
    ExternalReferences,
    List,
    AnyStr,
    define,
    field
)


@define
class Relationship:
    id: Id = field()
    type: AnyStr = field(validator=validators.in_(['relationship']))
    created: datetime = field()
    external_references: List[ExternalReferences] = field()
    modified: datetime = field()
    object_marking_refs: List[Id] = field()
    relationship_type: AnyStr = field()
    source_ref: Id = field()
    target_ref: Id = field()
    x_mitre_modified_by_ref: Id = field()
    revoked: bool = field(factory=bool)
    created_by_ref: Id = field(factory=Id)
    description: AnyStr = field(factory=str)
    x_mitre_deprecated: bool = field(factory=bool)
    x_mitre_version: SemVersion = field(factory=SemVersion)
    x_mitre_attack_spec_version: SemVersion = field(factory=SemVersion)
