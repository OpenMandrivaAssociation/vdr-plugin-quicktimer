
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


