# rpmrebuild autogenerated specfile

%define defaultbuildroot /
AutoProv: no
%undefine __find_provides
AutoReq: no
%undefine __find_requires
# Do not try autogenerate prereq/conflicts/obsoletes and check files
%undefine __check_files
%undefine __find_prereq
%undefine __find_conflicts
%undefine __find_obsoletes
# Be sure buildpolicy set to do nothing
%define __spec_install_post %{nil}
# Something that need for rpm-4.1
%define _missing_doc_files_terminate_build 0
#dummy
#dummy
#BUILDHOST:    localhost
#BUILDTIME:    Sun Dec 10 22:45:08 2017
#SOURCERPM:    lantern-5.9.13.src.rpm

#RPMVERSION:   5.9.13



#OS:           linux
#SIZE:           16750615
#ARCHIVESIZE:           16753420
#ARCH:         x86_64
BuildArch:     x86_64
Name:          lantern
Version:       5.9.13
Release:       1
Source0: %{name}-%{version}.tar.gz
License:       /usr/share/doc/lantern/copyright 
Group:         net
Summary:       Censorship circumvention tool\nLantern allows you to access sites blocked by internet censorship.\nWhen you run it, Lantern reroutes traffic to selected domains through servers located where such domains are uncensored.

Provides:      application()  
Provides:      application(lantern.desktop)  
Provides:      lantern = 5.9.13-1
Provides:      lantern(x86-64) = 5.9.13-1
Requires:      /bin/bash  
Requires:      libappindicator-devel  
Requires:      libappindicator-gtk3-devel  
#Requires:      rpmlib(CompressedFileNames) <= 3.0.4-1
#Requires:      rpmlib(FileDigests) <= 4.6.0-1
#Requires:      rpmlib(PayloadFilesHavePrefix) <= 4.0-1
#Requires:      rpmlib(PayloadIsXz) <= 5.2-1
#suggest
#enhance
%description

%prep
%setup -q

%install
%{__rm} -rf $RPM_BUILD_ROOT
cp -r %{_builddir}/%{name}-%{version} %{buildroot}/

%files
%dir %attr(0755, root, root) "/usr"
%attr(0777, root, root) "/usr/bin/lantern"
%dir %attr(0755, root, root) "/usr/lib/lantern"
%attr(0644, root, root) "/usr/lib/lantern/.packaged-lantern.yaml"
%attr(0644, root, root) "/usr/lib/lantern/lantern-binary"
%attr(0755, root, root) "/usr/lib/lantern/lantern.sh"
%attr(0644, root, root) "/usr/lib/lantern/lantern.yaml"
%dir %attr(0755, root, root) "/usr/share"
%dir %attr(0755, root, root) "/usr/share/applications"
%attr(0644, root, root) "/usr/share/applications/lantern.desktop"
%dir %attr(0755, root, root) "/usr/share/doc"
%dir %attr(0755, root, root) "/usr/share/doc/lantern"
%doc %attr(0644, root, root) "/usr/share/doc/lantern/changelog.gz"
%doc %attr(0644, root, root) "/usr/share/doc/lantern/copyright"
%dir %attr(0755, root, root) "/usr/share/icons"
%dir %attr(0755, root, root) "/usr/share/icons/hicolor"
%dir %attr(0755, root, root) "/usr/share/icons/hicolor/128x128"
%dir %attr(0755, root, root) "/usr/share/icons/hicolor/128x128/apps"
%attr(0644, root, root) "/usr/share/icons/hicolor/128x128/apps/lantern.png"
%changelog
