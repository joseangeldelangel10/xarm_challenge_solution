# Install script for directory: /home/leonardonava/ManipulatorsFeb2022-Students/04_03_2022/challenge/xarm_challenge/src/xarm_ros/examples/multi_xarm5

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/leonardonava/ManipulatorsFeb2022-Students/04_03_2022/challenge/xarm_challenge/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/leonardonava/ManipulatorsFeb2022-Students/04_03_2022/challenge/xarm_challenge/build/xarm_ros/examples/multi_xarm5/catkin_generated/installspace/multi_xarm5.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/multi_xarm5/cmake" TYPE FILE FILES
    "/home/leonardonava/ManipulatorsFeb2022-Students/04_03_2022/challenge/xarm_challenge/build/xarm_ros/examples/multi_xarm5/catkin_generated/installspace/multi_xarm5Config.cmake"
    "/home/leonardonava/ManipulatorsFeb2022-Students/04_03_2022/challenge/xarm_challenge/build/xarm_ros/examples/multi_xarm5/catkin_generated/installspace/multi_xarm5Config-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/multi_xarm5" TYPE FILE FILES "/home/leonardonava/ManipulatorsFeb2022-Students/04_03_2022/challenge/xarm_challenge/src/xarm_ros/examples/multi_xarm5/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/multi_xarm5" TYPE DIRECTORY FILES "/home/leonardonava/ManipulatorsFeb2022-Students/04_03_2022/challenge/xarm_challenge/src/xarm_ros/examples/multi_xarm5/launch")
endif()
