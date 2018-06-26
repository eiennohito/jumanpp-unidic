//
// Created by Arseny Tolmachev on 2018/06/20.
//

#include <unordered_map>
#include "unidic_args.h"
#include "args.h"
#include "unidic_output.h"
#include "core/analysis/analysis_result.h"
#include "core/impl/graphviz_format.h"
#include <iostream>

namespace jumanpp {

template<typename T, typename... Args>
std::unique_ptr<T> make_unique(Args &&... args) {
  return std::unique_ptr<T>(new T(std::forward<Args>(args)...));
};

Status UnidicArgs::parseArgs(UnidicArgs *result, int argc, const char *argv[]) {
  std::unordered_map<std::string, OutputFactory> outputMap{
    {"normal",   []() { return make_unique<NormalOutput>(); }},
    {"graphviz", []() { return make_unique<GraphVizOutput>(); }},
  };

  args::ArgumentParser parser{"Juman++ Unidic"};
  parser.helpParams.showProglineOptions = true;
  parser.helpParams.showValueName = true;

  args::HelpFlag help{parser, "HELP", "Print this help message", {'h', "help"}};
  args::ValueFlag<std::string> model{parser, "FILE", "Model file", {'d', "dicdir"}};
  args::MapFlag<std::string, OutputFactory> output{parser, "FORMAT", "Output format", {'O', "output-format-type"},
                                                   outputMap};
  args::Flag comments{parser, "COMMENT", "Handle Juman-style comments", {"handle-comments"}};

  try {
    if (!parser.ParseCLI(argc, argv)) {
      return JPPS_INVALID_PARAMETER << "Failed to parse command line: " << parser;
    }
  } catch (args::Help &h) {
    std::cerr << parser;
    exit(1);
  } catch (args::Error &e) {
    return JPPS_INVALID_PARAMETER << "Failed to parse command line: " << e.what();
  }

  if (model) {
    result->model_ = model.Get();
  }

  if (output) {
    result->outputFactory_ = output.Get();
  } else {
    result->outputFactory_ = outputMap["normal"];
  }

  result->handleComments_ = comments.Matched();

  return Status::Ok();
}

void dieOnError(Status s) {
  if (!s) {
    std::cerr << s;
    exit(1);
  }
}

} // namespace jumanpp