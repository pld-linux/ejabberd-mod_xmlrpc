%define		snap	r943

Summary:	XML-RPC server for ejabberd
Summary(pl.UTF-8):	Natywne sterowniki do MySQL-a dla demona ejabberd
Name:		ejabberd-mod_xmlrpc
Version:	0
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
# svn export http://svn.process-one.net/ejabberd-modules/mod_xmlrpc/trunk ejabberd-mod_xmlrpc
Source0:	%{name}-%{snap}.tar.bz2
# Source0-md5:	4792e19865defb7fffd17bd63432994f
BuildRequires:	erlang >= R9C
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mod_xmlrpc is a module for ejabberd, a XMPP/Jabber server written in
Erlang. It starts a XML-RPC server and waits for external requests.
Implemented calls include statistics and user administration. This
allows external programs written in any language like websites or
administrative tools to communicate with ejabberd to get information
or to make changes without the need to know ejabberd internals.

%prep
%setup -q -n %{name}

%build
# ???

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ejabberd/ebin

install *.beam $RPM_BUILD_ROOT%{_libdir}/ejabberd/ebin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
