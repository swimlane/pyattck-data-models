from .types import (
    Id,
    SemVersion
)
from .base import (
    BaseRelationship,
    ExternalReferences,
    List,
    AnyStr,
    define,
    field
)


@define
class Relationship(BaseRelationship):
    external_references: List[ExternalReferences] = field()
    object_marking_refs: List[Id] = field()
    x_mitre_modified_by_ref: Id = field()
    revoked: bool = field(factory=bool)
    created_by_ref: Id = field(factory=Id)
    description: AnyStr = field(factory=str)
    x_mitre_deprecated: bool = field(factory=bool)
    x_mitre_version: SemVersion = field(factory=SemVersion)
    x_mitre_attack_spec_version: SemVersion = field(factory=SemVersion)
