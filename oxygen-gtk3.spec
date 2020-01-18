
Name:       oxygen-gtk3
Epoch:      1
Version:    1.1.4
Release:    5%{?dist}
Summary:    Oxygen GTK+3 theme

Group:      User Interface/Desktops
License:    LGPLv2+
URL:        https://projects.kde.org/projects/playground/artwork/oxygen-gtk
Source0:    ftp://ftp.kde.org/pub/kde/stable/oxygen-gtk3/%{version}/src/%{name}-%{version}.tar.bz2

Patch0:     oxygen-gtk3-make-buttons-working-as-expected.patch
Patch1:     oxygen-gtk3-only-register-menubar-when-widget-is-valid.patch

BuildRequires:	cmake
BuildRequires:	gtk3-devel

%description
Oxygen-Gtk is a port of the default KDE widget theme (Oxygen), to gtk.

It's primary goal is to ensure visual consistency between gtk-based and
qt-based applications running under KDE. A secondary objective is to also
have a stand-alone nice looking gtk theme that would behave well on other
Desktop Environments.

Unlike other attempts made to port the KDE oxygen theme to gtk, this
attempt does not depend on Qt (via some Qt to Gtk conversion engine),
nor does render the widget appearance via hard-coded pixmaps, which
otherwise breaks every time some setting is changed in KDE.


%prep
%setup -q

%patch0 -p1 -b .make-buttons-working-as-expected
%patch1 -p1 -b .only-register-menubar-when-widget-is-valid

%build

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} \
  -DOXYGEN_FORCE_KDE_ICONS_AND_FONTS=0 \
  ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf $RPM_BUILD_ROOT
make install/fast DESTDIR=$RPM_BUILD_ROOT -C %{_target_platform}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/oxygen-gtk3-demo
%{_libdir}/gtk-3.0/*/theming-engines/liboxygen-gtk.so
%{_datadir}/themes/oxygen-gtk/


%changelog
* Mon Sep 19 2016 Jan Grulich <jgrulich@redhat.com> - 1:1.1.4-5
- Avoid firefox crash at startup
  Resolves: bz#1376205

* Tue Mar 22 2016 Jan Grulich <jgrulich@redhat.com> - 1:1.1.4-4
- Make buttons work as expected with GTK applications
  Resolves: bz#1295043

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1:1.1.4-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:1.1.4-2
- Mass rebuild 2013-12-27

* Fri May 31 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.1.4-1
- oxygen-gtk3-1.1.4

* Mon Apr 22 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.1.3-1
- oxygen-gtk3-1.1.3

* Wed Jan 30 2013 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.1.2-1
- oxygen-gtk3-1.1.2
- remove -DENABLE_INNER_SHADOWS_HACK=0 (fixed anaconda issue)

* Wed Oct 17 2012 Rex Dieter <rdieter@fedoraproject.org> 1.1.1-2
- workaround anaconda main menu not visible in F18 Beta TC2 KDE Live (#864058)
- -DENABLE_INNER_SHADOWS_HACK=0

* Fri Oct  5 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.1.1-1
- oxygen-gtk3-1.1.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.1.0-1
- oxygen-gtk3-1.1.0

* Fri Jun 15 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.5-1
- oxygen-gtk3-1.0.5

* Mon May 14 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.4-1
- oxygen-gtk3-1.0.4

* Sat Apr 14 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.3-1
- oxygen-gtk3-1.0.3

* Sat Mar 24 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.2.1-1
- oxygen-gtk3-1.0.2-1
- drop -DENABLE_INNER_SHADOWS_HACK=0

* Mon Mar 12 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.2-2
- ENABLE_INNER_SHADOWS_HACK=0 workaround for kde#295831

* Mon Mar 12 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.2-1
- oxygen-gtk3-1.0.2
- drop BR: dbus-glib-devel

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.1-2
- Rebuilt for c++ ABI breakage

* Thu Feb 16 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.1-1
- oxygen-gtk3-1.0.1
- drop blacklist patch

* Mon Feb 13 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.0-2
- Blacklist Evolution's MessageList from Inner Shadow hack (kde#292278)

* Tue Jan 17 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1:1.0.0-1
- oxygen-gtk3-1.0.0

* Thu Jan 12 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-0.3.20120112
- new snapshot fixes tooltips related bugs (kde#291106,291107,291198)

* Mon Jan  9 2012 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-0.2.20120109
- new snapshot fixes warnings when building against gtk-3.3.x (kde#291007)

* Mon Dec 19 2011 Alexey Kurov <nucleo@fedoraproject.org> - 1.2.0-0.1.20111219
- Initial RPM release
