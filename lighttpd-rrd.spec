Summary:	Produce RRD graphs from lighttpd
Summary(pl):	Tworzenie wykresów RRD z lighttpd
Name:		lighttpd-rrd
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	%{name}.conf
Source1:	%{name}-index.html
Source2:	%{name}-graph.sh
Source3:	%{name}.cron
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	crondaemon
Requires:	lighttpd >= 1.4.13-5.5
Requires:	lighttpd-mod_alias
Requires:	lighttpd-mod_indexfile
Requires:	lighttpd-mod_rrdtool
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapp		%{name}
%define		_sysconfdir	/etc/lighttpd/webapps.d
%define		_appdir		/var/lib/lighttpd/rrd

%description
Produce graphs from RRD data produced by lighttpd mod_rrdtool module.

%description -l pl
Tworzenie wykresów z danych RRD tworzonych przez modu³ mod_rrdtool
lighttpd.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir},%{_sbindir},/etc/cron.d}

install %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/rrd.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_appdir}/index.html
install %{SOURCE2} $RPM_BUILD_ROOT%{_sbindir}/lighttpd-rrdgraph
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.d/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service -q lighttpd restart

%postun
if [ "$1" = 0 ]; then
	%service -q lighttpd restart
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/rrd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/cron.d/%{name}
%attr(755,root,root) %{_sbindir}/lighttpd-rrdgraph
%dir %attr(775,root,stats) %{_appdir}
%{_appdir}/index.html
