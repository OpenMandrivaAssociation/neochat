%undefine __cmake_in_source_build

Name: neochat
Version: 1.0
Release: 1
License: GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and BSD
Summary: Client for matrix, the decentralized communication protocol
URL: https://invent.kde.org/network/neochat
Source0: https://invent.kde.org/network/neochat/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Widgets)

BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5DBusAddons)

BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Quotient)
BuildRequires: pkgconfig(libcmark)

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules

BuildRequires: pkgconfig(appstream-glib)
BuildRequires: ninja

Requires: hicolor-icon-theme
Requires: kf5-kirigami2%{?_isa}
Requires: kf5-kitemmodels%{?_isa}
Requires: qt5-qtquickcontrols2%{?_isa}

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
%autosetup -n %{name}-%{version} -p1
sed -e 's/5.76.0/5.75.0/g' -i CMakeLists.txt

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%ninja_build

%install
%ninja_install -C build

%files
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml
%{_datadir}/knotifications5/%{name}.notifyrc
