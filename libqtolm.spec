%define major 3
%define libpackage %mklibname qtolm %{major}
%define devpackage %mklibname -d qtolm

%undefine __cmake_in_source_build
%global appname QtOlm
%global libname lib%{appname}

Name: libqtolm
Version: 3.0.1
Release: 1

License: GPLv3+
URL: https://gitlab.com/b0/libqtolm/
Summary: Qt wrapper for libolm
Source0: https://gitlab.com/b0/libqtolm/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: ninja

%description
Special Qt wrapper for libolm library.

%package -n %{libpackage}
Group:		System/Libraries
Summary:	Library for special Qt wrapper for libolm.

%description -n %{libpackage}
Library for special Qt wrapper for libolm.

%package -n %{devpackage}
Summary: Development files for %{name}
Requires:	%{libpackage} = %{EVRD}

%description -n %{devpackage}
Development files for libQtOlm

%prep
%autosetup -n %{name}-v%{version}

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH="include/%{appname}"
%ninja_build

%install
%ninja_install -C build

%files -n %{libpackage}
%license LICENSE
%{_libdir}/%{libname}.so.%{major}*

%files -n %{devpackage}
%{_includedir}/%{appname}/
%{_libdir}/cmake/%{appname}/
%{_libdir}/pkgconfig/%{appname}.pc
%{_libdir}/%{libname}.so
