# Stamp - Simple Hostname & Timestamp to File Service

A simple service to print the system hostname and current timestamp to an output file.

### Prerequisites

* **Ansible** - This script is deployed using Ansible and it is assumed an existing ansible configuration is in place to deploy this service.

**Linux**

* **Systemd** - The service requires an operating system running systemd (For example CentOS 7, or Ubuntu 16.04)

**Windows**

* **pywin32** - pywin32 should be installed ```pip install pywin32```
* **SMWinservice** - A copy of [SMWinservice from Davide Mastromatteo](http://thepythoncorner.com/dev/how-to-create-a-windows-service-in-python/)

The following Ansible variables must be set, for example within the host variables, to sucessfully deploy the Ansible playbook:

* stamp_lin_bindir - The directory of the service executable (For example: "/tmp")
* stamp_lin_logdir - The directory of the service log output (For example: "/var/log/stamp")
* stamp_win_bindir - The directory of the service executable (For example: "C:\stamp")
* stamp_win_logdir - The directory of the service log output (For example: "C:\stamp")
* stamp_log - The log filename (For example: "stamp.log")
* stamp_schedule - The schedule for logging output in minutes (For example "5")

Included is an example host configuration: host_vars.example

### Deployment

To deploy the script run the playbook with the following command:

```
ansible-playbook -i hosts/example stamp.yml
```

