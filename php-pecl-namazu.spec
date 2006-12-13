%define		_modname	namazu
%define		_status		beta
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{_modname} - full-text search extension using Namazu
Summary(pl):	%{_modname} - pe³notekstowe wyszukiwanie z u¿yciem Namazu
Name:		php-pecl-%{_modname}
Version:	2.2.0
%define		_rc RC1
%define		_rel 6
Release:	0.%{_rc}.%{_rel}
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}%{_rc}.tgz
# Source0-md5:	3b1a01c812df4db4348b724f22fa2f09
URL:		http://pecl.php.net/package/namazu/
BuildRequires:	namazu-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.322
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Namazu is a full-text search system. This module an interface to the
Namazu library. This extension is originally made by Takuya Tsukada.

In PECL status of this extension is: %{_status}.

%description -l pl
Namazu jest to system wyszukiwania pe³notektsowego. Ten modu³ jest
interfejsem do biblioteki Namazu. Rozszerzenie pocz±tkowo naspisane
przez Takuya Tsukada.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}%{_rc}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}%{_rc}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}%{_rc}/{CREDITS,EXPERIMENTAL,sample,README*}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
