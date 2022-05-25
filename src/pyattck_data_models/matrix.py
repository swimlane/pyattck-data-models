from .types import (
    Id, 
    SemVersion,
    MitreDomain
)
from .base import (
    BaseModel,
    List,
    AnyStr,
    define,
    field,
    validators
)


@define
class Matrix(BaseModel):
    type: AnyStr = field(validator=validators.in_(['x-mitre-matrix']))
    tactic_refs: List[Id] = field()
    created_by_ref: Id = field()
    description: AnyStr = field()
    x_mitre_attack_spec_version: SemVersion = field()
    x_mitre_modified_by_ref: Id = field()
    x_mitre_domains: List[MitreDomain] = field(factory=list)