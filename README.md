# Stamp - Simple Hostname & Timestamp to File Service

A simple service to print the system hostname and current timestamp to an output file.

### Prerequisites

* **Ansible** - This script is deployed using Ansible and it is assumed an existing ansible configuration is in place to deploy this service.
* **Systemd** - The service requires an operating system running systemd (For example CentOS 7, or Ubuntu 16.04)

The following Ansible variables must be set, for example within the host variables, to sucessfully deploy the Ansible playbook:

* stamp_bindir - The directory of the service executable (For example: "/tmp")
* stamp_logdir - The directory of the service log outpur (For example: "/var/log/stamp")
* stamp_schedule - The schedule for logging output in minutes (For example "5")

Included is an example host configuration 
