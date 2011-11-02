Name:		texlive-newvbtm
Version:	1.1
Release:	1
Summary:	Define your own verbatim-like environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/newvbtm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newvbtm.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Defines general purpose macro named \newverbatim to define your
own verbatim-like environment. It also has a supplementary
style file varvbtm.sty to provide set of macros for variants of
verbatim, such as tab emulation.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
