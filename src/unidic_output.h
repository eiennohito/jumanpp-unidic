//
// Created by Arseny Tolmachev on 2018/06/20.
//

#ifndef JUMANPP_UNIDIC_UNIDIC_OUTPUT_H
#define JUMANPP_UNIDIC_UNIDIC_OUTPUT_H

#include <iostream>
#include "util/status.hpp"
#include "core/analysis/output.h"
#include "core/analysis/analysis_result.h"
#include "core/impl/graphviz_format.h"
#include "unidic_args.h"

namespace jumanpp {

struct UnidicFields : public virtual UnidicOutput {
  core::analysis::StringField surface;
  core::analysis::StringField pos1;
  core::analysis::StringField pos2;
  core::analysis::StringField pos3;
  core::analysis::StringField pos4;
  core::analysis::StringField cType;
  core::analysis::StringField cForm;
  core::analysis::StringField lForm;
  core::analysis::StringField lemma;
  core::analysis::StringField orth;
  core::analysis::StringField pron;
  core::analysis::StringField orthBase;
  core::analysis::StringField pronBase;
  core::analysis::StringField goshu;
  core::analysis::StringField iType;
  core::analysis::StringField iForm;
  core::analysis::StringField fType;
  core::analysis::StringField fForm;
  core::analysis::StringField iConType;
  core::analysis::StringField fConType;
  core::analysis::StringField type;
  core::analysis::StringField kana;
  core::analysis::StringField kanaBase;
  core::analysis::StringField form;
  core::analysis::StringField formBase;
  core::analysis::StringField aType;
  core::analysis::StringField aConType;
  core::analysis::StringField aModType;
  core::analysis::StringField lid;
  core::analysis::StringField lemma_id;

  core::analysis::AnalysisResult resultFiller;
  core::analysis::AnalysisPath top1;

  UnidicArgs args;

  Status initialize(const core::analysis::Analyzer &ana, const UnidicArgs& args) override;
};


struct GraphVizOutput: public virtual UnidicOutput {
  core::format::GraphVizFormat gvf;
  Status initialize(const core::analysis::Analyzer &ana, const UnidicArgs& args) override {
    core::format::GraphVizBuilder gvb;
    gvb.row({"surface"});
    gvb.row({"lemma"});
    gvb.row({"pos1", "pos2"});
    gvb.row({"cType", "cForm"});
    gvb.row({"pron"});
    return gvb.build(&gvf, 5);
  }

  bool outputResult(const core::analysis::Analyzer &ana, StringPiece comment, std::ostream &os) override {
    gvf.reset();
    dieOnError(gvf.initialize(ana.output()));
    dieOnError(gvf.render(ana));
    os << gvf.result();
    return true;
  }
};

struct NormalOutput : UnidicFields {
  bool outputResult(const core::analysis::Analyzer &ana, StringPiece comment, std::ostream &os) override;
};

} // namespace jumanpp

#endif //JUMANPP_UNIDIC_UNIDIC_OUTPUT_H
