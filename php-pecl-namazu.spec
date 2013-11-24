%define		php_name	php%{?php_suffix}
%define		modname	namazu
%define		status		beta
%define		_rc RC1
%define		rel 8
Summary:	%{modname} - full-text search extension using Namazu
Summary(pl.UTF-8):	%{modname} - pełnotekstowe wyszukiwanie z użyciem Namazu
Name:		%{php_name}-pecl-%{modname}
Version:	2.2.0
Release:	0.%{_rc}.%{rel}
License:	PHP or GPL
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}%{_rc}.tgz
# Source0-md5:	3b1a01c812df4db4348b724f22fa2f09
URL:		http://pecl.php.net/package/namazu/
BuildRequires:	namazu-devel
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Namazu is a full-text search system. This module an interface to the
Namazu library. This extension is originally made by Takuya Tsukada.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Namazu jest to system wyszukiwania pełnotektsowego. Ten moduł jest
interfejsem do biblioteki Namazu. Rozszerzenie początkowo naspisane
przez Takuya Tsukada.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}%{?_rc}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
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
%doc CREDITS EXPERIMENTAL README* sample
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
