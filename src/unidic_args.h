//
// Created by Arseny Tolmachev on 2018/06/20.
//

#ifndef JUMANPP_UNIDIC_UNIDIC_ARGS_H
#define JUMANPP_UNIDIC_UNIDIC_ARGS_H

#include <functional>

#include "util/status.hpp"
#include "unidic_output.h"

namespace jumanpp {

struct UnidicArgs {
  std::string model_;
  OutputFactory outputFactory_;
  i32 beamSize_ = 5;
  i32 globalLeft_ = 6;
  i32 globalCheck_ = 1;
  i32 globalRight_ = 4;

  static Status parseArgs(UnidicArgs* result, int argc, const char *argv[]);
};


} // namespace jumanpp

#endif //JUMANPP_UNIDIC_UNIDIC_ARGS_H
