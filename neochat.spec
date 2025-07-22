%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define oname neochat
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: neochat
Version: 25.04.3
Release: %{?git:0.%{git}.}1
License: GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and BSD
Summary: Client for matrix, the decentralized communication protocol
URL: https://invent.kde.org/network/neochat

%if 0%{?git:1}
Source0: https://invent.kde.org/network/neochat/-/archive/%{gitbranch}/neochat-%{gitbranchd}.tar.bz2#/neochat-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/neochat-%{version}.tar.xz
%endif

BuildRequires: cmake(Qt6)
BuildRequires: cmake(QCoro6)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Location)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebView)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6Kirigami2)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6QmlNetwork)
BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(QuotientQt6)
BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6Purpose)
BuildRequires: pkgconfig(libcmark)
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(appstream-glib)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: qt6-qtbase-theme-gtk3
BuildRequires: qt6-qtmultimedia-gstreamer
Requires: hicolor-icon-theme
Requires: kf6-kirigami
Requires: %{_lib}KF6ItemModels
#Requires: qml(org.kde.kquickimageeditor)
#Requires: qt6-qtquickcontrols2
Requires: %{_lib}KF6SyntaxHighlighting
Requires: kirigami-addons-kde6
#Requires: qt6-qtlocation
Requires: %{_lib}Qt6Multimedia
Requires: kf6-kquickcharts
Requires: kquickimageeditor-qt6
Requires: qml(QtLocation) >= 6.0
Requires: kf6-prison
Requires: %{_lib}Qt6Positioning
BuildSystem: cmake
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
BuildOption: -DBUILD_WITH_QT6:BOOL=ON
%rename plasma6-neochat

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/%{oname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml
%{_datadir}/knotifications6/neochat.notifyrc
%{_datadir}/qlogging-categories6/neochat.categories
%{_datadir}/krunner/dbusplugins/plasma-runner-neochat.desktop
%{_mandir}/man1/neochat.1*
%{_qtdir}/plugins/kf6/purpose/neochatshareplugin.so
