//
// Created by Arseny Tolmachev on 2018/06/11.
//

#include "core/env.h"
#include "core/analysis/analysis_result.h"
#include "unidic-2.3.0-simple.spec.h"

#include <iostream>
#include <string>

using namespace jumanpp;

struct ResultOutputter
{
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
    core::analysis::StringField iType;
    core::analysis::StringField iForm;
    core::analysis::StringField fType;
    core::analysis::StringField fForm;
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

    Status initialize(const core::analysis::Analyzer &ana)
    {
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
        JPP_RETURN_IF_ERROR(output.stringField("iType", &iType));
        JPP_RETURN_IF_ERROR(output.stringField("iForm", &iForm));
        JPP_RETURN_IF_ERROR(output.stringField("fType", &fType));
        JPP_RETURN_IF_ERROR(output.stringField("fForm", &fForm));
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

    bool outputResult(const core::analysis::Analyzer &ana, std::ostream &os)
    {
        if (!resultFiller.reset(ana))
            return false;
        if (!resultFiller.fillTop1(&top1))
            return false;

        auto &output = ana.output();
        core::analysis::NodeWalker walker;

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
            os << iType[walker] << ',';
            os << iForm[walker] << ',';
            os << fType[walker] << ',';
            os << fForm[walker] << ',';
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
};

void dieOnError(Status s)
{
    if (!s)
    {
        std::cerr << s;
        exit(1);
    }
}

int main(int argc, const char *argv[])
{
    core::JumanppEnv env;
    dieOnError(env.loadModel(StringPiece::fromCString(argv[1])));

    env.setBeamSize(5);
    env.setGlobalBeam(6, 1, 5);

    jumanpp_generated::Unidic230Simple cg;
    dieOnError(env.initFeatures(&cg));

    core::analysis::Analyzer analyzer;

    dieOnError(env.makeAnalyzer(&analyzer));

    ResultOutputter out;
    dieOnError(out.initialize(analyzer));

    std::string input;
    while (std::getline(std::cin, input))
    {
        Status s = analyzer.analyze(input);
        if (!s)
        {
            std::cerr << "Failed to analyze [" << input << "]: " << s;
            continue;
        }
        out.outputResult(analyzer, std::cout);
    }

    return 0;
}