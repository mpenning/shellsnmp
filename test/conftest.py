import platform
import sys
import os
THIS_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(os.path.abspath(THIS_DIR), "../"))
sys.path.insert(0, os.path.abspath(THIS_DIR))

import pytest
from shellsnmp.Poller import SNMP

NETSNMP_Oxsq_STR = """ifDescr.10101 GigabitEthernet0/1
ifDescr.10102 GigabitEthernet0/2
"""

NETSNMP_sq_STR = """RFC1213-MIB::ifDescr.10101 = STRING: "GigabitEthernet0/1"
RFC1213-MIB::ifDescr.10102 = STRING: "GigabitEthernet0/2"
"""

NETSNMP_Oxsq_INT = """ifIndex.10101 436212224
ifIndex.10102 436212227
"""

NETSNMP_sq_INT = """RFC1213-MIB::ifIndex.10101 = INTEGER: 436212224
RFC1213-MIB::ifIndex.10102 = INTEGER: 436212227
"""

@pytest.yield_fixture(scope='session')
def netsnmp_Oxsq_str(request):
    yield NETSNMP_Oxsq_STR

@pytest.yield_fixture(scope='session')
def netsnmp_sq_str(request):
    yield NETSNMP_sq_STR

@pytest.yield_fixture(scope='session')
def netsnmp_Oxsq_int(request):
    yield NETSNMP_Oxsq_INT

@pytest.yield_fixture(scope='session')
def netsnmp_sq_int(request):
    yield NETSNMP_sq_INT
