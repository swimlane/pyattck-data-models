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

@define
class GeneratedNistControlMap:
    data: dict = field()

    def __attrs_post_init__(self):
        if self.data:
            return_dict = {}
            for key,val in self.data.items():
                try:
                    Id().validate(key)
                except Exception as e:
                    raise e
                return_dict[key] = []
                if isinstance(val, list):
                    for item in val:
                        try:
                            Id().validate(item)
                        except Exception as e:
                            raise e
                    return_dict[key] = val
            self.data = return_dict
