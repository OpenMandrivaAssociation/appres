Name:		appres
Version:	1.0.3
Release:	%mkrel 3
Summary:	List X application resource database
Group:		System/X11
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
The appres program prints the resources seen by an application (or
sub-hierarchy of an application) with the specified class and instance
names. It can be used to determine which resources a particular
program will load.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x 	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/appres
%{_mandir}/man1/appres.1*



%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2011.0
+ Revision: 662785
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 592583
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-2mdv2010.1
+ Revision: 522000
- rebuilt for 2010.1

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2010.0
+ Revision: 448646
- new release

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdv2010.0
+ Revision: 413036
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-5mdv2009.1
+ Revision: 349991
- 2009.1 rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2009.0
+ Revision: 220354
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2008.1
+ Revision: 148467
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 08 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-2mdv2008.0
+ Revision: 82308
- rebuild for 2008
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages extension


* Mon Feb 05 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.1-1mdv2007.0
+ Revision: 116380
- new upstream version: 1.0.1
- rebuild to fix cooker uploading
- Fixing some information on the specfile
- increment release
- Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix description

