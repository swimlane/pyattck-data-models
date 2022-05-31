# -*- coding: utf-8 -*-
import json

from pyattck_data_models.attack import MitreAttck
from pyattck_data_models.generated import GeneratedData
from pyattck_data_models.nist import NistControls, GeneratedNistControlMap
from pyattck_data_models.malware import Malware
from pyattck_data_models.tool import Tool
from pyattck_data_models.actor import Actor
from pyattck_data_models.datacomponent import DataComponent
from pyattck_data_models.datasource import DataSource
from pyattck_data_models.mitigation import Mitigation
from pyattck_data_models.tactic import Tactic
from pyattck_data_models.technique import Technique


ENTERPRISE_ATTCK_JSON = json.load(open("tests/resources/enterprise_attck_json.json"))
GENERATED_ATTCK_JSON = json.load(open("tests/resources/generated_attck_data.json"))
GENERATED_NIST_JSON = json.load(open("tests/resources/generated_nist_json.json"))
ICS_ATTCK_JSON = json.load(open("tests/resources/ics_attck_json.json"))
MOBILE_ATTCK_JSON = json.load(open("tests/resources/mobile_attck_json.json"))
NIST_CONTROLS_JSON = json.load(open("tests/resources/nist_controls_json.json"))
PRE_ATTCK_JSON = json.load(open("tests/resources/pre_attck_json.json"))


ENTERPRISE_OBJ = MitreAttck(**ENTERPRISE_ATTCK_JSON)


def test_enterprise():
    assert MitreAttck(**ENTERPRISE_ATTCK_JSON)

def test_ics():
    assert MitreAttck(**ICS_ATTCK_JSON)

def test_mobile():
    assert MitreAttck(**MOBILE_ATTCK_JSON)

def test_pre_attck():
    assert MitreAttck(**PRE_ATTCK_JSON)

def test_generated_data():
    assert GeneratedData(**GENERATED_ATTCK_JSON)

def test_nist_controls():
    assert NistControls(**NIST_CONTROLS_JSON)

def test_controls():
    assert GeneratedNistControlMap(**{"data": GENERATED_NIST_JSON})

def test_actor():
    for item in ENTERPRISE_OBJ.objects:
        if item.type == 'intrusion-set':
            for malware in item.malwares:
                assert isinstance(malware, Malware)
            for tool in item.tools:
                assert isinstance(tool, Tool)
            for technique in item.techniques:
                assert isinstance(technique, Technique)

def test_datacomponent():
    for item in ENTERPRISE_OBJ.objects:
        if item.type == 'x-mitre-data-component':
            for technique in item.techniques:
                assert isinstance(technique, Technique)

def test_datasource():
    for item in ENTERPRISE_OBJ.objects:
        if item.type == 'x-mitre-data-source':
            for technique in item.techniques:
                assert isinstance(technique, Technique)
            for component in item.data_components:
                assert isinstance(component, DataComponent)

def test_malware():
    for item in ENTERPRISE_OBJ.objects:
        if item.type == 'malware':
            for technique in item.techniques:
                assert isinstance(technique, Technique)
            for actor in item.actors:
                assert isinstance(actor, Actor)

def test_mitigation():
    for item in ENTERPRISE_OBJ.objects:
        if item.type == 'course-of-action':
            for technique in item.techniques:
                assert isinstance(technique, Technique)

def test_tactic():
    for item in ENTERPRISE_OBJ.objects:
        if item.type == 'x-mitre-tactic':
            for technique in item.techniques:
                assert isinstance(technique, Technique)

def test_technique():
    for item in ENTERPRISE_OBJ.objects:
        if item.type == 'attack-pattern':
            for actor in item.actors:
                assert isinstance(actor, Actor)
            for component in item.data_components:
                assert isinstance(component, DataComponent)
            for source in item.data_sources:
                assert isinstance(source, DataSource)
            for malware in item.malwares:
                assert isinstance(malware, Malware)
            for mitigation in item.mitigations:
                assert isinstance(mitigation, Mitigation)
            for tactic in item.tactics:
                assert isinstance(tactic, Tactic)
            for technique in item.techniques:
                assert isinstance(technique, Technique)
            for tool in item.tools:
                assert isinstance(tool, Tool)

def test_tactic():
    for item in ENTERPRISE_OBJ.objects:
        if item.type == 'tool':
            for technique in item.techniques:
                assert isinstance(technique, Technique)
            for actor in item.actors:
                assert isinstance(actor, Actor)
