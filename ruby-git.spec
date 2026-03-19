#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	git
Summary:	A package for using Git in Ruby code
Name:		ruby-%{pkgname}
Version:	4.3.1
Release:	1
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	e02f4a13be9de937f3ebd933a7bb590e
URL:		http://github.com/schacon/ruby-git
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rake
BuildRequires:	ruby-rdoc
BuildRequires:	ruby-test-unit
%endif
Requires:	git-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/Git is a Ruby library that can be used to create, read and
manipulate Git repositories by wrapping system calls to the git
binary.

%prep
%setup -q -n %{pkgname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
