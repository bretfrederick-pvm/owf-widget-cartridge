
Ozone Widget Cartridge on OpenShift
===================

This git repository contains the source for the owf-widget-cartridge RPM package.

Dependencies:

Provides:
 - Ozone Widget template

Building the RPM package
------------------------
Prerequisites

* RHEL or Fedora with the "Development Tools" group installed

* The Tito rpm build tools

> yum install tito

* Git (if not already installed)

> yum install git

* Clone & build the repo

> git clone https://*yourusername*@bitbucket.org/pvm-engineering/owf-widget-cartridge.git

> cd owf-widget-cartridge

> tito build --rpm --test

Tito will generate the rpm package in /tmp/tito/noarch/owf-cartridge{*}.rpm

Open Issues/Stories/Tasks
----------
See the component backlog @ https://pvm-engineering.atlassian.net/browse/OS/component/10300 
