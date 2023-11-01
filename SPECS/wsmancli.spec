Name:           wsmancli
Version:        2.6.0
Release:        16%{?dist}
License:        BSD
Url:            http://www.openwsman.org/
# You can get this tarball here:
# https://github.com/Openwsman/wsmancli/archive/v%{version}.tar.gz
Source:         wsmancli-%{version}.tar.gz
Source1:        COPYING
Source2:        README
Source3:        AUTHORS
BuildRequires: make
BuildRequires:  openwsman-devel >= 2.1.0 pkgconfig curl-devel
BuildRequires:  autoconf automake libtool
Requires:       openwsman curl
Patch0:         missing-pthread-symbols.patch
Patch1:         http-unauthorized-improve.patch
Summary:        WS-Management-Command line Interface

%description
Command line interface for managing 
systems using Web Services Management protocol.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1 -b .http-unauthorized-improve
cp -fp %SOURCE1 %SOURCE2 %SOURCE3 .;

%build
./bootstrap
%configure --disable-more-warnings 
make %{?_smp_flags}

%install
make DESTDIR=%{buildroot} install

%files
%{_bindir}/wsman
%{_bindir}/wseventmgr
%{_mandir}/man1/wsman*
%{_mandir}/man1/wseventmgr*
%doc COPYING README AUTHORS

%changelog
* Mon Nov 28 2022 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.6.0-16
- Improve handling of HTTP 401 Unauthorized
  Resolves: #2127416

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 2.6.0-15
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.6.0-14
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 18 2017 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.6.0-6
- Fix the dist tag, remove Group

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.6.0-1
- Update to wsmancli-2.6.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 12 2014 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.3.1-1
- Update to wsmancli-2.3.1

* Thu Sep 19 2013 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.3.0-4
- Rebuild because of soname change in openswman

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.3.0-1
- Update to wsmancli-2.3.0

* Tue Sep 18 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.7.1-3
- Fix issues found by fedora-review utility in the spec file

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 11 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.7.1-1
- Update to wsmancli-2.2.7.1

* Wed Mar 23 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.5-1
- Update to wsmancli-2.2.5

* Tue Feb 22 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.4-3
- Fix option issue on big endian architectures

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.4-1
- Update to wsmancli-2.2.4

* Wed Mar  3 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.3-1
- Update to wsmancli-2.2.3

* Mon Jan 25 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.0-5
- Fix Source URL
- Use tarball from upstream
- Add COPYING, README and AUTHORS to sources (previously placed in the modified tarball)

* Fri Nov  6 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 2.1.0-4
- Missing symbols from pthread library.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild


* Tue Sep 30 2008  <srinivas_ramanatha@dell.com> - 2.1.0-1%{?dist}
- Modified the spec file to adhere to fedora packaging guidelines.

