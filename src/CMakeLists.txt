include(../jumanpp/cmake/JumanppStaticFeatures.cmake)
jumanpp_gen_static(unidic-2.3.0-simple.spec Unidic230Simple JPP_US_CGDIR JPP_US_CG_SRC)

add_executable(jumanpp-unidic-simple
  jumanpp-unidic-simple.cc
  unidic_args.h unidic_args.cc
  unidic_output.h unidic_output.cc
  ${JPP_US_CG_SRC})
target_include_directories(jumanpp-unidic-simple PRIVATE ${JPP_US_CGDIR})
target_link_libraries(jumanpp-unidic-simple jpp_core)