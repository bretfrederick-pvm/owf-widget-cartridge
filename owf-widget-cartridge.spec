%global cartridgedir %{_libexecdir}/openshift/cartridges/v2/owf-widget/

Summary:       Provides an Ozone Widget Quickstart Applications
Name:          owf-widget-cartridge
Version: 0.8.13
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.shadow-soft.com
Source0:       https://bitbucket.org/pvm-engineering/owf-widget-cartridge
Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-cartridge-jbossews
%if 0%{?rhel}
Requires:      maven3
%endif
%if 0%{?fedora}
Requires:      maven
%endif
BuildRequires: jpackage-utils
BuildArch:     noarch

%description
Provides an Ozone Widget template application for OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%post
# To modify an alternative you should:
# - remove the previous version if it's no longer valid
# - install the new version with an increased priority
# - set the new version as the default to be safe

%if 0%{?rhel}
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/java/apache-maven-3.0.3 100
alternatives --set maven-3.0 /usr/share/java/apache-maven-3.0.3
%endif

%if 0%{?fedora}
alternatives --remove maven-3.0 /usr/share/java/apache-maven-3.0.3
alternatives --install /etc/alternatives/maven-3.0 maven-3.0 /usr/share/maven 102
alternatives --set maven-3.0 /usr/share/maven
%endif

/usr/sbin/oo-admin-cartridge --action install -R -s %{cartridgedir}../
if [ -f /usr/sbin/oo-admin-broker-cache ]
then
    echo "clearing broker cache"
    /usr/sbin/oo-admin-broker-cache --clear --console
fi

%postun
/usr/sbin/oo-admin-cartridge --action erase --name widget --version 1.0 --cartridge_version 0.0.1
if [ -f /usr/sbin/oo-admin-broker-cache ]
then
    echo "clearing broker cache"
    /usr/sbin/oo-admin-broker-cache --clear --console
fi

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Mon Dec 30 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.13-1
- update README (bret.frederick@patvmackinc.com)
- OS-44 added collapsible panels for owf testing tools
  (bret.frederick@patvmackinc.com)
- OS-44 fixed name in erase command (bret.frederick@patvmackinc.com)
- OS-44 #time 6h #comment added pub/sub test to template app
  (bret.frederick@patvmackinc.com)
- test (bret.frederick@patvmackinc.com)
- OS-44 #comment finished Intents integration (bret.frederick@patvmackinc.com)
- OS-44 #comment added Intents (sayHello) to the template app
  (bret.frederick@patvmackinc.com)
- OS-44 #comment added owf detection to template page
  (bret.frederick@patvmackinc.com)
- OS-44 #comment added OWF javascript libs (bret.frederick@patvmackinc.com)
- OS-44 #comment widget name and universal name always unique
  (bret.frederick@patvmackinc.com)
- OS-44 #comment added sayHello intent to widget template
  (bret.frederick@patvmackinc.com)
- OS-44 #time 2h #comment added widget descriptor URL and cart property to show
  the URL to users (bret.frederick@patvmackinc.com)
- OS-44 #time 2h #comment baseline app working (bret.frederick@patvmackinc.com)
- fixed cart name (bret.frederick@patvmackinc.com)
- fixed bad manifest entry (bret.frederick@patvmackinc.com)

* Wed Dec 11 2013 Bret Frederick <bret.frederick@patvmackinc.com> 0.8.12-1
- new package built with tito

