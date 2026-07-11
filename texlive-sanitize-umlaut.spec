%global tl_name sanitize-umlaut
%global tl_revision 77720

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.0
Release:	%{tl_revision}.1
Summary:	Sanitize umlauts for MakeIndex and pdfLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sanitize-umlaut
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sanitize-umlaut.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sanitize-umlaut.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package sanitizes umlauts to be used directly in index entries for
MakeIndex and friends with pdfLaTeX. This means that inside \index an
umlaut can be used as "U or as U. In both cases, the letter is written
as "U into the raw index file for correct processing with MakeIndex and
pdfLaTeX.

