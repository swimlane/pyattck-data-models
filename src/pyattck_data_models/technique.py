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
class Command:
    source: AnyStr = field(factory=str)
    command: AnyStr = field(factory=str)
    name: AnyStr = field(factory=str)


@define
class KillChainPhases:
    kill_chain_name: AnyStr = field()
    phase_name: AnyStr = field()


@define
class Technique(BaseModel):
    type: AnyStr = field(validator=validators.in_(['attack-pattern']))
    description: AnyStr = field()
    created_by_ref: Id = field()
    x_mitre_modified_by_ref: Id = field()
    kill_chain_phases: List[KillChainPhases] = field()
    x_mitre_platforms: List[MitrePlatform] = field()
    x_mitre_domains: List[MitreDomain] = field()
    x_mitre_data_sources: List = field()
    x_mitre_contributors: List = field()

    x_mitre_impact_type: List = field(factory=list)
    x_mitre_deprecated: bool = field(factory=bool)
    x_mitre_effective_permissions: List = field(factory=list)
    x_mitre_remote_support: bool = field(factory=bool)
    x_mitre_permissions_required: List = field(factory=list)
    x_mitre_is_subtechnique: bool = field(factory=bool)
    x_mitre_detection: AnyStr = field(factory=str)
    x_mitre_defense_bypassed: List = field(factory=list)
    x_mitre_system_requirements: List = field(factory=list)
    x_mitre_attack_spec_version: SemVersion = field(factory=SemVersion)
    revoked: bool = field(factory=bool)

    command_list: List = field(factory=list)
    commands: List[Command] = field(factory=list) # need to define this object better
    queries: List = field(factory=list) # need to define this object better
    datasets: List = field(factory=list) # need to define this object better
    possible_detections: List = field(factory=list) # need to define this object better
    external_reference: List = field(factory=list)

    controls: List = field(factory=list)

    @property
    def actors(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='intrusion-set'
        )

    @property
    def data_components(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='x-mitre-data-component'
        )

    @property
    def data_sources(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='x-mitre-data-source'
        )

    @property
    def malwares(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='malware'
        )

    @property
    def mitigations(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='course-of-action'
        )

    @property
    def tactics(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='x-mitre-tactic'
        )
    
    @property
    def techniques(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='attack-pattern'
        )

    @property
    def tools(self):
        return self._get_relationship_objects(
            parent_id=self.id,
            parent_type='tool'
        )

    def __attrs_post_init__(self):
        if self.controls:
            from .control import Control
            return_list = []
            for item in self.controls:
                try:
                    return_list.append(Control(**item))
                except ValueError as ve:
                    raise ve
            self.controls = return_list
        
