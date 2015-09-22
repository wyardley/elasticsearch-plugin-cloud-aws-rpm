%define debug_package %{nil}
%define base_install_dir /usr/share/elasticsearch

# Avoid running brp-java-repack-jars
%define __os_install_post %{nil}

Name:           elasticsearch-plugin-cloud-aws
Version:        2.7.1
Release:        1%{?dist}
Summary:        Elasticsearch plugin to leverage AWS services such as EC2 and S3.
Group:          System Environment/Daemons
License:        ASLv2.0
URL:            https://github.com/elasticsearch/elasticsearch-cloud-aws
Source0:        https://download.elasticsearch.org/elasticsearch/elasticsearch-cloud-aws/elasticsearch-cloud-aws-%{version}.zip
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:      noarch
Requires:       elasticsearch >= 1.7.0, elasticsearch < 1.8.0

%description
Elasticsearch plugin to leverage AWS services such as EC2 and S3
for discovery and backup.

%prep
%setup -q -c

%install
%{__mkdir} -p %{buildroot}/%{base_install_dir}/plugins/cloud-aws
%{__install} -D -m 755 *.jar %{buildroot}/%{base_install_dir}/plugins/cloud-aws

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{base_install_dir}/plugins/cloud-aws
%attr(755, root, elasticsearch) %{base_install_dir}/plugins/cloud-aws/*

%doc

%changelog
* Tue Sep 22 2015 Will Yardley <wby@axs.com>
- Update for version 2.7.1 (ES v 1.7.x)
- Fork from:
  https://github.com/phrawzty/elasticsearch-plugin-cloud-aws-rpm
* Fri May 15 2015 Dan <phrawzty@mozilla.com>
- Init for v2.4.1 (ES v1.4.x)
