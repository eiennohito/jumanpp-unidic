//
// Created by Arseny Tolmachev on 2018/06/20.
//

#include "unidic_output.h"

namespace jumanpp {


Status UnidicFields::initialize(const core::analysis::Analyzer &ana, const UnidicArgs& args) {
  this->args = args;

  auto &output = ana.output();
  JPP_RETURN_IF_ERROR(output.stringField("surface", &surface));
  JPP_RETURN_IF_ERROR(output.stringField("pos1", &pos1));
  JPP_RETURN_IF_ERROR(output.stringField("pos2", &pos2));
  JPP_RETURN_IF_ERROR(output.stringField("pos3", &pos3));
  JPP_RETURN_IF_ERROR(output.stringField("pos4", &pos4));
  JPP_RETURN_IF_ERROR(output.stringField("cType", &cType));
  JPP_RETURN_IF_ERROR(output.stringField("cForm", &cForm));
  JPP_RETURN_IF_ERROR(output.stringField("lForm", &lForm));
  JPP_RETURN_IF_ERROR(output.stringField("lemma", &lemma));
  JPP_RETURN_IF_ERROR(output.stringField("orth", &orth));
  JPP_RETURN_IF_ERROR(output.stringField("pron", &pron));
  JPP_RETURN_IF_ERROR(output.stringField("orthBase", &orthBase));
  JPP_RETURN_IF_ERROR(output.stringField("pronBase", &pronBase));
  JPP_RETURN_IF_ERROR(output.stringField("goshu", &goshu));
  JPP_RETURN_IF_ERROR(output.stringField("iType", &iType));
  JPP_RETURN_IF_ERROR(output.stringField("iForm", &iForm));
  JPP_RETURN_IF_ERROR(output.stringField("fType", &fType));
  JPP_RETURN_IF_ERROR(output.stringField("fForm", &fForm));
  JPP_RETURN_IF_ERROR(output.stringField("iConType", &iConType));
  JPP_RETURN_IF_ERROR(output.stringField("fConType", &fConType));
  JPP_RETURN_IF_ERROR(output.stringField("type", &type));
  JPP_RETURN_IF_ERROR(output.stringField("kana", &kana));
  JPP_RETURN_IF_ERROR(output.stringField("kanaBase", &kanaBase));
  JPP_RETURN_IF_ERROR(output.stringField("form", &form));
  JPP_RETURN_IF_ERROR(output.stringField("formBase", &formBase));
  JPP_RETURN_IF_ERROR(output.stringField("aType", &aType));
  JPP_RETURN_IF_ERROR(output.stringField("aConType", &aConType));
  JPP_RETURN_IF_ERROR(output.stringField("aModType", &aModType));
  JPP_RETURN_IF_ERROR(output.stringField("lid", &lid));
  JPP_RETURN_IF_ERROR(output.stringField("lemma_id", &lemma_id));
  return Status::Ok();
}

bool NormalOutput::outputResult(const core::analysis::Analyzer &ana, StringPiece comment, std::ostream &os) {
  if (!resultFiller.reset(ana))
    return false;
  if (!resultFiller.fillTop1(&top1))
    return false;

  auto &output = ana.output();
  core::analysis::NodeWalker walker;

  if (args.handleComments_ && !comment.empty()) {
    os << '#' << comment << '\n';
  }

  core::analysis::ConnectionPtr cptr{};
  while (top1.nextBoundary())
  {
    if (!top1.nextNode(&cptr) || !output.locate(cptr.latticeNodePtr(), &walker) || !walker.next())
    {
      return false;
    }

    if (walker.eptr().isSpecial() && type[walker] == "未知語") {
      os << surface[walker] << '\t';
      os << pos1[walker] << ',';
      os << pos2[walker] << ',';
      os << pos3[walker] << ',';
      os << pos4[walker] << ',';
      os << cType[walker] << ',';
      os << cForm[walker] << '\n';
      continue;
    }

    os << surface[walker] << '\t';
    os << pos1[walker] << ',';
    os << pos2[walker] << ',';
    os << pos3[walker] << ',';
    os << pos4[walker] << ',';
    os << cType[walker] << ',';
    os << cForm[walker] << ',';
    os << lForm[walker] << ',';
    os << lemma[walker] << ',';
    os << orth[walker] << ',';
    os << pron[walker] << ',';
    os << orthBase[walker] << ',';
    os << pronBase[walker] << ',';
    os << goshu[walker] << ',';
    os << iType[walker] << ',';
    os << iForm[walker] << ',';
    os << fType[walker] << ',';
    os << fForm[walker] << ',';
    os << iConType[walker] << ',';
    os << fConType[walker] << ',';
    os << type[walker] << ',';
    os << kana[walker] << ',';
    os << kanaBase[walker] << ',';
    os << form[walker] << ',';
    os << formBase[walker] << ',';
    os << aType[walker] << ',';
    os << aConType[walker] << ',';
    os << aModType[walker] << ',';
    os << lid[walker] << ',';
    os << lemma_id[walker] << '\n';
  }
  os << "EOS" << std::endl;
  return true;
}

} // namespace jumanpp