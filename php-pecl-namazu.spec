%define		_modname	namazu
%define		_status		beta
Summary:	%{_modname} - full-text search extension using Namazu
Summary(pl.UTF-8):	%{_modname} - pełnotekstowe wyszukiwanie z użyciem Namazu
Name:		php-pecl-%{_modname}
Version:	2.2.0
%define		_rc RC1
%define		_rel 7
Release:	0.%{_rc}.%{_rel}
License:	PHP or GPL
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}%{_rc}.tgz
# Source0-md5:	3b1a01c812df4db4348b724f22fa2f09
URL:		http://pecl.php.net/package/namazu/
BuildRequires:	namazu-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Namazu is a full-text search system. This module an interface to the
Namazu library. This extension is originally made by Takuya Tsukada.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Namazu jest to system wyszukiwania pełnotektsowego. Ten moduł jest
interfejsem do biblioteki Namazu. Rozszerzenie początkowo naspisane
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
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}%{_rc}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}%{_rc}/{CREDITS,EXPERIMENTAL,sample,README*}
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
