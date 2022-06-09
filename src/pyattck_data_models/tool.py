from .types import (
    Id, 
    SemVersion,
    MitreDomain,
    MitrePlatform
)
from .base import (
    BaseModel,
    ExternalReferences,
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
    labels: List = field()

    x_mitre_platforms: List[MitrePlatform] = field(factory=list)
    x_mitre_aliases: List = field(factory=list)
    x_mitre_contributors: List = field(factory=list)
    external_references: List[ExternalReferences] = field(factory=list)
    object_marking_refs: List[Id] = field(factory=list)
    revoked: bool = field(factory=bool)
    x_mitre_deprecated: bool = field(factory=bool)

    # External collected data properties (if applicable)
    c2_data: dict = field(factory=dict)
    external_dataset: List = field(factory=list) # need to define this object better
    additional_names: List = field(factory=list)
    attribution_links: List = field(factory=list)
    additional_comments: List = field(factory=list)
    names: List = field(factory=list)
    comments: List = field(factory=list)
    family: List = field(factory=list)
    links: List = field(factory=list)
    license: AnyStr = field(factory=str)
    price: AnyStr = field(factory=str)
    github: AnyStr = field(factory=str)
    site: AnyStr = field(factory=str)
    twitter: AnyStr = field(factory=str)
    evaluator: AnyStr = field(factory=str)
    date: AnyStr = field(factory=str)
    version: int = field(factory=int)
    implementation: AnyStr = field(factory=str)
    how_to: AnyStr = field(factory=str)
    slingshot: AnyStr = field(factory=str)
    kali: AnyStr = field(factory=str)
    server: AnyStr = field(factory=str)
    implant: AnyStr = field(factory=str)
    multi_user: bool = field(factory=bool)
    ui: bool = field(factory=bool)
    dark_mode: bool = field(factory=bool)
    api: bool = field(factory=bool)
    windows: bool = field(factory=bool)
    linux: bool = field(factory=bool)
    macos: bool = field(factory=bool)
    tcp: bool = field(factory=bool)
    http: bool = field(factory=bool)
    http2: bool = field(factory=bool)
    http3: bool = field(factory=bool)
    dns: bool = field(factory=bool)
    doh: bool = field(factory=bool)
    icmp: bool = field(factory=bool)
    ftp: bool = field(factory=bool)
    imap: bool = field(factory=bool)
    mapi: bool = field(factory=bool)
    smb: bool = field(factory=bool)
    ldap: bool = field(factory=bool)
    key_exchange: bool = field(factory=bool)
    stego: bool = field(factory=bool)
    proxy_aware: bool = field(factory=bool)
    domainfront: bool = field(factory=bool)
    custom_profile: bool = field(factory=bool)
    jitter: bool = field(factory=bool)
    working_hours: bool = field(factory=bool)
    kill_date: bool = field(factory=bool)
    chaining: bool = field(factory=bool)
    logging: bool = field(factory=bool)
    in_wild: bool = field(factory=bool)
    attck_mapping: bool = field(factory=bool)
    dashboard: bool = field(factory=bool)
    blog: AnyStr = field(factory=str)
    c2_matrix_indicators: AnyStr = field(factory=str)
    jarm: bool = field(factory=bool)
    actively_maint: bool = field(factory=bool)
    slack: bool = field(factory=bool)
    slack_members: bool = field(factory=bool)
    gh_issues: bool = field(factory=bool)
    notes: AnyStr = field(factory=str)

    # used in mobile attack
    x_mitre_old_attack_id: AnyStr = field(factory=str)

    # NOT used in mobile attack
    x_mitre_attack_spec_version: SemVersion = field(factory=SemVersion)
    x_mitre_modified_by_ref: Id = field(factory=Id)
    x_mitre_domains: List[MitreDomain] = field(factory=list)

    def __attrs_post_init__(self):
        if self.external_references:
            return_list = []
            for item in self.external_references:
                return_list.append(ExternalReferences(**item))
            self.external_references = return_list

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
