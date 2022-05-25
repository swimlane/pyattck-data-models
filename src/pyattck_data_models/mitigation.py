from .types import (
    Id,
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
class Mitigation(BaseModel):
    type: AnyStr = field(validator=validators.in_(['course-of-action']))
    description: AnyStr = field()
    created_by_ref: Id = field()
    x_mitre_modified_by_ref: Id = field()
    x_mitre_domains: List[MitreDomain] = field()
    x_mitre_deprecated: bool = field(factory=bool)

    @property
    def techniques(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='attack-pattern'
        )
