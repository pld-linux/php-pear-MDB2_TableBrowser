%define		status		alpha
%define		pearname	MDB2_TableBrowser
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Database table abstraction library
Summary(pl.UTF-8):	%{pearname} - biblioteka abstrakcji tabeli bazy danych
Name:		php-pear-%{pearname}
Version:	0.1.3
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	d5fc8947e973dbeb04011cd1d03a8bd2
URL:		http://pear.php.net/package/MDB2_TableBrowser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
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

In PEAR status of this package is: %{status}.

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

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/MDB2_TableBrowser/README .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log README
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MDB2/TableBrowser
%{php_pear_dir}/MDB2/TableBrowser.php
