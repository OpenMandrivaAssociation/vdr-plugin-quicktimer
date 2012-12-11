
%define plugin	quicktimer
%define name	vdr-plugin-%plugin
%define version	0.1.2
%define rel	10

Summary:	VDR plugin: Create new timers quickly
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-quicktimer/
Source:		http://phivdr.dyndns.org/vdr/vdr-quicktimer/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Create timers by entering channel, day and start time. Creating
timers from TV magazines is fast and does not require browsing EPG.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.2-10mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.2-9mdv2009.1
+ Revision: 359357
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-8mdv2009.0
+ Revision: 197969
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-7mdv2009.0
+ Revision: 197714
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.2-6mdv2008.1
+ Revision: 145193
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-5mdv2008.1
+ Revision: 103188
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-4mdv2008.0
+ Revision: 50037
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-3mdv2008.0
+ Revision: 42124
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-2mdv2008.0
+ Revision: 22672
- rebuild for new vdr

* Sat Apr 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.2-1mdv2008.0
+ Revision: 16568
- 0.1.2
- update URL


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-7mdv2007.0
+ Revision: 90966
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-6mdv2007.1
+ Revision: 74077
- rebuild for new vdr
- Import vdr-plugin-quicktimer

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-2mdv2007.0
- rebuild for new vdr

* Thu Jul 20 2006 Anssi Hannula <anssi@mandriva.org> 0.1.1-1mdv2007.0
- initial Mandriva release

