cmake_minimum_required(VERSION 3.25)
project(Learning)

set(CMAKE_CXX_STANDARD 17)

add_executable(Learning src/templateTest.cpp src/main.cpp src/test.cpp src/test.h src/test.ui)

add_executable(templateTest src/templateTest.cpp)