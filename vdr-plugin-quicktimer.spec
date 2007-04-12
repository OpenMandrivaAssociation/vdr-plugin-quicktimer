
%define plugin	quicktimer
%define name	vdr-plugin-%plugin
%define version	0.1.1
%define rel	7

Summary:	VDR plugin: Create new timers quickly
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://users.tkk.fi/~phintuka/vdr/vdr-quicktimer/
Source:		http://users.tkk.fi/~phintuka/vdr/vdr-quicktimer/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
Create timers by entering channel, day and start time. Creating
timers from TV magazines is fast and does not require browsing EPG.

%prep
%setup -q -n %plugin-%version

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

