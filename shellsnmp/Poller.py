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

    def _parse(self, text, options=''):
        """Parse the output of bulkwalk()"""
        retval = dict()
        for line in text.splitlines():
            line.strip()
            try:
                ## --> Parse assuming the line has a non-empty value
                if options=='Oxsq':
                    mm = re.search(r'^\S+?\.(?P<index>\d+)\s+(?P<value>\S.+)$', line.strip())
                elif options=='sq':
                    # RFC1213-MIB::ifDescr.10101 = STRING: "GigabitEthernet0/1"
                    mm = re.search(r'^\S+?\.(?P<index>\d+)\s+=\s+(INTEGER|STRING):\s+\"*(?P<value>\S.+?)\"*$', line.strip())
                assert mm is not None, "Could not parse: '{0}'".format(line)

            except AssertionError:
                ## --> Parse assuming the line has an empty value
                if options=='Oxsq':
                    mm = re.search(r'^\S+?\.(?P<index>\d+)', line.strip())
                elif options=='sq':
                    # RFC1213-MIB::ifDescr.10101 = STRING: "GigabitEthernet0/1"
                    mm = re.search(r'^\S+?\.(?P<index>\d+)\s+=\s+(STRING):\s*\"*\"*$', line.strip())

            assert mm is not None, "Could not parse: '{0}'".format(line)
            tmp = mm.groupdict()
            index, value = tmp.get('index'), tmp.get('value', '')
            # Special case for double quoted empty string...
            if value == '""':
                value = ''
            retval[self._cast(index)] = self._cast(value)
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
            proc = Popen(cmd, shell=True, stdout=PIPE)
            return self._parse(proc.stdout.read(), options='Oxsq'), arrow.now()

        else:
            # RFC1213-MIB::ifDescr.10101 = STRING: "GigabitEthernet0/1"
            cmd = 'snmpbulkwalk -v 2c -c {0} -sq {1} {2}'.format(
                self.community, self.host, oidspec)
            proc = Popen(cmd, shell=True, stdout=PIPE)
            return self._parse(proc.stdout.read(), options='sq'), arrow.now()

