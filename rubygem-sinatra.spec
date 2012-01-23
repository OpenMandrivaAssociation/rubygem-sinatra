# Generated from sinatra-1.2.6.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	sinatra

Summary:	Classy web-development dressed in a DSL
Name:		rubygem-%{rbname}

Version:	1.2.6
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://sinatra.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Classy web-development dressed in a DSL

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{ruby_gemdir}/gems/%{rbname}-%{version}/
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec


%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
