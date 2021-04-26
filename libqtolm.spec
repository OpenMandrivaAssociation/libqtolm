%define appname QtOlm
%define major 3
%define libname %mklibname %{appname} %{major}
%define develname %mklibname -d %{appname}

%undefine __cmake_in_source_build

Summary: Qt wrapper for libolm
Name: libqtolm
Version: 3.0.1
Release: 3
License: GPLv3+
Group: System/libraries
URL: https://gitlab.com/b0/libqtolm/
Source0: https://gitlab.com/b0/libqtolm/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Network)
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: ninja

%description
Special Qt wrapper for libolm library.

%package -n %{libname}
Summary: Library for special Qt wrapper for libolm.
Group: System/Libraries
%rename %{_lib}qtolm3

%description -n %{libname}
Library for special Qt wrapper for libolm.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
%rename %{_lib}qtolm-devel

%description -n %{develname}
Development files for libQtOlm.

%prep
%autosetup -n %{name}-v%{version}

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_INCLUDEDIR:PATH="include/%{appname}"

%ninja_build

%install
%ninja_install -C build

%files -n %{libname}
%license LICENSE
%{_libdir}/lib*%{appname}*.so.%{major}*

%files -n %{develname}
%{_includedir}/%{appname}
%{_libdir}/cmake/%{appname}
%{_libdir}/pkgconfig/%{appname}.pc
%{_libdir}/lib*%{appname}.so
