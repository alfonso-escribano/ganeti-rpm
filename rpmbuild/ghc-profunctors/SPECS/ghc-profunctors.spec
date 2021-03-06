# generated by cabal-rpm-0.12.3
# https://fedoraproject.org/wiki/Packaging:Haskell

%global pkg_name profunctors
%global pkgver %{pkg_name}-%{version}

Name:           ghc-%{pkg_name}
Version:        4.4.1
Release:        1%{?dist}
Summary:        Profunctors

License:        BSD
Url:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-transformers-devel
# End cabal-rpm deps

%description
Profunctors.


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
This package provides the Haskell %{pkg_name} library development files.


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
%doc CHANGELOG.markdown README.markdown


%changelog
* Mon Apr 15 2019 Jun Futagawa <jfut@integ.jp> - 4.4.1-1
- Rebase spec file by cabal-rpm spec bifunctors-4.4.1

* Fri Jan  9 2015 Jun Futagawa <jfut@integ.jp> - 4.0.4-2
- Rebuild for ghc-transformers-compat update

* Tue Aug  5 2014 Jun Futagawa <jfut@integ.jp> - 4.0.4-1
- Removed ExclusiveArch
- Removed ghc_devel_package

* Tue Aug  5 2014 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.5
