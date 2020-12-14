#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mistune
Version  : 0.8.4
Release  : 32
URL      : https://files.pythonhosted.org/packages/2d/a4/509f6e7783ddd35482feda27bc7f72e65b5e7dc910eca4ab2164daf9c577/mistune-0.8.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/2d/a4/509f6e7783ddd35482feda27bc7f72e65b5e7dc910eca4ab2164daf9c577/mistune-0.8.4.tar.gz
Summary  : The fastest markdown parser in pure Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mistune-license = %{version}-%{release}
Requires: mistune-python = %{version}-%{release}
Requires: mistune-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : nose

%description
=======
        
        The fastest markdown parser in pure Python with renderer features,
        inspired by marked_.

%package license
Summary: license components for the mistune package.
Group: Default

%description license
license components for the mistune package.


%package python
Summary: python components for the mistune package.
Group: Default
Requires: mistune-python3 = %{version}-%{release}

%description python
python components for the mistune package.


%package python3
Summary: python3 components for the mistune package.
Group: Default
Requires: python3-core
Provides: pypi(mistune)

%description python3
python3 components for the mistune package.


%prep
%setup -q -n mistune-0.8.4
cd %{_builddir}/mistune-0.8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602133605
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mistune
cp %{_builddir}/mistune-0.8.4/LICENSE %{buildroot}/usr/share/package-licenses/mistune/9e95f9efe7446cb800a88f09c761a96b25f5aab8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mistune/9e95f9efe7446cb800a88f09c761a96b25f5aab8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
