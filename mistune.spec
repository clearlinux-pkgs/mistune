#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mistune
Version  : 0.7.4
Release  : 5
URL      : http://pypi.debian.net/mistune/mistune-0.7.4.tar.gz
Source0  : http://pypi.debian.net/mistune/mistune-0.7.4.tar.gz
Summary  : The fastest markdown parser in pure Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mistune-legacypython
Requires: mistune-python3
Requires: mistune-python
BuildRequires : nose-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======
        
        The fastest markdown parser in pure Python with renderer features,
        inspired by marked_.

%package legacypython
Summary: legacypython components for the mistune package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the mistune package.


%package python
Summary: python components for the mistune package.
Group: Default
Requires: mistune-legacypython
Requires: mistune-python3

%description python
python components for the mistune package.


%package python3
Summary: python3 components for the mistune package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mistune package.


%prep
%setup -q -n mistune-0.7.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507160310
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1507160310
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
