#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# for your packages to be recognized by python
d = generate_distutils_setup(
 packages=['check_odometry', 'check_odometry_ros'],
 package_dir={'check_odometry': 'common/src/check_odometry', 'check_odometry_ros': 'ros/src/check_odometry_ros'}
)

setup(**d)
