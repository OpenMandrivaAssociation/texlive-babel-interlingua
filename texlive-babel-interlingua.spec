Name:		texlive-babel-interlingua
Version:	30276
Release:	1
Summary:	TeXLive babel-interlingua package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-interlingua.r30276.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-interlingua.doc.r30276.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-interlingua.source.r30276.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive babel-interlingua package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-interlingua/interlingua.ldf
%doc %{_texmfdistdir}/doc/generic/babel-interlingua/interlingua.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-interlingua/interlingua.dtx
%doc %{_texmfdistdir}/source/generic/babel-interlingua/interlingua.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
