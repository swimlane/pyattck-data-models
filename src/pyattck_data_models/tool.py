from .types import (
    Id, 
    SemVersion,
    MitreDomain,
    MitrePlatform
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
class Tool(BaseModel):
    type: AnyStr = field(validator=validators.in_(['tool']))
    description: AnyStr = field()
    created_by_ref: Id = field()
    x_mitre_modified_by_ref: Id = field()
    x_mitre_attack_spec_version: SemVersion = field()
    labels: List = field()
    x_mitre_aliases: List = field()
    x_mitre_domains: List[MitreDomain] = field()
    x_mitre_platforms: List[MitrePlatform] = field()
    x_mitre_contributors: List = field()

    revoked: bool = field(factory=bool)
    x_mitre_deprecated: bool = field(factory=bool)

    c2_data: dict = field(factory=dict)
    external_dataset: List = field(factory=list) # need to define this object better
    additional_names: List = field(factory=list)
    attribution_links: List = field(factory=list)
    additional_comments: List = field(factory=list)
    family: List = field(factory=list)

    @property
    def actors(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='intrusion-set'
        )

    @property
    def techniques(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='attack-pattern'
        )
