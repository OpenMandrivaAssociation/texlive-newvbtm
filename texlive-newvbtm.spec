Name:		texlive-newvbtm
Version:	23996
Release:	2
Summary:	Define your own verbatim-like environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newvbtm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines general purpose macro named \newverbatim to define your
own verbatim-like environment. It also has a supplementary
style file varvbtm.sty to provide set of macros for variants of
verbatim, such as tab emulation.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/newvbtm/newvbtm.sty
%{_texmfdistdir}/tex/latex/newvbtm/varvbtm.sty
%doc %{_texmfdistdir}/doc/latex/newvbtm/README
%doc %{_texmfdistdir}/doc/latex/newvbtm/newvbtm-man.pdf
%doc %{_texmfdistdir}/doc/latex/newvbtm/newvbtm-man.tex
#- source
%doc %{_texmfdistdir}/source/latex/newvbtm/newvbtm.dtx
%doc %{_texmfdistdir}/source/latex/newvbtm/newvbtm.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
