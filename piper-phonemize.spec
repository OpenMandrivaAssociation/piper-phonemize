%define major 1
%define libname %mklibname piper_phonemize
%define devname %mklibname piper_phonemize -d

Name:		piper-phonemize
Version:	2023.11.14
Release:	2
Source0:	https://github.com/rhasspy/piper-phonemize/archive/refs/tags/%{version}-4.tar.gz
Summary:	Phonemize library used by old versions of the Piper TTS engine
URL:		https://github.com/rhasspy/piper-phonemize
License:	MIT
Group:		System/Libraries
BuildSystem:	cmake
BuildRequires:	pkgconfig(nlohmann_json)
BuildRequires:	pkgconfig(libonnxruntime) >= 1.28.0
BuildRequires:	pkgconfig(espeak-ng)

%patchlist
piper-phonemize-system-libs.patch

%description
Phonemize library used by old versions of the Piper TTS engine.

This library is obsoleted by espeak-ng in current Piper, but it is
still used by the fork of Piper used to implement Text-to-Speech
in Proton.

%package -n %{libname}
Summary:	Phonemize library used by old versions of the Piper TTS engine
Group:		System/Libraries

%description -n %{libname}
Phonemize library used by old versions of the Piper TTS engine

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	pkgconfig(nlohmann_json)

%description -n %{devname}
Development files (Headers etc.) for %{name}, the
phonemize library used by old versions of the Piper TTS engine

This library is obsoleted by espeak-ng in current Piper, but it is
still used by the fork of Piper used to implement Text-to-Speech
in Proton.

%prep -a
# We use the system copy
rm src/json.hpp

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_datadir}/libtashkeel_model.ort

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
