%define url_ver %(echo %{version} | cut -d. -f1,2)
%define _disable_rebuild_configure 1

Summary:	VCS support for Thunar file manager
Name:		thunar-vcs-plugin
Version:	0.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		https://goodies.xfce.org/projects/thunar-plugins/%{name}
Source0:	http://archive.xfce.org/src/thunar-plugins/%{name}/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(thunarx-3) >= 1.2.0
BuildRequires:	intltool
BuildRequires:	pkgconfig(exo-2) >= 0.6.0
BuildRequires:	pkgconfig(libxfce4util-1.0) >= 4.11
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.14.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.18.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.18.0
BuildRequires:	pkgconfig(apr-1) >= 0.9.7
BuildRequires:	subversion-devel >= 1.5
BuildRequires:	git
Suggests:	git

%description
The Thunar VCS Plugin adds Subversion actions to the context menu of thunar.
This gives a VCS integration to Thunar.

The current features are:
- Most of the svn action: add, blame, checkout, cleanup, commit, copy, delete,
  export, import, lock, log, move, properties, relocate, resolved, revert,
  status, switch, unlock, update.
- Subversion info in file properties dialog.
- Basic git support: add, blame, branch, clean, clone, log, move, reset,
  stash, status.


%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/thunarx-3/thunar-vcs-plugin.so
%{_libexecdir}/tvp-git-helper
%{_libexecdir}/tvp-svn-helper
%{_iconsdir}/hicolor/*/apps/*
