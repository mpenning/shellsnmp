#!/usr/bin/env python

import sys
import re
import os
THIS_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(os.path.abspath(THIS_DIR), "../shellsnmp/"))

from shellsnmp.Poller import SNMP
import pytest

def test_Poller_SNMP__parse_01(netsnmp_Oxsq_str):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_Oxsq_str)
    result_correct = {10101: 'GigabitEthernet0/1', 10102: 'GigabitEthernet0/2'}
    assert test_result==result_correct

def test_Poller_SNMP__parse_02(netsnmp_sq_str):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_sq_str)
    result_correct = {10101: 'GigabitEthernet0/1', 10102: 'GigabitEthernet0/2'}
    assert test_result==result_correct

