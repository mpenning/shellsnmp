from subprocess import Popen, PIPE
import re

import arrow

class SNMP(object):
    def __init__(self, host='', community='public'):
        assert host
        self.host = host
        self.community = community

    def _cast(self, text):
        if re.search(r'^\s*\d+\s*$', text):
            # Integer
            return int(text)
        elif re.search(r'^\s*\d+\.\d+\.\d+\.\d+\s*$', text):
            # IP Address
            return str(text)
        else:
            return str(text)

    def _parse(self, text):
        """Parse the output of bulkwalk()"""
        retval = dict()
        for line in text.splitlines():
            mm = re.search('^(?P<index>\S+)\s+(?P<type>=\s+STRING:\s+)*"*(?P<value>\S.+?)"*$', line)
            assert mm is not None, "Could not parse: '{0}'".format(line)
            tmp = mm.groupdict()
            index, value = tmp.get('index'), tmp.get('value')
            retval[self._cast(index.split('.')[-1])] = self._cast(value)
        return retval

    def pivot_table(self, vals1, vals2):
        """Use the common oid index values to combine into one table"""
        assert vals1
        assert vals2
        retval = dict()
        for idx, val1 in vals1.items():
            retval[val1] =vals2.get(idx)
        return retval

    def bulkwalk(self, oidspec="", mibfile=""):
        assert oidspec
        if mibfile:
            # ifDescr.10101 GigabitEthernet0/1
            cmd = 'snmpbulkwalk -v 2c -m {0} -c {1} -Oxsq {2} {3}'.format(
                mibfile, self.community, self.host, oidspec)
        else:
            # RFC1213-MIB::ifDescr.10101 = STRING: "GigabitEthernet0/1"
            cmd = 'snmpbulkwalk -v 2c -c {0} -sq {1} {2}'.format(
                self.community, self.host, oidspec)

        proc = Popen(cmd, shell=True, stdout=PIPE)
        return self._parse(proc.stdout.read()), arrow.now()

