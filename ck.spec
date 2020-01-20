%define major 0

%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		ck
Version:	0.7.0
Release:	1
Summary:	Library for high performance concurrent programming
Group:		Development/C
License:	BSD
URL:		http://concurrencykit.org
Source:		http://concurrencykit.org/releases/ck-%{version}.tar.gz

BuildRequires: gcc

%description
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures designed to
aid in the design and implementation of high performance concurrent systems. It
is designed to minimize dependencies on operating system-specific interfaces
and most of the interface relies only on a strict subset of the standard
library and more popular compiler extensions.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:        Library for high performance concurrent programming
Group:          System/Libraries

%description -n %{libname}
Concurrency Kit provides a plethora of concurrency primitives, safe memory
reclamation mechanisms and lock-less and lock-free data structures designed to
aid in the design and implementation of high performance concurrent systems. It
is designed to minimize dependencies on operating system-specific interfaces
and most of the interface relies only on a strict subset of the standard
library and more popular compiler extensions.

%files -n %{libname}
%doc LICENSE
%{_libdir}/libck.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:        Header files and libraries for CK development
Group:          Development/C
Requires:       %{libname} = %{EVRD}

%description -n %{devname}
Header files and static library for CK.

%files -n %{devname}
%{_libdir}/libck.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3.*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
./configure 		\
	--libdir=%{_libdir} 			\
	--includedir=%{_includedir}/%{name}	\
	--mandir=%{_mandir}			\
	--prefix=%{_prefix}
%make_build

%install
%make_install
# fix weird mode of the shared library
chmod 0755 %{buildroot}%{_libdir}/libck.so.*

# remove static library
rm %{buildroot}%{_libdir}/libck.a

%check
# Tests work fine locally but on ABF they either fail or hang forever...
# make check || :
