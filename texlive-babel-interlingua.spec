%global tl_name babel-interlingua
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Babel support for Interlingua
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/interlingua
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-interlingua.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-interlingua.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-interlingua.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of
Interlingua in babel. Translations to Interlingua of standard "LaTeX
names" (no shortcuts are provided). Interlingua itself is an auxiliary
language, built from the common vocabulary of Spanish/Portuguese,
English, Italian and French, with some normalisation of spelling.

