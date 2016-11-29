import platform
import sys
import os
THIS_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(os.path.abspath(THIS_DIR), "../"))
sys.path.insert(0, os.path.abspath(THIS_DIR))

import pytest
from shellsnmp.Poller import SNMP

NETSNMP_Oxsq_STR1 = """ifDescr.10101 GigabitEthernet0/1
ifDescr.10102 GigabitEthernet0/2
"""

NETSNMP_Oxsq_STR2 = """ifAlias.10101 [Connection to SFO]
ifAlias.10102 [Connection to ATL]
ifAlias.10103
"""

# Quoted
NETSNMP_sq_STR1 = """RFC1213-MIB::ifDescr.10101 = STRING: "GigabitEthernet0/1"
RFC1213-MIB::ifDescr.10102 = STRING: "GigabitEthernet0/2"
"""

# Unquoted
NETSNMP_sq_STR2 = """RFC1213-MIB::ifDescr.10101 = STRING: GigabitEthernet0/1
RFC1213-MIB::ifDescr.10102 = STRING: GigabitEthernet0/2
"""

# Quoted string, multi-word
NETSNMP_sq_STR3 = """RFC1213-MIB::ifAlias.10101 = STRING: "[Connection to SFO]"
IF-MIB::ifAlias.10102 = STRING: "[Connection to ATL]"
IF-MIB::ifAlias.10103 = STRING: ""
"""

# Unquoted string, multi-word
NETSNMP_sq_STR4 = """RFC1213-MIB::ifAlias.10101 = STRING: [Connection to SFO]
IF-MIB::ifAlias.10102 = STRING: [Connection to ATL]
IF-MIB::ifAlias.10103 = STRING: 
"""

NETSNMP_Oxsq_INT = """ifIndex.10101 436212224
ifIndex.10102 436212227
"""

NETSNMP_sq_INT = """RFC1213-MIB::ifIndex.10101 = INTEGER: 436212224
RFC1213-MIB::ifIndex.10102 = INTEGER: 436212227
"""

@pytest.yield_fixture(scope='session')
def netsnmp_Oxsq_str1(request):
    yield NETSNMP_Oxsq_STR1

@pytest.yield_fixture(scope='session')
def netsnmp_Oxsq_str2(request):
    yield NETSNMP_Oxsq_STR2

# Quoted string, single word
@pytest.yield_fixture(scope='session')
def netsnmp_sq_str1(request):
    yield NETSNMP_sq_STR1

# Unquoted string, single word
@pytest.yield_fixture(scope='session')
def netsnmp_sq_str2(request):
    yield NETSNMP_sq_STR2

# Quoted string, multi-word
@pytest.yield_fixture(scope='session')
def netsnmp_sq_str3(request):
    yield NETSNMP_sq_STR3

# Unquoted string, multi-word
@pytest.yield_fixture(scope='session')
def netsnmp_sq_str4(request):
    yield NETSNMP_sq_STR4

@pytest.yield_fixture(scope='session')
def netsnmp_Oxsq_int(request):
    yield NETSNMP_Oxsq_INT

@pytest.yield_fixture(scope='session')
def netsnmp_sq_int(request):
    yield NETSNMP_sq_INT

