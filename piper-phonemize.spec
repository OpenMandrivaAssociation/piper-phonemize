%define gitver %(echo %version | tr _ -)
Name:          piper-phonemize
Version:       2023.11.14_4
Release:       1
Summary:       C++ library for converting text to phonemes for Piper
Group:         Applications/Multimedia
URL:           https://github.com/rhasspy/piper-phonemize
Source:        https://github.com/rhasspy/piper-phonemize/archive/%{gitver}/%{name}-%{gitver}.tar.gz
#Patch0:        piper-phonemize-2023.11.14_4-system-espeak-ng.patch
License:       MIT

BuildRequires: glibc-devel
#BuildRequires: libespeak-ng-devel
BuildRequires:  pkgconfig(espeak-ng)
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
%autosetup -n %{name}-%{gitver} -p1

%build
%cmake

%make_build

%install
%make_install -C build

%files
%{_bindir}/piper_phonemize
%{_datadir}/libtashkeel_model.ort

%files -n lib%{name}
%{_libdir}/libonnxruntime.so.*
%{_libdir}/libpiper_phonemize.so.*
%doc LICENSE.md

%files -n lib%{name}-devel
%{_includedir}/cpu_provider_factory.h
%{_includedir}/onnxruntime_*h
%dir %{_includedir}/piper-phonemize
%{_includedir}/piper-phonemize/*
%{_includedir}/provider_options.h
%{_libdir}/libonnxruntime.so
%{_libdir}/libpiper_phonemize.so
%doc README.md
