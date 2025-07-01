%define gitver %(echo %version | tr _ -)
Name:          piper-phonemize
Version:       2023.11.14_4
Release:       2mamba
Summary:       C++ library for converting text to phonemes for Piper
Group:         Applications/Multimedia
Vendor:        openmamba
Distribution:  openmamba
Packager:      Silvan Calarco <silvan.calarco@mambasoft.it>
URL:           https://github.com/rhasspy/piper-phonemize
Source:        https://github.com/rhasspy/piper-phonemize.git/%{gitver}/piper-phonemize-%{version}.tar.bz2
Patch0:        piper-phonemize-2023.11.14_4-system-espeak-ng.patch
License:       MIT
## AUTOBUILDREQ-BEGIN
BuildRequires: glibc-devel
BuildRequires: libespeak-ng-devel
BuildRequires: libgcc
BuildRequires: libstdc++6-devel
## AUTOBUILDREQ-END
BuildRequires: cmake
Requires:      lib%{name} = %{?epoch:%epoch:}%{version}-%{release}

%description
C++ library for converting text to phonemes for Piper.

%package -n lib%{name}
Group:         System/Libraries
Summary:       Shared libraries for %{name}

%description -n lib%{name}
This package contains shared libraries for %{name}.

%package -n lib%{name}-devel
Group:         Development/Libraries
Summary:       Development files for %{name}
Requires:      lib%{name} = %{?epoch:%epoch:}%{version}-%{release}

%description -n lib%{name}-devel
This package contains libraries and header files for developing applications that use %{name}.


%debug_package

%prep
%setup -q
%patch 0 -p1

%build
%cmake \
   -DESPEAK_NG_DIR=%{_prefix}

%cmake_build

%install
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"
%cmake_install

%clean
[ "%{buildroot}" != / ] && rm -rf "%{buildroot}"

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/piper_phonemize
%{_datadir}/libtashkeel_model.ort

%files -n lib%{name}
%defattr(-,root,root)
%{_libdir}/libonnxruntime.so.*
%{_libdir}/libpiper_phonemize.so.*
%doc LICENSE.md

%files -n lib%{name}-devel
%defattr(-,root,root)
%{_includedir}/cpu_provider_factory.h
%{_includedir}/onnxruntime_*h
%dir %{_includedir}/piper-phonemize
%{_includedir}/piper-phonemize/*
%{_includedir}/provider_options.h
%{_libdir}/libonnxruntime.so
%{_libdir}/libpiper_phonemize.so
%doc README.md
