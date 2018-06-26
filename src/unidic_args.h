//
// Created by Arseny Tolmachev on 2018/06/20.
//

#ifndef JUMANPP_UNIDIC_UNIDIC_ARGS_H
#define JUMANPP_UNIDIC_UNIDIC_ARGS_H

#include <functional>

#include "util/status.hpp"
#include "core/analysis/analyzer.h"

namespace jumanpp {

struct UnidicOutput;

using OutputFactory = std::function<std::unique_ptr<UnidicOutput>()>;

struct UnidicArgs {
  std::string model_;
  OutputFactory outputFactory_;
  i32 beamSize_ = 5;
  i32 globalLeft_ = 6;
  i32 globalCheck_ = 1;
  i32 globalRight_ = 4;
  bool handleComments_ = false;

  static Status parseArgs(UnidicArgs* result, int argc, const char *argv[]);
};

struct UnidicOutput {
  virtual ~UnidicOutput() = default;
  virtual Status initialize(const core::analysis::Analyzer& ana, const UnidicArgs& args) = 0;
  virtual bool outputResult(const core::analysis::Analyzer& ana, StringPiece comment, std::ostream &os) = 0;
};

void dieOnError(Status s);

} // namespace jumanpp

#endif //JUMANPP_UNIDIC_UNIDIC_ARGS_H
