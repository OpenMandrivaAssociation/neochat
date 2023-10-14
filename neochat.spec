%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

# Try avoid git in future, switch to upcoming stable release.
# Before update to next git or whatever please at least check if current version/git works and not crashing on desktop archs (x86_64 or znver1)
#define git 20211107
#define gitcommit 71d01593b141f12bcf6556f8fb3e4e41d8a2c1d3

Name: neochat
Version: 23.08.2
Release: %{?git:0.%{git}.}1
License: GPLv2 and GPLv2+ and GPLv3 and GPLv3+ and BSD
Summary: Client for matrix, the decentralized communication protocol
URL: https://invent.kde.org/network/neochat
%if 0%{?git:1}
Source0: https://invent.kde.org/network/neochat/-/archive/%{?git:master}%{!?git:v%{version}}/%{name}-%{?git:%{git}}%{!?git:%{version}}.tar.gz
%else
Source0: https://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif

BuildRequires: cmake(QCoro5)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KF5Kirigami2)
BuildRequires: cmake(KF5KirigamiAddons)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(Olm)
BuildRequires: cmake(QtOlm)
BuildRequires: cmake(Quotient)
BuildRequires: cmake(KQuickImageEditor)
BuildRequires: cmake(KF5QQC2DesktopStyle)
BuildRequires: pkgconfig(libcmark)
BuildRequires: cmake(ECM)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(appstream-glib)
BuildRequires: qml(org.kde.syntaxhighlighting)
Requires: hicolor-icon-theme
Requires: kirigami2
Requires: %{_lib}KF5ItemModels5
Requires: qml(org.kde.kquickimageeditor)
Requires: qt5-qtquickcontrols2
Requires: qml(org.kde.syntaxhighlighting)
Requires: kirigami-addons-kde5
Requires: qt5-qtlocation
Requires: qt5-qtmultimedia
Requires: kquickcharts

%description
Neochat is a client for Matrix, the decentralized communication protocol for
instant messaging. It is a fork of Spectral, using KDE frameworks, most
notably Kirigami, KConfig and KI18n.

%prep
%autosetup -n %{name}-%{version} -p1
export CC=gcc
export CXX=g++
%cmake_kde5

%build
# Switch to GCC because Clang 16 crashing at compiling time. Same with libquotient.
export CC=gcc
export CXX=g++
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --with-man

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.appdata.xml
%{_datadir}/knotifications5/%{name}.notifyrc
%{_datadir}/krunner/dbusplugins/plasma-runner-neochat.desktop
%{_mandir}/man1/neochat.1*
%{_datadir}/qlogging-categories5/neochat.categories
