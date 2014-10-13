Name:           ros-indigo-stdr-simulator
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS stdr_simulator package

Group:          Development/Libraries
License:        GPLv3
URL:            http://stdr-simulator-ros-pkg.github.io
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-stdr-gui
Requires:       ros-indigo-stdr-launchers
Requires:       ros-indigo-stdr-msgs
Requires:       ros-indigo-stdr-parser
Requires:       ros-indigo-stdr-resources
Requires:       ros-indigo-stdr-robot
Requires:       ros-indigo-stdr-samples
Requires:       ros-indigo-stdr-server
BuildRequires:  ros-indigo-catkin

%description
A simple, flexible and scalable 2D multi-robot simulator.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Oct 13 2014 Chris Zalidis <zalidis@gmail.com> - 0.2.0-0
- Autogenerated by Bloom

