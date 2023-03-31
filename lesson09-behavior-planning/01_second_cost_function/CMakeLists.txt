cmake_minimum_required(VERSION 3.10.0)
project(cost)

set(CMAKE_BUILD_TYPE "Debug" CACHE STRING "set build type to debug")
set(CMAKE_CXX_FLAGS "-std=c++11")

# eigen
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIRS})

add_executable(cost main.cpp cost.cpp)

