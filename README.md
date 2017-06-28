# Capture-Py
Capture-Py is a malware analysis tool that makes a copy of any files deleted or modified in a given directory and sub-directories. It was intended to be a subsitute for Capture-Bat on 64bit systems.

The original utility Capture-Bat implemented network packet capture, registery monitoring and tracking of what process created the file.  Capture-Py doesn't do this yet but is easily augmented by running Sysmon (https://technet.microsoft.com/en-us/sysinternals/sysmon or Process Monitor (https://technet.microsoft.com/en-au/processmonitor) which both do an excellent job.
