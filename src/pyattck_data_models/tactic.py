from .types import (
    Id,
    SemVersion
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
class Tactic(BaseModel):
    type: AnyStr = field(validator=validators.in_(['x-mitre-tactic']))
    description: AnyStr = field()
    created_by_ref: Id = field()
    x_mitre_modified_by_ref: Id = field()
    x_mitre_shortname: AnyStr = field()
    x_mitre_contributors: List = field()
    x_mitre_attack_spec_version: SemVersion = field()

    @property
    def techniques(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='attack-pattern'
        )
