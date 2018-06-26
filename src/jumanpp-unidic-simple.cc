//
// Created by Arseny Tolmachev on 2018/06/11.
//

#include "core/env.h"
#include "unidic-2.3.0-simple.spec.h"

#include <iostream>
#include <string>
#include "unidic_args.h"

using namespace jumanpp;

int main(int argc, const char *argv[]) {
  core::JumanppEnv env;
  UnidicArgs args;
  dieOnError(UnidicArgs::parseArgs(&args, argc, argv));
  dieOnError(env.loadModel(args.model_));

  env.setBeamSize(args.beamSize_);
  env.setGlobalBeam(args.globalLeft_, args.globalCheck_, args.globalRight_);

  jumanpp_generated::Unidic230Simple cg;
  dieOnError(env.initFeatures(&cg));

  core::analysis::Analyzer analyzer;

  dieOnError(env.makeAnalyzer(&analyzer));

  auto out = args.outputFactory_();
  dieOnError(out->initialize(analyzer, args));

  std::string comment;
  std::string input;
  while (std::getline(std::cin, input)) {
    if (args.handleComments_) {
      if (input.size() > 1 && input[0] == '#') {
        comment.assign(input.begin() + 1, input.end());
        continue;
      }
    }

    Status s = analyzer.analyze(input);
    if (!s) {
      std::cerr << "Failed to analyze [" << input << "]: " << s;
      continue;
    }
    out->outputResult(analyzer, comment, std::cout);
  }

  return 0;
}