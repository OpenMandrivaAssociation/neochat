%define git 20210427
%define gitcommit 7e778d225baeefaf937ce8f022f86e10eb46e708

Name: neochat
Version: 1.0.1
Release: %{?git:0.%{git}.}1
License: GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and BSD
Summary: Client for matrix, the decentralized communication protocol
URL: https://invent.kde.org/network/neochat
# git archive --format=tar.gz -o ../neochat-$(date +%Y%m%d).tar.gz --prefix=neochat-master-7e778d225baeefaf937ce8f022f86e10eb46e708/ master
Source0: https://invent.kde.org/network/neochat/-/archive/%{?git:master}%{!?git:%{version}}/%{name}-%{?git:%{git}}%{!?git:%{version}}.tar.gz

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
BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(KF5QQC2DesktopStyle)
BuildRequires: pkgconfig(libcmark)
BuildRequires: cmake(ECM)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(appstream-glib)
Requires: hicolor-icon-theme
Requires: kirigami2
Requires: %{_lib}KF5ItemModels5
Requires: qml(org.kde.kquickimageeditor)
Requires: qt5-qtquickcontrols2

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
%autosetup -n %{name}-%{?git:master-%{gitcommit}}%{!?git:%{version}} -p1

%build
%cmake_kde5
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
