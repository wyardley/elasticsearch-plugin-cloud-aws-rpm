%define debug_package %{nil}
%define base_install_dir /usr/share/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-cloud-aws
Version:        2.1.2
Release:        1%{?dist}
Summary:        Elasticsearch plugin to leverage AWS services such as EC2 and S3.
Group:          System Environment/Daemons
License:        ASLv2.0
URL:            https://github.com/elasticsearch/elasticsearch-cloud-aws
Source0:        https://download.elastic.co/elasticsearch/release/org/elasticsearch/plugin/cloud-aws/2.1.2/cloud-aws-2.1.2.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
Requires:       elasticsearch >= 2.1.2, elasticsearch < 2.1.3

%description
Elasticsearch plugin to leverage AWS services such as EC2 and S3
for discovery and backup.

%prep
%setup -q -c

%install
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins/cloud-aws
%{__install} -D -m 0755 *.jar %{buildroot}/%{base_install_dir}/plugins/cloud-aws
%{__install} -m 0644 plugin-descriptor.properties %{buildroot}/%{base_install_dir}/plugins/cloud-aws

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/cloud-aws
%attr(755, root, elasticsearch) %{base_install_dir}/plugins/cloud-aws/*

%doc

%changelog
* Wed Feb 02 2016 Will Yardley <wby@axs.com>
- Update for version 2.1.2 (ES v 2.1.2)
* Wed Jan 27 2016 Will Yardley <wby@axs.com>
- Update for version 2.1.1 (ES v 2.1.1)
* Thu Nov 12 2015 Will Yardley <wby@axs.com>
- Update for version 2.0.0 (ES v 2.0.0)
* Tue Sep 22 2015 Will Yardley <wby@axs.com>
- Update for version 2.7.1 (ES v 1.7.x)
- Fork from:
  https://github.com/phrawzty/elasticsearch-plugin-cloud-aws-rpm
* Fri May 15 2015 Dan <phrawzty@mozilla.com>
- Init for v2.4.1 (ES v1.4.x)
