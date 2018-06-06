Name:           SoapyUHD
Version:	%{VERSION}
Release:        1%{?dist}
Summary:        SoapySDR UHD Support Module
License:        GPLv3
Group:          Development/Libraries/C and C++
Url:            https://github.com/pothosware/SoapyUHD
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:	uhd-devel
BuildRequires:	SoapySDR-devel
BuildRequires:	boost-devel

%description
SoapySDR UHD Support Module

%prep
%setup -n %{name}-soapy-uhd-%{version}

%build
mkdir build
cmake . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc README.md
%{_libdir}/SoapySDR/modules0.6/libuhdSupport.so
%{_libdir}/uhd/modules/libsoapySupport.so

%changelog

