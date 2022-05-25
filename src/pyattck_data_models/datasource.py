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
class DataSource(BaseModel):
    type: AnyStr = field(validator=validators.in_(['x-mitre-data-source']))
    description: AnyStr = field()
    x_mitre_modified_by_ref: Id = field()
    x_mitre_contributors: List = field()
    x_mitre_attack_spec_version: SemVersion = field()
    x_mitre_platforms: List[MitrePlatform] = field()
    x_mitre_collection_layers: List = field()
    x_mitre_domains: List[MitreDomain] = field()
    created_by_ref: Id = field()
    
    aliases: List = field(factory=list) 
    revoked: bool = field(factory=bool)
    x_mitre_deprecated: bool = field(factory=bool)


    @property
    def data_components(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='x-mitre-data-component'
        )

    @property
    def techniques(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='attack-pattern'
        )
