%{?scl:%scl_package nodejs-path-is-absolute}
%{!?scl:%global pkg_name %{name}}

%global npm_name path-is-absolute
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-path-is-absolute
Version:	1.0.0
Release:	1%{?dist}
Summary:	Node.js 0.12 path.isAbsolute() ponyfill
Url:		https://github.com/sindresorhus/path-is-absolute
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
%endif

%description
Node.js 0.12 path.isAbsolute() ponyfill

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/path-is-absolute

%doc readme.md license

%changelog
* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- Initial build
