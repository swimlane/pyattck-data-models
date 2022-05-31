from .base import (
    BaseModel,
    List,
    AnyStr,
    define,
    field
)


@define
class Control(BaseModel):
    revoked: bool = field()
    x_mitre_family: AnyStr = field(factory=str)
    x_mitre_impact: List = field(factory=list)
    x_mitre_priority: AnyStr = field(factory=str)

    @property
    def techniques(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='attack-pattern'
        )
