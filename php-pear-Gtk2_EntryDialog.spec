%include	/usr/lib/rpm/macros.php
%define		_class		Gtk2
%define		_subclass	EntryDialog
%define		_status		beta
%define		_pearname	Gtk2_EntryDialog

Summary:	%{_pearname} - Message box with text entry field
Summary(pl):	%{_pearname} - Okno komunikatu z polem na wpisanie tekstu
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7f17755e2600475a04a30ef8910d368b
URL:		http://pear.php.net/package/Gtk2_EntryDialog/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-gtk2
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk2 message box with additional text entry field.

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet dostarcza klasy do obs³ugi okna wiadomo¶ci Gtk2 z polem na
wpisanie tekstu.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/{examples/normal.php,examples/simple.php,examples/verysimple.php}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Gtk2/EntryDialog.php
