#!/usr/bin/env python

import sys
import re
import os
THIS_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(os.path.abspath(THIS_DIR), "../shellsnmp/"))

from shellsnmp.Poller import SNMP
import pytest

def test_Poller_SNMP__parse_str_01(netsnmp_Oxsq_str1):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_Oxsq_str1, options='Oxsq')
    result_correct = {10101: 'GigabitEthernet0/1', 10102: 'GigabitEthernet0/2'}
    assert test_result==result_correct

# Quoted string, single word
def test_Poller_SNMP__parse_str_02(netsnmp_sq_str1):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_sq_str1, options='sq')
    result_correct = {10101: 'GigabitEthernet0/1', 10102: 'GigabitEthernet0/2'}
    assert test_result==result_correct

# Unquoted string, single word
def test_Poller_SNMP__parse_str_02(netsnmp_sq_str2):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_sq_str2, options='sq')
    result_correct = {10101: 'GigabitEthernet0/1', 10102: 'GigabitEthernet0/2'}
    assert test_result==result_correct

# Unquoted string, multi-word (options: Oxsq)
def test_Poller_SNMP__parse_str_02(netsnmp_Oxsq_str2):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_Oxsq_str2, options='Oxsq')
    result_correct = {10101: '[Connection to SFO]', 10102: '[Connection to ATL]', 10103: ''}
    assert test_result==result_correct

# Quoted string, multi-word (options: sq)
def test_Poller_SNMP__parse_str_03(netsnmp_sq_str3):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_sq_str3, options='sq')
    result_correct = {10101: '[Connection to SFO]', 10102: '[Connection to ATL]', 10103: ''}
    assert test_result==result_correct

# Unquoted string, multi-word (options: sq)
def test_Poller_SNMP__parse_str_04(netsnmp_sq_str4):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_sq_str4, options='sq')
    result_correct = {10101: '[Connection to SFO]', 10102: '[Connection to ATL]', 10103: ''}
    assert test_result==result_correct

def test_Poller_SNMP__parse_int_01(netsnmp_Oxsq_int):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_Oxsq_int, options='Oxsq')
    result_correct = {10101: 436212224, 10102: 436212227}
    assert test_result==result_correct

def test_Poller_SNMP__parse_int_02(netsnmp_sq_int):
    snmp = SNMP(community='public', host='10.0.0.1')
    test_result = snmp._parse(netsnmp_sq_int, options='sq')
    result_correct = {10101: 436212224, 10102: 436212227}
    assert test_result==result_correct

