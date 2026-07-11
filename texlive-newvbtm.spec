%global tl_name newvbtm
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Define your own verbatim-like environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newvbtm
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines general purpose macro named \newverbatim to define your own
verbatim-like environment. It also has a supplementary style file
varvbtm.sty to provide set of macros for variants of verbatim, such as
tab emulation.

