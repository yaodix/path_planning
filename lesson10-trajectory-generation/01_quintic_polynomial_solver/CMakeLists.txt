cmake_minimum_required(VERSION 3.10.0)
project(grader)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_FLAGS "-std=c++11")

# eigen
find_package(Eigen3 REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIRS})

add_executable(grader main.cpp )

