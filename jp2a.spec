Name:		jp2a
Version:	1.0.6
Release:	1
License:	GPLv2
Url:		https://sourceforge.net/projects/jp2a
Source0:	http://sourceforge.net/projects/jp2a/files/jp2a/%{version}/%{name}-%{version}.tar.bz2
Summary:	Converts JPG images to ASCII
Group:		Graphics
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ncursesw)

%description
jp2a is a small utility that converts JPEG images to ASCII.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc LICENSES AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
