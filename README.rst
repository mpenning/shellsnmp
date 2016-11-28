#########
shellsnmp
#########

*Shamelessly (ab)using NET-SNMP shell commands for a quick-and-dirty Python SNMP lib*

Why
---

- I'm not fond of the pySNMP_ API
- snimpy_ requires loading libffi-dev and libsmi-dev (i.e. root privs) on the system
- It's fast enough

Usage
-----

Be sure you have MIB files loaded on your system. You can download them from
Cisco's FTP site like this... 
`wget ftp://ftp.cisco.com/pub/mibs/v2/MIB-NAME.my` ::

    from shellsnmp.Poller import SNMP

    snmp = SNMP(community='public', host='172.16.1.3')
    status, time = snmp.bulkwalk(mibfile='/path/to/IF-MIB.my', 
        oidspec='ifOperStatus')

Note that only `bulkwalk()` has been implemented at this time.

Installation
------------

::

    pip install shellsnmp


License and Copyright
---------------------

Licensed MIT

Copyright 2016 - David Michael Pennington (mike /|at|\ pennington.net)

.. _`pySNMP`: http://pysnmp.sourceforge.net/
.. _`snimpy`: https://github.com/vincentbernat/snimpy
