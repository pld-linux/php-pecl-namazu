%define		_modname	namazu
%define		_status		beta

Summary:	%{_modname} - full-text search extension using Namazu
Summary(pl):	%{_modname} - pe³notekstowe wyszukiwanie z u¿yciem Namazu
Name:		php-pecl-%{_modname}
Version:	2.2.0
%define		_version 2.2.0RC1
Release:	0.RC1.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{_version}.tgz
# Source0-md5:	3b1a01c812df4db4348b724f22fa2f09
URL:		http://pecl.php.net/package/namazu/
BuildRequires:	libtool
BuildRequires:	namazu-devel
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

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
cd %{_modname}-%{_version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{_version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{_version}/{CREDITS,EXPERIMENTAL,sample,README*}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
