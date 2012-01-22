#
%define		_state		stable
%define		orgname		kwallet
%define		qtver		4.8.0

Summary:	K Desktop Environment - KDE Wallet Manager
Name:		kde4-kwallet
Version:	4.8.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	346fea9e992b85bf8de285160dfb9705
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
Obsoletes:	kde4-kdeutils-kwalletmanager
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
K Desktop Environment - KDE Wallet Manager.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwalletmanager
%attr(755,root,root) %{_libdir}/kde4/kcm_kwallet.so
%{_desktopdir}/kde4/kwalletmanager-kwalletd.desktop
%{_desktopdir}/kde4/kwalletmanager.desktop
%{_datadir}/apps/kwalletmanager
%{_iconsdir}/hicolor/*/apps/kwalletmanager.png
%{_iconsdir}/hicolor/*/apps/kwalletmanager2.png
%{_datadir}/kde4/services/kwalletconfig.desktop
%{_datadir}/kde4/services/kwalletmanager_show.desktop
