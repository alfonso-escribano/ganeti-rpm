# generated by cabal-rpm-0.12.3
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name generic-deriving
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        1.6.3
Release:        2%{?dist}
Summary:        Generic programming library for generalised deriving

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-template-haskell-devel
# End cabal-rpm deps

%description
This package provides functionality for generalising the deriving mechanism in
Haskell to arbitrary classes. It was first described in the paper:

* /A generic deriving mechanism for Haskell/. Jose Pedro Magalhaes, Atze
Dijkstra, Johan Jeuring, and Andres Loeh. Haskell'10.

The current implementation integrates with the new GHC Generics. See
<http://www.haskell.org/haskellwiki/GHC.Generics> for more information.
Template Haskell code is provided for supporting GHC before version 7.2.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


%prep
%setup -q -n %{pkgver}


%build
%ghc_lib_build


%install
%ghc_lib_install


%post devel
%ghc_pkg_recache


%postun devel
%ghc_pkg_recache


%files -f %{name}.files
%license LICENSE


%files devel -f %{name}-devel.files
%doc examples


%changelog
* Mon Apr 15 2019 Jun Futagawa <jfut@integ.jp> - 1.6.3-2
- Rebase spec file by cabal-rpm spec generic-deriving-1.6.3

* Tue Aug  5 2014 Jun Futagawa <jfut@integ.jp> - 1.6.3-1
- Removed ExclusiveArch
- Removed ghc_devel_package

* Tue Aug  5 2014 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.5
