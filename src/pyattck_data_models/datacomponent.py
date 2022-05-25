from .base import (
    BaseModel,
    List,
    AnyStr,
    define,
    field,
    validators
)
from .types import (
    Id,
    SemVersion,
    MitreDomain
)


@define
class DataComponent(BaseModel):
    type: AnyStr = field(validator=validators.in_(['x-mitre-data-component']))
    description: AnyStr = field()
    created_by_ref: Id = field()
    x_mitre_modified_by_ref: Id = field()
    x_mitre_data_source_ref: Id = field()
    object_marking_refs: List[Id] = field()
    x_mitre_domains: List[MitreDomain] = field()
    x_mitre_attack_spec_version: SemVersion = field()

    @property
    def techniques(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='attack-pattern'
        )
