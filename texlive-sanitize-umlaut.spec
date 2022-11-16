Name:		texlive-sanitize-umlaut
Version:	63770
Release:	1
Summary:	Sanitize umlauts for MakeIndex and pdfLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sanitize-umlaut
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanitize-umlaut.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sanitize-umlaut.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package sanitizes umlauts to be used directly in index
entries for MakeIndex and friends with pdfLaTeX. This means
that inside \index an umlaut can be used as "U or as U. In both
cases, the letter is written as "U into the raw index file for
correct processing with MakeIndex and pdfLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/sanitize-umlaut
%doc %{_texmfdistdir}/doc/latex/sanitize-umlaut

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
