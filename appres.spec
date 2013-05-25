Summary:	List X application resource database
Name:		appres
Version:	1.0.4
Release:	1
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		appres-aarch64.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xt)

%description
The appres program prints the resources seen by an application (or
sub-hierarchy of an application) with the specified class and instance
names. It can be used to determine which resources a particular
program will load.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}
%make

%install
%makeinstall_std

%files
%{_bindir}/appres
%{_mandir}/man1/appres.1*

