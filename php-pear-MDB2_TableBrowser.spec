%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	TableBrowser
%define		_status		alpha
%define		_pearname	MDB2_TableBrowser
Summary:	%{_pearname} - Database table abstraction library
Summary(pl.UTF-8):	%{_pearname} - biblioteka abstrakcji tabeli bazy danych
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	88734e3c2185fb707667e711983940e2
Patch0:		%{name}-paths.patch
URL:		http://pear.php.net/package/MDB2_TableBrowser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Table browsing objects allow your code to handle any database table in
an abstract way. By freeing your code from the database details it is
possible for you to build generic data reporting or manipulation
functions.

Put another way, if you really hate using SQL in your code, having to
piece together bits of sql to make queries...this library gives you an
alternative.

Currently only the single table browser is implemented. If you need to
work with data that spans multiple tables, you can build a table view
as this library works with them as well.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Obiekty opisujące tabele baz danych pozwalają na obsługę tabel w
kodzie w sposób abstrakcyjny. Przez uwolnienie kodu od potrzeby
opisywania tabeli możliwe jest na tworzenie ogólnych funkcji do
raportowania czy modyfikowania danych.

Opisując to w inny sposób, jeśli niepożądane jest posiadanie zapytań
SQL wewnątrz kodu, tworzenie zapytań z części, biblioteka ta dostarcza
alternatywy.

Obecnie zaimplementowana jest tylko obsługa pojedynczej tabeli. Jeśli
istnieje potrzeba obsługi danych rozrzuconych na kilka tabel,
konieczne będzie stworzenie widoku, z którym klasa ta współpracuje
równie dobrze.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/MDB2_TableBrowser/Examples/example.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/TableBrowser
%{php_pear_dir}/MDB2/TableBrowser.php
