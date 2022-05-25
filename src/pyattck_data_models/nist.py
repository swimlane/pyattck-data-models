from datetime import datetime

from attrs import validators

from .types import Id
from .base import (
    List,
    AnyStr,
    define,
    field,
    ExternalReferences
)


@define
class ControlObject:
    id: Id = field()
    name: AnyStr = field()
    created: datetime = field()
    external_references: List[ExternalReferences] = field()
    modified: datetime = field()
    description: AnyStr = field()
    type: AnyStr = field(validator=validators.in_(['course-of-action']))
    x_mitre_family: AnyStr = field()
    x_mitre_priority: AnyStr = field()
    x_mitre_impact: list = field(factory=list)


@define
class NistControls:
    id: Id = field()
    objects: List[ControlObject] = field(factory=list)

    def __attrs_post_init__(self):
        if self.objects:
            return_list = []
            for item in self.objects:
                try:
                    return_list.append(ControlObject(**item))
                except Exception as e:
                    raise e
            self.objects = return_list
