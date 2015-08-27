%define plugin	quicktimer

Summary:	VDR plugin: Create new timers quickly
Name:		vdr-plugin-%plugin
Version:	0.1.2
Release:	12
Group:		Video
License:	GPL
URL:		http://phivdr.dyndns.org/vdr/vdr-quicktimer/
Source:		http://phivdr.dyndns.org/vdr/vdr-quicktimer/vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Create timers by entering channel, day and start time. Creating
timers from TV magazines is fast and does not require browsing EPG.

%prep
%setup -q -n %plugin-%{version}
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY




