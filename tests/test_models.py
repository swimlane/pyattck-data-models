# -*- coding: utf-8 -*-
import json

from pyattck_data_models.attack import MitreAttck
from pyattck_data_models.generated import GeneratedData
from pyattck_data_models.nist import NistControls


ENTERPRISE_ATTCK_JSON = json.load(open("tests/resources/enterprise_attck_json.json"))
GENERATED_ATTCK_JSON = json.load(open("tests/resources/generated_attck_json.json"))
GENERATED_NIST_JSON = json.load(open("tests/resources/generated_nist_json.json"))
ICS_ATTCK_JSON = json.load(open("tests/resources/ics_attck_json.json"))
MOBILE_ATTCK_JSON = json.load(open("tests/resources/mobile_attck_json.json"))
NIST_CONTROLS_JSON = json.load(open("tests/resources/nist_controls_json.json"))
PRE_ATTCK_JSON = json.load(open("tests/resources/pre_attck_json.json"))


def test_enterprise():
    assert MitreAttck(**ENTERPRISE_ATTCK_JSON)

def test_ics():
    assert MitreAttck(**ICS_ATTCK_JSON)

def test_mobile():
    assert MitreAttck(**MOBILE_ATTCK_JSON)

def test_pre_attck():
    assert MitreAttck(**PRE_ATTCK_JSON)
