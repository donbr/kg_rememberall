# Combined Context for LLM

Source Directory: ../data/raw/GLiNER
Generated On: 2025-01-13 21:59:07

## SOURCE:  https://github.com/urchade/GLiNER

- refer to README for citation details.

## Directory Summary

* .png: 3 files
* .jpg: 1 files
* .py: 50 files
* .txt: 1 files
* .toml: 1 files
* .md: 3 files
* No extension: 1 files
* .json: 1 files
* .yaml: 4 files

## Table of Contents

- [Combined Context for LLM](#combined-context-for-llm)
  - [SOURCE:  https://github.com/urchade/GLiNER](#source--httpsgithubcomurchadegliner)
  - [Directory Summary](#directory-summary)
  - [Table of Contents](#table-of-contents)
  - [File: image.png](#file-imagepng)
  - [File: demo.jpg](#file-demojpg)
  - [File: demo.py](#file-demopy)
  - [File: requirements.txt](#file-requirementstxt)
  - [File: pyproject.toml](#file-pyprojecttoml)
  - [File: README.md](#file-readmemd)
    - [Usage](#usage)
      - [Expected Output](#expected-output)
  - [🌟 Maintainers](#-maintainers)
  - [👨‍💻 Model Authors](#-model-authors)
  - [📚 Citation](#-citation)
  - [Support and funding](#support-and-funding)
  - [File: train.py](#file-trainpy)
  - [File: eval.py](#file-evalpy)
  - [File: RELEASE.md](#file-releasemd)
    - [Step 2: (Optional) Make sure all tests pass](#step-2-optional-make-sure-all-tests-pass)
    - [Step 3: Add a tag for your release](#step-3-add-a-tag-for-your-release)
    - [Step 4: (Optional) Prepare the release notes](#step-4-optional-prepare-the-release-notes)
    - [Step 5: Create the wheels for your release](#step-5-create-the-wheels-for-your-release)
    - [Step 6: Upload your package on PyPI test](#step-6-upload-your-package-on-pypi-test)
    - [Step 7: Publish on PyPI](#step-7-publish-on-pypi)
    - [Step 8: (Optional) Publish your release notes](#step-8-optional-publish-your-release-notes)
    - [Step 9: Bump the dev version on the main branch](#step-9-bump-the-dev-version-on-the-main-branch)
    - [Install via Conda](#install-via-conda)
    - [Install from Source](#install-from-source)
    - [🚀 Basic Use Case](#-basic-use-case)
      - [Expected Output](#expected-output-1)
    - [🔌 Usage with spaCy](#-usage-with-spacy)
      - [Expected Output](#expected-output-2)
  - [Multitask Usage](#multitask-usage)
    - [Classification](#classification)
      - [Quick Usage Examples](#quick-usage-examples)
    - [Question-Answering](#question-answering)
      - [Quick Usage Examples](#quick-usage-examples-1)
    - [Relation Extraction](#relation-extraction)
      - [Quick Usage Examples](#quick-usage-examples-2)
      - [Construct relations extraction pipeline with utca](#construct-relations-extraction-pipeline-with-utca)
    - [Open Information Extraction](#open-information-extraction)
      - [Quick Usage Examples](#quick-usage-examples-3)
    - [Summariztion](#summariztion)
      - [Quick Usage Examples](#quick-usage-examples-4)
  - [📊 NER Benchmark Results](#-ner-benchmark-results)
  - [ONNX convertion:](#onnx-convertion)
  - [🛠 Areas of Improvements / research](#-areas-of-improvements--research)
  - [File: custom\_train.py](#file-custom_trainpy)
  - [File: data/process\_pilener.py](#file-dataprocess_pilenerpy)
  - [File: data/process\_nuner.py](#file-dataprocess_nunerpy)
  - [File: examples/sample\_data.json](#file-examplessample_datajson)
  - [File: examples/convert\_to\_onnx.py](#file-examplesconvert_to_onnxpy)
  - [File: examples/synthetic\_data\_generation.py](#file-examplessynthetic_data_generationpy)
  - [File: examples/load\_local\_model.py](#file-examplesload_local_modelpy)
  - [File: examples/exal\_example\_conll.py](#file-examplesexal_example_conllpy)
  - [File: examples/gliner\_spacy\_demo.py](#file-examplesgliner_spacy_demopy)
  - [File: examples/quickstart.py](#file-examplesquickstartpy)
  - [File: examples/finetune.py](#file-examplesfinetunepy)
  - [File: configs/config\_span.yaml](#file-configsconfig_spanyaml)
  - [File: configs/config\_token.yaml](#file-configsconfig_tokenyaml)
  - [File: configs/config.yaml](#file-configsconfigyaml)
  - [File: configs/config\_biencoder.yaml](#file-configsconfig_biencoderyaml)
  - [File: logo/FI Group.png](#file-logofi-grouppng)
  - [File: logo/FI\_COMPLET\_CW.png](#file-logofi_complet_cwpng)
  - [File: gliner/__init__.py](#file-glinerinitpy)
  - [File: gliner/model.py](#file-glinermodelpy)
  - [File: gliner/utils.py](#file-glinerutilspy)
  - [File: gliner/config.py](#file-glinerconfigpy)
  - [File: gliner/evaluation/evaluator.py](#file-glinerevaluationevaluatorpy)
  - [File: gliner/evaluation/__init__.py](#file-glinerevaluationinitpy)
  - [File: gliner/evaluation/evaluate.py](#file-glinerevaluationevaluatepy)
  - [File: gliner/onnx/__init__.py](#file-glineronnxinitpy)
  - [File: gliner/onnx/model.py](#file-glineronnxmodelpy)
  - [File: gliner/data\_processing/__init__.py](#file-glinerdata_processinginitpy)
  - [File: gliner/data\_processing/processor.py](#file-glinerdata_processingprocessorpy)
  - [File: gliner/data\_processing/tokenizer.py](#file-glinerdata_processingtokenizerpy)
  - [File: gliner/data\_processing/dataset.py](#file-glinerdata_processingdatasetpy)
  - [File: gliner/data\_processing/utils.py](#file-glinerdata_processingutilspy)
  - [File: gliner/data\_processing/collator.py](#file-glinerdata_processingcollatorpy)
  - [File: gliner/modeling/__init__.py](#file-glinermodelinginitpy)
  - [File: gliner/modeling/loss\_functions.py](#file-glinermodelingloss_functionspy)
  - [File: gliner/modeling/span\_rep.py](#file-glinermodelingspan_reppy)
  - [File: gliner/modeling/base.py](#file-glinermodelingbasepy)
  - [File: gliner/modeling/layers.py](#file-glinermodelinglayerspy)
  - [File: gliner/modeling/scorers.py](#file-glinermodelingscorerspy)
  - [File: gliner/modeling/encoder.py](#file-glinermodelingencoderpy)
  - [File: gliner/training/__init__.py](#file-glinertraininginitpy)
  - [File: gliner/training/trainer.py](#file-glinertrainingtrainerpy)
  - [File: gliner/multitask/open\_extraction.py](#file-glinermultitaskopen_extractionpy)
  - [File: gliner/multitask/classification.py](#file-glinermultitaskclassificationpy)
  - [File: gliner/multitask/question\_answering.py](#file-glinermultitaskquestion_answeringpy)
  - [File: gliner/multitask/__init__.py](#file-glinermultitaskinitpy)
  - [File: gliner/multitask/base.py](#file-glinermultitaskbasepy)
  - [File: gliner/multitask/summarization.py](#file-glinermultitasksummarizationpy)
  - [File: gliner/multitask/relation\_extraction.py](#file-glinermultitaskrelation_extractionpy)
  - [File: gliner/decoding/decoder.py](#file-glinerdecodingdecoderpy)
  - [File: gliner/decoding/__init__.py](#file-glinerdecodinginitpy)
  - [File: gliner/decoding/utils.py](#file-glinerdecodingutilspy)
  - [File: tests/test\_models.py](#file-teststest_modelspy)
  - [File: tests/test\_features\_selection.py](#file-teststest_features_selectionpy)

## File: image.png

<a name='file-image.png'></a>
*Description*: No specific description available.

*This file is binary and cannot be displayed as text.*
## File: demo.jpg

<a name='file-demo.jpg'></a>
*Description*: No specific description available.

*This file is binary and cannot be displayed as text.*
## File: demo.py

<a name='file-demo.py'></a>
*Description*: This is a Python script.

```python
from typing import Dict, Union
from gliner import GLiNER
import gradio as gr

model = GLiNER.from_pretrained("model/", load_tokenizer=True)

examples = [
    [
        "Libretto by Marius Petipa, based on the 1822 novella ``Trilby, ou Le Lutin d'Argail`` by Charles Nodier, first presented by the Ballet of the Moscow Imperial Bolshoi Theatre on January 25/February 6 (Julian/Gregorian calendar dates), 1870, in Moscow with Polina Karpakova as Trilby and Ludiia Geiten as Miranda and restaged by Petipa for the Imperial Ballet at the Imperial Bolshoi Kamenny Theatre on January 17–29, 1871 in St. Petersburg with Adèle Grantzow as Trilby and Lev Ivanov as Count Leopold.",
        "person, book, location, date, actor, character",
        0.3,
        True,
    ],
    [
        """
* Data Scientist, Data Analyst, or Data Engineer with 1+ years of experience.
* Experience with technologies such as Docker, Kubernetes, or Kubeflow
* Machine Learning experience preferred
* Experience with programming languages such as Python, C++, or SQL preferred
* Experience with technologies such as Databricks, Qlik, TensorFlow, PyTorch, Python, Dash, Pandas, or NumPy preferred
* BA or BS degree
* Active Secret OR Active Top Secret or Active TS/SCI clearance
""",
        "software package, programing language, software tool, degree, job title",
        0.3,
        False,
    ],
    [
        "However, both models lack other frequent DM symptoms including the fibre-type dependent atrophy, myotonia, cataract and male-infertility.",
        "disease, symptom",
        0.3,
        False,
    ],
    [
        "Synergy between signal transduction pathways is obligatory for expression of c-fos in B and T cell lines: implication for c-fos control via surface immunoglobulin and T cell antigen receptors.",
        "DNA, RNA, cell line, cell type, protein",
        0.3,
        False,
    ],
    [
        "The choice of the encoder and decoder modules of dnpg can be quite flexible, for instance long short term memory networks (lstm) or convolutional neural network (cnn).",
        "short acronym, long acronym",
        0.3,
        False,
    ],
    [
        "Amelia Earhart flew her single engine Lockheed Vega 5B across the Atlantic to Paris.",
        "person, company, location, airplane",
        0.3,
        True,
    ],
    [
        "Feldman is a contributor to NBC Sports Boston's ``State of the Revs`` and ``Revolution Postgame Live`` programs as well as to 98.5 the SportsHub, SiriusXM FC's MLS coverage and to other New England and national radio outlets and podcasts.",
        "person, company, location",
        0.3,
        False,
    ],
    [
        "On 25 July 1948, on the 39th anniversary of Bleriot's crossing of the English Channel, the Type 618 Nene-Viking flew Heathrow to Paris (Villacoublay) in the morning carrying letters to Bleriot's widow and son (secretary of the FAI), who met it at the airport.",
        "date, location, person, organization",
        0.3,
        False,
    ],
    [
        "Leo & Ian won the 1962 Bathurst Six Hour Classic at Mount Panorama driving a Daimler SP250 sports car, (that year the 500 mile race for touring cars were held at Phillip Island)",
        "person, date, location, organization, competition",
        0.3,
        False,
    ],
    [
        "The Shore Line route of the CNS & M until 1955 served, from south to north, the Illinois communities of Chicago, Evanston, Wilmette, Kenilworth, Winnetka, Glencoe, Highland Park, Highwood, Fort Sheridan, Lake Forest, Lake Bluff, North Chicago, Waukegan, Zion, and Winthrop Harbor as well as Kenosha, Racine, and Milwaukee (the ``KRM'') in Wisconsin.",
        "location, organization, date",
        0.3,
        False,
    ],
    [
        "Comet C/2006 M4 (SWAN) is a non-periodic comet discovered in late June 2006 by Robert D. Matson of Irvine, California and Michael Mattiazzo of Adelaide, South Australia in publicly available images of the Solar and Heliospheric Observatory (SOHO).",
        "person, organization, date, location",
        0.3,
        False,
    ],
    [
        "From November 29, 2011 to March 31, 2012, Karimloo returned to ``Les Misérables`` to play the lead role of Jean Valjean at The Queen's Theatre, London, for which he won the 2013 Theatregoers' Choice Award for Best Takeover in a Role.",
        "person, actor, award, date, location",
        0.3,
        False,
    ],
    [
        "A Mexicali health clinic supported by former Baja California gubernatorial candidate Enrique Acosta Fregoso (PRI) was closed on June 15 after selling a supposed COVID-19 ``cure'' for between MXN $10,000 and $50,000.",
        "location, organization, person, date, currency",
        0.3,
        False,
    ],
    [
        "Built in 1793, it was the home of Mary Young Pickersgill when she moved to Baltimore in 1806 and the location where she later sewed the ``Star Spangled Banner'', in 1813, the huge out-sized garrison flag that flew over Fort McHenry at Whetstone Point in Baltimore Harbor in the summer of 1814 during the British Royal Navy attack in the Battle of Baltimore during the War of 1812.",
        "date, person, location, organization, event, flag",
        0.3,
        False,
    ],
]


def ner(
    text, labels: str, threshold: float, nested_ner: bool
) -> Dict[str, Union[str, int, float]]:
    labels = labels.split(",")
    return {
        "text": text,
        "entities": [
            {
                "entity": entity["label"],
                "word": entity["text"],
                "start": entity["start"],
                "end": entity["end"],
                "score": 0,
            }
            for entity in model.predict_entities(
                text, labels, flat_ner=not nested_ner, threshold=threshold
            )
        ],
    }


with gr.Blocks(title="GLiNER-M-v2.1") as demo:
    gr.Markdown(
        """
        # GLiNER-base
        GLiNER is a Named Entity Recognition (NER) model capable of identifying any entity type using a bidirectional transformer encoder (BERT-like). It provides a practical alternative to traditional NER models, which are limited to predefined entities, and Large Language Models (LLMs) that, despite their flexibility, are costly and large for resource-constrained scenarios.
        ## Links
        * Model: https://huggingface.co/urchade/gliner_multi-v2.1
        * All GLiNER models: https://huggingface.co/models?library=gliner
        * Paper: https://arxiv.org/abs/2311.08526
        * Repository: https://github.com/urchade/GLiNER
        """
    )
    with gr.Accordion("How to run this model locally", open=False):
        gr.Markdown(
            """
            ## Installation
            To use this model, you must install the GLiNER Python library:
            ```
            !pip install gliner
            ```
         
            ## Usage
            Once you've downloaded the GLiNER library, you can import the GLiNER class. You can then load this model using `GLiNER.from_pretrained` and predict entities with `predict_entities`.
            """
        )
        gr.Code(
            '''
from gliner import GLiNER
model = GLiNER.from_pretrained("urchade/gliner_mediumv2.1")
text = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
"""
labels = ["person", "award", "date", "competitions", "teams"]
entities = model.predict_entities(text, labels)
for entity in entities:
    print(entity["text"], "=>", entity["label"])
            ''',
            language="python",
        )
        gr.Code(
            """
Cristiano Ronaldo dos Santos Aveiro => person
5 February 1985 => date
Al Nassr => teams
Portugal national team => teams
Ballon d'Or => award
UEFA Men's Player of the Year Awards => award
European Golden Shoes => award
UEFA Champions Leagues => competitions
UEFA European Championship => competitions
UEFA Nations League => competitions
Champions League => competitions
European Championship => competitions
            """
        )

    input_text = gr.Textbox(
        value=examples[0][0], label="Text input", placeholder="Enter your text here"
    )
    with gr.Row() as row:
        labels = gr.Textbox(
            value=examples[0][1],
            label="Labels",
            placeholder="Enter your labels here (comma separated)",
            scale=2,
        )
        threshold = gr.Slider(
            0,
            1,
            value=0.3,
            step=0.01,
            label="Threshold",
            info="Lower the threshold to increase how many entities get predicted.",
            scale=1,
        )
        nested_ner = gr.Checkbox(
            value=examples[0][2],
            label="Nested NER",
            info="Allow for nested NER?",
            scale=0,
        )
    output = gr.HighlightedText(label="Predicted Entities")
    submit_btn = gr.Button("Submit")
    examples = gr.Examples(
        examples,
        fn=ner,
        inputs=[input_text, labels, threshold, nested_ner],
        outputs=output,
        cache_examples=True,
    )

    # Submitting
    input_text.submit(
        fn=ner, inputs=[input_text, labels, threshold, nested_ner], outputs=output
    )
    labels.submit(
        fn=ner, inputs=[input_text, labels, threshold, nested_ner], outputs=output
    )
    threshold.release(
        fn=ner, inputs=[input_text, labels, threshold, nested_ner], outputs=output
    )
    submit_btn.click(
        fn=ner, inputs=[input_text, labels, threshold, nested_ner], outputs=output
    )
    nested_ner.change(
        fn=ner, inputs=[input_text, labels, threshold, nested_ner], outputs=output
    )

demo.queue()
demo.launch(debug=True)

```

## File: requirements.txt

<a name='file-requirements.txt'></a>
*Description*: This text file contains general information.

```plaintext
torch>=2.0.0
transformers>=4.38.2,<=4.45.2
huggingface_hub>=0.21.4
onnxruntime-gpu
sentencepiece
tqdm

```

## File: pyproject.toml

<a name='file-pyproject.toml'></a>
*Description*: No specific description available.

```plaintext
[build-system]
requires = ["setuptools>=61.0.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools.packages.find]
include = ["gliner", "gliner.*"]

[tool.setuptools.dynamic]
version = {attr = "gliner.__version__"}

[project]
name = "gliner"
description = "Generalist model for NER (Extract any entity types from texts)"
readme = "README.md"
requires-python = ">=3.8"
license = {text = "Apache-2.0"}
keywords = [
    "named-entity-recognition",
    "ner",
    "data-science",
    "natural-language-processing",
    "artificial-intelligence",
    "nlp",
    "machine-learning",
    "transformers"
]
authors = [
    {name = "Urchade Zaratiana"},
    {name = "Nadi Tomeh"},
    {name = "Pierre Holat"},
    {name = "Thierry Charnois"},
]
maintainers = [
    {name = "Urchade Zaratiana"},
]

dependencies = [
    "torch>=2.0.0",
    "transformers>=4.38.2",
    "huggingface_hub>=0.21.4",
    "tqdm",
    "onnxruntime",
    "sentencepiece",
]

dynamic = ["version"]

[project.optional-dependencies]
gpu = ["onnxruntime-gpu"]


[project.urls]
Homepage = "https://github.com/urchade/GLiNER"

```

## File: README.md

<a name='file-README.md'></a>
*Description*: No specific description available.

```plaintext
# 👑 GLiNER: Generalist and Lightweight Model for Named Entity Recognition

GLiNER is a Named Entity Recognition (NER) model capable of identifying any entity type using a bidirectional transformer encoder (BERT-like). It provides a practical alternative to traditional NER models, which are limited to predefined entities, and Large Language Models (LLMs) that, despite their flexibility, are costly and large for resource-constrained scenarios.

<p align="center">
    <a href="https://pypi.org/project/gliner/" target="_blank">
        <img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
        <img alt="Version" src="https://img.shields.io/pypi/v/gliner?style=for-the-badge&color=3670A0">
    </a>
</p>

<p align="center">
    <a href="https://aclanthology.org/2024.naacl-long.300/">📄 Paper</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="https://discord.gg/Y2yVxpSQnG">📢 Discord</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="https://huggingface.co/spaces/urchade/gliner_mediumv2.1">🤗 Demo</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="https://huggingface.co/models?library=gliner&sort=trending">🤗 Available models</a>
    <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
    <a href="https://colab.research.google.com/drive/1mhalKWzmfSTqMnR0wQBZvt9-ktTsATHB?usp=sharing">
        <img align="center" src="https://colab.research.google.com/assets/colab-badge.svg" />
    </a>
</p>

## Example Notebooks

Explore various examples including finetuning, ONNX conversion, and synthetic data generation. 

- [Example Notebooks](https://github.com/urchade/GLiNER/tree/main/examples)
- Finetune on Colab &nbsp;[<img align="center" src="https://colab.research.google.com/assets/colab-badge.svg" />](https://colab.research.google.com/drive/1HNKd74cmfS9tGvWrKeIjSxBt01QQS7bq?usp=sharing)
## 🛠 Installation & Usage

### Installation
```bash
!pip install gliner
```

### Usage
After the installation of the GLiNER library, import the `GLiNER` class. Following this, you can load your chosen model with `GLiNER.from_pretrained` and utilize `predict_entities` to discern entities within your text.

```python
from gliner import GLiNER

# Initialize GLiNER with the base model
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")

# Sample text for entity prediction
text = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
"""

# Labels for entity prediction
# Most GLiNER models should work best when entity types are in lower case or title case
labels = ["Person", "Award", "Date", "Competitions", "Teams"]

# Perform entity prediction
entities = model.predict_entities(text, labels, threshold=0.5)

# Display predicted entities and their labels
for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

#### Expected Output

```
Cristiano Ronaldo dos Santos Aveiro => person
5 February 1985 => date
Al Nassr => teams
Portugal national team => teams
Ballon d'Or => award
UEFA Men's Player of the Year Awards => award
European Golden Shoes => award
UEFA Champions Leagues => competitions
UEFA European Championship => competitions
UEFA Nations League => competitions
European Championship => competitions
```
## 🌟 Maintainers

<div align="center">
  <table>
    <tr>
      <td align="center">
        <strong>Urchade Zaratiana</strong><br>
        <em>PhD Student at LIPN</em><br>
        <a href="https://www.linkedin.com/in/urchade-zaratiana/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
      </td>
      <td align="center">
        <strong>Ihor Stepanov</strong><br>
        <em>Co-Founder at Knowledgator</em><br>
        <a href="https://www.linkedin.com/in/ihor-stepanov/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
      </td>
    </tr>
  </table>
</div>

## 👨‍💻 Model Authors
The model authors are:
* [Urchade Zaratiana](https://huggingface.co/urchade)
* Nadi Tomeh
* Pierre Holat
* Thierry Charnois

## 📚 Citation

If you find GLiNER useful in your research, please consider citing our paper:

```bibtex
@inproceedings{zaratiana-etal-2024-gliner,
    title = "{GL}i{NER}: Generalist Model for Named Entity Recognition using Bidirectional Transformer",
    author = "Zaratiana, Urchade  and
      Tomeh, Nadi  and
      Holat, Pierre  and
      Charnois, Thierry",
    editor = "Duh, Kevin  and
      Gomez, Helena  and
      Bethard, Steven",
    booktitle = "Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.naacl-long.300",
    doi = "10.18653/v1/2024.naacl-long.300",
    pages = "5364--5376",
    abstract = "Named Entity Recognition (NER) is essential in various Natural Language Processing (NLP) applications. Traditional NER models are effective but limited to a set of predefined entity types. In contrast, Large Language Models (LLMs) can extract arbitrary entities through natural language instructions, offering greater flexibility. However, their size and cost, particularly for those accessed via APIs like ChatGPT, make them impractical in resource-limited scenarios. In this paper, we introduce a compact NER model trained to identify any type of entity. Leveraging a bidirectional transformer encoder, our model, GLiNER, facilitates parallel entity extraction, an advantage over the slow sequential token generation of LLMs. Through comprehensive testing, GLiNER demonstrate strong performance, outperforming both ChatGPT and fine-tuned LLMs in zero-shot evaluations on various NER benchmarks.",
}
```
## Support and funding

This project has been supported and funded by **F.initiatives** and **Laboratoire Informatique de Paris Nord**.

F.initiatives has been an expert in public funding strategies for R&D, Innovation, and Investments (R&D&I) for over 20 years. With a team of more than 200 qualified consultants, F.initiatives guides its clients at every stage of developing their public funding strategy: from structuring their projects to submitting their aid application, while ensuring the translation of their industrial and technological challenges to public funders. Through its continuous commitment to excellence and integrity, F.initiatives relies on the synergy between methods and tools to offer tailored, high-quality, and secure support.

<p align="center">
  <img src="logo/FI_COMPLET_CW.png" alt="FI Group" width="300"/>
</p>

We also extend our heartfelt gratitude to the open-source community for their invaluable contributions, which have been instrumental in the success of this project.



```

## File: LICENSE

<a name='file-LICENSE'></a>
*Description*: No specific description available.

```plaintext
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

## File: train.py

<a name='file-train.py'></a>
*Description*: This is a Python script.

```python
import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"
import argparse
import random
import json

from transformers import AutoTokenizer
import torch

from gliner import GLiNERConfig, GLiNER
from gliner.training import Trainer, TrainingArguments
from gliner.data_processing.collator import DataCollatorWithPadding, DataCollator
from gliner.utils import load_config_as_namespace
from gliner.data_processing import WordsSplitter, GLiNERDataset


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default= "configs/config.yaml")
    parser.add_argument('--log_dir', type=str, default = 'models/')
    parser.add_argument('--compile_model', type=bool, default = False)
    parser.add_argument('--freeze_language_model', type=bool, default = False)
    parser.add_argument('--new_data_schema', type=bool, default = False)
    args = parser.parse_args()
    
    device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

    config = load_config_as_namespace(args.config)
    config.log_dir = args.log_dir

    with open(config.train_data, 'r') as f:
        data = json.load(f)

    print('Dataset size:', len(data))
    #shuffle
    random.shuffle(data)    
    print('Dataset is shuffled...')

    train_data = data[:int(len(data)*0.9)]
    test_data = data[int(len(data)*0.9):]

    print('Dataset is splitted...')


    if config.prev_path is not None:
        tokenizer = AutoTokenizer.from_pretrained(config.prev_path)
        model = GLiNER.from_pretrained(config.prev_path)
        model_config = model.config
    else:
        model_config = GLiNERConfig(**vars(config))
        tokenizer = AutoTokenizer.from_pretrained(model_config.model_name)
    
        words_splitter = WordsSplitter(model_config.words_splitter_type)

        model = GLiNER(model_config, tokenizer=tokenizer, words_splitter=words_splitter)

        if not config.labels_encoder:
            model_config.class_token_index=len(tokenizer)
            tokenizer.add_tokens([model_config.ent_token, model_config.sep_token], special_tokens=True)
            model_config.vocab_size = len(tokenizer)
            model.resize_token_embeddings([model_config.ent_token, model_config.sep_token], 
                                        set_class_token_index = False,
                                        add_tokens_to_tokenizer=False)

    if args.compile_model:
        torch.set_float32_matmul_precision('high')
        model.to(device)
        model.compile_for_training()
        
    if args.freeze_language_model:
        model.model.token_rep_layer.bert_layer.model.requires_grad_(False)
    else:
        model.model.token_rep_layer.bert_layer.model.requires_grad_(True)

    if args.new_data_schema:
        train_dataset = GLiNERDataset(train_data, model_config, tokenizer, words_splitter)
        test_dataset = GLiNERDataset(test_data, model_config, tokenizer, words_splitter)
        data_collator = DataCollatorWithPadding(model_config)
    else:
        train_dataset = train_data
        test_dataset = test_data
        data_collator = DataCollator(model.config, data_processor=model.data_processor, prepare_labels=True)

    training_args = TrainingArguments(
        output_dir=config.log_dir,
        learning_rate=float(config.lr_encoder),
        weight_decay=float(config.weight_decay_encoder),
        others_lr=float(config.lr_others),
        others_weight_decay=float(config.weight_decay_other),
        lr_scheduler_type=config.scheduler_type,
        warmup_ratio=config.warmup_ratio,
        per_device_train_batch_size=config.train_batch_size,
        per_device_eval_batch_size=config.train_batch_size,
        max_grad_norm=config.max_grad_norm,
        max_steps=config.num_steps,
        evaluation_strategy="epoch",
        save_steps = config.eval_every,
        save_total_limit=config.save_total_limit,
        dataloader_num_workers = 8,
        use_cpu = False,
        report_to="none",
        bf16=True,
        )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
    )
    trainer.train()

```

## File: eval.py

<a name='file-eval.py'></a>
*Description*: This is a Python script.

```python
import argparse

from gliner import GLiNER
from gliner.evaluation import get_for_all_path


def create_parser():
    parser = argparse.ArgumentParser(description="Span-based NER")
    parser.add_argument("--model", type=str, default="logs/model_12000", help="Path to model folder")
    parser.add_argument("--log_dir", type=str, default="logs", help="Path to model folder")
    parser.add_argument('--data', type=str, default='data/ie_data/NER/', help='Path to the eval datasets directory')
    return parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    model = GLiNER.from_pretrained(args.model, load_tokenizer=True).to("cuda:0")
    get_for_all_path(model, -1, args.log_dir, args.data)
```

## File: RELEASE.md

<a name='file-RELEASE.md'></a>
*Description*: No specific description available.

```plaintext
# A guide to making a release

This guide collects the steps we do in GLiNER to make a release on PyPI. They result from (variations of) hard-learned lessons and while following this guide is completely optional, it’s strongly recommended to do so. 🙂 This is a truncated version of the [SetFit](https://github.com/huggingface/setfit/blob/main/RELEASE.md) release guide, which is more exhaustive and does some additional steps.

### Preparation

To be able to make a release for a given project, you’ll need an account on [PyPI](https://pypi.org/) and on [Test PyPI](https://test.pypi.org/). If you are making a release for an existing project, your username will need to be added to that project by one of the current maintainers on PyPI. Note that we strongly recommend enabling two-factor authentication on PyPI.

You will also need to install twine in your Python environment with `pip install twine`.

Additionally, it can be nice to familiarize yourself with [Semantic Versioning](https://semver.org/). This is a fairly strict document, but it provides a useful summary that library maintainers should follow:

> Given a version number MAJOR.MINOR.PATCH, increment the:
> 
> 1. MAJOR version when you make incompatible API changes
> 2. MINOR version when you add functionality in a backward compatible manner
> 3. PATCH version when you make backward compatible bug fixes
> 
> Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

The very first release should be "0.1.0".

## Releases

### Step 1: Adjust the version of your package

You should have the current version specified in [`gliner/__init__.py`](gliner/__init__.py). This version should be a dev version (e.g. `0.1.0.dev`) before you release, change it to the name of the version you are releasing:

```diff
- __version__ = "0.4.0.dev"
+ __version__ = "0.4.0"
```

Commit the changes on your release branch and push them:

```bash
git add gliner
git commit -m "Release: v{VERSION}"
git push -u origin main
```

### Step 2: (Optional) Make sure all tests pass

If you add tests, then you should also add CI, e.g. like this [`tests.yaml`](https://github.com/tomaarsen/SpanMarkerNER/blob/main/.github/workflows/tests.yaml) file. This will automatically run tests whenever you make changes, it can be very useful. Make sure all tests that you may have pass before proceeding to the next step.

### Step 3: Add a tag for your release

A tag will flag the exact commit associated to your release (and be easier to remember than the commit hash!). The tag should be `v<VERSION>` so for instance `v4.12.0`. 

Here is how you can create and push your tag:

```bash
git tag v<VERSION>
git push --tags origin main
```

### Step 4: (Optional) Prepare the release notes

You can then put your release notes in a Draft Release on GitHub, in [https://github.com/urchade/GLiNER/releases](https://github.com/urchade/GLiNER/releases) and write a small paragraph highlighting each of the new features this release is adding.

You can use the previously created tag to let GitHub auto-generate some release notes based on recent pull requests.

### Step 5: Create the wheels for your release

This is what you'll upload on PyPI and what everyone will download each time they `pip install` your package.

Clean previous builds by deleting the `build` and `dist` directories or by running:

```
rm -rf build && rm -rf dist
```

Then run:

```bash
python -m build
```

This will create two folders, `build` and a `dist` with the new versions of your package. These contain a 1) source distribution and a 2) wheel.

### Step 6: Upload your package on PyPI test

**DO NOT SKIP THIS STEP!**

This is the most important check before actually releasing your package in the wild. Upload the package on PyPI test and check you can properly install it.

To upload it:

```bash
twine upload dist/* -r pypitest --repository-url=https://test.pypi.org/legacy/
```

You will be prompted for your username and password. If that doesn't work, you can create an API Token for your Test PyPI account and create a `~/.pypirc` account if it doesn't already exist, with:

```
[distutils]
  index-servers =
    gliner_test

[gliner_test]
  repository = https://test.pypi.org/legacy/
  username = __token__
  password = pypi-...
```
(some more details on this [here](https://pypi.org/help/#apitoken))

And then run:
```bash
twine upload dist/* -r gliner_test
```

Once that has uploaded the package, in a fresh environment containing all dependencies you need (tip: you can use Google Colab for this!), try to install your new package from the PyPI test server. First install all dependencies, and then your package.

```bash
python -m pip install torch transformers huggingface_hub flair tqdm
python -m pip install -i https://testpypi.python.org/pypi gliner
```

If everything works, you should be able to run this code:

```python
from gliner import GLiNER

model = GLiNER.from_pretrained("urchade/gliner_base")

text = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
"""

labels = ["person", "award", "date", "competitions", "teams"]

entities = model.predict_entities(text, labels, threshold=0.5)

for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

### Step 7: Publish on PyPI

This cannot be undone if you messed up, so make sure you have run Step 6!

Once you’re fully ready, upload your package on PyPI:

```bash
twine upload dist/* -r pypi
```

You will be prompted for your username and password, unless you're using the recommended [PyPI API token](https://pypi.org/help/#apitoken). 

### Step 8: (Optional) Publish your release notes

Go back to the draft you did at step 4 ([https://github.com/urchade/GLiNER/releases](https://github.com/urchade/GLiNER/releases)) and publish them.

### Step 9: Bump the dev version on the main branch

You’re almost done! Just go back to the `main` branch and change the dev version in [`gliner/__init__.py`](gliner/__init__.py) to the new version you’re developing, for instance `4.13.0.dev` if just released `4.12.0`.

```

## File: README_Extended.md

<a name='file-README_Extended.md'></a>
*Description*: No specific description available.

```plaintext
# 👑 GLiNER: Generalist and Lightweight Model for Named Entity Recognition

GLiNER is a Named Entity Recognition (NER) model capable of identifying any entity type using a bidirectional transformer encoder (BERT-like). It provides a practical alternative to traditional NER models, which are limited to predefined entities, and Large Language Models (LLMs) that, despite their flexibility, are costly and large for resource-constrained scenarios.

* **Paper**: 📄 [GLiNER: Generalist Model for Named Entity Recognition using Bidirectional Transformer](https://arxiv.org/abs/2311.08526)
* **Getting Started:** &nbsp; [<img align="center" src="https://colab.research.google.com/assets/colab-badge.svg" />](https://colab.research.google.com/drive/1mhalKWzmfSTqMnR0wQBZvt9-ktTsATHB?usp=sharing)
* **Demo:** 🤗 [Hugging Face](https://huggingface.co/spaces/urchade/gliner_mediumv2.1)

## Models Status
### 📢 Updates
- 🔍 Join the GLiNER **discord** server: [https://discord.gg/Y2yVxpSQnG](https://discord.gg/Y2yVxpSQnG)
- Synthetic data generation example is available (examples/synthetic_data_generation.ipynb).
- 🆕 `gliner_multi_pii-v1` is available. This version has been optimized to recognize and classify Personally Identifiable Information (PII) within text. This version has been finetuned on six languages (English, French, German, Spanish, Italian, Portugese).
- 🚀 `gliner_multi-v2.1`, `gliner_small-v2.1`, `gliner_medium-v2.1`, and `gliner_large-v2.1` are available under the Apache 2.0 license.
- 🆕 [gliner-spacy](https://github.com/theirstory/gliner-spacy) is available. Install it with `pip install gliner-spacy`. See Example of usage [below](https://github.com/urchade/GLiNER/tree/main#-usage-with-spacy).
- 🧬 `gliner_large_bio-v0.1` is a gliner model specialized for biomedical text. It is available under the Apache 2.0 license.
- 📚 Training dataset preprocessing scripts are now available in the `data/` directory, covering both [Pile-NER](https://huggingface.co/datasets/Universal-NER/Pile-NER-type) and [NuNER](https://huggingface.co/datasets/numind/NuNER) datasets.

### Finetuning GLiNER
- 📘 See this [directory](https://github.com/urchade/GLiNER/tree/main/examples/finetuning)

### 🌟 Available Models on Hugging Face

#### 🇬🇧 For English
- **GLiNER Base**: `urchade/gliner_base` *(CC BY NC 4.0)*
- **GLiNER Small**: `urchade/gliner_small` *(CC BY NC 4.0)*
- **GLiNER Small v2**: `urchade/gliner_small-v2` *(Apache 2.0)*
- **GLiNER Small v2.1**: `urchade/gliner_small-v2.1` *(Apache 2.0)*
- **GLiNER Medium**: `urchade/gliner_medium` *(CC BY NC 4.0)*
- **GLiNER Medium v2**: `urchade/gliner_medium-v2` *(Apache 2.0)*
- **GLiNER Medium v2.1**: `urchade/gliner_medium-v2.1` *(Apache 2.0)*
- **GLiNER Large**: `urchade/gliner_large` *(CC BY NC 4.0)*
- **GLiNER Large v2**: `urchade/gliner_large-v2` *(Apache 2.0)*
- **GLiNER Large v2.1**: `urchade/gliner_large-v2.1` *(Apache 2.0)*


- **GLiNER NuNerZero span**: `numind/NuNER_Zero-span`  *(MIT)* - +4.5% more powerful GLiNER Large v2.1
- **GLiNER News**: `EmergentMethods/gliner_medium_news-v2.1` *(Apache 2.0)* 9.5% improvement over GLiNER Large v2.1 on 18 benchmark datasets

##### 🇬🇧 English word-level Entity Recognition

Word-level models work **better for finding multi-word entities, highlighting sentences or paragraphs**. They require additional output postprocessing that can be found in the corresponding model card.
- **GLiNER NuNerZero**: `numind/NuNER_Zero`  *(MIT)* - +3% more powerful GLiNER Large v2.1, better suitable to detect multi-word entities
- **GLiNER NuNerZero 4k context**: `numind/NuNER_Zero-4k`  *(MIT)* - 4k-long-context NuNerZero

#### 🌍 For Other Languages
- **Korean**: 🇰🇷 `taeminlee/gliner_ko`
- **Italian**: 🇮🇹 `DeepMount00/universal_ner_ita`
- **Multilingual**: 🌐 `urchade/gliner_multi` *(CC BY NC 4.0)* and `urchade/gliner_multi-v2.1` *(Apache 2.0)*

#### 🔬 Domain Specific Models
- **Personally Identifiable Information**: 🔍 `urchade/gliner_multi_pii-v1` *(Apache 2.0)*
    - This model is capable of recognizing various types of *personally identifiable information* (PII), including but not limited to these entity types: `person`, `organization`, `phone number`, `address`, `passport number`, `email`, `credit card number`, `social security number`, `health insurance id number`, `date of birth`, `mobile phone number`, `bank account number`, `medication`, `cpf`, `driver's license number`, `tax identification number`, `medical condition`, `identity card number`, `national id number`, `ip address`, `email address`, `iban`, `credit card expiration date`, `username`, `health insurance number`, `registration number`, `student id number`, `insurance number`, `flight number`, `landline phone number`, `blood type`, `cvv`, `reservation number`, `digital signature`, `social media handle`, `license plate number`, `cnpj`, `postal code`, `passport_number`, `serial number`, `vehicle registration number`, `credit card brand`, `fax number`, `visa number`, `insurance company`, `identity document number`, `transaction number`, `national health insurance number`, `cvc`, `birth certificate number`, `train ticket number`, `passport expiration date`, and `social_security_number`.
- **Biomedical**: 🧬 `urchade/gliner_large_bio-v0.1` *(Apache 2.0)*
- **Birds attribute extraction**: 🐦 `wjbmattingly/gliner-large-v2.1-bird`  *(Apache 2.0)*

#### 📚 Multi-task Models
- **GLiNER multi-task large v0.5** `knowledgator/gliner-multitask-large-v0.5` *(Apache 2.0)* - +4.5% on NER benchmarks over GLiNER Large v2.1, supports prompting, relation extraction, summarization and question-answering tasks.
- **GLiNER multi-task v1.0** `knowledgator/gliner-multitask-v1.0` *(Apache 2.0)* - +5.0% on NER benchmarks over GLiNER Large v2.1, supports prompting, relation extraction, summarization, classification and question-answering tasks.
- **GLiNER Llama multi-task v1.0** `knowledgator/gliner-llama-multitask-1B-v1.0` *(Apache 2.0)* - +3.5% on NER benchmarks over GLiNER Large v2.1, supports prompting, relation extraction, summarization, classification and question-answering tasks.

## 🛠 Installation & Usage

To provide instructions on how to install the GLiNER model from source, you can add steps for cloning the repository and installing it manually. Here’s how you can incorporate those instructions:

---

## 🛠 Installation & Usage

To begin using the GLiNER model, you can install the GLiNER Python library through pip, conda, or directly from the source.

### Install via Pip

```bash
!pip install gliner
```

If you intend to use the GPU-backed ONNX runtime, install GLiNER with the GPU feature. This also installs the `onnxruntime-gpu` dependency.

```bash
!pip install gliner[gpu]
```

### Install via Conda

```bash
conda install -c conda-forge gliner
```

### Install from Source

To install the GLiNER library from source, follow these steps:

1. **Clone the Repository:**

   First, clone the GLiNER repository from GitHub:

   ```bash
   git clone https://github.com/urchade/GLiNER
   ```

2. **Navigate to the Project Directory:**

   Change to the directory containing the cloned repository:

   ```bash
   cd GLiNER
   ```

3. **Install Dependencies:**

   It's a good practice to create and activate a virtual environment before installing dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```

   Install the required dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install the GLiNER Package:**

   Finally, install the GLiNER package using the setup script:

   ```bash
   pip install .
   ```

5. **Verify Installation:**

   You can verify the installation by importing the library in a Python script:

   ```python
   import gliner
   print(gliner.__version__)
   ```
---

### 🚀 Basic Use Case

After the installation of the GLiNER library, import the `GLiNER` class. Following this, you can load your chosen model with `GLiNER.from_pretrained` and utilize `predict_entities` to discern entities within your text.

```python
from gliner import GLiNER

# Initialize GLiNER with the base model
model = GLiNER.from_pretrained("urchade/gliner_mediumv2.1")

# Sample text for entity prediction
text = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
"""

# Labels for entity prediction
labels = ["Person", "Award", "Date", "Competitions", "Teams"]

# Perform entity prediction
entities = model.predict_entities(text, labels, threshold=0.5)

# Display predicted entities and their labels
for entity in entities:
    print(entity["text"], "=>", entity["label"])
```

#### Expected Output

```
Cristiano Ronaldo dos Santos Aveiro => person
5 February 1985 => date
Al Nassr => teams
Portugal national team => teams
Ballon d'Or => award
UEFA Men's Player of the Year Awards => award
European Golden Shoes => award
UEFA Champions Leagues => competitions
UEFA European Championship => competitions
UEFA Nations League => competitions
European Championship => competitions
```

### 🔌 Usage with spaCy

GLiNER can be seamlessly integrated with spaCy. To begin, install the `gliner-spacy` library via pip:

```bash
pip install gliner-spacy
```

Following installation, you can add GLiNER to a spaCy NLP pipeline. Here's how to integrate it with a blank English pipeline; however, it's compatible with any spaCy model.

```python
import spacy
from gliner_spacy.pipeline import GlinerSpacy

# Configuration for GLiNER integration
custom_spacy_config = {
    "gliner_model": "urchade/gliner_mediumv2.1",
    "chunk_size": 250,
    "labels": ["person", "organization", "email"],
    "style": "ent",
    "threshold": 0.3,
    "map_location": "cpu" # only available in v.0.0.7
}

# Initialize a blank English spaCy pipeline and add GLiNER
nlp = spacy.blank("en")
nlp.add_pipe("gliner_spacy", config=custom_spacy_config)

# Example text for entity detection
text = "This is a text about Bill Gates and Microsoft."

# Process the text with the pipeline
doc = nlp(text)

# Output detected entities
for ent in doc.ents:
    print(ent.text, ent.label_, ent._.score) # ent._.score only available in v. 0.0.7
```

#### Expected Output

```
Bill Gates => person
Microsoft => organization
```

## Multitask Usage
GLiNER-Multitask models are designed to extract relevant information from plain text based on a user-provided custom prompt. The advantage of such encoder-based multitask models is that they enable efficient and more controllable information extraction with a single model that reduces costs on computational and storage resources. Moreover, such encoder models are more interpretable, efficient and tunable than LLMs, which are hard to fine-tune and use for information extraction.

**Supported tasks:**:
   * Named Entity Recognition (NER): Identifies and categorizes entities such as names, organizations, dates, and other specific items in the text.
   * Relation Extraction: Detects and classifies relationships between entities within the text.
   * Summarization: Extract the most important sentences that summarize the input text, capturing the essential information.
   * Sentiment Extraction: Identify parts of the text that signalize a positive, negative, or neutral sentiment;
   * Key-Phrase Extraction: Identifies and extracts important phrases and keywords from the text.
   * Question-answering: Finding an answer in the text given a question;
   * Open Information Extraction: Extracts pieces of text given an open prompt from a user, for example, product description extraction;
   * Text classification: Classifying text by matching labels specified in the prompt;

We prepared high-level classes that simplify the usage and evaluation of GLiNER multi-task models for different task types.

### Classification

The `GLiNERClassifier` is a pipeline for text classification tasks based on the GLiNER model. It evaluates input text against a set of predefined labels, supporting both single-label and multi-label classification. It also calculates F1 scores for evaluation on datasets.

#### Quick Usage Examples

1. **Initialize the Classifier**  
   Load a pretrained model and initialize the `GLiNERClassifier`.

   ```python
   from gliner import GLiNER
   from gliner.multitask import GLiNERClassifier

   model_id = 'knowledgator/gliner-multitask-v1.0'
   model = GLiNER.from_pretrained(model_id)
   classifier = GLiNERClassifier(model=model)
   ```

2. **Classify a Text**  
   Classify a single text into a list of labels.

   ```python
   text = "SpaceX successfully launched a new rocket into orbit."
   labels = ['science', 'technology', 'business', 'sports']
   predictions = classifier(text, classes=labels, multi_label=False)
   print(predictions)
   ```

3. **Evaluate on a Dataset**  
   Evaluate the model on a dataset from Hugging Face.

   ```python
   metrics = classifier.evaluate('dair-ai/emotion')
   print(metrics)
   ```

### Question-Answering

The `GLiNERQuestionAnswerer` is a pipeline for question-answering tasks based on the GLiNER model. It extracts answers based on questions and input text. You can leverage `GLiNERSquadEvaluator` to evaluate a model on the SQuAD dataset.

#### Quick Usage Examples

1. **Initialize the Question-Answerer**  
   Load a pretrained model and initialize the `GLiNERQuestionAnswerer`.

   ```python
   from gliner import GLiNER
   from gliner.multitask import GLiNERQuestionAnswerer

   model_id = 'knowledgator/gliner-multitask-v1.0'
   model = GLiNER.from_pretrained(model_id)
   answerer = GLiNERQuestionAnswerer(model=model)
   ```

2. **Extract an answer from a Text**  
   Extract an answer to the input question.

   ```python
   text = "SpaceX successfully launched a new rocket into orbit."
   question = 'Which company launched a new rocker?'
   predictions = answerer(text, questions=question)
   print(predictions)
   ```

3. **Evaluate on a Dataset**  
   Evaluate the model on a dataset from Hugging Face.

   ```python
   from gliner.multitask import GLiNERSquadEvaluator
   model_id = 'knowledgator/gliner-multitask-v1.0'
   evaluator = GLiNERSquadEvaluator(model_id=model_id)
   metrics = evaluator.evaluate( threshold=0.25)
   print(metrics)
   ```

### Relation Extraction

The `GLiNERRelationExtractor` is a pipeline for extracting relationships between entities in a text using the GLiNER model. The pipeline combines both zero-shot named entity recognition and relation extraction. It identifies entity pairs and their relations based on a specified by user set of relation types.

#### Quick Usage Examples

1. **Initialize the Relation Extractor**  
   Load a pretrained model and initialize the `GLiNERRelationExtractor`.

   ```python
   from gliner import GLiNER
   from gliner.multitask import GLiNERRelationExtractor

   model_id = 'knowledgator/gliner-multitask-v1.0'
   model = GLiNER.from_pretrained(model_id)
   relation_extractor = GLiNERRelationExtractor(model=model)
   ```

2. **Extract Relations from Text**  
   Identify relationships between entities in a given text.

   ```python
   text = "Elon Musk founded SpaceX in 2002 to reduce space transportation costs."
   relations = ['founded', 'owns', 'works for']
   entities = ['person', 'company', 'year']
   predictions = relation_extractor(text, entities=entities, relations=relations)
   print(predictions)
   ```

3. **Evaluate on a Dataset**  
   Evaluate the model on a relation extraction dataset.

   ```python
   from datasets import load_dataset

   dataset = load_dataset('docred', split='test')
   metrics = relation_extractor.evaluate(dataset=dataset)
   print(metrics)
   ```

For more nuance tuning of relation extraction pipeline, we recommend to use `utca` framework.

#### Construct relations extraction pipeline with [utca](https://github.com/Knowledgator/utca)
First of all, we need import neccessary components of the library and initalize predictor - GLiNER model and construct pipeline that combines NER and realtions extraction:
```python
from utca.core import RenameAttribute
from utca.implementation.predictors import (
    GLiNERPredictor,
    GLiNERPredictorConfig
)
from utca.implementation.tasks import (
    GLiNER,
    GLiNERPreprocessor,
    GLiNERRelationExtraction,
    GLiNERRelationExtractionPreprocessor,
)

predictor = GLiNERPredictor( # Predictor manages the model that will be used by tasks
    GLiNERPredictorConfig(
        model_name = "knowledgator/gliner-multitask-v1.0", # Model to use
        device = "cuda:0", # Device to use
    )
)

pipe = (
    GLiNER( # GLiNER task produces classified entities that will be at the "output" key.
        predictor=predictor,
        preprocess=GLiNERPreprocessor(threshold=0.7) # Entities threshold
    ) 
    | RenameAttribute("output", "entities") # Rename output entities from GLiNER task to use them as inputs in GLiNERRelationExtraction
    | GLiNERRelationExtraction( # GLiNERRelationExtraction is used for relation extraction.
        predictor=predictor,
        preprocess=(
            GLiNERPreprocessor(threshold=0.5) # Relations threshold
            | GLiNERRelationExtractionPreprocessor()
        )
    )
)
```

To run pipeline we need to specify entity types and relations with their parameters:

```python
r = pipe.run({
    "text": text, # Text to process
    "labels": ["organisation", "founder", "position", "date"],
    "relations": [{ # Relation parameters
        "relation": "founder", # Relation label. Required parameter.
        "pairs_filter": [("organisation", "founder")], # Optional parameter. It specifies possible members of relations by their entity labels.
        "distance_threshold": 100, # Optional parameter. It specifies the max distance between spans in the text (i.e., the end of the span that is closer to the start of the text and the start of the next one).
    }, {
        "relation": "inception date",
        "pairs_filter": [("organisation", "date")],
    }, {
        "relation": "held position",
        "pairs_filter": [("founder", "position")],
    }]
})

print(r["output"])
```

### Open Information Extraction

The `GLiNEROpenExtractor` is a pipeline designed to extract information from a text given a user query. By default in terms of GLiNER labels `match` tag is used, however, we recommend combining prompting and selecting appropriate tags for your tasks. 

#### Quick Usage Examples

1. **Initialize the Information Extractor**  
   Load a pretrained model and initialize the `GLiNEROpenExtractor`.

   ```python
   from gliner import GLiNER
   from gliner.multitask import GLiNEROpenExtractor

   model_id = 'knowledgator/gliner-multitask-v1.0'
   model = GLiNER.from_pretrained(model_id)
   extractor = GLiNEROpenExtractor(model=model, prompt="Extract all companies related to space technologies")
   ```

2. **Extract Information from Text**  
   Identify relevant information from a given text.

   ```python
   text = "Elon Musk founded SpaceX in 2002 to reduce space transportation costs. Also Elon is founder of Tesla, NeuroLink and many other companies."
   labels = ['company']
   predictions = relation_extractor(text, labels=labels)
   print(predictions)
   ```

### Summariztion

The `GLiNERSummarizer` pipeline leverages the GLiNER model for performing summarization tasks as extraction process. 

#### Quick Usage Examples

1. **Initialize the Summarizer**  
   Load a pretrained model and initialize the `GLiNERSummarizer`.

   ```python
   from gliner import GLiNER
   from gliner.multitask import GLiNERSummarizer

   model_id = 'knowledgator/gliner-multitask-v1.0'
   model = GLiNER.from_pretrained(model_id)
   summarizer = GLiNERSummarizer(model=model)
   ```

2. **Summarize the Text**  
   Extract the most important information from a given text and construct summary.

   ```python
   text = "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975 to develop and sell BASIC interpreters for the Altair 8800. During his career at Microsoft, Gates held the positions of chairman, chief executive officer, president and chief software architect, while also being the largest individual shareholder until May 2014."
   summary = relation_extractor(text, threshold=0.1)
   print(summary)
   ```

##  📊 NER Benchmark Results

<img align="center" src="https://cdn-uploads.huggingface.co/production/uploads/6317233cc92fd6fee317e030/Y5f7tK8lonGqeeO6L6bVI.png" />

## ONNX convertion:
To convert previously trained GLiNER models to ONNX format, you can use the `convert_to_onnx.py` script. You need to provide the `model_path` and `save_path` arguments to specify the location of the model and where to save the ONNX file, respectively. Additionally, if you wish to quantize the model, set the `quantize` argument to True (it quantizes to *IntU8* by default).

Example usage:

```bash

python convert_to_onnx.py --model_path /path/to/your/model --save_path /path/to/save/onnx --quantize True
```

To load the converted ONNX models, you can use the following code snippet:

```python

from gliner import GLiNER

model = GLiNER.from_pretrained("path_to_your_model", load_onnx_model=True, load_tokenizer=True)

```
The `load_onnx_model` argument ensures that the GLiNER class recognizes that it should load the ONNX model instead of a PyTorch model.
Setting the `load_tokenizer`` argument to True loads the tokenizer from your model directory, including any additional tokens that were added during training.

## 🛠 Areas of Improvements / research

- [ ] Extend the model to relation extraction. Our preliminary work [GraphER](https://github.com/urchade/GraphER).
- [ ] Allow longer context (eg. train with long context transformers such as Longformer, LED, etc.)
- [ ] Use Bi-encoder (entity encoder and span encoder) allowing precompute entity embeddings
- [ ] Filtering mechanism to reduce number of spans before final classification to save memory and computation when the number entity types is large
- [ ] Improve understanding of more detailed prompts/instruction, eg. "Find the first name of the person in the text"
- [ ] Better loss function: for instance use ```Focal Loss``` (see [this paper](https://proceedings.neurips.cc/paper/2020/file/aeb7b30ef1d024a76f21a1d40e30c302-Paper.pdf)) instead of ```BCE``` to handle class imbalance, as some entity types are more frequent than others
- [ ] Improve multi-lingual capabilities: train on more languages, and use multi-lingual training data

*Content truncated for brevity.*

```

## File: convert_to_onnx.py

<a name='file-convert_to_onnx.py'></a>
*Description*: This is a Python script.

```python
import os
import argparse
import numpy as np

from gliner import GLiNER

import torch
from onnxruntime.quantization import quantize_dynamic, QuantType

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, default= "logs/model_12000")
    parser.add_argument('--save_path', type=str, default = 'model/')
    parser.add_argument('--quantize', type=bool, default = True)
    args = parser.parse_args()
    
    if not os.path.exists(args.save_path):
        os.makedirs(args.save_path)

    onnx_save_path = os.path.join(args.save_path, "model.onnx")

    print("Loading a model...")
    gliner_model = GLiNER.from_pretrained(args.model_path, load_tokenizer=True)

    text = "ONNX is an open-source format designed to enable the interoperability of AI models across various frameworks and tools."
    labels = ['format', 'model', 'tool', 'cat']

    inputs, _ = gliner_model.prepare_model_inputs([text], labels)
        
    if gliner_model.config.span_mode == 'token_level':
        all_inputs =  (inputs['input_ids'], inputs['attention_mask'], 
                        inputs['words_mask'], inputs['text_lengths'])
        input_names = ['input_ids', 'attention_mask', 'words_mask', 'text_lengths']
        dynamic_axes={
            "input_ids": {0: "batch_size", 1: "sequence_length"},
            "attention_mask": {0: "batch_size", 1: "sequence_length"},
            "words_mask": {0: "batch_size", 1: "sequence_length"},
            "text_lengths": {0: "batch_size", 1: "value"},
            "logits": {0: "position", 1: "batch_size", 2: "sequence_length", 3: "num_classes"},
        }
    else:
        all_inputs =  (inputs['input_ids'], inputs['attention_mask'], 
                        inputs['words_mask'], inputs['text_lengths'],
                        inputs['span_idx'], inputs['span_mask'])
        input_names = ['input_ids', 'attention_mask', 'words_mask', 'text_lengths', 'span_idx', 'span_mask']
        dynamic_axes={
            "input_ids": {0: "batch_size", 1: "sequence_length"},
            "attention_mask": {0: "batch_size", 1: "sequence_length"},
            "words_mask": {0: "batch_size", 1: "sequence_length"},
            "text_lengths": {0: "batch_size", 1: "value"},
            "span_idx": {0: "batch_size", 1: "num_spans", 2: "idx"},
            "span_mask": {0: "batch_size", 1: "num_spans"},
            "logits": {0: "batch_size", 1: "sequence_length", 2: "num_spans", 3: "num_classes"},
        }
    print('Converting the model...')
    torch.onnx.export(
        gliner_model.model,
        all_inputs,
        f=onnx_save_path,
        input_names=input_names,
        output_names=["logits"],
        dynamic_axes=dynamic_axes,
        opset_version=14,
    )

    if args.quantize:
        quantized_save_path = os.path.join(args.save_path, "model_quantized.onnx")
        # Quantize the ONNX model
        print("Quantizing the model...")
        quantize_dynamic(
            onnx_save_path,  # Input model
            quantized_save_path,  # Output model
            weight_type=QuantType.QUInt8  # Quantize weights to 8-bit integers
        )
    print("Done!")
```

## File: custom_train.py

<a name='file-custom_train.py'></a>
*Description*: This is a Python script.

```python
import argparse
import json
import os
import re
import random
from tqdm import tqdm

from transformers import (
    get_cosine_schedule_with_warmup,
    get_linear_schedule_with_warmup,
    get_constant_schedule_with_warmup,
    get_polynomial_decay_schedule_with_warmup,
    get_inverse_sqrt_schedule,
)
import torch
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data import DataLoader
from torch.utils.data.distributed import DistributedSampler

from transformers.trainer import (
    is_sagemaker_mp_enabled,
    get_parameter_names,
    ALL_LAYERNORM_LAYERS,
)
from transformers import AutoTokenizer

from gliner import GLiNER, GLiNERConfig
from gliner.data_processing import SpanProcessor, TokenProcessor, SpanBiEncoderProcessor, TokenBiEncoderProcessor
from gliner.data_processing.tokenizer import WordsSplitter
from gliner.data_processing.collator import DataCollatorWithPadding, DataCollator
from gliner.utils import load_config_as_namespace
from gliner.evaluation import get_for_all_path


def save_top_k_checkpoints(model: GLiNER, save_path: str, checkpoint: int, top_k: int = 5):
    """
    Save the top-k checkpoints (latest k checkpoints) of a model and tokenizer.

    Parameters:
        model (GLiNER): The model to save.
        save_path (str): The directory path to save the checkpoints.
        top_k (int): The number of top checkpoints to keep. Defaults to 5.
    """
    # Save the current model and tokenizer
    if isinstance(model, DDP):
        model.module.save_pretrained(os.path.join(save_path, str(checkpoint)))
    else:
        model.save_pretrained(os.path.join(save_path, str(checkpoint)))
    
    # List all files in the directory
    files = os.listdir(save_path)

    # Filter files to keep only the model checkpoints
    checkpoint_folders = [file for file in files if re.search(r'model_\d+', file)]

    # Sort checkpoint files by modification time (latest first)
    checkpoint_folders.sort(key=lambda x: os.path.getmtime(os.path.join(save_path, x)), reverse=True)

    # Keep only the top-k checkpoints
    for checkpoint_folder in checkpoint_folders[top_k:]:
        checkpoint_folder = os.path.join(save_path, checkpoint_folder)
        checkpoint_files = [os.path.join(checkpoint_folder, f) for f in os.listdir(checkpoint_folder)]
        for file in checkpoint_files:
            os.remove(file)
        os.rmdir(os.path.join(checkpoint_folder))


class Trainer:
    def __init__(self, config, allow_distributed, compile_model=False, device='cuda'):
        self.config = config
        self.lr_encoder = float(self.config.lr_encoder)
        self.lr_others = float(self.config.lr_others)
        self.weight_decay_encoder = float(self.config.weight_decay_encoder)
        self.weight_decay_other = float(self.config.weight_decay_other)

        self.compile_model = compile_model

        self.device = device

        self.model_config = GLiNERConfig(**vars(config))

        tokenizer = AutoTokenizer.from_pretrained(config.model_name)
        
        if config.labels_encoder is None:
            self.model_config.class_token_index=len(tokenizer)
            tokenizer.add_tokens([self.model_config.ent_token, self.model_config.sep_token])
            self.model_config.vocab_size = len(tokenizer)

        self.allow_distributed = allow_distributed

        self.optimizer = None

    def setup_distributed(self, rank, world_size):
        os.environ['MASTER_ADDR'] = 'localhost'
        os.environ['MASTER_PORT'] = '12356'
        torch.cuda.set_device(rank)
        dist.init_process_group("nccl", rank=rank, world_size=world_size)

    def cleanup_distributed(self):
        dist.destroy_process_group()

    def create_optimizer(self, opt_model, **optimizer_kwargs):
        """
        Setup the optimizer.

        We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the
        Trainer's init through `optimizers`, or subclass and override this method in a subclass.
        """
        if self.optimizer is None:
            decay_parameters = get_parameter_names(opt_model, ALL_LAYERNORM_LAYERS)
            decay_parameters = [name for name in decay_parameters if "bias" not in name]
            if self.lr_others is not None:
                encoder_parameters = [name for name, _ in opt_model.named_parameters() if "token_rep_layer" in name]
                optimizer_grouped_parameters = [
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n in decay_parameters and n not in encoder_parameters and p.requires_grad)
                        ],
                        "weight_decay": self.weight_decay_other,
                        "lr": self.lr_others,
                    },
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n not in decay_parameters and n not in encoder_parameters and p.requires_grad)
                        ],
                        "weight_decay": 0.0,
                        "lr": self.lr_others,
                    },
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n in decay_parameters and n in encoder_parameters and p.requires_grad)
                        ],
                        "weight_decay": self.weight_decay_encoder,
                        "lr": self.lr_encoder,
                    },
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n not in decay_parameters and n in encoder_parameters and p.requires_grad)
                        ],
                        "weight_decay": 0.0,
                        "lr": self.lr_encoder,
                    },
                ]
            else:
                optimizer_grouped_parameters = [
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n in decay_parameters and p.requires_grad)
                        ],
                        "weight_decay": self.weight_decay_encoder,
                        "lr": self.lr_encoder,
                    },
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n not in decay_parameters and p.requires_grad)
                        ],
                        "weight_decay": 0.0,
                        "lr": self.lr_encoder,
                    },
                ]

            self.optimizer = torch.optim.AdamW(optimizer_grouped_parameters, **optimizer_kwargs)

        return self.optimizer
    
    def setup_model_and_optimizer(self, rank=None, device=None):
        if device is None:
            device = self.device
        if self.config.prev_path is not None:
            model = GLiNER.from_pretrained(self.config.prev_path).to(device)
            model.config = self.model_config
        else:
            model = GLiNER(self.model_config).to(device)
            if self.config.labels_encoder is None:
                model.resize_token_embeddings([self.model_config.ent_token, self.model_config.sep_token], 
                                    set_class_token_index = False,
                                    add_tokens_to_tokenizer=False)
        if rank is not None:
            model = DDP(model, device_ids=[rank], output_device=rank, find_unused_parameters=False)
            if self.config.labels_encoder is None:
                model.module.resize_token_embeddings([self.model_config.ent_token, self.model_config.sep_token], 
                                set_class_token_index = False,
                                add_tokens_to_tokenizer=False)
        optimizer = self.create_optimizer(model.model)

        if self.compile_model:
            model.compile_for_training()

        return model, optimizer

    def create_dataloader(self, dataset, data_processor, sampler=None, shuffle=True):
        # dataset = GLiNERDataset(dataset, config = self.config, data_processor=self.data_processor)
        # collator = DataCollatorWithPadding(self.config)
        collator = DataCollator(self.config, data_processor=data_processor, prepare_labels=True)
        data_loader = DataLoader(dataset, batch_size=self.config.train_batch_size, num_workers=12,
                                                        shuffle=shuffle, collate_fn=collator, sampler=sampler)
        return data_loader
    
    def train_dist(self, rank, world_size, dataset):
        # Init distributed process group
        self.setup_distributed(rank, world_size)

        device = f'cuda:{rank}'

        model, optimizer = self.setup_model_and_optimizer(rank, device=device)

        sampler = DistributedSampler(dataset, num_replicas=world_size, rank=rank, shuffle=True, drop_last=False)

        train_loader = self.create_dataloader(dataset, model.data_processor, sampler=sampler, shuffle=False)

        num_steps = self.config.num_steps // world_size

        self.train(model=model, optimizer=optimizer, train_loader=train_loader,
                   num_steps=num_steps, device=device, rank=rank)

        self.cleanup_distributed()

    def init_scheduler(self, scheduler_type, optimizer, num_warmup_steps, num_steps):
        if scheduler_type == "cosine":
            scheduler = get_cosine_schedule_with_warmup(
                optimizer,
                num_warmup_steps=num_warmup_steps,
                num_training_steps=num_steps
            )
        elif scheduler_type == "linear":
            scheduler = get_linear_schedule_with_warmup(
                optimizer,
                num_warmup_steps=num_warmup_steps,
                num_training_steps=num_steps
            )
        elif scheduler_type == "constant":
            scheduler = get_constant_schedule_with_warmup(
                optimizer,
                num_warmup_steps=num_warmup_steps,
            )
        elif scheduler_type == "polynomial":
            scheduler = get_polynomial_decay_schedule_with_warmup(
                optimizer,
                num_warmup_steps=num_warmup_steps,
                num_training_steps=num_steps
            )
        elif scheduler_type == "inverse_sqrt":
            scheduler = get_inverse_sqrt_schedule(
                optimizer,
                num_warmup_steps=num_warmup_steps,
            )
        else:
            raise ValueError(
                f"Invalid scheduler_type value: '{scheduler_type}' \n Supported scheduler types: 'cosine', 'linear', 'constant', 'polynomial', 'inverse_sqrt'"
            )
        return scheduler

    def train(self, model, optimizer, train_loader, num_steps, device='cuda', rank=None):
        model.train()
        pbar = tqdm(range(num_steps))

        warmup_ratio = self.config.warmup_ratio
        eval_every = self.config.eval_every
        save_total_limit = self.config.save_total_limit
        log_dir = self.config.log_dir
        val_data_dir = self.config.val_data_dir

        num_warmup_steps = int(num_steps * warmup_ratio) if warmup_ratio < 1 else int(warmup_ratio)

        scheduler = self.init_scheduler(self.config.scheduler_type, optimizer, num_warmup_steps, num_steps)
        iter_train_loader = iter(train_loader)
        scaler = torch.cuda.amp.GradScaler()

        for step in pbar:
            optimizer.zero_grad()

            try:
                x = next(iter_train_loader)
            except StopIteration:
                iter_train_loader = iter(train_loader)
                x = next(iter_train_loader)

            for k, v in x.items():
                if isinstance(v, torch.Tensor):
                    x[k] = v.to(device)
            
            try:
                with torch.cuda.amp.autocast(dtype=torch.float16):
                    loss = model(alpha = self.config.loss_alpha,
                                    gamma = self.config.loss_gamma,
                                    label_smoothing = self.config.label_smoothing,
                                    reduction = self.config.loss_reduction,
                                    **x).loss

                if torch.isnan(loss).any():
                    print("Warning: NaN loss detected")
                    continue

                scaler.scale(loss).backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), self.config.max_grad_norm)
                scaler.step(optimizer)
                scaler.update()
                scheduler.step()
                del x
                torch.cuda.empty_cache()
            except Exception as e:
                print(f"Error: {e}")
                del x
                torch.cuda.empty_cache()
                continue

            description = f"step: {step} | epoch: {step // len(train_loader)} | loss: {loss.item():.2f}"
            pbar.set_description(description)

            if (step + 1) % eval_every == 0:
                if rank is None or rank == 0:
                    checkpoint = f'model_{step + 1}'
                    save_top_k_checkpoints(model, log_dir, checkpoint, save_total_limit)
                    if val_data_dir != "none":
                        get_for_all_path(model, step, log_dir, val_data_dir)
                    model.train()

    def run(self):
        with open(self.config.train_data, 'r') as f:
            data = json.load(f)
        random.shuffle(data) 
        if torch.cuda.device_count() > 1 and self.allow_distributed:
            world_size = torch.cuda.device_count()
            mp.spawn(self.train_dist, args=(world_size, data), nprocs=world_size, join=True)
        else:
            model, optimizer = self.setup_model_and_optimizer()

            train_loader = self.create_dataloader(data, model.data_processor, shuffle=True)

            self.train(model, optimizer, train_loader, num_steps=self.config.num_steps, device=self.device)


def create_parser():
    parser = argparse.ArgumentParser(description="Span-based NER")
    parser.add_argument("--config", type=str, default="configs/config.yaml", help="Path to config file")
    parser.add_argument('--log_dir', type=str, default='logs', help='Path to the log directory')
    parser.add_argument('--allow_distributed', type=bool, default=False,
                        help='Whether to allow distributed training if there are more than one GPU available')
    parser.add_argument('--compile_model', type=bool, default=False,
                        help='Whether to apply torch.compile to a modell or not')
    return parser


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    config = load_config_as_namespace(args.config)
    config.log_dir = args.log_dir

    trainer = Trainer(config, allow_distributed=args.allow_distributed,
                      compile_model = args.compile_model,
                      device='cuda' if torch.cuda.is_available() else 'cpu')
    trainer.run()
```

## File: data/process_pilener.py

<a name='file-data-process_pilener.py'></a>
*Description*: This is a Python script.

```python
import json
import re
import ast
from tqdm import tqdm

def load_data(filepath):
    """Loads data from a JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def tokenize_text(text):
    """Tokenizes the input text into a list of tokens."""
    return re.findall(r'\w+(?:[-_]\w+)*|\S', text)

def extract_entity_spans(entry):
    """Extracts entity spans from an entry."""
    len_start = len("What describes ")
    len_end = len(" in the text?")
    entity_types, entity_texts, negative = [], [], []

    for c in entry['conversations']:
        if c['from'] == 'human' and c['value'].startswith('Text: '):
            text = c['value'][len('Text: '):]
            tokenized_text = tokenize_text(text)
        elif c['from'] == 'human' and c['value'].startswith('What describes '):
            entity_type = c['value'][len_start:-len_end]
            entity_types.append(entity_type)
        elif c['from'] == 'gpt' and c['value'].startswith('['):
            if c['value'] == '[]':
                negative.append(entity_types.pop())
                continue
            texts_ents = ast.literal_eval(c['value'])
            entity_texts.extend(texts_ents)
            num_repeat = len(texts_ents) - 1
            entity_types.extend([entity_types[-1]] * num_repeat)

    entity_spans = []
    for j, entity_text in enumerate(entity_texts):
        entity_tokens = tokenize_text(entity_text)
        matches = []
        for i in range(len(tokenized_text) - len(entity_tokens) + 1):
            if " ".join(tokenized_text[i:i + len(entity_tokens)]).lower() == " ".join(entity_tokens).lower():
                matches.append((i, i + len(entity_tokens) - 1, entity_types[j]))
        if matches:
            entity_spans.extend(matches)

    return {"tokenized_text": tokenized_text, "ner": entity_spans, "negative": negative}

def process_data(data):
    """Processes a list of data entries to extract entity spans."""
    all_data = [extract_entity_spans(entry) for entry in tqdm(data)]
    return all_data

def save_data_to_file(data, filepath):
    """Saves the processed data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    # download the pile-ner data: "wget https://huggingface.co/datasets/Universal-NER/Pile-NER-type/blob/main/train.json"
    path_pile_ner = 'train.json'
    data = load_data(path_pile_ner)
    processed_data = process_data(data)
    save_data_to_file(processed_data, 'pilener_train.json')

    print("dataset size:", len(processed_data))
```

## File: data/process_nuner.py

<a name='file-data-process_nuner.py'></a>
*Description*: This is a Python script.

```python
from datasets import load_dataset
import re
import ast
import json
from tqdm import tqdm


def tokenize_text(text):
    """Tokenizes the input text into a list of tokens."""
    return re.findall(r'\w+(?:[-_]\w+)*|\S', text)


def process_entities(dataset):
    """Processes entities in the dataset to extract tokenized text and named entity spans."""
    all_data = []
    for el in tqdm(dataset["entity"]):
        try:
            tokenized_text = tokenize_text(el["input"])
            parsed_output = ast.literal_eval(el["output"])
            entity_texts, entity_types = zip(*[i.split(" <> ") for i in parsed_output])

            entity_spans = []
            for j, entity_text in enumerate(entity_texts):
                entity_tokens = tokenize_text(entity_text)
                matches = []
                for i in range(len(tokenized_text) - len(entity_tokens) + 1):
                    if " ".join(tokenized_text[i:i + len(entity_tokens)]).lower() == " ".join(entity_tokens).lower():
                        matches.append((i, i + len(entity_tokens) - 1, entity_types[j]))
                if matches:
                    entity_spans.extend(matches)

        except Exception as e:
            continue

        all_data.append({"tokenized_text": tokenized_text, "ner": entity_spans})
    return all_data


def save_data_to_file(data, filepath):
    """Saves the processed data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    dataset = load_dataset("numind/NuNER")
    processed_data = process_entities(dataset)

    save_data_to_file(processed_data, 'nuner_train.json')

    print("dataset size:", len(processed_data))
```

## File: examples/sample_data.json

<a name='file-examples-sample_data.json'></a>
*Description*: This JSON file contains structured data.

```json
[{"tokenized_text": ["State", "University", "of", "New", "York", "Press", ",", "1997", "."], "ner": [[0, 5, "Publisher"]]}, {"tokenized_text": ["A", "message", "from", "Katarzyna", "\u2026", "for", "September", "1", ",", "2014", "."], "ner": [[3, 3, "Person"], [6, 9, "Date"]]}, {"tokenized_text": ["Welcome", "to", "all", "you", "folks", "in", "the", "Washington", "DC", "and", "Richmond", "area", "who", "heard", "my", "husband", ",", "comedian", "Christian", "Finnegan", ",", "pimping", "this", "site", "on", "the", "radio", "."], "ner": [[7, 8, "City"], [10, 10, "City"], [18, 19, "Person"]]}, {"tokenized_text": ["A", "sharing", "session", "on", "10", "years", "of", "World", "Clean-Up", "Day", "."], "ner": [[7, 9, "Event"], [1, 2, "Event"]]}, {"tokenized_text": ["Want", "to", "know", "how", "to", "sharpen", "kitchen", "shears", "?"], "ner": [[6, 7, "kitchen utensil"], [5, 5, "action"]]}, {"tokenized_text": ["Lightly", "humourous", "at", "times", ",", "it", "'", "s", "a", "very", "enjoyable", "read", "."], "ner": [[0, 1, "Tone"], [10, 10, "Emotion"]]}, {"tokenized_text": ["RSVP", "here", "!", "We", "\u2019", "ll", "be", "at", "a", "number", "of", "locations", "in", "2017", ",", "so", "be", "sure", "you", "check", "the", "venue", "!"], "ner": [[0, 0, "Event"], [13, 13, "Time"], [21, 21, "Location"]]}, {"tokenized_text": ["Please", "confirm", "your", "Wedding", "Reservation", "by", "sending", "your", "$", "100", ".", "00", "Deposit", "within", "a", "week", "of", "making", "your", "reservation", "."], "ner": [[3, 4, "Event Reservation"], [8, 12, "Payment"]]}, {"tokenized_text": ["Know", "East", "Jordan", "Class", "of", "2001", "graduates", "that", "are", "NOT", "on", "this", "List", "?", "Help", "us", "Update", "the", "2001", "Class", "List", "by", "adding", "missing", "names", "."], "ner": [[1, 5, "Educational institution"], [18, 20, "Document"]]}, {"tokenized_text": ["Pure", "Grapeseed", "oil", "extracted", "from", "the", "seed", "of", "the", "grape", "vitus", "vinifera", "."], "ner": [[1, 2, "Ingredient"], [9, 11, "Plant species"]]}, {"tokenized_text": ["According", "to", "the", "2015", "census", ",", "it", "has", "a", "population", "of", "70", ",", "757", "people", "."], "ner": [[3, 4, "Time"], [11, 14, "Quantity"]]}, {"tokenized_text": ["Earth", "Day", "Activities", "for", "the", "Whole", "Family", "!"], "ner": [[0, 1, "holiday/event"], [2, 2, "action/event"], [5, 6, "group/person"]]}, {"tokenized_text": ["Online", "Application", "Portal", "for", "LIBANIA", "K", ".", "G", "."], "ner": [[0, 2, "Technology Platform"], [4, 8, "Company"]]}, {"tokenized_text": ["All", "samples", "for", "analysis", "must", "be", "received", "with", "an", "appropriate", "Chain", "of", "Custody", "(", "COC", ")", "or", "sample", "submission", "form", "detailing", "the", "required", "analysis", "for", "the", "sample", "before", "work", "can", "commence", "."], "ner": [[10, 15, "Sample Submission"], [17, 17, "Analysis Requirement"], [26, 26, "Analysis Requirement"]]}, {"tokenized_text": ["Is", "the", "process", "the", "same", "as", "with", "that", "of", "regular", "scissors", "?"], "ner": [[2, 2, "tool/process"], [9, 10, "tool"]]}, {"tokenized_text": ["With", "this", "in", "mind", ",", "here", "are", "10", "tips", "that", "will", "help", "you", "pack", "like", "a", "boss", "and", "to", "do", "all", "of", "that", "on", "a", "short", "notice", "."], "ner": [[7, 8, "Action Item"], [13, 16, "Action Item"], [25, 26, "Time Frame"]]}, {"tokenized_text": ["Oroquieta", "is", "a", "city", "in", "and", "the", "capital", "of", "the", "province", "of", "Misamis", "Occidental", ",", "Philippines", "."], "ner": [[0, 0, "City"], [12, 13, "Province"], [15, 15, "Country"]]}, {"tokenized_text": ["First", ",", "remember", "there", "is", "no", "\u201c", "magic", "formula", "\u201d", "to", "female", "modeling", ".", "But", ",", "don", "\u2019", "t", "give", "up", "for", "that", "reason", ".", "Online", ",", "you", "\u2019", "ll", "find", "tons", "of", "modeling", "tips", "for", "female", "beginners", "to", "browse", "."], "ner": [[11, 12, "occupation"], [36, 37, "target audience"], [33, 34, "resource"]]}, {"tokenized_text": ["There", "is", "nothing", "better", "than", "going", "on", "a", "trip", ".", "However", ",", "you", "may", "never", "know", "what", "you", "could", "encounter", "there", "and", "in", "order", "to", "be", "ready", "for", "anything", "you", "need", "to", "pack", "properly", "."], "ner": [[8, 8, "activity/event"], [19, 19, "experience"]]}, {"tokenized_text": ["Shingle", "Express", ",", "Inc", ".", "has", "been", "providing", "reliable", "and", "quality", "gutter", "installations", "in", "Thornton", ",", "PA", "since", "2009", "."], "ner": [[0, 4, "Company"], [14, 16, "Location"], [18, 18, "Date"]]}, {"tokenized_text": ["You", "\u2019", "ll", "hear", "a", "new", "dial", "tone", "\u2013", "now", "enter", "the", "Chinese", "phone", "number", ",", "starting", "with", "the", "normal", "international", "dial", "code", "0086", "."], "ner": [[12, 14, "Phone Number"], [20, 22, "Phone Number Component"], [23, 23, "Phone Number Component"]]}, {"tokenized_text": ["We", "don", "'", "t", "have", "many", "details", "about", "this", "fly", ",", "apart", "from", "who", "tied", "it", "and", "the", "country", "of", "origin", "."], "ner": [[9, 9, "insect species"], [18, 20, "geographical location"], [14, 14, "action"]]}, {"tokenized_text": ["Returns", "a", "list", "of", "all", "nontoken", "English", "card", "names", "in", "Scryfall", "\u2019", "s", "database", ".", "Values", "are", "updated", "as", "soon", "as", "a", "new", "card", "is", "entered", "for", "spoiler", "seasons", "."], "ner": [[10, 13, "database"], [6, 8, "card name"], [27, 28, "event"]]}, {"tokenized_text": ["This", "is", "a", "writing", "course", "that", "prepares", "students", "for", "the", "many", "technical", "writing", "tasks", "they", "will", "encounter", "in", "the", "workplace", ".", "It", "provides", "thorough", "coverage", "of", "the", "basic", "skills", "and", "common", "techniques", "of", "technical", "writing", "."], "ner": [[3, 4, "education"], [7, 7, "group of people"], [11, 13, "job requirements"], [27, 28, "writing skills"], [30, 31, "writing techniques"]]}, {"tokenized_text": ["\"", "THE", "EXIT", "\"", "Signed", "by", "the", "artist", ".", "Size", ":", "A3", "(", "29", ",", "7", "x", "42", "cm", ")", "."], "ner": [[1, 2, "artwork title"], [7, 7, "person/artist name"], [9, 9, "physical attribute"]]}, {"tokenized_text": ["Few", "minutes", "walking", "from", "\"", "Le", "Carreau", "du", "Temple", "\"", "square", ",", "\"", "Republique", "\"", ",", "\"", "Bastille", "\"", "or", "\"", "Place", "des", "Vosges", "\"", "."], "ner": [[5, 8, "Landmark"], [13, 13, "Landmark"], [17, 17, "Landmark"], [21, 23, "Landmark"]]}, {"tokenized_text": ["The", "company", "offers", "the", "Ultra", "colposcope", ",", "a", "noninvasive", "device", "used", "to", "screen", "for", "cervical", "cancer", "by", "allowing", "the", "detection", "and", "diagnosis", "of", "precancerous", "lesions", "on", "the", "cervix", "."], "ner": [[4, 5, "Medical device"], [14, 15, "Medical condition"], [23, 24, "Medical condition"], [27, 27, "Anatomy"]]}, {"tokenized_text": ["Your", "Cub", "Cadet", "7300", "Compact", "Tractor", "Service", "manual", "will", "come", "to", "you", "in", "pdf", "format", "and", "is", "compressed", "for", "a", "lightning", "fast", "download", "!", "After", "downloading", "your", "Cub", "Cadet", "7300", "Compact", "Tractor", "Service", "manual", "you", "can", "view", "it", "on", "your", "computer", "or", "print", "one", "or", "all", "of", "the", "pages", "needed", "."], "ner": [[1, 5, "Product"], [27, 31, "Product"], [6, 7, "Document"], [32, 33, "Document"], [13, 14, "File type"], [40, 40, "Device"], [48, 48, "Document component"]]}, {"tokenized_text": ["Despite", "the", "rather", "serene", "appearance", "of", "my", "web", "page", "this", "week", ",", "this", "has", "personally", "been", "a", "rather", "hectic", "week", ".", "Following", "the", "earlier", "advice", "of", "a", "number", "of", "visitors", "to", "my", "page", ",", "I", "had", "been", "trying", "to", "avoid", "too", "many", "hours", "at", "the", "computer", "in", "an", "attempt", "to", "relieve", "the", "stress", "on", "my", "back", "."], "ner": [[7, 8, "website"], [10, 10, "time period"], [19, 19, "time period"], [29, 29, "website users"], [45, 45, "electronic device"], [52, 52, "mental/physical strain"]]}, {"tokenized_text": ["And", "now", "we", "'", "re", "delighted", "to", "bring", "you", "Indigo", "-", "the", "latest", "colour", "added", "to", "Michael", "Harding", "'", "s", "range", "of", "professional", "oil", "paints", "-", "sold", "exclusively", "here", "at", "Cass", "Art", "this", "summer", "."], "ner": [[9, 9, "Color"], [16, 17, "Brand"], [30, 31, "Retailer"], [33, 33, "Time"]]}, {"tokenized_text": ["The", "Triangle", "Scholarly", "Communication", "Institute", ",", "funded", "by", "the", "Andrew", "W", ".", "Mellon", "Foundation", ",", "invites", "proposals", "from", "groups", "interested", "in", "participating", "in", "a", "unique", "collaborative", "program", ",", "to", "be", "held", "over", "four", "days", "in", "Chapel", "Hill", ",", "North", "Carolina", ",", "in", "October", "2018", "."], "ner": [[0, 4, "Event/Program"], [9, 13, "Organization"], [35, 39, "Location"], [42, 43, "Time"]]}, {"tokenized_text": ["Cervical", "cancer", "if", "not", "caught", "early", "in", "the", "precancerous", "stage", "can", "be", "deadly", ".", "Approximately", "250", ",", "000", "women", "die", "each", "year", "around", "the", "world", "due", "to", "the", "disease", ",", "according", "to", "Scottish", "medical", "device", "firm", "DYSIS", "Medical", "."], "ner": [[0, 1, "medical condition"], [8, 9, "medical condition"], [15, 18, "demographic group"], [32, 37, "organization"]]}, {"tokenized_text": ["When", "We", "Were", "Kings", "won", "an", "Oscar", "for", "Best", "Documentary", "in", "1997", ".", "It", "feels", "as", "fresh", "as", "ever", "."], "ner": [[0, 3, "Film Title"], [6, 6, "Award"], [8, 9, "Award Category"], [11, 11, "Year"]]}, {"tokenized_text": ["Their", "key", "shareholders", "-", "African", "governments", "-", "seem", "incapable", "of", "acting", "decisively", "to", "stop", "the", "rot", ".", "Russell", "Southwood", "look", "at", "three", "different", "companies", "-", "Togo", "Telecom", ",", "Gabon", "Telecom", "and", "Sotelco", "in", "Congo-Brazzaville", "-", "whose", "current", "situation", "neatly", "illustrates", "what", "\u2019", "s", "happening", "."], "ner": [[4, 5, "Political entity"], [25, 26, "Telecommunications company"], [28, 29, "Telecommunications company"], [31, 31, "Telecommunications company"], [17, 18, "Person"]]}, {"tokenized_text": ["\u201a", "Visual", "Energy", "I", "\u2019", "is", "an", "album", "which", "Marcator", "recorded", "in", "1986", "with", "the", "flautist", "and", "saxophonist", "J\u00fcrgen", "Volbeding", ".", "It", "presents", "the", "climax", "of", "Marcator", "\u2019", "s", "electronic-meditative", "work", "."], "ner": [[9, 9, "Person"], [26, 26, "Person"], [1, 3, "Album"], [12, 12, "Date"], [15, 15, "Person"], [17, 17, "Person"], [18, 19, "Person"]]}, {"tokenized_text": ["Angel", "City", "Derby", "\u2013", "shots", "!", "shots", "!", "shots", "!"], "ner": [[0, 2, "Organization"], [4, 4, "Activity"], [6, 6, "Activity"], [8, 8, "Activity"]]}, {"tokenized_text": ["A", "timeless", "piece", "that", "will", "be", "around", "forever", "."], "ner": [[1, 2, "artistic creation"]]}, {"tokenized_text": ["Fine", "art", "Print", "(", "Gicl\u00e9e", ")", "Epson", "Enhanced", "Matte", "192g", "paper", "."], "ner": [[0, 2, "Artwork"], [4, 4, "Printing technique"], [6, 10, "Printing paper"]]}, {"tokenized_text": ["NOW", "AVAILABLE", "FOR", "2019-2020", ".", "This", "exceptionally", "spacious", "8", "bedroom", "property", "features", "a", "large", "modern", "kitchen", "with", "dishwasher", ".", "The", "bedrooms", "are", "all", "large", "and", "are", "furnished", "with", "double", "beds", ",", "wardrobes", "and", "desk", ".", "The", "property", "is", "situated", "close", "to", "the", "University", "in", "a", "sought", "after", "location", "."], "ner": [[3, 3, "Time"], [8, 10, "Accommodation"], [13, 15, "Kitchen"], [17, 17, "Appliance"], [20, 20, "Accommodation"], [28, 29, "Furniture"], [31, 31, "Furniture"], [33, 33, "Furniture"], [42, 42, "Educational institution"], [45, 47, "Location"]]}, {"tokenized_text": ["Prom", "Updo", "Hairstyles", "-", "Easy", "Prom", "Hairstyles", ".", "Red", "carpet", "ready", "updos", "hairstyles", "are", "much", "easier", "achieve", "than", "check", "out", "our", "picks", "for", "best", "easy", "prom", "your", "marks", "get", "set", "."], "ner": [[0, 2, "Hairstyle"], [8, 9, "Event Venue"], [4, 6, "Hairstyle"], [27, 27, "Idiom"], [28, 29, "Idiom"]]}, {"tokenized_text": ["Call", "us", "on", "0402", "139", "072", "we", "are", "more", "than", "happy", "to", "chat", "and", "answer", "any", "enquiries", ".", "If", "we", "happen", "to", "miss", "your", "call", "please", "leave", "a", "message", "and", "we", "will", "contact", "you", "asap", "."], "ner": [[3, 5, "phone number"], [12, 12, "communication method"], [16, 16, "inquiry type"], [28, 28, "communication method"], [34, 34, "time frame"]]}, {"tokenized_text": ["Classroom", "crisis", "\u2013", "Alex", "Wood", ".", "Education", "Consultant", "and", "Genealogist", "."], "ner": [[0, 1, "Issue/problem"], [3, 4, "Person"]]}, {"tokenized_text": ["Beyonc\u00e9", "is", "fighting", "against", "inequality", "and", "world", "hunger", "the", "best", "way", "she", "knows", "how", ":", "with", "a", "huge", "concert", "."], "ner": [[0, 0, "Person"], [4, 4, "Social Issue"], [6, 7, "Global Issue"], [18, 18, "Event"]]}, {"tokenized_text": ["The", "textile", "/", "garments", "industry", "dominates", "the", "Bangladesh", "industrial", "landscape", ".", "Many", "nnew", "jobs", "\u2013", "mostly", "for", "women", "\u2013", "have", "been", "created", "by", "the", "country", "\u2019", "s", "dynamic", "private", "ready-made", "garment", "industry", ",", "which", "grew", "at", "double-digit", "rates", "through", "most", "of", "the", "1990s", "."], "ner": [[7, 7, "Country"], [1, 4, "Industry"], [17, 17, "Gender"], [28, 31, "Industry"], [36, 37, "Measurement"], [42, 42, "Time period"]]}, {"tokenized_text": ["Family", "flat", "located", "on", "an", "upper", "floor", "(", "with", "lift", ")", "in", "the", "North", "historical", "Marais", "area", "-", "right", "bank", "of", "Paris", "."], "ner": [[0, 1, "Accommodation"], [5, 6, "Location"], [9, 9, "Facility"], [13, 16, "Location"], [18, 21, "Location"]]}, {"tokenized_text": ["3", "titles", "of", "more", "than", "20", "minutes", "each", "create", "musical", "images", "powered", "by", "analogue", "synthesizers", "together", "with", "brass", ",", "guitar", "and", "even", "sitar", "sounds", ",", "which", "modern", "digital", "technology", "is", "unlikely", "to", "reproduce", "."], "ner": [[13, 14, "musical instrument"], [17, 17, "musical instrument"], [19, 19, "musical instrument"], [22, 22, "musical instrument"], [27, 28, "technology"]]}, {"tokenized_text": ["The", "HotHouse", "is", "an", "urban", "\u201c", "country", "cafe", "\u201d", "featuring", "great", "Southern", "regional", "classics", "such", "as", "Shrimp", "and", "Grits", "and", "Fried", "Green", "Tomatoes", "."], "ner": [[0, 1, "Restaurant/Cafe"], [16, 18, "Food"], [20, 22, "Food"]]}, {"tokenized_text": ["Alsace", "is", "well", "known", "for", "it", "\u2019", "s", "beautiful", "Christmas", "Markets", ".", "The", "Strasbourg", "Christmas", "Market", "is", "the", "oldest", "Christmas", "market", "in", "France", "."], "ner": [[0, 0, "Location"], [13, 15, "Event"]]}, {"tokenized_text": ["A", "screenshot", "of", "video", "footage", "that", "shows", "a", "man", "approaching", "the", "altar", "at", "the", "Cathedral", "Basilica", "of", "the", "Sacred", "Heart", "and", "punching", "Newark", "Archdiocese", "Auxiliary", "Bishop", "Manuel", "Cruz", "in", "the", "face", "during", "mass", "on", "Jan", "."], "ner": [[14, 19, "Religious Place"], [22, 27, "Religious Leader"], [32, 32, "Religious Ceremony"], [34, 34, "Time/Date"]]}, {"tokenized_text": ["Battery", "charging", "cradle", "for", "use", "with", "3M", "\u2122", "Versaflo", "\u2122", "Powered", "Air", "Turbo", "."], "ner": [[0, 2, "product"], [6, 12, "product"], [11, 12, "device"], [0, 0, "object"], [1, 1, "action"], [2, 2, "object"]]}, {"tokenized_text": ["AlienDVR", "-", "Mobile", "Software", "for", "you", "AlienDVR", "View", "live", "images", "from", "you", "mobile", "!"], "ner": [[0, 0, "Software"], [6, 6, "Software"], [2, 2, "Hardware"], [12, 12, "Hardware"], [8, 9, "Media"]]}, {"tokenized_text": ["The", "last", "week", "before", "Christmas", "is", "when", "you", "\u2019", "ll", "see", "the", "biggest", "crowds", "."], "ner": [[4, 4, "Holiday/Event"], [2, 4, "Time/Period"]]}, {"tokenized_text": ["30pm", ".", "Alternatively", "you", "can", "visit", "the", "the", "Vicarage", "(", "30", "Jubilee", "Close", ")", "on", "a", "Thursday", "afternoon", "from", "1-3pm", "."], "ner": [[8, 8, "Building"], [11, 12, "Location"], [16, 17, "Time"]]}, {"tokenized_text": ["It", "is", "made", "of", "beautiful", "quilted", "caviar", "leather", "with", "a", "bold", "CC", "logo", "on", "the", "front", "and", "silvertone", "hardware", "."], "ner": [[5, 7, "material"], [11, 12, "brand/logo"], [17, 18, "material"]]}, {"tokenized_text": ["Hobart", "made", "183-6", "batting", "first", ",", "with", "opener", "Matthew", "Wade", "top-scoring", "with", "58", "even", "as", "Ben", "McDermott", "hit", "an", "unbeaten", "39", "."], "ner": [[0, 0, "Cricket Team"], [8, 9, "Cricketer"], [15, 16, "Cricketer"], [12, 12, "Batting Score"], [20, 20, "Batting Score"]]}, {"tokenized_text": ["Generate", "an", "official", "SPE", "electronic", "invitation", "letter", "to", "assist", "you", "in", "the", "visa", "process", "."], "ner": [[3, 6, "Official document"], [12, 13, "Procedure"]]}, {"tokenized_text": ["The", "IHC", "Family-Wh\u0101nau", "Liaison", "programme", "is", "a", "pilot", "programme", "running", "in", "Northland", ",", "Manawat\u016b", "/", "Horowhenua", "and", "Christchurch", "with", "thanks", "to", "the", "IHC", "Foundation", "."], "ner": [[1, 4, "programme name"], [11, 11, "geographic location"], [13, 15, "geographic location"], [17, 17, "geographic location"], [22, 23, "organization"]]}, {"tokenized_text": ["We", "recruit", "the", "most", "senior", "Java", "consultants", ",", "Java", "developers", "and", "Java", "programmers", "delivering", "professional", "consulting", "services", "for", "Java", "project", "work", "."], "ner": [[5, 6, "Job title"], [8, 9, "Job title"], [11, 12, "Job title"]]}, {"tokenized_text": ["Happy", "New", "Year", "!", "Welcome", "Sandhills", "Music", "Center", "to", "our", "Dealers", "!"], "ner": [[5, 7, "Business/organization"], [10, 10, "Business/organization"]]}, {"tokenized_text": ["Way", "back", "in", "1570", "at", "Place", "Broglie", ".", "The", "Christmas", "Market", "takes", "place", "every", "year", "around", "the", "end", "of", "November", "to", "the", "end", "of", "December", "."], "ner": [[3, 3, "Date"], [5, 6, "Location"], [9, 10, "Event"]]}, {"tokenized_text": ["Traversing", "southern", "China", ",", "a", "group", "of", "activists", "led", "by", "Ye", "Haiyan", "(", "aka", "Sparrow", ")", "protest", "a", "scandalous", "incident", "where", "a", "school", "principal", "and", "a", "government", "official", "allegedly", "raped", "six", "school", "girls", "."], "ner": [[1, 2, "geographical location"], [10, 15, "person"], [7, 7, "group"], [22, 23, "person"], [26, 27, "person"], [30, 32, "group"], [18, 19, "event"]]}, {"tokenized_text": ["This", "chic", "and", "durable", "Chanel", "Beige", "Clair", "Quilted", "Caviar", "Leather", "Grand", "Shopping", "Tote", "Bag", "will", "be", "your", "new", "favorite", "bag", "."], "ner": [[4, 13, "Fashion Item"], [4, 4, "Fashion Brand"], [8, 9, "Material Type"], [11, 13, "Bag Type"]]}, {"tokenized_text": ["We", "cordially", "welcome", "customers", "from", "at", "home", "and", "abroad", "to", "join", "us", "and", "cooperate", "with", "us", "to", "enjoy", "a", "better", "future", ".", "for", "Stretch", "Wrap", "Target", ",", "stretch", "wrap", "target", ",", "stretch", "wrap", "gauge", ",", "that", "will", "be", "more", "conveniently", "to", "service", "our", "customers", "."], "ner": [[3, 3, "person/group"], [43, 43, "person/group"], [6, 6, "location"], [8, 8, "location"], [23, 25, "product/service"], [27, 29, "product/service"], [23, 24, "product/service"], [27, 28, "product/service"], [31, 32, "product/service"], [33, 33, "measurement"], [41, 41, "action"]]}, {"tokenized_text": ["When", "you", "are", "not", "behind", "the", "wheel", ",", "battling", "traffic", "and", "pondering", "directions", "that", "just", "are", "not", "getting", "you", "where", "you", "want", "to", "go", ",", "it", "is", "best", "to", "have", "someone", "drive", "you", "."], "ner": [[9, 9, "transportation"], [12, 12, "navigation"], [30, 30, "transportation service"]]}]
```

## File: examples/convert_to_onnx.py

<a name='file-examples-convert_to_onnx.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install onnx


# In[ ]:


import torch
from gliner import GLiNER


# In[ ]:


model = GLiNER.from_pretrained("urchade/gliner_medium")


# In[ ]:


# save

model.save_pretrained("gliner_medium")


# In[ ]:


gliner_model = GLiNER.from_pretrained("gliner_medium", load_tokenizer=True)


# In[ ]:


import os

onnx_save_path = os.path.join("gliner_medium", "model.onnx")


# In[ ]:


text = "ONNX is an open-source format designed to enable the interoperability of AI models across various frameworks and tools."
labels = ['format', 'model', 'tool', 'cat']

inputs, _ = gliner_model.prepare_model_inputs([text], labels)


# In[ ]:


if gliner_model.config.span_mode == 'token_level':
    all_inputs =  (inputs['input_ids'], inputs['attention_mask'], 
                    inputs['words_mask'], inputs['text_lengths'])
    input_names = ['input_ids', 'attention_mask', 'words_mask', 'text_lengths']
    dynamic_axes={
        "input_ids": {0: "batch_size", 1: "sequence_length"},
        "attention_mask": {0: "batch_size", 1: "sequence_length"},
        "words_mask": {0: "batch_size", 1: "sequence_length"},
        "text_lengths": {0: "batch_size", 1: "value"},
        "logits": {0: "position", 1: "batch_size", 2: "sequence_length", 3: "num_classes"},
    }
else:
    all_inputs =  (inputs['input_ids'], inputs['attention_mask'], 
                    inputs['words_mask'], inputs['text_lengths'],
                    inputs['span_idx'], inputs['span_mask'])
    input_names = ['input_ids', 'attention_mask', 'words_mask', 'text_lengths', 'span_idx', 'span_mask']
    dynamic_axes={
        "input_ids": {0: "batch_size", 1: "sequence_length"},
        "attention_mask": {0: "batch_size", 1: "sequence_length"},
        "words_mask": {0: "batch_size", 1: "sequence_length"},
        "text_lengths": {0: "batch_size", 1: "value"},
        "span_idx": {0: "batch_size", 1: "num_spans", 2: "idx"},
        "span_mask": {0: "batch_size", 1: "num_spans"},
        "logits": {0: "batch_size", 1: "sequence_length", 2: "num_spans", 3: "num_classes"},
    }
print('Converting the model...')
torch.onnx.export(
    gliner_model.model,
    all_inputs,
    f=onnx_save_path,
    input_names=input_names,
    output_names=["logits"],
    dynamic_axes=dynamic_axes,
    opset_version=14,
)


# In[ ]:


#quantize model
from onnxruntime.quantization import quantize_dynamic, QuantType

quantized_save_path = os.path.join("gliner_medium", "model_quantized.onnx")
# Quantize the ONNX model
print("Quantizing the model...")
quantize_dynamic(
    onnx_save_path,  # Input model
    quantized_save_path,  # Output model
    weight_type=QuantType.QUInt8  # Quantize weights to 8-bit integers
)


# In[ ]:


# load onnx model
model = GLiNER.from_pretrained("gliner_medium", load_onnx_model=True, load_tokenizer=True)


# In[ ]:


text = """
Libretto by Marius Petipa, based on the 1822 novella ``Trilby, ou Le Lutin d'Argail`` by Charles Nodier, first presented by the Ballet of the Moscow Imperial Bolshoi Theatre on January 25/February 6 (Julian/Gregorian calendar dates), 1870, in Moscow with Polina Karpakova as Trilby and Ludiia Geiten as Miranda and restaged by Petipa for the Imperial Ballet at the Imperial Bolshoi Kamenny Theatre on January 17–29, 1871 in St. Petersburg with Adèle Grantzow as Trilby and Lev Ivanov as Count Leopold.
"""

labels = ["person", "book", "location", "date", "actor", "character"]

entities = model.predict_entities(text, labels, threshold=0.4)

for entity in entities:
    print(entity["text"], "=>", entity["label"])


# In[ ]:


# load quantized model
model = GLiNER.from_pretrained("gliner_medium", load_onnx_model=True, load_tokenizer=True, onnx_model_file="model_quantized.onnx")


# In[ ]:


text = """
Libretto by Marius Petipa, based on the 1822 novella ``Trilby, ou Le Lutin d'Argail`` by Charles Nodier, first presented by the Ballet of the Moscow Imperial Bolshoi Theatre on January 25/February 6 (Julian/Gregorian calendar dates), 1870, in Moscow with Polina Karpakova as Trilby and Ludiia Geiten as Miranda and restaged by Petipa for the Imperial Ballet at the Imperial Bolshoi Kamenny Theatre on January 17–29, 1871 in St. Petersburg with Adèle Grantzow as Trilby and Lev Ivanov as Count Leopold.
"""

labels = ["person", "book", "location", "date", "actor", "character"]

entities = model.predict_entities(text, labels, threshold=0.4)

for entity in entities:
    print(entity["text"], "=>", entity["label"])


```

## File: examples/synthetic_data_generation.py

<a name='file-examples-synthetic_data_generation.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# # **Using LLMs to Generate Synthetic Data for Fine-Tuning GLiNER**
# 
# In this notebook, we'll explore a simple way to generate synthetic data for fine-tuning GLiNER. I have used a similar approach to generate training data for [**PII extraction**](https://huggingface.co/urchade/gliner_multi_pii-v1). We will be using `Mistral-7B-Instruct-v0.2`, though I think there are better LLMs available online (like LLaMa-3 ... etc).
# 
# Additionally, the prompt used in this example is far from optimal, so you should adapt it to your specific use case or domain. This notebook serves only as an example for practitioners, as some people have requested one.
# 
# In this notebook, we generate **fully synthetic data**, including both text and entity annotations, but if you have quality data from your target domain, *you can alternatively have the LLM annotate your existing data*. 📊📝
# 
# Feel free to experiment and tailor the approach to better suit your needs! *Happy fine-tuning!* 🌟

# In[2]:


# install vllm (https://github.com/vllm-project/vllm)


# In[2]:


from vllm import LLM, SamplingParams


# ## Load large language model

# In[3]:


LLM_MODEL = "mistralai/Mistral-7B-Instruct-v0.2" # you can use a better model
NUM_GPUs = 4


# In[4]:


llm = LLM(model=LLM_MODEL, tensor_parallel_size=NUM_GPUs, dtype="half")


# In[5]:


# sampling parameters
sampling_params = SamplingParams(top_k=100, max_tokens=1000, top_p=0.8, stop="<end>")


# ## Prompting function

# In[6]:


def create_json_prompt_for_synthetic_data(**kwargs):
    
    # Use dictionary comprehension to filter out 'n/a' values and to keep the code flexible
    attributes = {key: value for key, value in kwargs.items() if value != "n/a"}
    
    # Building the initial part of the prompt
    prompt = """
**Objective:**
Produce realistic text passages that include clearly identified named entities. Each entity should be meticulously labeled according to its type for straightforward extraction.

**Format Requirements:**
- The output should be formatted in JSON, containing the text and the corresponding entities list.
- Each entity in the text should be accurately marked and annotated in the 'entities' list.
- Meticulously follow all the listed attributes.

**Entity Annotation Details:**
- All entity types must be in lowercase. For example, use "type" not "TYPE".
- Entity types can be multiwords separate by space. For instance, use "entity type" rather than "entity_type".
- Entities spans can be nested within other entities.
- A single entity may be associated with multiple types. list them in the key "types".

**Output Schema:**

<start attribute_1="value1" attribute_2="value2" ...>
{
  "text": "{text content}",
  "entities": [
    {"entity": "entity name", "types": ["type 1", "type 2", ...]},
    ...
  ]
}
<end>

**Here are some real world examples**:"""

    # Create a string of attributes for the <start> tag, excluding any 'n/a' values
    attributes_string = " ".join([f'{key}="{value}"' for key, value in attributes.items()])

    # Adding the dynamically created attributes string to the prompt
    prompt += f"""
<start {attributes_string}>
"""

    return prompt


# ## Example of generation

# In[7]:


import json

def generate(**kwargs):
    outputs = llm.generate([create_json_prompt_for_synthetic_data(**kwargs)], sampling_params)
    return json.loads(outputs[0].outputs[0].text)


# In[8]:


generate(language="french", types_of_text="detailled job ads", sector="machine learning", country="france")


# ## Functions

# In[9]:


# post processing functions

import re

def tokenize_text(text):
    """Tokenize the input text into a list of tokens."""
    return re.findall(r'\w+(?:[-_]\w+)*|\S', text)

def extract_entities(data):
    all_examples = []

    for dt in data:

        # Attempt to extract entities; skip current record on failure
        try:
            tokens = tokenize_text(dt['text'])
            ents = [(k["entity"], k["types"]) for k in dt['entities']]
        except:
            continue

        spans = []
        for entity in ents:
            entity_tokens = tokenize_text(str(entity[0]))

            # Find the start and end indices of each entity in the tokenized text
            for i in range(len(tokens) - len(entity_tokens) + 1):
                if " ".join(tokens[i:i + len(entity_tokens)]).lower() == " ".join(entity_tokens).lower():
                    for el in entity[1]:
                        spans.append((i, i + len(entity_tokens) - 1, el.lower().replace('_', ' ')))

        # Append the tokenized text and its corresponding named entity recognition data
        all_examples.append({"tokenized_text": tokens, "ner": spans})

    return all_examples

# generation functions
def generate_from_prompts(prompts, llm, sampling_params):
    outputs = llm.generate(prompts, sampling_params)

    all_outs = []
    
    for output in outputs:
        try:
            js = json.loads(output.outputs[0].text.strip())
        except:
            continue
            
        all_outs.append(js)

    return all_outs, extract_entities(all_outs)


# ## Use case: synthetic data for job ads

# In[10]:


# I have used GPT-4 to generate these

# List of countries
countries = [
    "Madagascar", "Taiwan", "USA", "Germany", "France", "Spain", "Russia", "China", 
    "Japan", "Brazil", "India", "Egypt", "South Africa", "Australia", "Canada", 
    "Mexico", "Indonesia", "Nigeria", "Turkey", "United Kingdom", "Italy", "Poland", 
    "Argentina", "Netherlands", "Belgium", "Switzerland", "Sweden", "Norway", "Finland",
    "Denmark", "Portugal", "Greece", "Iran", "Thailand", "Philippines", "Vietnam", 
    "South Korea", "Saudi Arabia", "Israel", "UAE", "New Zealand", "Ireland", "Malaysia",
    "Singapore", "Hong Kong", "Czech Republic", "Hungary", "Romania", "Colombia", 
    "Peru", "Venezuela", "Chile", "Morocco", "Algeria", "Tunisia", "Nepal", "Pakistan", "Bangladesh", 
    "Kazakhstan", "Ukraine", "Austria", "Croatia", "Serbia", "Kenya", "Ghana", "Zimbabwe",
    "Cuba", "Panama", "Fiji", "Mongolia", "North Korea", "Myanmar", "Ethiopia", "Tanzania",
    "Algeria", "Libya", "Jordan", "Qatar", "Oman", "Kuwait", "Lebanon", "Bulgaria", "Slovakia",
    "Lithuania", "Latvia", "Estonia", "Cyprus", "Luxembourg", "Macao", "Bhutan", "Maldives",
    "Angola", "Cameroon", "Senegal", "Mali", "Zambia", "Uganda", "Namibia", "Botswana",
    "Mozambique", "Ivory Coast", "Burkina Faso", "Malawi", "Gabon", "Lesotho", "Gambia",
    "Guinea", "Cape Verde", "Rwanda", "Benin", "Burundi", "Somalia", "Eritrea", "Djibouti",
    "Togo", "Seychelles", "Chad", "Central African Republic", "Liberia", "Mauritania", "Sri Lanka",
    "Sierra Leone", "Equatorial Guinea", "Swaziland", "Congo (Kinshasa)", "Congo (Brazzaville)"
]

# job sectors
job_sectors = [
    # Finance Sector Specializations
    "Investment Banking",
    "Corporate Finance",
    "Asset Management",
    "Risk Management",
    "Quantitative Analysis",
    "Financial Planning",
    
    # Machine Learning and AI Specializations
    "Natural Language Processing",
    "Computer Vision",
    "Deep Learning",
    "Reinforcement Learning",
    "Predictive Analytics",
    "Algorithm Development",
    
    # Healthcare Sector Specializations
    "Medical Research",
    "Clinical Trials",
    "Health Informatics",
    "Biomedical Engineering",
    "Public Health Administration",
    "Pharmaceuticals",
    
    # Education Sector Specializations
    "Curriculum Development",
    "Educational Technology",
    "Special Education",
    "Higher Education Administration",
    "Educational Policy",
    "Language Instruction",
    
    # Manufacturing Sector Specializations
    "Process Engineering",
    "Quality Control",
    "Industrial Design",
    "Supply Chain Optimization",
    "Robotics Manufacturing",
    "Lean Manufacturing",
    
    # Energy Sector Specializations
    "Renewable Energy Systems",
    "Oil and Gas Exploration",
    "Energy Efficiency Consulting",
    "Nuclear Engineering",
    "Smart Grid Technology",
    "Energy Policy",
    
    # Environmental Sector Specializations
    "Wildlife Conservation",
    "Environmental Science",
    "Water Resource Management",
    "Sustainability Strategy",
    "Climate Change Analysis",
    "Environmental Law",
    
    # Media and Communications Specializations
    "Digital Marketing",
    "Journalism",
    "Public Relations",
    "Film Production",
    "Broadcasting",
    "Content Strategy",
    
    # Legal Sector Specializations
    "Corporate Law",
    "International Law",
    "Intellectual Property",
    "Environmental Law",
    "Civil Litigation",
    "Criminal Defense",
    
    # Retail Sector Specializations
    "E-commerce Strategy",
    "Store Management",
    "Merchandise Planning",
    "Customer Experience Management",
    "Retail Analytics",
    "Supply Chain Logistics"
]


# ### Generate prompts

# In[11]:


# create prompts
NUM_SAMPLES = 100

import random

all_prompts = []

for i in range(NUM_SAMPLES):
    # sample
    job_sector = random.choice(job_sectors)
    country = random.choice(countries)
    
    prompt = create_json_prompt_for_synthetic_data(language="english", 
                                                   types_of_text="detailled job ads", 
                                                   sector=job_sector, 
                                                   country=country)
    all_prompts.append(prompt)


# ### Generate outputs

# In[12]:


output, processed_output = generate_from_prompts(all_prompts, llm, sampling_params)


# In[13]:


output[0]


# ### Some statistics

# In[26]:


lengths = []

for d in processed_output:
    lengths.append(len(d["tokenized_text"]))

print("Avg num tokens:", sum(lengths) / len(lengths))


# In[27]:


len_ner = []

for d in processed_output:
    len_ner.append(len(d["ner"]))
        
print("Avg num of entities:", sum(len_ner) / len(len_ner))


# In[28]:


unique_entities = []

for d in processed_output:
    for n in d["ner"]:
        unique_entities.append((str(n[2]).lower()))

print("Unique entity types:", len(unique_entities))


# In[21]:


# Top 10 entity types

from collections import Counter
Counter(unique_entities).most_common()[:10]


# ### Save for training

# In[22]:


# Save to JSON
def save_data_to_file(data, filepath):
    """Saves the processed data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f)


# In[23]:


output_file = "job_ads_data_gliner.json"

save_data_to_file(processed_output, output_file)


# In[ ]:





```

## File: examples/load_local_model.py

<a name='file-examples-load_local_model.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from gliner import GLiNER


# In[ ]:


# first load your model

model = GLiNER.from_pretrained("gliner-community/gliner_medium-v2.5")


# ## Option 1

# In[ ]:


# save

model.save_pretrained("gliner_Med")


# In[ ]:


# load

loaded_model = GLiNER.from_pretrained("gliner_Med", load_tokenizer = True, local_files_only=True)


# ## Option 2

# In[ ]:


def save_model(current_model, path):
    config = current_model.config
    dict_save = {"model_weights": current_model.state_dict(), "config": config}
    torch.save(dict_save, path)


def load_model(path, model_name=None):
    
    dict_load = torch.load(path, map_location=torch.device('cpu'))
    config = dict_load["config"]

    print(f"'{config.model_name}' should be available for local processing")

    if model_name is not None:
        config.model_name = model_name

    loaded_model = GLiNER(config)
    loaded_model.load_state_dict(dict_load["model_weights"])
    return loaded_model


# In[ ]:


# save the model weight

save_model(model, "model_weight.pt")


# In[ ]:


# load model weight

loaded_model = load_model("model_weight.pt")
print("success !!")


# ## Testing

# In[ ]:


text = """
Libretto by Marius Petipa, based on the 1822 novella ``Trilby, ou Le Lutin d'Argail`` by Charles Nodier, first presented by the Ballet of the Moscow Imperial Bolshoi Theatre on January 25/February 6 (Julian/Gregorian calendar dates), 1870, in Moscow with Polina Karpakova as Trilby and Ludiia Geiten as Miranda and restaged by Petipa for the Imperial Ballet at the Imperial Bolshoi Kamenny Theatre on January 17–29, 1871 in St. Petersburg with Adèle Grantzow as Trilby and Lev Ivanov as Count Leopold.
"""

labels = ["person", "book", "location", "date", "actor", "character"]

entities = loaded_model.predict_entities(text, labels, threshold=0.4)

for entity in entities:
    print(entity["text"], "=>", entity["label"])


# In[ ]:





```

## File: examples/exal_example_conll.py

<a name='file-examples-exal_example_conll.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install datasets')


# In[10]:


from datasets import load_dataset


# In[11]:


def ner_tags_to_spans(samples, tag_to_id):
    """
    Converts NER tags in the dataset samples to spans (start, end, entity type).
    
    Args:
        samples (dict): A dictionary containing the tokens and NER tags.
        tag_to_id (dict): A dictionary mapping NER tags to IDs.
    
    Returns:
        dict: A dictionary containing tokenized text and corresponding NER spans.
    """
    ner_tags = samples["ner_tags"]
    id_to_tag = {v: k for k, v in tag_to_id.items()}
    spans = []
    start_pos = None
    entity_name = None

    for i, tag in enumerate(ner_tags):
        if tag == 0:  # 'O' tag
            if entity_name is not None:
                spans.append((start_pos, i - 1, entity_name))
                entity_name = None
                start_pos = None
        else:
            tag_name = id_to_tag[tag]
            if tag_name.startswith('B-'):
                if entity_name is not None:
                    spans.append((start_pos, i - 1, entity_name))
                entity_name = tag_name[2:]
                start_pos = i
            elif tag_name.startswith('I-'):
                continue

    # Handle the last entity if the sentence ends with an entity
    if entity_name is not None:
        spans.append((start_pos, len(samples["tokens"]) - 1, entity_name))
    
    return {"tokenized_text": samples["tokens"], "ner": spans}


# In[ ]:


# step 1: load data
dataset = load_dataset("eriktks/conll2003")


# In[13]:


# Step 2: Define NER tag-to-ID mapping
tag_to_id = {
    'O': 0, 'B-person': 1, 'I-person': 2, 'B-organization': 3, 'I-organization': 4,
    'B-location': 5, 'I-location': 6, 'B-others': 7, 'I-others': 8
}


# In[14]:


# Convert NER tags to spans for the training data
gliner_data_conll = [ner_tags_to_spans(i, tag_to_id) for i in dataset['train']]


# In[15]:


# Load the pre-trained GLiNER model
from gliner import GLiNER
import torch

model = GLiNER.from_pretrained("urchade/gliner_small", load_tokenizer=True) #true if a model was trained from scratch with new code base

if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"

model = model.to(device)


# In[17]:


# Evaluate the model on the first 100 samples
evaluation_results = model.evaluate(
    gliner_data_conll[:100], flat_ner=True, entity_types=["person", "organization", "location", "others"]
)


# In[18]:


print(evaluation_results)


# In[ ]:





```

## File: examples/gliner_spacy_demo.py

<a name='file-examples-gliner_spacy_demo.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
from gliner_spacy.pipeline import GlinerSpacy


# In[2]:


nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("gliner_spacy")


# In[3]:


text = "This is a text about Bill Gates and Microsoft."
doc = nlp(text)


# In[4]:


from spacy import displacy


# In[5]:


displacy.render(doc, style="ent")


# In[6]:


for ent in doc.ents:
    print(ent.text, ent.label_)


# In[ ]:





```

## File: examples/quickstart.py

<a name='file-examples-quickstart.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gliner import GLiNER


# In[ ]:


# available models: https://huggingface.co/urchade

model = GLiNER.from_pretrained("urchade/gliner_medium")
model.eval()
print("ok")


# In[ ]:


text = """
Libretto by Marius Petipa, based on the 1822 novella ``Trilby, ou Le Lutin d'Argail`` by Charles Nodier, first presented by the Ballet of the Moscow Imperial Bolshoi Theatre on January 25/February 6 (Julian/Gregorian calendar dates), 1870, in Moscow with Polina Karpakova as Trilby and Ludiia Geiten as Miranda and restaged by Petipa for the Imperial Ballet at the Imperial Bolshoi Kamenny Theatre on January 17–29, 1871 in St. Petersburg with Adèle Grantzow as Trilby and Lev Ivanov as Count Leopold.
"""

labels = ["person", "book", "location", "date", "actor", "character"]

entities = model.predict_entities(text, labels, threshold=0.4)

for entity in entities:
    print(entity["text"], "=>", entity["label"])


# In[ ]:





```

## File: examples/finetune.py

<a name='file-examples-finetune.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install gliner')
get_ipython().system(' pip install accelerate -U')


# In[5]:


# download data
get_ipython().system(' wget https://huggingface.co/datasets/urchade/synthetic-pii-ner-mistral-v1/resolve/main/data.json')


# In[6]:


import json
import random


# In[7]:


train_path = "data.json"

with open(train_path, "r") as f:
    data = json.load(f)

print('Dataset size:', len(data))

random.shuffle(data)
print('Dataset is shuffled...')

train_dataset = data[:int(len(data)*0.9)]
test_dataset = data[int(len(data)*0.9):]

print('Dataset is splitted...')


# In[8]:


import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"

import torch
from gliner import GLiNERConfig, GLiNER
from gliner.training import Trainer, TrainingArguments
from gliner.data_processing.collator import DataCollatorWithPadding, DataCollator
from gliner.utils import load_config_as_namespace
from gliner.data_processing import WordsSplitter, GLiNERDataset


# In[9]:


device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu')

model = GLiNER.from_pretrained("urchade/gliner_small")


# In[10]:


# use it for better performance, it mimics original implementation but it's less memory efficient
data_collator = DataCollator(model.config, data_processor=model.data_processor, prepare_labels=True)


# In[11]:


# Optional: compile model for faster training
model.to(device)
print("done")


# In[ ]:


# calculate number of epochs
num_steps = 500
batch_size = 8
data_size = len(train_dataset)
num_batches = data_size // batch_size
num_epochs = max(1, num_steps // num_batches)

training_args = TrainingArguments(
    output_dir="models",
    learning_rate=5e-6,
    weight_decay=0.01,
    others_lr=1e-5,
    others_weight_decay=0.01,
    lr_scheduler_type="linear", #cosine
    warmup_ratio=0.1,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    focal_loss_alpha=0.75,
    focal_loss_gamma=2,
    num_train_epochs=num_epochs,
    evaluation_strategy="steps",
    save_steps = 100,
    save_total_limit=10,
    dataloader_num_workers = 0,
    use_cpu = False,
    report_to="none",
    )

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    tokenizer=model.data_processor.transformer_tokenizer,
    data_collator=data_collator,
)

trainer.train()


# In[16]:


trained_model = GLiNER.from_pretrained("models/checkpoint-100", load_tokenizer=True)


# In[17]:


text = """
Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
"""

# Labels for entity prediction
labels = ["Person", "Award"] # for v2.1 use capital case for better performance

# Perform entity prediction
entities = trained_model.predict_entities(text, labels, threshold=0.5)

# Display predicted entities and their labels
for entity in entities:
    print(entity["text"], "=>", entity["label"])


```

## File: configs/config_span.yaml

<a name='file-configs-config_span.yaml'></a>
*Description*: No specific description available.

```plaintext
# Model Configuration
model_name: microsoft/deberta-v3-small  # Hugging Face model
name: "span level gliner"
max_width: 12
hidden_size: 768
dropout: 0.4
fine_tune: true
subtoken_pooling: first
span_mode: markerV0

# Training Parameters
num_steps: 30000
train_batch_size: 8
eval_every: 5000
warmup_ratio: 0.1
scheduler_type: "cosine"

# loss function
loss_alpha: -1 # focal loss alpha, if -1, no focal loss
loss_gamma: 0 # focal loss gamma, if 0, no focal loss
label_smoothing: 0
loss_reduction: "sum"

# Learning Rate and weight decay Configuration
lr_encoder: 1e-5
lr_others: 5e-5
weight_decay_encoder: 0.01
weight_decay_other: 0.01

max_grad_norm: 1.0

# Directory Paths
root_dir: span_gliner_logs
train_data: "data.json" # see https://github.com/urchade/GLiNER/tree/main/data
val_data_dir: "none"
# "NER_datasets": val data from the paper can be obtained from "https://drive.google.com/file/d/1T-5IbocGka35I7X3CE6yKe5N_Xg2lVKT/view"

# Pretrained Model Path
# Use "none" if no pretrained model is being used
prev_path: "none"

save_total_limit: 10 #maximum amount of checkpoints to save

# Advanced Training Settings
size_sup: -1
max_types: 25
shuffle_types: true
random_drop: true
max_neg_type_ratio: 1
max_len: 384
freeze_token_rep: false

```

## File: configs/config_token.yaml

<a name='file-configs-config_token.yaml'></a>
*Description*: No specific description available.

```plaintext
# Model Configuration
model_name: microsoft/deberta-v3-small  # Hugging Face model
name: "token level gliner"
max_width: 100
hidden_size: 768
dropout: 0.1
fine_tune: true
subtoken_pooling: first
span_mode: token_level

# Training Parameters
num_steps: 30000
train_batch_size: 8
eval_every: 5000
warmup_ratio: 0.1
scheduler_type: "cosine"

# loss function
loss_alpha: -1 # focal loss alpha, if -1, no focal loss
loss_gamma: 0 # focal loss gamma, if 0, no focal loss
label_smoothing: 0
loss_reduction: "sum"

# Learning Rate and weight decay Configuration
lr_encoder: 1e-5
lr_others: 5e-5
weight_decay_encoder: 0.01
weight_decay_other: 0.01

max_grad_norm: 1.0

# Directory Paths
root_dir: gliner_logs
train_data: "train.json" # see https://github.com/urchade/GLiNER/tree/main/data
val_data_dir: "NER_datasets"
# "NER_datasets": val data from the paper can be obtained from "https://drive.google.com/file/d/1T-5IbocGka35I7X3CE6yKe5N_Xg2lVKT/view"

# Pretrained Model Path
# Use "none" if no pretrained model is being used
prev_path: "none"

save_total_limit: 10 #maximum amount of checkpoints to save

# Advanced Training Settings
size_sup: -1
max_types: 25
shuffle_types: true
random_drop: true
max_neg_type_ratio: 1
max_len: 384
freeze_token_rep: false


```

## File: configs/config.yaml

<a name='file-configs-config.yaml'></a>
*Description*: No specific description available.

```plaintext
# Model Configuration
model_name: microsoft/deberta-v3-small # Hugging Face model
labels_encoder: "BAAI/bge-small-en-v1.5"
name: "span level gliner"
max_width: 12
hidden_size: 768
dropout: 0.3
fine_tune: true
subtoken_pooling: first
fuse_layers: false
post_fusion_schema: "l2l-l2t-t2t"
span_mode: markerV0

# Training Parameters
num_steps: 100000
train_batch_size: 8
eval_every: 5000
warmup_ratio: 0.05
scheduler_type: "cosine"

# loss function
loss_alpha: 0.75
loss_gamma: 0
label_smoothing: 0
loss_reduction: "sum"

# Learning Rate and weight decay Configuration
lr_encoder: 1e-5
lr_others: 3e-5
weight_decay_encoder: 0.1
weight_decay_other: 0.01

max_grad_norm: 10.0

# Directory Paths
root_dir: gliner_logs
train_data: "data.json" #"data/nuner_train.json" # see https://github.com/urchade/GLiNER/tree/main/data
val_data_dir: "none"
# "NER_datasets": val data from the paper can be obtained from "https://drive.google.com/file/d/1T-5IbocGka35I7X3CE6yKe5N_Xg2lVKT/view"

# Pretrained Model Path
# Use "none" if no pretrained model is being used
prev_path: null

save_total_limit: 3 #maximum amount of checkpoints to save

# Advanced Training Settings
size_sup: -1
max_types: 100
shuffle_types: true
random_drop: true
max_neg_type_ratio: 1
max_len: 512
freeze_token_rep: false

```

## File: configs/config_biencoder.yaml

<a name='file-configs-config_biencoder.yaml'></a>
*Description*: No specific description available.

```plaintext
# Model Configuration
model_name: microsoft/deberta-v3-small # Hugging Face model
labels_encoder: "microsoft/deberta-v3-small"
name: "span level gliner"
max_width: 12
hidden_size: 768
dropout: 0.4
fine_tune: true
subtoken_pooling: first
fuse_layers: false
post_fusion_schema: ""
span_mode: markerV0

# Training Parameters
num_steps: 30000
train_batch_size: 8
eval_every: 1000
warmup_ratio: 0.1
scheduler_type: "cosine"

# loss function
loss_alpha: -1
loss_gamma: 0
label_smoothing: 0
loss_reduction: "sum"

# Learning Rate and weight decay Configuration
lr_encoder: 1e-5
lr_others: 5e-5
weight_decay_encoder: 0.01
weight_decay_other: 0.01

max_grad_norm: 10.0

# Directory Paths
root_dir: gliner_logs
train_data: "data.json" #"data/nuner_train.json" # see https://github.com/urchade/GLiNER/tree/main/data
val_data_dir: "none"
# "NER_datasets": val data from the paper can be obtained from "https://drive.google.com/file/d/1T-5IbocGka35I7X3CE6yKe5N_Xg2lVKT/view"

# Pretrained Model Path
# Use "none" if no pretrained model is being used
prev_path: null

save_total_limit: 3 #maximum amount of checkpoints to save

# Advanced Training Settings
size_sup: -1
max_types: 25
shuffle_types: true
random_drop: true
max_neg_type_ratio: 1
max_len: 386
freeze_token_rep: false

```

## File: logo/FI Group.png

<a name='file-logo-FI Group.png'></a>
*Description*: No specific description available.

*This file is binary and cannot be displayed as text.*
## File: logo/FI_COMPLET_CW.png

<a name='file-logo-FI_COMPLET_CW.png'></a>
*Description*: No specific description available.

*This file is binary and cannot be displayed as text.*
## File: gliner/__init__.py

<a name='file-gliner-__init__.py'></a>
*Description*: This is a Python script.

```python
__version__ = "0.2.15"

from .model import GLiNER
from .config import GLiNERConfig
# from .multitask import (GLiNERClassifier, GLiNERQuestionAnswerer, GLiNEROpenExtractor,
#                                 GLiNERRelationExtractor, GLiNERSummarizer, GLiNERSquadEvaluator,
#                                     GLiNERDocREDEvaluator)

__all__ = ["GLiNER"]

```

## File: gliner/model.py

<a name='file-gliner-model.py'></a>
*Description*: This is a Python script.

```python
import json
import os
import re
import warnings
from tqdm import tqdm
from pathlib import Path
from typing import Dict, List, Optional, Union

import onnxruntime as ort
import torch
from torch.utils.data import DataLoader
from huggingface_hub import PyTorchModelHubMixin, snapshot_download
from torch import nn
from transformers import AutoConfig, AutoTokenizer
from safetensors import safe_open
from safetensors.torch import save_file

from .config import GLiNERConfig
from .data_processing import SpanProcessor, SpanBiEncoderProcessor, TokenProcessor, TokenBiEncoderProcessor
from .data_processing.collator import DataCollator, DataCollatorWithPadding
from .data_processing.tokenizer import WordsSplitter
from .decoding import SpanDecoder, TokenDecoder
from .evaluation import Evaluator
from .modeling.base import BaseModel, SpanModel, TokenModel
from .onnx.model import BaseORTModel, SpanORTModel, TokenORTModel


class GLiNER(nn.Module, PyTorchModelHubMixin):
    def __init__(
        self,
        config: GLiNERConfig,
        model: Optional[Union[BaseModel, BaseORTModel]] = None,
        tokenizer: Optional[Union[str, AutoTokenizer]] = None,
        words_splitter: Optional[Union[str, WordsSplitter]] = None,
        data_processor: Optional[Union[SpanProcessor, TokenProcessor]] = None,
        encoder_from_pretrained: bool = True,
    ):
        """
        Initialize the GLiNER model.

        Args:
            config (GLiNERConfig): Configuration object for the GLiNER model.
            model (Optional[Union[BaseModel, BaseORTModel]]): GLiNER model to use for predictions. Defaults to None.
            tokenizer (Optional[Union[str, AutoTokenizer]]): Tokenizer to use. Can be a string (path or name) or an AutoTokenizer instance. Defaults to None.
            words_splitter (Optional[Union[str, WordsSplitter]]): Words splitter to use. Can be a string or a WordsSplitter instance. Defaults to None.
            data_processor (Optional[Union[SpanProcessor, TokenProcessor]]): Data processor - object that prepare input to a model. Defaults to None.
            encoder_from_pretrained (bool): Whether to load the encoder from a pre-trained model or init from scratch. Defaults to True.
        """
        super().__init__()
        self.config = config

        if tokenizer is None and data_processor is None:
            tokenizer = AutoTokenizer.from_pretrained(config.model_name)

        if words_splitter is None and data_processor is None:
            words_splitter = WordsSplitter(config.words_splitter_type)

        if config.span_mode == "token_level":
            if model is None:
                self.model = TokenModel(config, encoder_from_pretrained)
            else:
                self.model = model
            if data_processor is None:
                if config.labels_encoder is not None:
                    labels_tokenizer = AutoTokenizer.from_pretrained(config.labels_encoder)
                    self.data_processor = TokenBiEncoderProcessor(config, tokenizer, words_splitter, labels_tokenizer)
                else:
                    self.data_processor = TokenProcessor(config, tokenizer, words_splitter)

            else:
                self.data_processor = data_processor
            self.decoder = TokenDecoder(config)
        else:
            if model is None:
                self.model = SpanModel(config, encoder_from_pretrained)
            else:
                self.model = model
            if data_processor is None:
                if config.labels_encoder is not None:
                    labels_tokenizer = AutoTokenizer.from_pretrained(config.labels_encoder)
                    self.data_processor = SpanBiEncoderProcessor(config, tokenizer, words_splitter, labels_tokenizer)
                else:
                    self.data_processor = SpanProcessor(config, tokenizer, words_splitter)
            else:
                self.data_processor = data_processor
            self.decoder = SpanDecoder(config)

        if config.vocab_size != -1 and config.vocab_size != len(
            self.data_processor.transformer_tokenizer
        ):
            warnings.warn(f"""Vocab size of the model ({config.vocab_size}) does't match length of tokenizer ({len(self.data_processor.transformer_tokenizer)}). 
                            You should to consider manually add new tokens to tokenizer or to load tokenizer with added tokens.""")

        if isinstance(self.model, BaseORTModel):
            self.onnx_model = True
        else:
            self.onnx_model = False

        # to suppress an AttributeError when training
        self._keys_to_ignore_on_save = None

    def forward(self, *args, **kwargs):
        """Wrapper function for the model's forward pass."""
        output = self.model(*args, **kwargs)
        return output

    @property
    def device(self):
        if self.onnx_model:
            providers = self.model.session.get_providers()
            if 'CUDAExecutionProvider' in providers:
                return torch.device('cuda')
            return torch.device('cpu')
        device = next(self.model.parameters()).device
        return device

    def resize_token_embeddings(
        self,
        add_tokens,
        set_class_token_index=True,
        add_tokens_to_tokenizer=True,
        pad_to_multiple_of=None,
    ) -> nn.Embedding:
        """
        Resize the token embeddings of the model.

        Args:
            add_tokens: The tokens to add to the embedding layer.
            set_class_token_index (bool, optional): Whether to set the class token index. Defaults to True.
            add_tokens_to_tokenizer (bool, optional): Whether to add the tokens to the tokenizer. Defaults to True.
            pad_to_multiple_of (int, optional): If set, pads the embedding size to be a multiple of this value. Defaults to None.

        Returns:
            nn.Embedding: The resized embedding layer.
        """
        if set_class_token_index:
            self.config.class_token_index = (
                len(self.data_processor.transformer_tokenizer) + 1
            )
        if add_tokens_to_tokenizer:
            self.data_processor.transformer_tokenizer.add_tokens(add_tokens)
        new_num_tokens = len(self.data_processor.transformer_tokenizer)
        model_embeds = self.model.token_rep_layer.resize_token_embeddings(
            new_num_tokens, pad_to_multiple_of
        )
        # update vocab size
        self.config.vocab_size = model_embeds.num_embeddings

        if self.config.encoder_config is not None:
            self.config.encoder_config.vocab_size = model_embeds.num_embeddings

        return model_embeds

    def prepare_texts(self, texts: List[str]):
        """
        Prepare inputs for the model.

        Args:
            texts (str): The input text or texts to process.
            labels (str): The corresponding labels for the input texts.
        """
        all_tokens = []
        all_start_token_idx_to_text_idx = []
        all_end_token_idx_to_text_idx = []

        for text in texts:
            tokens = []
            start_token_idx_to_text_idx = []
            end_token_idx_to_text_idx = []
            for token, start, end in self.data_processor.words_splitter(text):
                tokens.append(token)
                start_token_idx_to_text_idx.append(start)
                end_token_idx_to_text_idx.append(end)
            all_tokens.append(tokens)
            all_start_token_idx_to_text_idx.append(start_token_idx_to_text_idx)
            all_end_token_idx_to_text_idx.append(end_token_idx_to_text_idx)

        input_x = [{"tokenized_text": tk, "ner": None} for tk in all_tokens]

        return input_x, all_start_token_idx_to_text_idx, all_end_token_idx_to_text_idx


    def prepare_model_inputs(self, texts: List[str], labels: List[str], prepare_entities: bool = True):
        """
        Prepare inputs for the model.

        Args:
            texts (str): The input text or texts to process.
            labels (str): The corresponding labels for the input texts.
        """
        # preserving the order of labels
        labels = list(dict.fromkeys(labels))

        class_to_ids = {k: v for v, k in enumerate(labels, start=1)}
        id_to_classes = {k: v for v, k in class_to_ids.items()}

        input_x, all_start_token_idx_to_text_idx, all_end_token_idx_to_text_idx = self.prepare_texts(texts)

        raw_batch = self.data_processor.collate_raw_batch(input_x, labels,
                                                        class_to_ids = class_to_ids,
                                                        id_to_classes = id_to_classes)
        raw_batch["all_start_token_idx_to_text_idx"] = all_start_token_idx_to_text_idx
        raw_batch["all_end_token_idx_to_text_idx"] = all_end_token_idx_to_text_idx

        model_input = self.data_processor.collate_fn(raw_batch, prepare_labels=False,
                                                        prepare_entities=prepare_entities)
        model_input.update(
            {
                "span_idx": raw_batch["span_idx"] if "span_idx" in raw_batch else None,
                "span_mask": raw_batch["span_mask"]
                if "span_mask" in raw_batch
                else None,
                "text_lengths": raw_batch["seq_length"],
            }
        )

        device = self.device
        for key in model_input:
            if model_input[key] is not None and isinstance(
                model_input[key], torch.Tensor
            ):
                model_input[key] = model_input[key].to(device)

        return model_input, raw_batch

    def predict_entities(
        self, text, labels, flat_ner=True, threshold=0.5, multi_label=False
    ):
        """
        Predict entities for a single text input.

        Args:
            text: The input text to predict entities for.
            labels: The labels to predict.
            flat_ner (bool, optional): Whether to use flat NER. Defaults to True.
            threshold (float, optional): Confidence threshold for predictions. Defaults to 0.5.
            multi_label (bool, optional): Whether to allow multiple labels per entity. Defaults to False.

        Returns:
            The list of entity predictions.
        """
        return self.batch_predict_entities(
            [text],
            labels,
            flat_ner=flat_ner,
            threshold=threshold,
            multi_label=multi_label,
        )[0]

    @torch.no_grad()
    def batch_predict_entities(
        self, texts, labels, flat_ner=True, threshold=0.5, multi_label=False
    ):
        """
        Predict entities for a batch of texts.

        Args:
            texts (List[str]): A list of input texts to predict entities for.
            labels (List[str]): A list of labels to predict.
            flat_ner (bool, optional): Whether to use flat NER. Defaults to True.
            threshold (float, optional): Confidence threshold for predictions. Defaults to 0.5.
            multi_label (bool, optional): Whether to allow multiple labels per token. Defaults to False.

        Returns:
            The list of lists with predicted entities.
        """

        model_input, raw_batch = self.prepare_model_inputs(texts, labels)

        model_output = self.model(**model_input)[0]

        if not isinstance(model_output, torch.Tensor):
            model_output = torch.from_numpy(model_output)

        outputs = self.decoder.decode(
            raw_batch["tokens"],
            raw_batch["id_to_classes"],
            model_output,
            flat_ner=flat_ner,
            threshold=threshold,
            multi_label=multi_label,
        )

        all_entities = []
        for i, output in enumerate(outputs):
            start_token_idx_to_text_idx = raw_batch["all_start_token_idx_to_text_idx"][
                i
            ]
            end_token_idx_to_text_idx = raw_batch["all_end_token_idx_to_text_idx"][i]
            entities = []
            for start_token_idx, end_token_idx, ent_type, ent_score in output:
                start_text_idx = start_token_idx_to_text_idx[start_token_idx]
                end_text_idx = end_token_idx_to_text_idx[end_token_idx]
                entities.append(
                    {
                        "start": start_token_idx_to_text_idx[start_token_idx],
                        "end": end_token_idx_to_text_idx[end_token_idx],
                        "text": texts[i][start_text_idx:end_text_idx],
                        "label": ent_type,
                        "score": ent_score,
                    }
                )
            all_entities.append(entities)

        return all_entities

    @torch.no_grad()
    def run(
        self, texts, labels, flat_ner=True, threshold=0.5, multi_label=False, batch_size=8
    ):
        """
        Predict entities for a batch of texts.

        Args:
            texts (List[str]): A list of input texts to predict entities for.
            labels (List[str]): A list of labels to predict.
            flat_ner (bool, optional): Whether to use flat NER. Defaults to True.
            threshold (float, optional): Confidence threshold for predictions. Defaults to 0.5.
            multi_label (bool, optional): Whether to allow multiple labels per token. Defaults to False.

        Returns:
            The list of lists with predicted entities.
        """
        self.eval()
        # raw input preparation
        input_x, all_start_token_idx_to_text_idx, all_end_token_idx_to_text_idx = self.prepare_texts(texts)

        # labels = list(dict.fromkeys(labels))

        collator = DataCollator(
            self.config,
            data_processor=self.data_processor,
            return_tokens=True,
            return_entities=True,
            return_id_to_classes=True,
            prepare_labels=False,
            entity_types=labels,
        )
        data_loader = torch.utils.data.DataLoader(
            input_x, batch_size=batch_size, shuffle=False, collate_fn=collator
        )

        outputs = []
        # Iterate over data batches
        for batch in data_loader:
            # Move the batch to the appropriate device
            if not self.onnx_model:
                for key in batch:
                    if isinstance(batch[key], torch.Tensor):
                        batch[key] = batch[key].to(self.device)

            # Perform predictions
            model_output = self.model(**batch)[0]

            if not isinstance(model_output, torch.Tensor):
                model_output = torch.from_numpy(model_output)

            decoded_outputs = self.decoder.decode(
                batch["tokens"],
                batch["id_to_classes"],
                model_output,
                flat_ner=flat_ner,
                threshold=threshold,
                multi_label=multi_label,
            )
            outputs.extend(decoded_outputs)

        all_entities = []
        for i, output in enumerate(outputs):
            start_token_idx_to_text_idx = all_start_token_idx_to_text_idx[i]
            end_token_idx_to_text_idx = all_end_token_idx_to_text_idx[i]
            entities = []
            for start_token_idx, end_token_idx, ent_type, ent_score in output:
                start_text_idx = start_token_idx_to_text_idx[start_token_idx]
                end_text_idx = end_token_idx_to_text_idx[end_token_idx]
                entities.append(
                    {
                        "start": start_token_idx_to_text_idx[start_token_idx],
                        "end": end_token_idx_to_text_idx[end_token_idx],
                        "text": texts[i][start_text_idx:end_text_idx],
                        "label": ent_type,
                        "score": ent_score,
                    }
                )
            all_entities.append(entities)

        return all_entities

    def predict_with_embeds(
        self, text, labels_embeddings, labels, flat_ner=True, threshold=0.5, multi_label=False
    ):
        """
        Predict entities for a single text input.

        Args:
            text: The input text to predict entities for.
            labels: The labels to predict.
            flat_ner (bool, optional): Whether to use flat NER. Defaults to True.
            threshold (float, optional): Confidence threshold for predictions. Defaults to 0.5.
            multi_label (bool, optional): Whether to allow multiple labels per entity. Defaults to False.

        Returns:
            The list of entity predictions.
        """
        return self.batch_predict_with_embeds(
            [text],
            labels_embeddings,
            labels,
            flat_ner=flat_ner,
            threshold=threshold,
            multi_label=multi_label,
        )[0]

    @torch.no_grad()
    def batch_predict_with_embeds(
        self, texts, labels_embeddings, labels, flat_ner=True, threshold=0.5, multi_label=False
    ):
        """
        Predict entities for a batch of texts.

        Args:
            texts (List[str]): A list of input texts to predict entities for.
            labels (List[str]): A list of labels to predict.
            flat_ner (bool, optional): Whether to use flat NER. Defaults to True.
            threshold (float, optional): Confidence threshold for predictions. Defaults to 0.5.
            multi_label (bool, optional): Whether to allow multiple labels per token. Defaults to False.

        Returns:
            The list of lists with predicted entities.
        """

        model_input, raw_batch = self.prepare_model_inputs(texts, labels, prepare_entities = False)

        model_output = self.model(labels_embeddings = labels_embeddings, **model_input)[0]

        if not isinstance(model_output, torch.Tensor):
            model_output = torch.from_numpy(model_output)

        outputs = self.decoder.decode(
            raw_batch["tokens"],
            raw_batch["id_to_classes"],
            model_output,
            flat_ner=flat_ner,
            threshold=threshold,
            multi_label=multi_label,
        )

        all_entities = []
        for i, output in enumerate(outputs):
            start_token_idx_to_text_idx = raw_batch["all_start_token_idx_to_text_idx"][
                i
            ]
            end_token_idx_to_text_idx = raw_batch["all_end_token_idx_to_text_idx"][i]
            entities = []
            for start_token_idx, end_token_idx, ent_type, ent_score in output:
                start_text_idx = start_token_idx_to_text_idx[start_token_idx]
                end_text_idx = end_token_idx_to_text_idx[end_token_idx]
                entities.append(
                    {
                        "start": start_token_idx_to_text_idx[start_token_idx],
                        "end": end_token_idx_to_text_idx[end_token_idx],
                        "text": texts[i][start_text_idx:end_text_idx],
                        "label": ent_type,
                        "score": ent_score,
                    }
                )
            all_entities.append(entities)

        return all_entities

    def evaluate(
        self,
        test_data,
        flat_ner=False,
        multi_label=False,
        threshold=0.5,
        batch_size=12,
        entity_types=None,
    ):
        """
        Evaluate the model on a given test dataset.

        Args:
            test_data (List[Dict]): The test data containing text and entity annotations.
            flat_ner (bool): Whether to use flat NER. Defaults to False.
            multi_label (bool): Whether to use multi-label classification. Defaults to False.
            threshold (float): The threshold for predictions. Defaults to 0.5.
            batch_size (int): The batch size for evaluation. Defaults to 12.
            entity_types (Optional[List[str]]): List of entity types to consider. Defaults to None.

        Returns:
            tuple: A tuple containing the evaluation output and the F1 score.
        """
        self.eval()
        # Create the dataset and data loader
        # dataset = GLiNERDataset(test_data, config = self.config, data_processor=self.data_processor,
        #                                             return_tokens = True, return_id_to_classes = True,
        #                                             prepare_labels= False, return_entities = True,
        #                                             entities=entity_types, get_negatives=False)
        # collator = DataCollatorWithPadding(self.config)
        dataset = test_data
        collator = DataCollator(
            self.config,
            data_processor=self.data_processor,
            return_tokens=True,
            return_entities=True,
            return_id_to_classes=True,
            prepare_labels=False,
            entity_types=entity_types,
        )
        data_loader = torch.utils.data.DataLoader(
            dataset, batch_size=batch_size, shuffle=False, collate_fn=collator

*Content truncated for brevity.*

```

## File: gliner/utils.py

<a name='file-gliner-utils.py'></a>
*Description*: This is a Python script.

```python
import argparse
import yaml

def load_config_as_namespace(config_file):
    with open(config_file, "r") as f:
        config_dict = yaml.safe_load(f)
    return argparse.Namespace(**config_dict)

def is_module_available(module_name):
    """
    Checks whether the specified Python module is available.
    
    Args:
        module_name (str): The name of the module to check.
        
    Returns:
        bool: True if the module is available, False otherwise.
    """
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

class MissedPackageException(Exception):
    """Raised when the requested decoder model is not supported."""
    pass

```

## File: gliner/config.py

<a name='file-gliner-config.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional
from transformers import PretrainedConfig
from transformers.models.auto import CONFIG_MAPPING

class GLiNERConfig(PretrainedConfig):
    model_type = "gliner"
    is_composition = True
    def __init__(self, 
                 model_name: str = "microsoft/deberta-v3-small",
                 labels_encoder: str = None,
                 name: str = "span level gliner",
                 max_width: int = 12,
                 hidden_size: int = 512,
                 dropout: float = 0.4,
                 fine_tune: bool = True,
                 subtoken_pooling: str = "first",
                 span_mode: str = "markerV0",
                 post_fusion_schema: str = '', #l2l-l2t-t2t
                 num_post_fusion_layers: int = 1, 
                 vocab_size: int = -1,
                 max_neg_type_ratio: int = 1,
                 max_types: int = 25,
                 max_len: int = 384,
                 words_splitter_type: str = "whitespace",
                 has_rnn: bool = True,
                 fuse_layers: bool = False,
                 embed_ent_token: bool = True,
                 class_token_index: int = -1,
                 encoder_config: Optional[dict] = None,
                 labels_encoder_config: Optional[dict] = None,
                 ent_token = "<<ENT>>",
                 sep_token = "<<SEP>>",
                 **kwargs):
        super().__init__(**kwargs)
        if isinstance(encoder_config, dict):
            encoder_config["model_type"] = (encoder_config["model_type"] 
                                                if "model_type" in encoder_config 
                                                else "deberta-v2")
            encoder_config = CONFIG_MAPPING[encoder_config["model_type"]](**encoder_config)
        self.encoder_config = encoder_config

        if isinstance(labels_encoder_config, dict):
            labels_encoder_config["model_type"] = (labels_encoder_config["model_type"] 
                                                if "model_type" in labels_encoder_config 
                                                else "deberta-v2")
            labels_encoder_config = CONFIG_MAPPING[labels_encoder_config["model_type"]](**labels_encoder_config)
        self.labels_encoder_config = labels_encoder_config

        self.model_name = model_name
        self.labels_encoder = labels_encoder
        self.name = name
        self.max_width = max_width
        self.hidden_size = hidden_size
        self.dropout = dropout
        self.fine_tune = fine_tune
        self.subtoken_pooling = subtoken_pooling
        self.span_mode = span_mode
        self.post_fusion_schema = post_fusion_schema
        self.num_post_fusion_layers = num_post_fusion_layers
        self.vocab_size = vocab_size
        self.max_neg_type_ratio = max_neg_type_ratio
        self.max_types = max_types
        self.max_len = max_len
        self.words_splitter_type = words_splitter_type
        self.has_rnn = has_rnn
        self.fuse_layers = fuse_layers
        self.class_token_index = class_token_index
        self.embed_ent_token = embed_ent_token
        self.ent_token = ent_token
        self.sep_token = sep_token

# Register the configuration
from transformers import CONFIG_MAPPING
CONFIG_MAPPING.update({"gliner": GLiNERConfig})
```

## File: gliner/evaluation/evaluator.py

<a name='file-gliner-evaluation-evaluator.py'></a>
*Description*: This is a Python script.

```python
import warnings
from collections import defaultdict
from typing import Union, List, Literal

import numpy as np
import torch


class UndefinedMetricWarning(UserWarning):
    pass


def _prf_divide(
    numerator: np.ndarray,
    denominator: np.ndarray,
    metric: Literal["precision", "recall", "f-score"],
    modifier: str,
    average: str,
    warn_for: List[str],
    zero_division: Union[str, int] = "warn",
) -> np.ndarray:
    """Performs division and handles divide-by-zero with warnings."""
    with np.errstate(divide="ignore", invalid="ignore"):
        result = np.true_divide(numerator, denominator)
        result[denominator == 0] = 0.0 if zero_division in ["warn", 0] else 1.0

    if denominator == 0 and zero_division == "warn" and metric in warn_for:
        msg_start = f"{metric.title()}"
        if "f-score" in warn_for:
            msg_start += " and F-score" if metric in warn_for else "F-score"
        msg_start += " are" if "f-score" in warn_for else " is"
        _warn_prf(
            average=average,
            modifier=modifier,
            msg_start=msg_start,
            result_size=len(result),
        )

    return result


def _warn_prf(average: str, modifier: str, msg_start: str, result_size: int):
    axis0, axis1 = ("label", "sample") if average == "samples" else ("sample", "label")
    if result_size == 1:
        msg = f"{msg_start} ill-defined and being set to 0.0 due to no {modifier} {axis0}."  # noqa: E501
    else:
        msg = f"{msg_start} ill-defined and being set to 0.0 in {axis1}s with no {modifier} {axis0}s."  # noqa: E501
    msg += " Use `zero_division` parameter to control this behavior."
    warnings.warn(msg, UndefinedMetricWarning, stacklevel=3)


def extract_tp_actual_correct(y_true, y_pred):
    entities_true = defaultdict(set)
    entities_pred = defaultdict(set)

    for type_name, (start, end), idx in y_true:
        entities_true[type_name].add((start, end, idx))
    for type_name, (start, end), idx in y_pred:
        entities_pred[type_name].add((start, end, idx))

    target_names = sorted(set(entities_true.keys()) | set(entities_pred.keys()))

    tp_sum = np.array([], dtype=np.int32)
    pred_sum = np.array([], dtype=np.int32)
    true_sum = np.array([], dtype=np.int32)
    for type_name in target_names:
        entities_true_type = entities_true.get(type_name, set())
        entities_pred_type = entities_pred.get(type_name, set())
        tp_sum = np.append(tp_sum, len(entities_true_type & entities_pred_type))
        pred_sum = np.append(pred_sum, len(entities_pred_type))
        true_sum = np.append(true_sum, len(entities_true_type))

    return pred_sum, tp_sum, true_sum, target_names


def flatten_for_eval(y_true, y_pred):
    all_true = []
    all_pred = []

    for i, (true, pred) in enumerate(zip(y_true, y_pred)):
        all_true.extend([t + [i] for t in true])
        all_pred.extend([p + [i] for p in pred])

    return all_true, all_pred


def compute_prf(y_true, y_pred, average="micro"):
    y_true, y_pred = flatten_for_eval(y_true, y_pred)

    pred_sum, tp_sum, true_sum, target_names = extract_tp_actual_correct(y_true, y_pred)

    if average == "micro":
        tp_sum = np.array([tp_sum.sum()])
        pred_sum = np.array([pred_sum.sum()])
        true_sum = np.array([true_sum.sum()])

    precision = _prf_divide(
        numerator=tp_sum,
        denominator=pred_sum,
        metric="precision",
        modifier="predicted",
        average=average,
        warn_for=["precision", "recall", "f-score"],
        zero_division="warn",
    )

    recall = _prf_divide(
        numerator=tp_sum,
        denominator=true_sum,
        metric="recall",
        modifier="true",
        average=average,
        warn_for=["precision", "recall", "f-score"],
        zero_division="warn",
    )

    denominator = precision + recall
    denominator[denominator == 0.0] = 1
    f_score = 2 * (precision * recall) / denominator

    return {"precision": precision[0], "recall": recall[0], "f_score": f_score[0]}


class Evaluator:
    def __init__(self, all_true, all_outs):
        self.all_true = all_true
        self.all_outs = all_outs

    def get_entities_fr(self, ents):
        all_ents = []
        for s, e, lab in ents:
            all_ents.append([lab, (s, e)])
        return all_ents

    def get_entities_pr(self, ents):
        all_ents = []
        for s, e, lab, _ in ents:
            all_ents.append([lab, (s, e)])
        return all_ents

    def transform_data(self):
        all_true_ent = []
        all_outs_ent = []
        for i, j in zip(self.all_true, self.all_outs):
            e = self.get_entities_fr(i)
            all_true_ent.append(e)
            e = self.get_entities_pr(j)
            all_outs_ent.append(e)
        return all_true_ent, all_outs_ent

    @torch.no_grad()
    def evaluate(self):
        all_true_typed, all_outs_typed = self.transform_data()
        precision, recall, f1 = compute_prf(all_true_typed, all_outs_typed).values()
        output_str = f"P: {precision:.2%}\tR: {recall:.2%}\tF1: {f1:.2%}\n"
        return output_str, f1


def is_nested(idx1, idx2):
    # Return True if idx2 is nested inside idx1 or vice versa
    return (idx1[0] <= idx2[0] and idx1[1] >= idx2[1]) or (
        idx2[0] <= idx1[0] and idx2[1] >= idx1[1]
    )


def has_overlapping(idx1, idx2, multi_label=False):
    # Check for any overlap between two spans
    if idx1[:2] == idx2[:2]:  # Exact same boundaries can be considered as overlapping
        return not multi_label
    if idx1[0] > idx2[1] or idx2[0] > idx1[1]:
        return False
    return True


def has_overlapping_nested(idx1, idx2, multi_label=False):
    # Return True if idx1 and idx2 overlap, but neither is nested inside the other
    if idx1[:2] == idx2[:2]:  # Exact same boundaries, not considering labels here
        return not multi_label
    if (idx1[0] > idx2[1] or idx2[0] > idx1[1]) or is_nested(idx1, idx2):
        return False
    return True


from functools import partial


def greedy_search(spans, flat_ner=True, multi_label=False):  # start, end, class, score
    if flat_ner:
        has_ov = partial(has_overlapping, multi_label=multi_label)
    else:
        has_ov = partial(has_overlapping_nested, multi_label=multi_label)

    new_list = []
    span_prob = sorted(spans, key=lambda x: -x[-1])

    for i in range(len(spans)):
        b = span_prob[i]
        flag = False
        for new in new_list:
            if has_ov(b[:-1], new):
                flag = True
                break
        if not flag:
            new_list.append(b)

    new_list = sorted(new_list, key=lambda x: x[0])
    return new_list

```

## File: gliner/evaluation/__init__.py

<a name='file-gliner-evaluation-__init__.py'></a>
*Description*: This is a Python script.

```python
from .evaluator import Evaluator
from .evaluate import get_for_all_path, get_for_one_path
```

## File: gliner/evaluation/evaluate.py

<a name='file-gliner-evaluation-evaluate.py'></a>
*Description*: This is a Python script.

```python
import glob
import json
import os
import os
import numpy as np
import argparse
import torch
from tqdm import tqdm
import random

def open_content(path):
    paths = glob.glob(os.path.join(path, "*.json"))
    train, dev, test, labels = None, None, None, None
    for p in paths:
        if "train" in p:
            with open(p, "r") as f:
                train = json.load(f)
        elif "dev" in p:
            with open(p, "r") as f:
                dev = json.load(f)
        elif "test" in p:
            with open(p, "r") as f:
                test = json.load(f)
        elif "labels" in p:
            with open(p, "r") as f:
                labels = json.load(f)
    return train, dev, test, labels


def process(data):
    words = data['sentence'].split()
    entities = []  # List of entities (start, end, type)

    for entity in data['entities']:
        start_char, end_char = entity['pos']

        # Initialize variables to keep track of word positions
        start_word = None
        end_word = None

        # Iterate through words and find the word positions
        char_count = 0
        for i, word in enumerate(words):
            word_length = len(word)
            if char_count == start_char:
                start_word = i
            if char_count + word_length == end_char:
                end_word = i
                break
            char_count += word_length + 1  # Add 1 for the space

        # Append the word positions to the list
        entities.append((start_word, end_word, entity['type'].lower()))

    # Create a list of word positions for each entity
    sample = {
        "tokenized_text": words,
        "ner": entities
    }

    return sample


# create dataset
def create_dataset(path):
    train, dev, test, labels = open_content(path)
    train_dataset = []
    dev_dataset = []
    test_dataset = []
    for data in train:
        train_dataset.append(process(data))
    for data in dev:
        dev_dataset.append(process(data))
    for data in test:
        test_dataset.append(process(data))
    labels = [label.lower() for label in labels]
    return train_dataset, dev_dataset, test_dataset, labels


@torch.no_grad()
def get_for_one_path(path, model):
    # load the dataset
    _, _, test_dataset, entity_types = create_dataset(path)

    data_name = path.split("/")[-1]  # get the name of the dataset

    # check if the dataset is flat_ner
    flat_ner = True
    if any([i in data_name for i in ["ACE", "GENIA", "Corpus"]]):
        flat_ner = False

    # evaluate the model
    results, f1 = model.evaluate(test_dataset, flat_ner=flat_ner, threshold=0.5, batch_size=12,
                                 entity_types=entity_types)
    return data_name, results, f1


def get_for_all_path(model, steps, log_dir, data_paths):
    all_paths = glob.glob(f"{data_paths}/*")

    all_paths = sorted(all_paths)

    # move the model to the device
    device = next(model.parameters()).device
    model.to(device)
    # set the model to eval mode
    model.eval()

    # log the results
    save_path = os.path.join(log_dir, "results.txt")

    with open(save_path, "a") as f:
        f.write("##############################################\n")
        # write step
        f.write("step: " + str(steps) + "\n")

    zero_shot_benc = ["mit-movie", "mit-restaurant", "CrossNER_AI", "CrossNER_literature", "CrossNER_music",
                      "CrossNER_politics", "CrossNER_science"]

    zero_shot_benc_results = {}
    all_results = {}  # without crossNER

    for p in tqdm(all_paths):
        if "sample_" not in p:
            data_name, results, f1 = get_for_one_path(p, model)
            # write to file
            with open(save_path, "a") as f:
                f.write(data_name + "\n")
                f.write(str(results) + "\n")

            if data_name in zero_shot_benc:
                zero_shot_benc_results[data_name] = f1
            else:
                all_results[data_name] = f1

    avg_all = sum(all_results.values()) / len(all_results)
    avg_zs = sum(zero_shot_benc_results.values()) / len(zero_shot_benc_results)

    save_path_table = os.path.join(log_dir, "tables.txt")

    # results for all datasets except crossNER
    table_bench_all = ""
    for k, v in all_results.items():
        table_bench_all += f"{k:20}: {v:.1%}\n"
    # (20 size aswell for average i.e. :20)
    table_bench_all += f"{'Average':20}: {avg_all:.1%}"

    # results for zero-shot benchmark
    table_bench_zeroshot = ""
    for k, v in zero_shot_benc_results.items():
        table_bench_zeroshot += f"{k:20}: {v:.1%}\n"
    table_bench_zeroshot += f"{'Average':20}: {avg_zs:.1%}"

    # write to file
    with open(save_path_table, "a") as f:
        f.write("##############################################\n")
        f.write("step: " + str(steps) + "\n")
        f.write("Table for all datasets except crossNER\n")
        f.write(table_bench_all + "\n\n")
        f.write("Table for zero-shot benchmark\n")
        f.write(table_bench_zeroshot + "\n")
        f.write("##############################################\n\n")


def sample_train_data(data_paths, sample_size=10000):
    all_paths = glob.glob(f"{data_paths}/*")

    all_paths = sorted(all_paths)

    # to exclude the zero-shot benchmark datasets
    zero_shot_benc = ["CrossNER_AI", "CrossNER_literature", "CrossNER_music",
                      "CrossNER_politics", "CrossNER_science", "ACE 2004"]

    new_train = []
    # take 10k samples from each dataset
    for p in tqdm(all_paths):
        if any([i in p for i in zero_shot_benc]):
            continue
        train, dev, test, labels = create_dataset(p)

        # add label key to the train data
        for i in range(len(train)):
            train[i]["label"] = labels

        random.shuffle(train)
        train = train[:sample_size]
        new_train.extend(train)

    return new_train

```

## File: gliner/onnx/__init__.py

<a name='file-gliner-onnx-__init__.py'></a>
*Description*: This is a Python script.

```python

```

## File: gliner/onnx/model.py

<a name='file-gliner-onnx-model.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional, Dict, Any
from abc import ABC, abstractmethod
import warnings
import onnxruntime as ort
import numpy as np
import torch

from ..modeling.base import GLiNERModelOutput

class BaseORTModel(ABC):
    def __init__(self, session: ort.InferenceSession):
        self.session = session
        self.input_names = {input_key.name: idx for idx, input_key in enumerate(self.session.get_inputs())}
        self.output_names = {output_key.name: idx for idx, output_key in enumerate(self.session.get_outputs())}

    def prepare_inputs(self, inputs: Dict[str, torch.Tensor]) -> Dict[str, np.ndarray]:
        """
        Prepare inputs for ONNX model inference.
        
        Args:
            inputs (Dict[str, torch.Tensor]): Dictionary of input names and tensors.
        
        Returns:
            Dict[str, np.ndarray]: Dictionary of input names and numpy arrays.
        """
        if not isinstance(inputs, dict):
            raise ValueError("Inputs must be a dictionary of input names and tensors.")
        
        prepared_inputs = {}
        for key, tensor in inputs.items():
            if key not in self.input_names:
                warnings.warn(f"Input key '{key}' not found in ONNX model's input names. Ignored.")
                continue
            prepared_inputs[key] = tensor.cpu().detach().numpy()
        return prepared_inputs

    def run_inference(self, inputs: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Run the ONNX model inference.
        
        Args:
            inputs (Dict[str, np.ndarray]): Prepared inputs for the model.
        
        Returns:
            Dict[str, np.ndarray]: Model's outputs as numpy arrays.
        """
        onnx_outputs = self.session.run(None, inputs)
        outputs = {name: onnx_outputs[idx] for name, idx in self.output_names.items()}
        return outputs

    @abstractmethod
    def forward(self, input_ids, attention_mask, **kwargs) -> Dict[str, Any]:
        """
        Abstract method to perform forward pass. Must be implemented by subclasses.
        """
        pass
    
    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)
    
class SpanORTModel(BaseORTModel):
    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor, 
                words_mask: torch.Tensor, text_lengths: torch.Tensor, 
                span_idx: torch.Tensor, span_mask: torch.Tensor, **kwargs) -> Dict[str, Any]:
        """
        Forward pass for span model using ONNX inference.

        Args:
            input_ids (torch.Tensor): Input IDs tensor.
            attention_mask (torch.Tensor): Attention mask tensor.
            span_idx (torch.Tensor): Span indices tensor.
            span_mask (torch.Tensor): Span mask tensor.
            **kwargs: Additional arguments.
        
        Returns:
            Dict[str, Any]: Model outputs.
        """
        inputs = {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'words_mask': words_mask,
            'text_lengths': text_lengths,
            'span_idx': span_idx,
            'span_mask': span_mask
        }
        prepared_inputs = self.prepare_inputs(inputs)
        inference_output = self.run_inference(prepared_inputs)
        outputs = GLiNERModelOutput(
            logits=inference_output['logits']
        )
        return outputs

class TokenORTModel(BaseORTModel):
    def forward(self, input_ids: torch.Tensor, attention_mask: torch.Tensor, 
                words_mask: torch.Tensor, text_lengths: torch.Tensor, 
                **kwargs) -> Dict[str, Any]:
        """
        Forward pass for token model using ONNX inference.

        Args:
            input_ids (torch.Tensor): Input IDs tensor.
            attention_mask (torch.Tensor): Attention mask tensor.
            **kwargs: Additional arguments.
        
        Returns:
            Dict[str, Any]: Model outputs.
        """
        inputs = {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'words_mask': words_mask,
            'text_lengths': text_lengths,
        }
        prepared_inputs = self.prepare_inputs(inputs)
        inference_output = self.run_inference(prepared_inputs)
        outputs = GLiNERModelOutput(
            logits=inference_output['logits']
        )
        return outputs
```

## File: gliner/data_processing/__init__.py

<a name='file-gliner-data_processing-__init__.py'></a>
*Description*: This is a Python script.

```python
from .processor import SpanProcessor, SpanBiEncoderProcessor, TokenProcessor, TokenBiEncoderProcessor
from .collator import DataCollator
from .tokenizer import WordsSplitter
from .dataset import GLiNERDataset
```

## File: gliner/data_processing/processor.py

<a name='file-gliner-data_processing-processor.py'></a>
*Description*: This is a Python script.

```python
import random
import warnings
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import List, Tuple, Dict, Union
from concurrent.futures import ProcessPoolExecutor

import torch
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
import torch.nn.functional as F

from .utils import pad_2d_tensor

# Abstract base class for handling data processing
class BaseProcessor(ABC):
    def __init__(self, config, tokenizer, words_splitter, labels_tokenizer = None, preprocess_text=False):
        self.config = config
        self.transformer_tokenizer = tokenizer
        self.labels_tokenizer = labels_tokenizer

        self.words_splitter = words_splitter
        self.ent_token = config.ent_token
        self.sep_token = config.sep_token

        self.preprocess_text = preprocess_text

        # Check if the tokenizer has unk_token and pad_token
        self._check_and_set_special_tokens(self.transformer_tokenizer)
        if self.labels_tokenizer:
            self._check_and_set_special_tokens(self.labels_tokenizer)

    def _check_and_set_special_tokens(self, tokenizer):
        # Check for unk_token
        if tokenizer.unk_token is None:
            default_unk_token = '[UNK]'
            warnings.warn(
                f"The tokenizer is missing an 'unk_token'. Setting default '{default_unk_token}'.",
                UserWarning
            )
            tokenizer.unk_token = default_unk_token

        # Check for pad_token
        if tokenizer.pad_token is None:
            default_pad_token = '[PAD]'
            warnings.warn(
                f"The tokenizer is missing a 'pad_token'. Setting default '{default_pad_token}'.",
                UserWarning
            )
            tokenizer.pad_token = default_pad_token

    @staticmethod
    def get_dict(spans: List[Tuple[int, int, str]], classes_to_id: Dict[str, int]) -> Dict[Tuple[int, int], int]:
        dict_tag = defaultdict(int)
        for span in spans:
            if span[2] in classes_to_id:
                dict_tag[(span[0], span[1])] = classes_to_id[span[2]]
        return dict_tag

    @abstractmethod
    def preprocess_example(self, tokens: List[str], ner: List[Tuple[int, int, str]],
                         classes_to_id: Dict[str, int]) -> Dict:
        raise NotImplementedError("Subclasses should implement this method")

    @abstractmethod
    def create_labels(self) -> torch.Tensor:
        raise NotImplementedError("Subclasses should implement this method")
    
    @abstractmethod
    def tokenize_and_prepare_labels(self):
        pass

    @staticmethod
    def get_negatives(batch_list: List[Dict], sampled_neg: int = 5) -> List[str]:
        ent_types = []
        for b in batch_list:
            types = set([el[-1] for el in b['ner']])
            ent_types.extend(list(types))
        ent_types = list(set(ent_types))
        random.shuffle(ent_types)
        return ent_types[:sampled_neg]

    def prepare_text(self, text):
        new_text = []
        for token in text:
            if not token.strip():
                new_text.append(self.transformer_tokenizer.pad_token)
            else:
                redecoded = self.transformer_tokenizer.decode(
                                    self.transformer_tokenizer.encode(token), 
                                                    skip_special_tokens=True)
                if token!=redecoded:
                    new_text.append(self.transformer_tokenizer.unk_token)
                else:
                    new_text.append(token)
        return new_text
    
    def prepare_texts(self, texts):
        texts = [self.prepare_text(text) for text in texts]
        return texts

    def prepare_inputs(self, texts, entities):
        input_texts = []
        prompt_lengths = []
        for id, text in enumerate(texts):
            input_text = []
            if type(entities)==dict:
                entities_=entities
            else:
                entities_=entities[id]
            for ent in entities_:
                input_text.append(self.ent_token)
                input_text.append(ent)
            input_text.append(self.sep_token)
            prompt_length = len(input_text)
            prompt_lengths.append(prompt_length)
            input_text.extend(text)
            input_texts.append(input_text)
        return input_texts, prompt_lengths
    
    def prepare_word_mask(self, texts, tokenized_inputs, prompt_lengths = None):
        words_masks = []
        for id in range(len(texts)):
            if prompt_lengths is not None:
                prompt_length = prompt_lengths[id]
            else:
                prompt_length = 0
            words_mask = []
            prev_word_id=None
            words_count=0
            for word_id in tokenized_inputs.word_ids(id):
                if word_id is None:
                    words_mask.append(0)
                elif word_id != prev_word_id:
                    if words_count<prompt_length:
                        words_mask.append(0)
                    else:
                        masking_word_id = word_id-prompt_length+1
                        words_mask.append(masking_word_id)
                    words_count+=1
                else:
                    words_mask.append(0)
                prev_word_id = word_id
            words_masks.append(words_mask)
        return words_masks
    
    def tokenize_inputs(self, texts, entities):
        input_texts, prompt_lengths = self.prepare_inputs(texts, entities)

        if self.preprocess_text:
            input_texts = self.prepare_texts(input_texts)
            
        tokenized_inputs = self.transformer_tokenizer(input_texts, is_split_into_words = True, return_tensors='pt',
                                                                                truncation=True, padding="longest")
        words_masks = self.prepare_word_mask(texts, tokenized_inputs, prompt_lengths)
        tokenized_inputs['words_mask'] = torch.tensor(words_masks)
        return tokenized_inputs

    def batch_generate_class_mappings(self, batch_list: List[Dict], negatives: List[str]=None) -> Tuple[
        List[Dict[str, int]], List[Dict[int, str]]]:
        if negatives is None:
            negatives = self.get_negatives(batch_list, 100)
        class_to_ids = []
        id_to_classes = []
        for b in batch_list:
            max_neg_type_ratio = int(self.config.max_neg_type_ratio)
            neg_type_ratio = random.randint(0, max_neg_type_ratio) if max_neg_type_ratio else 0
            
            if "negatives" in b: # manually setting negative types
                negs_i = b["negatives"]
            else: # in-batch negative types
                negs_i = negatives[:len(b["ner"]) * neg_type_ratio] if neg_type_ratio else []

            types = list(set([el[-1] for el in b["ner"]] + negs_i))
            random.shuffle(types)
            types = types[:int(self.config.max_types)]

            if "label" in b: # labels are predefined
                types = b["label"]

            class_to_id = {k: v for v, k in enumerate(types, start=1)}
            id_to_class = {k: v for v, k in class_to_id.items()}
            class_to_ids.append(class_to_id)
            id_to_classes.append(id_to_class)

        return class_to_ids, id_to_classes

    def collate_raw_batch(self, batch_list: List[Dict], entity_types: List[Union[str, List[str]]] = None, 
                        negatives: List[str] = None, class_to_ids: Dict = None, id_to_classes: Dict = None) -> Dict:
        if entity_types is None and class_to_ids is None:
            # Generate mappings dynamically based on batch content
            class_to_ids, id_to_classes = self.batch_generate_class_mappings(batch_list, negatives)
            batch = [
                self.preprocess_example(b["tokenized_text"], b["ner"], class_to_ids[i]) 
                for i, b in enumerate(batch_list)
            ]
        else:
            if class_to_ids is None:
                # Handle cases for entity_types being a list of strings or list of lists
                if isinstance(entity_types[0], list):  # List of lists of strings
                    class_to_ids = []
                    id_to_classes = []
                    for i, types in enumerate(entity_types):
                        types = list(dict.fromkeys(types))
                        mapping = {k: v for v, k in enumerate(types, start=1)}
                        class_to_ids.append(mapping)
                        id_to_classes.append({v: k for k, v in mapping.items()})
                    batch = [
                        self.preprocess_example(b["tokenized_text"], b["ner"], class_to_ids[i]) 
                        for i, b in enumerate(batch_list)
                    ]
                else:  # Single list of strings
                    class_to_ids = {k: v for v, k in enumerate(entity_types, start=1)}
                    id_to_classes = {v: k for k, v in class_to_ids.items()}
                    batch = [
                        self.preprocess_example(b["tokenized_text"], b["ner"], class_to_ids) 
                        for b in batch_list
                    ]
            else:
                # Use provided mappings
                batch = [
                    self.preprocess_example(b["tokenized_text"], b["ner"], class_to_ids) 
                    for b in batch_list
                ]
        
        return self.create_batch_dict(batch, class_to_ids, id_to_classes)


    def collate_fn(self, batch, prepare_labels=True, *args, **kwargs):
        model_input_batch = self.tokenize_and_prepare_labels(batch, prepare_labels, *args, **kwargs)
        return model_input_batch
    
    @abstractmethod
    def create_batch_dict(self, batch: List[Dict], class_to_ids: List[Dict[str, int]],
                          id_to_classes: List[Dict[int, str]]) -> Dict:
        raise NotImplementedError("Subclasses should implement this method")

    def create_dataloader(self, data, entity_types=None, *args, **kwargs) -> DataLoader:
        return DataLoader(data, collate_fn=lambda x: self.collate_fn(x, entity_types), *args, **kwargs)


class BaseBiEncoderProcessor(BaseProcessor):
    def tokenize_inputs(self, texts, entities=None):
        if self.preprocess_text:
            texts = self.prepare_texts(texts)
            
        tokenized_inputs = self.transformer_tokenizer(texts, is_split_into_words = True, return_tensors='pt',
                                                                                truncation=True, padding="longest")

        if entities is not None:
            tokenized_labels = self.labels_tokenizer(entities, return_tensors='pt', truncation=True, padding="longest")

            tokenized_inputs['labels_input_ids'] = tokenized_labels['input_ids']
            tokenized_inputs['labels_attention_mask'] = tokenized_labels['attention_mask']

        words_masks = self.prepare_word_mask(texts, tokenized_inputs, prompt_lengths=None)
        tokenized_inputs['words_mask'] = torch.tensor(words_masks)
        return tokenized_inputs

    def batch_generate_class_mappings(self, batch_list: List[Dict], negatives: List[str]=None) -> Tuple[
        List[Dict[str, int]], List[Dict[int, str]]]:

        classes = []
        for b in batch_list:
            max_neg_type_ratio = int(self.config.max_neg_type_ratio)
            neg_type_ratio = random.randint(0, max_neg_type_ratio) if max_neg_type_ratio else 0
            
            if "negatives" in b: # manually setting negative types
                negs_i = b["negatives"]
            else: # in-batch negative types
                negs_i = []

            types = list(set([el[-1] for el in b["ner"]] + negs_i))
            

            if "label" in b: # labels are predefined
                types = b["label"]

            classes.extend(types)
        random.shuffle(classes)
        classes = list(set(classes))[:int(self.config.max_types*len(batch_list))]
        class_to_id = {k: v for v, k in enumerate(classes, start=1)}
        id_to_class = {k: v for v, k in class_to_id.items()}

        class_to_ids = [class_to_id for i in range(len(batch_list))]
        id_to_classes = [id_to_class for i in range(len(batch_list))]

        return class_to_ids, id_to_classes
    
class SpanProcessor(BaseProcessor):    
    def preprocess_example(self, tokens, ner, classes_to_id):
        if len(tokens) == 0:
            tokens = ["[PAD]"]
        max_len = self.config.max_len
        if len(tokens) > max_len:
            warnings.warn(f"Sentence of length {len(tokens)} has been truncated to {max_len}")
            tokens = tokens[:max_len]

        spans_idx = [(i, i + j) for i in range(len(tokens)) for j in range(self.config.max_width)]
        dict_lab = self.get_dict(ner, classes_to_id) if ner else defaultdict(int)
        span_label = torch.LongTensor([dict_lab[i] for i in spans_idx])
        spans_idx = torch.LongTensor(spans_idx)
        valid_span_mask = spans_idx[:, 1] > len(tokens) - 1
        span_label = span_label.masked_fill(valid_span_mask, -1)

        return {
            "tokens": tokens,
            "span_idx": spans_idx,
            "span_label": span_label,
            "seq_length": len(tokens),
            "entities": ner,
        }

    def create_batch_dict(self, batch, class_to_ids, id_to_classes):
        tokens = [el["tokens"] for el in batch]
        entities = [el["entities"] for el in batch]
        span_idx = pad_sequence([b["span_idx"] for b in batch], batch_first=True, padding_value=0)
        span_label = pad_sequence([el["span_label"] for el in batch], batch_first=True, padding_value=-1)
        seq_length = torch.LongTensor([el["seq_length"] for el in batch]).unsqueeze(-1)
        span_mask = span_label != -1

        return {
            "seq_length": seq_length,
            "span_idx": span_idx,
            "tokens": tokens,
            "span_mask": span_mask,
            "span_label": span_label,
            "entities": entities,
            "classes_to_id": class_to_ids,
            "id_to_classes": id_to_classes,
        }


    def create_labels(self, batch):
        labels_batch = []
        for id in range(len(batch['tokens'])):
            tokens = batch['tokens'][id]
            classes_to_id = batch['classes_to_id'][id]
            ner = batch['entities'][id]
            num_classes = len(classes_to_id)
            spans_idx = [(i, i + j) for i in range(len(tokens)) for j in range(self.config.max_width)]
            dict_lab = self.get_dict(ner, classes_to_id) if ner else defaultdict(int)
            span_label = torch.LongTensor([dict_lab[i] for i in spans_idx])
            spans_idx = torch.LongTensor(spans_idx)
            valid_span_mask = spans_idx[:, 1] > len(tokens) - 1
            span_label = span_label.masked_fill(valid_span_mask, 0)
            labels_one_hot = F.one_hot(span_label, num_classes + 1).float()
            labels_one_hot = labels_one_hot[:, 1:]
            labels_batch.append(labels_one_hot)
        
        # Convert the list of tensors to a single tensor
        if len(labels_batch) > 1:
            labels_batch = pad_2d_tensor(labels_batch)
        else:
            labels_batch = labels_batch[0]

        return labels_batch
    
    def tokenize_and_prepare_labels(self, batch, prepare_labels, *args, **kwargs):
        tokenized_input = self.tokenize_inputs(batch['tokens'], batch['classes_to_id'])
        if prepare_labels:
            labels = self.create_labels(batch)
            tokenized_input['labels'] = labels
        return tokenized_input

class SpanBiEncoderProcessor(SpanProcessor, BaseBiEncoderProcessor):   
    def tokenize_and_prepare_labels(self, batch, prepare_labels, prepare_entities=True, *args, **kwargs):
        if prepare_entities:
            if type(batch['classes_to_id']) == dict:
                entities = list(batch['classes_to_id'])
            else:
                entities = list(batch['classes_to_id'][0])
        else:
            entities = None
        tokenized_input = self.tokenize_inputs(batch['tokens'], entities)
        if prepare_labels:
            labels = self.create_labels(batch)
            tokenized_input['labels'] = labels
        return tokenized_input


class TokenProcessor(BaseProcessor):
    def preprocess_example(self, tokens, ner, classes_to_id):
        # Ensure there is always a token list, even if it's empty
        if len(tokens) == 0:
            tokens = ["[PAD]"]

        # Limit the length of tokens based on configuration maximum length
        max_len = self.config.max_len
        if len(tokens) > max_len:
            warnings.warn(f"Sentence of length {len(tokens)} has been truncated to {max_len}")
            tokens = tokens[:max_len]

        # Generate entity IDs based on the NER spans provided and their classes
        try: # 'NoneType' object is not iterable
            entities_id = [[i, j, classes_to_id[k]] for i, j, k in ner if k in classes_to_id]
        except TypeError:
            entities_id = []


        example = {
            'tokens': tokens,
            'seq_length': len(tokens),
            'entities': ner,
            'entities_id': entities_id
        }
        return example

    def create_batch_dict(self, batch, class_to_ids, id_to_classes):
        # Extract relevant data from batch for batch processing
        tokens = [el["tokens"] for el in batch]
        seq_length = torch.LongTensor([el["seq_length"] for el in batch]).unsqueeze(-1)
        entities = [el["entities"] for el in batch]
        entities_id = [el["entities_id"] for el in batch]

        # Assemble and return the batch dictionary
        batch_dict = {
            "tokens": tokens,
            "seq_length": seq_length,
            "entities": entities,
            "entities_id": entities_id,
            "classes_to_id": class_to_ids,
            "id_to_classes": id_to_classes,
        }

        return batch_dict

    def create_labels(self, entities_id, batch_size, seq_len, num_classes):
        word_labels = torch.zeros(
            3, batch_size, seq_len, num_classes, dtype=torch.float
        )
        # get batch_nums and span_pos
        for i, element in enumerate(entities_id):
            for ent in element:
                st, ed, sp_label = ent
                sp_label = sp_label - 1

                # prevent indexing errors
                if st >= seq_len or ed >= seq_len:
                    continue

                word_labels[0, i, st, sp_label] = 1  # start
                word_labels[1, i, ed, sp_label] = 1  # end
                word_labels[2, i, st:ed + 1, sp_label] = 1  # inside
        return word_labels

    def tokenize_and_prepare_labels(self, batch, prepare_labels, *args, **kwargs):
        batch_size = len(batch['tokens'])
        seq_len = batch['seq_length'].max()
        num_classes = max([len(cid) for cid in batch['classes_to_id']])

        tokenized_input = self.tokenize_inputs(batch['tokens'], batch['classes_to_id'])
        
        if prepare_labels:
            labels = self.create_labels(batch['entities_id'], batch_size, seq_len, num_classes)
            tokenized_input['labels'] = labels
        return tokenized_input

class TokenBiEncoderProcessor(TokenProcessor, BaseBiEncoderProcessor):   
    def tokenize_and_prepare_labels(self, batch, prepare_labels, prepare_entities=True, **kwargs):
        if prepare_entities:
            if type(batch['classes_to_id']) == dict:
                entities = list(batch['classes_to_id'])
            else:
                entities = list(batch['classes_to_id'][0])
        else:
            entities = None
        batch_size = len(batch['tokens'])
        seq_len = batch['seq_length'].max()
        num_classes = len(entities)

        tokenized_input = self.tokenize_inputs(batch['tokens'], entities)
        
        if prepare_labels:
            labels = self.create_labels(batch['entities_id'], batch_size, seq_len, num_classes)
            tokenized_input['labels'] = labels

        return tokenized_input
```

## File: gliner/data_processing/tokenizer.py

<a name='file-gliner-data_processing-tokenizer.py'></a>
*Description*: This is a Python script.

```python
import re


class TokenSplitterBase():
    def __init__(self):
        pass

    def __call__(self, text) -> (str, int, int):
        pass


class WhitespaceTokenSplitter(TokenSplitterBase):
    def __init__(self):
        self.whitespace_pattern = re.compile(r'\w+(?:[-_]\w+)*|\S')
    
    def __call__(self, text):
        for match in self.whitespace_pattern.finditer(text):
            yield match.group(), match.start(), match.end()


class SpaCyTokenSplitter(TokenSplitterBase):
    def __init__(self, lang=None):
        try:
            import spacy # noqa
        except ModuleNotFoundError as error:
            raise error.__class__(
                "Please install spacy with: `pip install spacy`"
            )
        if lang is None:
            lang = 'en'  # Default to English if no language is specified
        self.nlp = spacy.blank(lang)

    def __call__(self, text):
        doc = self.nlp(text)
        for token in doc:
            yield token.text, token.idx, token.idx + len(token.text)            


class MecabKoTokenSplitter(TokenSplitterBase):
    def __init__(self):
        try:
            import mecab  # noqa
        except ModuleNotFoundError as error:
            raise error.__class__(
                "Please install python-mecab-ko with: `pip install python-mecab-ko`"
            )
        self.tagger = mecab.MeCab()
    
    def __call__(self, text):
        tokens = self.tagger.morphs(text)

        last_idx = 0
        for morph in tokens:
            start_idx = text.find(morph, last_idx)
            end_idx = start_idx + len(morph)
            last_idx = end_idx
            yield morph, start_idx, end_idx

class JiebaTokenSplitter(TokenSplitterBase):
    def __init__(self):
        try:
            import jieba  # noqa
        except ModuleNotFoundError as error:
            raise error.__class__(
                "Please install jieba with: `pip install jieba`"
            )
        self.tagger = jieba
    
    def __call__(self, text):
        tokens = self.tagger.cut(text)
        last_idx = 0
        for token in tokens:
            start_idx = text.find(token, last_idx)
            end_idx = start_idx + len(token)
            last_idx = end_idx
            yield token, start_idx, end_idx

class HanLPTokenSplitter(TokenSplitterBase):
    def __init__(self, model_name="FINE_ELECTRA_SMALL_ZH"):
        try:
            import hanlp  # noqa
            import hanlp.pretrained
        except ModuleNotFoundError as error:
            raise error.__class__(
                "Please install hanlp with: `pip install hanlp`"
            )

        models = hanlp.pretrained.tok.ALL
        if model_name not in models:
            raise ValueError(f"HanLP: {model_name} is not available, choose between {models.keys()}")
        url = models[model_name]
        self.tagger = hanlp.load(url)
    
    def __call__(self, text):
        tokens = self.tagger(text)
        last_idx = 0
        for token in tokens:
            start_idx = text.find(token, last_idx)
            end_idx = start_idx + len(token)
            last_idx = end_idx
            yield token, start_idx, end_idx

class WordsSplitter(TokenSplitterBase):
    def __init__(self, splitter_type='whitespace'):
        if splitter_type=='whitespace':
            self.splitter = WhitespaceTokenSplitter()
        elif splitter_type == 'spacy':
            self.splitter = SpaCyTokenSplitter()
        elif splitter_type == 'mecab':
            self.splitter = MecabKoTokenSplitter()
        elif splitter_type == 'jieba':
            self.splitter = JiebaTokenSplitter()
        elif splitter_type == 'hanlp':
            self.splitter = HanLPTokenSplitter()    
        else:
            raise ValueError(f"{splitter_type} is not implemented, choose between 'whitespace', 'spacy', 'jieba', 'hanlp' and 'mecab'")
    
    def __call__(self, text):
        for token in self.splitter(text):
            yield token
```

## File: gliner/data_processing/dataset.py

<a name='file-gliner-data_processing-dataset.py'></a>
*Description*: This is a Python script.

```python
import random
from tqdm import tqdm 
from typing import Optional, List
from torch.utils.data import Dataset
from transformers import AutoTokenizer

from . import TokenProcessor, SpanProcessor, WordsSplitter
from ..config import GLiNERConfig

class GLiNERDataset(Dataset):
    def __init__(self, examples, 
                        config: Optional[GLiNERConfig], 
                        tokenizer: Optional[AutoTokenizer] = None, 
                        words_splitter: Optional[WordsSplitter] = None,
                        data_processor = None,
                        entities = None,
                        get_negatives:bool=True):
        self._data = examples
        self.config=config
        if data_processor is not None:
            self.data_processor = data_processor
        else:
            if config.span_mode == "token_level":
                self.data_processor = TokenProcessor(config, tokenizer, words_splitter, preprocess_text=True)
            else:
                self.data_processor = SpanProcessor(config, tokenizer, words_splitter, preprocess_text=True)
        
        self.max_neg_type_ratio = int(self.config.max_neg_type_ratio)
        self.get_negatives = get_negatives
        if not entities:
            self.all_entities = self._collect_all_entities()
        else:
            self.all_entities = entities
        self.max_negatives = min(50, len(self.all_entities))

    def _get_entities_from_example(self, example):
        entities = {ner[-1] for ner in example['ner']}
        return entities
    
    def _collect_all_entities(self):
        print("Collecting all entities...")
        all_entities = set()
        for example in tqdm(self._data):
            curr_entities = self._get_entities_from_example(example)
            all_entities.update(curr_entities)
        print('Total number of entity classes: ', len(all_entities))
        return list(all_entities)

    def _get_negatives(self):
        negatives = random.sample(self.all_entities, k=self.max_negatives)
        random.shuffle(negatives)
        return negatives
    
    def __len__(self):
        return len(self._data)

    def __getitem__(self, idx):
        try:
            example = self._data[idx]
            if self.get_negatives:
                curr_negatives = self._get_negatives()
            else:
                curr_negatives = None

            raw_batch = self.data_processor.collate_raw_batch([example], negatives = curr_negatives)
            
            model_input = self.data_processor.collate_fn(raw_batch, prepare_labels=True)
            if 'span_idx' in raw_batch:
                model_input['span_idx'] = raw_batch['span_idx']
            if 'span_mask' in raw_batch:
                model_input['span_mask'] = raw_batch['span_mask']
            if 'seq_length' in raw_batch:
                model_input['text_lengths'] = raw_batch['seq_length']
            return model_input
        except Exception as e:
            print(f"Skipping getting item due to error: {e}")
            return None
```

## File: gliner/data_processing/utils.py

<a name='file-gliner-data_processing-utils.py'></a>
*Description*: This is a Python script.

```python
import torch

def pad_2d_tensor(key_data):
    """
    Pad a list of 2D tensors to have the same size along both dimensions.
    
    :param key_data: List of 2D tensors to pad.
    :return: Tensor of padded tensors stacked along a new batch dimension.
    """
    if not key_data:
        raise ValueError("The input list 'key_data' should not be empty.")

    # Determine the maximum size along both dimensions
    max_rows = max(tensor.shape[0] for tensor in key_data)
    max_cols = max(tensor.shape[1] for tensor in key_data)
    
    tensors = []

    for tensor in key_data:
        rows, cols = tensor.shape
        row_padding = max_rows - rows
        col_padding = max_cols - cols

        # Pad the tensor along both dimensions
        padded_tensor = torch.nn.functional.pad(tensor, (0, col_padding, 0, row_padding),
                                                                 mode='constant', value=0)
        tensors.append(padded_tensor)

    # Stack the tensors into a single tensor along a new batch dimension
    padded_tensors = torch.stack(tensors)

    return padded_tensors
```

## File: gliner/data_processing/collator.py

<a name='file-gliner-data_processing-collator.py'></a>
*Description*: This is a Python script.

```python
import torch
from torch.nn.utils.rnn import pad_sequence
import torch.nn.functional as F
from .processor import SpanProcessor, TokenProcessor
from .utils import pad_2d_tensor

class DataCollator:
    def __init__(self, config, tokenizer=None, words_splitter=None, data_processor=None, 
                        return_tokens: bool = False,
                        return_id_to_classes: bool = False,
                        return_entities: bool = False,
                        prepare_labels: bool = False,
                        entity_types = None):
        self.config=config
        if data_processor is None:
            if config.span_mode == "token_level":
                self.data_processor = TokenProcessor(config, tokenizer, words_splitter)
            else:
                self.data_processor = SpanProcessor(config, tokenizer, words_splitter)
        else:
            self.data_processor = data_processor
        self.prepare_labels = prepare_labels
        self.return_tokens = return_tokens
        self.return_id_to_classes = return_id_to_classes
        self.return_entities = return_entities
        self.entity_types = entity_types

    def __call__(self, input_x):
        raw_batch = self.data_processor.collate_raw_batch(input_x, entity_types = self.entity_types)
        
        model_input = self.data_processor.collate_fn(raw_batch, prepare_labels=self.prepare_labels)
        model_input.update({"span_idx": raw_batch['span_idx'] if 'span_idx' in raw_batch else None, 
                            "span_mask": raw_batch["span_mask"] if 'span_mask' in raw_batch else None,
                            "text_lengths": raw_batch['seq_length']})
        if self.return_tokens:
            model_input['tokens'] = raw_batch['tokens']
        if self.return_id_to_classes:
            model_input['id_to_classes'] = raw_batch['id_to_classes']
        if self.return_entities:
            model_input['entities'] = raw_batch['entities']
        model_input = {k:v for k, v in model_input.items() if v is not None}
        return model_input

class DataCollatorWithPadding:
    def __init__(self, config=None):
        """
        Initialize the DataCollator with configs.
                """
        self.config = config

    def __call__(self, batch):
        if not batch:
            raise ValueError("Batch cannot be empty")
        batch = [item for item in batch if item is not None]
        # Extract all keys from the first item
        keys = batch[0].keys()

        # Create a dictionary to hold padded data
        padded_batch = {key: [] for key in keys}

        for key in keys:
            if key in {'tokens', 'id_to_classes', 'entities'}:
                padded_batch[key] = [item[key] for item in batch]
                continue
            # Collect data for the current key
            key_data = [item[key].squeeze(0) for item in batch]

            if isinstance(key_data[0], torch.Tensor):
                if key_data[0].dim() == 1:
                    # For 1D tensors, use pad_sequence
                    if key == 'span_label':
                        span_label = pad_sequence(key_data, batch_first=True, padding_value=-1)
                        span_mask = span_label != -1
                        padded_batch[key] = span_mask
                    else:
                        padded_batch[key] = pad_sequence(key_data, batch_first=True)
                elif key_data[0].dim() == 2: # span_idx case
                    padded_batch[key] = self._pad_2d_tensor(key_data)
                elif key == 'labels' and self.config.span_mode == 'token_level':
                    padded_batch[key] = self.pad_token_labels(key_data)
                else:
                    raise TypeError(f"Unsuported amount of dimension for key '{key}'")
            elif isinstance(key_data[0], list):
                # Pad list-like data
                max_length = max(len(seq) for seq in key_data)
                padded_batch[key] = torch.tensor(
                    [seq + [0] * (max_length - len(seq)) for seq in key_data],
                    dtype=torch.float32
                ).to(self.device)
            elif isinstance(key_data[0], (int, float)):
                # Directly convert numeric data to tensors
                padded_batch[key] = torch.tensor(key_data, dtype=torch.float32).to(self.device)
            else:
                raise TypeError(f"Unsupported data type for key '{key}': {type(key_data[0])}")
        padded_batch = {k:v for k,v in padded_batch.items() if v is not None}
        return padded_batch
    
    def _pad_2d_tensor(self, key_data):
        padded_tensors = pad_2d_tensor(key_data)
        return padded_tensors

    def pad_token_labels(self, key_data):
        if not key_data:
            raise ValueError("The input list 'key_data' should not be empty.")

        # Determine the maximum sequence length and number of classes
        max_seq_len = max(tensor.shape[2] for tensor in key_data)
        max_num_classes = max(tensor.shape[3] for tensor in key_data)
        
        padded_tensors = []

        for tensor in key_data:
            current_seq_len = tensor.shape[2]
            current_num_classes = tensor.shape[3]

            seq_padding = max_seq_len - current_seq_len
            class_padding = max_num_classes - current_num_classes

            # Pad tensor to the maximum sequence length and number of classes
            padded_tensor = F.pad(tensor, (0, class_padding, 0, seq_padding), mode='constant', value=0)
            padded_tensors.append(padded_tensor)
        
        # Concatenate the tensors along the batch dimension
        concatenated_labels = torch.cat(padded_tensors, dim=1)
        
        return concatenated_labels
```

## File: gliner/modeling/__init__.py

<a name='file-gliner-modeling-__init__.py'></a>
*Description*: This is a Python script.

```python

```

## File: gliner/modeling/loss_functions.py

<a name='file-gliner-modeling-loss_functions.py'></a>
*Description*: This is a Python script.

```python
import torch
import torch.nn.functional as F


def focal_loss_with_logits(
        inputs: torch.Tensor,
        targets: torch.Tensor,
        alpha: float = 0.25,
        gamma: float = 2,
        reduction: str = "none",
        label_smoothing: float = 0.0,
        ignore_index: int = -100  # default value for ignored index
) -> torch.Tensor:
    """
    Loss used in RetinaNet for dense detection: https://arxiv.org/abs/1708.02002.

    Args:
        inputs (Tensor): A float tensor of arbitrary shape.
                The predictions for each example.
        targets (Tensor): A float tensor with the same shape as inputs. Stores the binary
                classification label for each element in inputs
                (0 for the negative class and 1 for the positive class).
        alpha (float): Weighting factor in range (0,1) to balance
                positive vs negative examples or -1 for ignore. Default: ``0.25``.
        gamma (float): Exponent of the modulating factor (1 - p_t) to
                balance easy vs hard examples. Default: ``2``.
        reduction (string): ``'none'`` | ``'mean'`` | ``'sum'``
                ``'none'``: No reduction will be applied to the output.
                ``'mean'``: The output will be averaged.
                ``'sum'``: The output will be summed. Default: ``'none'``.
        label_smoothing (float): Specifies the amount of smoothing when computing the loss, 
                                                                where 0.0 means no smoothing.
        ignore_index (int): Specifies a target value that is ignored and does not contribute
                            to the input gradient. Default: ``-100``.
    Returns:
        Loss tensor with the reduction option applied.
    """
    # Create a mask to ignore specified index
    valid_mask = targets != ignore_index
    
    # Apply label smoothing if needed
    if label_smoothing != 0:
        with torch.no_grad():
            targets = targets * (1 - label_smoothing) + 0.5 * label_smoothing

    # Apply sigmoid activation to inputs
    p = torch.sigmoid(inputs)

    # Compute the binary cross-entropy loss without reduction
    loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction="none")

    # Apply the valid mask to the loss
    loss = loss * valid_mask

    # Apply focal loss modulation if gamma is greater than 0
    if gamma > 0:
        p_t = p * targets + (1 - p) * (1 - targets)
        loss = loss * ((1 - p_t) ** gamma)

    # Apply alpha weighting if alpha is specified
    if alpha >= 0:
        alpha_t = alpha * targets + (1 - alpha) * (1 - targets)
        loss = alpha_t * loss

    # Apply reduction method
    if reduction == "none":
        return loss
    elif reduction == "mean":
        return loss.sum() / valid_mask.sum()  # Normalize by the number of valid (non-ignored) elements
    elif reduction == "sum":
        return loss.sum()
    else:
        raise ValueError(
            f"Invalid value for argument 'reduction': '{reduction}'. "
            f"Supported reduction modes: 'none', 'mean', 'sum'"
        )
```

## File: gliner/modeling/span_rep.py

<a name='file-gliner-modeling-span_rep.py'></a>
*Description*: This is a Python script.

```python
import torch
import torch.nn.functional as F
from torch import nn

from .layers import create_projection_layer

class SpanQuery(nn.Module):

    def __init__(self, hidden_size, max_width, trainable=True):
        super().__init__()

        self.query_seg = nn.Parameter(torch.randn(hidden_size, max_width))

        nn.init.uniform_(self.query_seg, a=-1, b=1)

        if not trainable:
            self.query_seg.requires_grad = False

        self.project = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU()
        )

    def forward(self, h, *args):
        # h of shape [B, L, D]
        # query_seg of shape [D, max_width]

        span_rep = torch.einsum('bld, ds->blsd', h, self.query_seg)

        return self.project(span_rep)


class SpanMLP(nn.Module):

    def __init__(self, hidden_size, max_width):
        super().__init__()

        self.mlp = nn.Linear(hidden_size, hidden_size * max_width)

    def forward(self, h, *args):
        # h of shape [B, L, D]
        # query_seg of shape [D, max_width]

        B, L, D = h.size()

        span_rep = self.mlp(h)

        span_rep = span_rep.view(B, L, -1, D)

        return span_rep.relu()


class SpanCAT(nn.Module):

    def __init__(self, hidden_size, max_width):
        super().__init__()

        self.max_width = max_width

        self.query_seg = nn.Parameter(torch.randn(128, max_width))

        self.project = nn.Sequential(
            nn.Linear(hidden_size + 128, hidden_size),
            nn.ReLU()
        )

    def forward(self, h, *args):
        # h of shape [B, L, D]
        # query_seg of shape [D, max_width]

        B, L, D = h.size()

        h = h.view(B, L, 1, D).repeat(1, 1, self.max_width, 1)

        q = self.query_seg.view(1, 1, self.max_width, -1).repeat(B, L, 1, 1)

        span_rep = torch.cat([h, q], dim=-1)

        span_rep = self.project(span_rep)

        return span_rep


class SpanConvBlock(nn.Module):
    def __init__(self, hidden_size, kernel_size, span_mode='conv_normal'):
        super().__init__()

        if span_mode == 'conv_conv':
            self.conv = nn.Conv1d(hidden_size, hidden_size,
                                  kernel_size=kernel_size)

            # initialize the weights
            nn.init.kaiming_uniform_(self.conv.weight, nonlinearity='relu')

        elif span_mode == 'conv_max':
            self.conv = nn.MaxPool1d(kernel_size=kernel_size, stride=1)
        elif span_mode == 'conv_mean' or span_mode == 'conv_sum':
            self.conv = nn.AvgPool1d(kernel_size=kernel_size, stride=1)

        self.span_mode = span_mode

        self.pad = kernel_size - 1

    def forward(self, x):

        x = torch.einsum('bld->bdl', x)

        if self.pad > 0:
            x = F.pad(x, (0, self.pad), "constant", 0)

        x = self.conv(x)

        if self.span_mode == "conv_sum":
            x = x * (self.pad + 1)

        return torch.einsum('bdl->bld', x)


class SpanConv(nn.Module):
    def __init__(self, hidden_size, max_width, span_mode):
        super().__init__()

        kernels = [i + 2 for i in range(max_width - 1)]

        self.convs = nn.ModuleList()

        for kernel in kernels:
            self.convs.append(SpanConvBlock(hidden_size, kernel, span_mode))

        self.project = nn.Sequential(
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size)
        )

    def forward(self, x, *args):

        span_reps = [x]

        for conv in self.convs:
            h = conv(x)
            span_reps.append(h)

        span_reps = torch.stack(span_reps, dim=-2)

        return self.project(span_reps)


class SpanEndpointsBlock(nn.Module):
    def __init__(self, kernel_size):
        super().__init__()

        self.kernel_size = kernel_size

    def forward(self, x):
        B, L, D = x.size()

        span_idx = torch.LongTensor(
            [[i, i + self.kernel_size - 1] for i in range(L)]).to(x.device)

        x = F.pad(x, (0, 0, 0, self.kernel_size - 1), "constant", 0)

        # endrep
        start_end_rep = torch.index_select(x, dim=1, index=span_idx.view(-1))

        start_end_rep = start_end_rep.view(B, L, 2, D)

        return start_end_rep


class ConvShare(nn.Module):
    def __init__(self, hidden_size, max_width):
        super().__init__()

        self.max_width = max_width

        self.conv_weigth = nn.Parameter(
            torch.randn(hidden_size, hidden_size, max_width))

        nn.init.kaiming_uniform_(self.conv_weigth, nonlinearity='relu')

        self.project = nn.Sequential(
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size)
        )

    def forward(self, x, *args):
        span_reps = []

        x = torch.einsum('bld->bdl', x)

        for i in range(self.max_width):
            pad = i
            x_i = F.pad(x, (0, pad), "constant", 0)
            conv_w = self.conv_weigth[:, :, :i + 1]
            out_i = F.conv1d(x_i, conv_w)
            span_reps.append(out_i.transpose(-1, -2))

        out = torch.stack(span_reps, dim=-2)

        return self.project(out)


def extract_elements(sequence, indices):
    B, L, D = sequence.shape
    K = indices.shape[1]

    # Expand indices to [B, K, D]
    expanded_indices = indices.unsqueeze(2).expand(-1, -1, D)

    # Gather the elements
    extracted_elements = torch.gather(sequence, 1, expanded_indices)

    return extracted_elements


class SpanMarker(nn.Module):

    def __init__(self, hidden_size, max_width, dropout=0.4):
        super().__init__()

        self.max_width = max_width

        self.project_start = nn.Sequential(
            nn.Linear(hidden_size, hidden_size * 2, bias=True),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size * 2, hidden_size, bias=True),
        )

        self.project_end = nn.Sequential(
            nn.Linear(hidden_size, hidden_size * 2, bias=True),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size * 2, hidden_size, bias=True),
        )

        self.out_project = nn.Linear(hidden_size * 2, hidden_size, bias=True)

    def forward(self, h, span_idx):
        # h of shape [B, L, D]
        # query_seg of shape [D, max_width]

        B, L, D = h.size()

        # project start and end
        start_rep = self.project_start(h)
        end_rep = self.project_end(h)

        start_span_rep = extract_elements(start_rep, span_idx[:, :, 0])
        end_span_rep = extract_elements(end_rep, span_idx[:, :, 1])

        # concat start and end
        cat = torch.cat([start_span_rep, end_span_rep], dim=-1).relu()

        # project
        cat = self.out_project(cat)

        # reshape
        return cat.view(B, L, self.max_width, D)


class SpanMarkerV0(nn.Module):
    """
    Marks and projects span endpoints using an MLP.
    """

    def __init__(self, hidden_size: int, max_width: int, dropout: float = 0.4):
        super().__init__()
        self.max_width = max_width
        self.project_start = create_projection_layer(hidden_size, dropout)
        self.project_end = create_projection_layer(hidden_size, dropout)

        self.out_project = create_projection_layer(hidden_size * 2, dropout, hidden_size)

    def forward(self, h: torch.Tensor, span_idx: torch.Tensor) -> torch.Tensor:
        B, L, D = h.size()

        start_rep = self.project_start(h)
        end_rep = self.project_end(h)

        start_span_rep = extract_elements(start_rep, span_idx[:, :, 0])
        end_span_rep = extract_elements(end_rep, span_idx[:, :, 1])

        cat = torch.cat([start_span_rep, end_span_rep], dim=-1).relu()

        return self.out_project(cat).view(B, L, self.max_width, D)


class ConvShareV2(nn.Module):
    def __init__(self, hidden_size, max_width):
        super().__init__()

        self.max_width = max_width

        self.conv_weigth = nn.Parameter(
            torch.randn(hidden_size, hidden_size, max_width)
        )

        nn.init.xavier_normal_(self.conv_weigth)

    def forward(self, x, *args):
        span_reps = []

        x = torch.einsum('bld->bdl', x)

        for i in range(self.max_width):
            pad = i
            x_i = F.pad(x, (0, pad), "constant", 0)
            conv_w = self.conv_weigth[:, :, :i + 1]
            out_i = F.conv1d(x_i, conv_w)
            span_reps.append(out_i.transpose(-1, -2))

        out = torch.stack(span_reps, dim=-2)

        return out


class SpanRepLayer(nn.Module):
    """
    Various span representation approaches
    """

    def __init__(self, hidden_size, max_width, span_mode, **kwargs):
        super().__init__()

        if span_mode == 'marker':
            self.span_rep_layer = SpanMarker(hidden_size, max_width, **kwargs)
        elif span_mode == 'markerV0':
            self.span_rep_layer = SpanMarkerV0(hidden_size, max_width, **kwargs)
        elif span_mode == 'query':
            self.span_rep_layer = SpanQuery(
                hidden_size, max_width, trainable=True)
        elif span_mode == 'mlp':
            self.span_rep_layer = SpanMLP(hidden_size, max_width)
        elif span_mode == 'cat':
            self.span_rep_layer = SpanCAT(hidden_size, max_width)
        elif span_mode == 'conv_conv':
            self.span_rep_layer = SpanConv(
                hidden_size, max_width, span_mode='conv_conv')
        elif span_mode == 'conv_max':
            self.span_rep_layer = SpanConv(
                hidden_size, max_width, span_mode='conv_max')
        elif span_mode == 'conv_mean':
            self.span_rep_layer = SpanConv(
                hidden_size, max_width, span_mode='conv_mean')
        elif span_mode == 'conv_sum':
            self.span_rep_layer = SpanConv(
                hidden_size, max_width, span_mode='conv_sum')
        elif span_mode == 'conv_share':
            self.span_rep_layer = ConvShare(hidden_size, max_width)
        else:
            raise ValueError(f'Unknown span mode {span_mode}')

    def forward(self, x, *args):

        return self.span_rep_layer(x, *args)

```

## File: gliner/modeling/base.py

<a name='file-gliner-modeling-base.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional, Tuple
from abc import ABC, abstractmethod
from dataclasses import dataclass
import warnings

import torch
import torch.nn as nn
from torch.nn.utils.rnn import pad_sequence

from transformers.utils import ModelOutput

from .encoder import Encoder, BiEncoder
from .layers import LstmSeq2SeqEncoder, CrossFuser, create_projection_layer
from .scorers import Scorer
from .loss_functions import focal_loss_with_logits
from .span_rep import SpanRepLayer

@dataclass
class GLiNERModelOutput(ModelOutput):
    loss: Optional[torch.FloatTensor] = None
    logits: Optional[torch.FloatTensor] = None
    prompts_embedding: Optional[torch.FloatTensor] = None
    prompts_embedding_mask: Optional[torch.LongTensor] = None
    words_embedding: Optional[torch.FloatTensor] = None
    mask: Optional[torch.LongTensor] = None

def extract_word_embeddings(token_embeds, words_mask, attention_mask, 
                                    batch_size, max_text_length, embed_dim, text_lengths):
    words_embedding = torch.zeros(
        batch_size, max_text_length, embed_dim, dtype=token_embeds.dtype, device=token_embeds.device
    )

    batch_indices, word_idx = torch.where(words_mask>0)
    
    target_word_idx = words_mask[batch_indices, word_idx]-1

    words_embedding[batch_indices, target_word_idx] = token_embeds[batch_indices, word_idx]
    
    aranged_word_idx = torch.arange(max_text_length, 
                                        dtype=attention_mask.dtype, 
                                        device=token_embeds.device).expand(batch_size, -1)
    mask = aranged_word_idx<text_lengths
    return words_embedding, mask


def extract_prompt_features_and_word_embeddings(config, token_embeds, input_ids, attention_mask, 
                                                                    text_lengths, words_mask, embed_ent_token = True, **kwargs):
    # getting prompt embeddings
    batch_size, sequence_length, embed_dim = token_embeds.shape

    class_token_mask = input_ids == config.class_token_index
    num_class_tokens = torch.sum(class_token_mask, dim=-1, keepdim=True)

    max_embed_dim = num_class_tokens.max()
    max_text_length = text_lengths.max()
    aranged_class_idx = torch.arange(max_embed_dim, 
                                        dtype=attention_mask.dtype, 
                                        device=token_embeds.device).expand(batch_size, -1)
    
    batch_indices, target_class_idx = torch.where(aranged_class_idx<num_class_tokens)
    _, class_indices = torch.where(class_token_mask)
    if not embed_ent_token:
        class_indices+=1

    prompts_embedding = torch.zeros(
        batch_size, max_embed_dim, embed_dim, dtype=token_embeds.dtype, device=token_embeds.device
    )

    prompts_embedding_mask = (aranged_class_idx < num_class_tokens).to(attention_mask.dtype)

    prompts_embedding[batch_indices, target_class_idx] = token_embeds[batch_indices, class_indices]
    
    #getting words embedding
    words_embedding, mask = extract_word_embeddings(token_embeds, words_mask, attention_mask, 
                                    batch_size, max_text_length, embed_dim, text_lengths)

    return prompts_embedding, prompts_embedding_mask, words_embedding, mask

class BaseModel(ABC, nn.Module):
    def __init__(self, config, from_pretrained = False):
        super(BaseModel, self).__init__()
        self.config = config
        
        if not config.labels_encoder:
            self.token_rep_layer = Encoder(config, from_pretrained)
        else:
            self.token_rep_layer = BiEncoder(config, from_pretrained)
        if self.config.has_rnn:
            self.rnn = LstmSeq2SeqEncoder(config)

        if config.post_fusion_schema:
            self.config.num_post_fusion_layers = 3
            print('Initializing cross fuser...')
            print('Post fusion layer:', config.post_fusion_schema)
            print('Number of post fusion layers:', config.num_post_fusion_layers)

            self.cross_fuser = CrossFuser(self.config.hidden_size,
                                            self.config.hidden_size,
                                            num_heads=self.token_rep_layer.bert_layer.model.config.num_attention_heads,
                                            num_layers=self.config.num_post_fusion_layers,
                                            dropout=config.dropout, 
                                            schema=config.post_fusion_schema)
            
    def features_enhancement(self, text_embeds, labels_embeds, text_mask=None, labels_mask=None):
        labels_embeds, text_embeds = self.cross_fuser(labels_embeds, text_embeds, labels_mask, text_mask)
        return text_embeds, labels_embeds
    
    def _extract_prompt_features_and_word_embeddings(self, token_embeds, input_ids, attention_mask, 
                                                                    text_lengths, words_mask):
        prompts_embedding, prompts_embedding_mask, words_embedding, mask = extract_prompt_features_and_word_embeddings(self.config, 
                                                                                                                       token_embeds, 
                                                                                                                       input_ids, 
                                                                                                                       attention_mask, 
                                                                                                                       text_lengths, 
                                                                                                                       words_mask,
                                                                                                                       self.config.embed_ent_token)
        return prompts_embedding, prompts_embedding_mask, words_embedding, mask

    def get_uni_representations(self, 
                input_ids: Optional[torch.FloatTensor] = None,
                attention_mask: Optional[torch.LongTensor] = None,
                text_lengths: Optional[torch.Tensor] = None,
                words_mask: Optional[torch.LongTensor] = None,
                **kwargs):
        
        token_embeds = self.token_rep_layer(input_ids, attention_mask, **kwargs)

        prompts_embedding, prompts_embedding_mask, words_embedding, mask = self._extract_prompt_features_and_word_embeddings(token_embeds, input_ids, attention_mask, 
                                                                                                        text_lengths, words_mask)
        
        if self.config.has_rnn:
            words_embedding = self.rnn(words_embedding, mask)

        return prompts_embedding, prompts_embedding_mask, words_embedding, mask
    
    def get_bi_representations(self, 
                input_ids: Optional[torch.FloatTensor] = None,
                attention_mask: Optional[torch.LongTensor] = None,
                labels_embeds: Optional[torch.FloatTensor] = None,
                labels_input_ids: Optional[torch.FloatTensor] = None,
                labels_attention_mask: Optional[torch.LongTensor] = None,
                text_lengths: Optional[torch.Tensor] = None,
                words_mask: Optional[torch.LongTensor] = None,
                **kwargs): 
        if labels_embeds is not None:
            token_embeds = self.token_rep_layer.encode_text(input_ids, attention_mask, **kwargs)
        else:
            token_embeds, labels_embeds = self.token_rep_layer(input_ids, attention_mask,
                                                           labels_input_ids, labels_attention_mask, 
                                                                                            **kwargs) 
        batch_size, sequence_length, embed_dim = token_embeds.shape
        max_text_length = text_lengths.max()
        words_embedding, mask = extract_word_embeddings(token_embeds, words_mask, attention_mask, 
                                    batch_size, max_text_length, embed_dim, text_lengths)
        
        labels_embeds = labels_embeds.unsqueeze(0)
        labels_embeds = labels_embeds.expand(batch_size, -1, -1)
        labels_mask = torch.ones(labels_embeds.shape[:-1], dtype=attention_mask.dtype,
                                                        device = attention_mask.device)

        labels_embeds = labels_embeds.to(words_embedding.dtype)
        if hasattr(self, "cross_fuser"):
            words_embedding, labels_embeds = self.features_enhancement(words_embedding, labels_embeds, text_mask=mask, labels_mask=labels_mask)
        
        return labels_embeds, labels_mask, words_embedding, mask

    def get_representations(self, 
            input_ids: Optional[torch.FloatTensor] = None,
            attention_mask: Optional[torch.LongTensor] = None,
            labels_embeddings: Optional[torch.FloatTensor] = None,
            labels_input_ids: Optional[torch.FloatTensor] = None,
            labels_attention_mask: Optional[torch.LongTensor] = None,
            text_lengths: Optional[torch.Tensor] = None,
            words_mask: Optional[torch.LongTensor] = None,
            **kwargs):
        if self.config.labels_encoder:
            prompts_embedding, prompts_embedding_mask, words_embedding, mask = self.get_bi_representations(
                    input_ids, attention_mask, labels_embeddings, labels_input_ids, labels_attention_mask, 
                                                                        text_lengths, words_mask, **kwargs
            )
        else:
            prompts_embedding, prompts_embedding_mask, words_embedding, mask = self.get_uni_representations(
                                    input_ids, attention_mask, text_lengths, words_mask, **kwargs
            )
        return prompts_embedding, prompts_embedding_mask, words_embedding, mask 
    
    @abstractmethod
    def forward(self, x):
        pass

    def _loss(self, logits: torch.Tensor, labels: torch.Tensor, 
                    alpha: float = -1., gamma: float = 0.0, label_smoothing: float = 0.0):
        
        all_losses = focal_loss_with_logits(logits, labels,
                                            alpha=alpha,
                                            gamma=gamma,
                                            label_smoothing=label_smoothing)
        return all_losses

    @abstractmethod
    def loss(self, x):
        pass
    
class SpanModel(BaseModel):
    def __init__(self, config, encoder_from_pretrained):
        super(SpanModel, self).__init__(config, encoder_from_pretrained)
        self.span_rep_layer = SpanRepLayer(span_mode = config.span_mode, 
                                           hidden_size = config.hidden_size, 
                                           max_width = config.max_width,
                                           dropout = config.dropout)

        self.prompt_rep_layer = create_projection_layer(config.hidden_size, config.dropout)


    def forward(self,        
                input_ids: Optional[torch.FloatTensor] = None,
                attention_mask: Optional[torch.LongTensor] = None,
                labels_embeddings: Optional[torch.FloatTensor] = None,
                labels_input_ids: Optional[torch.FloatTensor] = None,
                labels_attention_mask: Optional[torch.LongTensor] = None,
                words_embedding: Optional[torch.FloatTensor] = None,
                mask: Optional[torch.LongTensor] = None,
                prompts_embedding: Optional[torch.FloatTensor] = None,
                prompts_embedding_mask: Optional[torch.LongTensor] = None,
                words_mask: Optional[torch.LongTensor] = None,
                text_lengths: Optional[torch.Tensor] = None,
                span_idx: Optional[torch.LongTensor] = None,
                span_mask: Optional[torch.LongTensor] = None,
                labels: Optional[torch.FloatTensor] = None,
                **kwargs
                ):

        prompts_embedding, prompts_embedding_mask, words_embedding, mask = self.get_representations(input_ids, attention_mask, 
                                                                                labels_embeddings, labels_input_ids, labels_attention_mask, 
                                                                                                                    text_lengths, words_mask)
        span_idx = span_idx*span_mask.unsqueeze(-1)

        span_rep = self.span_rep_layer(words_embedding, span_idx)
        
        prompts_embedding = self.prompt_rep_layer(prompts_embedding)

        scores = torch.einsum("BLKD,BCD->BLKC", span_rep, prompts_embedding)

        loss = None
        if labels is not None:
            loss = self.loss(scores, labels, prompts_embedding_mask, span_mask, **kwargs)

        output = GLiNERModelOutput(
            logits=scores,
            loss=loss,
            prompts_embedding=prompts_embedding,
            prompts_embedding_mask=prompts_embedding_mask,
            words_embedding=words_embedding,
            mask=mask,
        )
        return output
    
    def loss(self, scores, labels, prompts_embedding_mask, mask_label,
                        alpha: float = -1., gamma: float = 0.0, label_smoothing: float = 0.0, 
                        reduction: str = 'sum', **kwargs):
        
        batch_size = scores.shape[0]
        num_classes = prompts_embedding_mask.shape[-1]

        scores = scores.view(-1, num_classes)
        labels = labels.view(-1, num_classes)
        
        all_losses = self._loss(scores, labels, alpha, gamma, label_smoothing)

        masked_loss = all_losses.view(batch_size, -1, num_classes) * prompts_embedding_mask.unsqueeze(1)
        all_losses = masked_loss.view(-1, num_classes)

        mask_label = mask_label.view(-1, 1)
        
        all_losses = all_losses * mask_label.float()

        if reduction == "mean":
            loss = all_losses.mean()
        elif reduction == 'sum':
            loss = all_losses.sum()
        else:
            warnings.warn(
                f"Invalid Value for config 'loss_reduction': '{reduction} \n Supported reduction modes:"
                f" 'none', 'mean', 'sum'. It will be used 'sum' instead.")
            loss = all_losses.sum()
        return loss
    
class TokenModel(BaseModel):
    def __init__(self, config, encoder_from_pretrained):
        super(TokenModel, self).__init__(config, encoder_from_pretrained)
        self.scorer = Scorer(config.hidden_size, config.dropout)

    def forward(self,        
                input_ids: Optional[torch.FloatTensor] = None,
                attention_mask: Optional[torch.LongTensor] = None,
                labels_embeddings: Optional[torch.FloatTensor] = None,
                labels_input_ids: Optional[torch.FloatTensor] = None,
                labels_attention_mask: Optional[torch.LongTensor] = None,
                words_embedding: Optional[torch.FloatTensor] = None,
                mask: Optional[torch.LongTensor] = None,
                prompts_embedding: Optional[torch.FloatTensor] = None,
                prompts_embedding_mask: Optional[torch.LongTensor] = None,
                words_mask: Optional[torch.LongTensor] = None,
                text_lengths: Optional[torch.Tensor] = None,
                labels: Optional[torch.FloatTensor] = None,
                **kwargs
                ):

        prompts_embedding, prompts_embedding_mask, words_embedding, mask = self.get_representations(input_ids, attention_mask,
                                                                            labels_embeddings, labels_input_ids, labels_attention_mask,
                                                                                                                text_lengths, words_mask)
        
        scores = self.scorer(words_embedding, prompts_embedding)

        loss = None
        if labels is not None:
            loss = self.loss(scores, labels, prompts_embedding_mask, mask, **kwargs)
        
        output = GLiNERModelOutput(
            logits=scores,
            loss=loss,
            prompts_embedding=prompts_embedding,
            prompts_embedding_mask=prompts_embedding_mask,
            words_embedding=words_embedding,
            mask=mask,
        )
        return output
    
    def loss(self, scores, labels, prompts_embedding_mask, mask, 
                        alpha: float = -1., gamma: float = 0.0, label_smoothing: float = 0.0, 
                        reduction: str = 'sum', **kwargs):
        all_losses = self._loss(scores, labels, alpha, gamma, label_smoothing)

        all_losses = all_losses * prompts_embedding_mask.unsqueeze(1) * mask.unsqueeze(-1)

        if reduction == "mean":
            loss = all_losses.mean()
        elif reduction == 'sum':
            loss = all_losses.sum()
        else:
            warnings.warn(
                f"Invalid Value for config 'loss_reduction': '{reduction} \n Supported reduction modes:"
                f" 'none', 'mean', 'sum'. It will be used 'sum' instead.")
            loss = all_losses.sum()
        return loss

```

## File: gliner/modeling/layers.py

<a name='file-gliner-modeling-layers.py'></a>
*Description*: This is a Python script.

```python
import torch
from torch import nn
import torch.nn.functional as F
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence, pad_sequence

class LstmSeq2SeqEncoder(nn.Module):
    def __init__(self, config, num_layers=1, dropout=0., bidirectional=True):
        super(LstmSeq2SeqEncoder, self).__init__()
        self.lstm = nn.LSTM(input_size=config.hidden_size,
                            hidden_size=config.hidden_size//2,
                            num_layers=num_layers,
                            dropout=dropout,
                            bidirectional=bidirectional,
                            batch_first=True)

    def forward(self, x, mask, hidden=None):
        # Packing the input sequence
        lengths = mask.sum(dim=1).cpu()
        packed_x = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)

        # Passing packed sequence through LSTM
        packed_output, hidden = self.lstm(packed_x, hidden)

        # Unpacking the output sequence
        output, _ = pad_packed_sequence(packed_output, batch_first=True)

        return output


def create_projection_layer(hidden_size: int, dropout: float, out_dim: int = None) -> nn.Sequential:
    """
    Creates a projection layer with specified configurations.
    """
    if out_dim is None:
        out_dim = hidden_size

    return nn.Sequential(
        nn.Linear(hidden_size, out_dim * 4),
        nn.ReLU(),
        nn.Dropout(dropout),
        nn.Linear(out_dim * 4, out_dim)
    )

class MultiheadAttention(nn.Module):
    def __init__(self, hidden_size, num_heads, dropout) -> None:
        super().__init__()
        self.hidden_size=hidden_size
        self.num_heads=num_heads
        self.attention_head_size=hidden_size//num_heads
        self.attention_probs_dropout_prob=dropout
        self.query_layer = nn.Linear(hidden_size, hidden_size)
        self.key_layer = nn.Linear(hidden_size, hidden_size)
        self.value_layer = nn.Linear(hidden_size, hidden_size)

    def transpose_for_scores(self, x: torch.Tensor) -> torch.Tensor:
        new_x_shape = x.size()[:-1] + (self.num_heads, self.attention_head_size)
        x = x.view(new_x_shape)
        return x.permute(0, 2, 1, 3)
    
    def forward(self, query, key=None, value=None, head_mask=None, attn_mask=None):
        query = self.transpose_for_scores(self.query_layer(query))
        if key is None:
            key = self.transpose_for_scores(self.key_layer(query))
        else:
            key = self.transpose_for_scores(self.key_layer(key))
        if value is None and key is None:
            value = self.transpose_for_scores(self.value_layer(query))
        elif value is None and key is not None:
            value = self.transpose_for_scores(self.value_layer(key))
        else:
            value = self.transpose_for_scores(self.value_layer(value))

        context_layer = torch.nn.functional.scaled_dot_product_attention(
            query,
            key,
            value,
            head_mask,
            self.attention_probs_dropout_prob if self.training else 0.0,
            is_causal=False,
            scale=None,
        )

        context_layer = context_layer.permute(0, 2, 1, 3).contiguous()
        new_context_layer_shape = context_layer.size()[:-2] + (self.hidden_size,)
        context_layer = context_layer.view(new_context_layer_shape)

        return context_layer, None
    
class SelfAttentionBlock(nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        self.self_attn = MultiheadAttention(d_model, num_heads, dropout=dropout)
        self.pre_norm = nn.LayerNorm(d_model)
        self.post_norm = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)
        self.q_proj = nn.Linear(d_model, d_model)
        self.k_proj = nn.Linear(d_model, d_model)
        self.v_proj = nn.Linear(d_model, d_model)

    def forward(self, x, mask=None):
        x = self.pre_norm(x)
        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)
        attn_output, _ = self.self_attn(q, k, v, attn_mask=mask)
        output = x + self.dropout(attn_output)
        return self.post_norm(output)

class CrossAttentionBlock(nn.Module):
    def __init__(self, d_model, num_heads, dropout=0.1):
        super().__init__()
        self.cross_attn = MultiheadAttention(d_model, num_heads, dropout=dropout)
        self.pre_norm = nn.LayerNorm(d_model)
        self.post_norm = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)
        self.v_proj = nn.Linear(d_model, d_model)

    def forward(self, query, key, value=None, mask=None):
        query = self.pre_norm(query)
        if value is None:
            value = self.v_proj(key)
        attn_output, _ = self.cross_attn(query, key, value, attn_mask=mask)
        output = query + self.dropout(attn_output)
        return self.post_norm(output)
    
class CrossFuser(nn.Module):
    def __init__(self, d_model, query_dim, num_heads=8, num_layers=1, dropout=0.1, schema='l2l-l2t'):
        super().__init__()
        self.d_model = d_model
        self.schema = schema.split('-')
        layers = []
        for _ in range(num_layers):
            layer = []
            for attn_type in self.schema:
                if attn_type in {'l2l', 't2t'}:
                    layer.append(SelfAttentionBlock(d_model, num_heads, dropout))
                else:
                    layer.append(CrossAttentionBlock(d_model, num_heads, dropout))
            layer = nn.ModuleList(layer)
            layers.append(layer)

        self.layers = nn.ModuleList(layers)
        # self.dense_i = nn.Linear(query_dim, d_model)
        # self.dense_o = nn.Linear(d_model, query_dim)

    def forward(self, query, key, query_mask=None, key_mask=None):
        # query = self.dense_i(query)
        for sublayers in self.layers:
            for id, layer in enumerate(sublayers):
                if self.schema[id] == 'l2l':
                    if query_mask is not None:
                        self_attn_mask = query_mask.unsqueeze(1) * query_mask.unsqueeze(2)
                    else:
                        self_attn_mask = None
                    query = layer(query, mask=self_attn_mask)
                elif self.schema[id] == 't2t':
                    if key_mask is not None:
                        self_attn_mask = key_mask.unsqueeze(1) * key_mask.unsqueeze(2)
                    else:
                        self_attn_mask = None
                    key = layer(key, mask=self_attn_mask)
                elif self.schema[id] == 'l2t':
                    if query_mask is not None and key_mask is not None:
                        cross_attn_mask = query_mask.unsqueeze(-1) * key_mask.unsqueeze(1)
                    else:
                        cross_attn_mask = None
                    query = layer(query, key, mask=cross_attn_mask)
                elif self.schema[id] == 't2l':
                    if query_mask is not None and key_mask is not None:
                        cross_attn_mask = key_mask.unsqueeze(-1) * query_mask.unsqueeze(1)
                    else:
                        cross_attn_mask = None
                    key = layer(key, query, mask=cross_attn_mask)
        # query=self.dense_o(query)   
        return query, key

class LayersFuser(nn.Module):
    def __init__(self, num_layers, hidden_size, output_size=None):
        super().__init__()
        self.num_layers = num_layers
        self.hidden_size = hidden_size
        self.output_size = output_size if output_size is not None else hidden_size
        
        # Squeeze operation
        self.squeeze = nn.Linear(hidden_size, 1)
        
        # Excitation operation
        self.W1 = nn.Linear(num_layers, num_layers // 2)
        self.W2 = nn.Linear(num_layers // 2, num_layers)
        
        # Final projection
        self.output_projection = nn.Linear(self.hidden_size, self.output_size)
        
    def forward(self, encoder_outputs):
        # encoder_outputs is a list of tensors, each of shape [B, L, D]
        B, L, D = encoder_outputs[0].shape
        
        # Concatenate all layers
        U = torch.stack(encoder_outputs[1:], dim=1)  # [B, K, L, D]

        # Squeeze operation
        Z = self.squeeze(U).squeeze(-1)  # [B, K, L]
        Z = Z.mean(dim=2)  # [B, K]
        
        # Excitation operation
        s = self.W2(F.relu(self.W1(Z)))  # [B, K]
        s = torch.sigmoid(s)  # [B, K]
        
        # Apply attention weights
        U_weighted = U * s.unsqueeze(-1).unsqueeze(-1)  # [B, K, L, D]
        
        # Sum across layers
        U_sum = U_weighted.sum(dim=1)  # [B, L, D]
        
        # final projection
        output = self.output_projection(U_sum)  # [B, L, output_size]
        
        return output
```

## File: gliner/modeling/scorers.py

<a name='file-gliner-modeling-scorers.py'></a>
*Description*: This is a Python script.

```python
import torch
from torch import nn

class Scorer(nn.Module):
    def __init__(self, hidden_size, dropout=0.1):
        super().__init__()

        self.proj_token = nn.Linear(hidden_size, hidden_size * 2)
        self.proj_label = nn.Linear(hidden_size, hidden_size * 2)

        self.out_mlp = nn.Sequential(
            nn.Linear(hidden_size * 3, hidden_size * 4),
            nn.Dropout(dropout),
            nn.ReLU(),
            nn.Linear(hidden_size * 4, 3)  # start, end, score
        )

    def forward(self, token_rep, label_rep):
        batch_size, seq_len, hidden_size = token_rep.shape
        num_classes = label_rep.shape[1]

        # (batch_size, seq_len, 3, hidden_size)
        token_rep = self.proj_token(token_rep).view(batch_size, seq_len, 1, 2, hidden_size)
        label_rep = self.proj_label(label_rep).view(batch_size, 1, num_classes, 2, hidden_size)

        # (2, batch_size, seq_len, num_classes, hidden_size)
        token_rep = token_rep.expand(-1, -1, num_classes, -1, -1).permute(3, 0, 1, 2, 4)
        label_rep = label_rep.expand(-1, seq_len, -1, -1, -1).permute(3, 0, 1, 2, 4)

        # (batch_size, seq_len, num_classes, hidden_size * 3)
        cat = torch.cat([token_rep[0], label_rep[0], token_rep[1] * label_rep[1]], dim=-1)

        # (batch_size, seq_len, num_classes, 3)
        scores = self.out_mlp(cat).permute(3, 0, 1, 2)

        return scores

```

## File: gliner/modeling/encoder.py

<a name='file-gliner-modeling-encoder.py'></a>
*Description*: This is a Python script.

```python
import warnings
from pathlib import Path

import torch
from torch import nn
from transformers import AutoModel, AutoConfig

from .layers import LayersFuser
from ..utils import is_module_available, MissedPackageException

IS_LLM2VEC = is_module_available('llm2vec')
IS_PEFT = is_module_available('peft')
IS_TURBOT5 = is_module_available('turbot5')

if IS_LLM2VEC:
    from llm2vec.models import MistralBiModel, LlamaBiModel, GemmaBiModel, Qwen2BiModel
    DECODER_MODEL_MAPPING = {
        "MistralConfig": MistralBiModel,
        "LlamaConfig": LlamaBiModel,
        "GemmaConfig": GemmaBiModel,
        "Qwen2Config": Qwen2BiModel
    }
else:
    DECODER_MODEL_MAPPING = {}

if IS_TURBOT5:
    from turbot5.model.modeling import T5EncoderModel
else:
    from transformers import T5EncoderModel

if IS_PEFT:
    from peft import LoraConfig, get_peft_model

class Transformer(nn.Module):
    def __init__(self, model_name, config, from_pretrained=False, labels_encoder = False):
        super().__init__()
        if labels_encoder:
            encoder_config = config.labels_encoder_config
        else:
            encoder_config = config.encoder_config
        if encoder_config is None:
            encoder_config = AutoConfig.from_pretrained(model_name)
            if config.vocab_size!=-1:
                encoder_config.vocab_size = config.vocab_size

        config_name = encoder_config.__class__.__name__

        if config_name in DECODER_MODEL_MAPPING:
            if not IS_LLM2VEC:
                raise MissedPackageException(f"The llm2vec package must be installed to use this decoder model: {config_name}")
            else:
                print('Loading decoder model using LLM2Vec...')
                ModelClass = DECODER_MODEL_MAPPING[config_name]
            custom = True
            kwargs = {}
        elif config_name in {'T5Config', 'MT5Config'}:
            custom = True
            ModelClass = T5EncoderModel
            if IS_TURBOT5:
                kwargs = {"attention_type": 'flash'}
            else:
                kwargs = {}
        else:
            custom = False
            ModelClass = AutoModel

        if from_pretrained:
            self.model = ModelClass.from_pretrained(model_name, trust_remote_code=True)
        else:
            if not custom:
                self.model = ModelClass.from_config(encoder_config, trust_remote_code=True)
            else:
                self.model = ModelClass(encoder_config, **kwargs)

        adapter_config_file = Path(model_name) / "adapter_config.json"

        if adapter_config_file.exists():
            if not IS_PEFT:
                warnings.warn(f"Adapter configs were detected, if you want to apply them you need to install peft package.")
            else:
                adapter_config = LoraConfig.from_pretrained(model_name)
                self.model = get_peft_model(self.model, adapter_config)

        if config.fuse_layers:
            self.layers_fuser = LayersFuser(encoder_config.num_hidden_layers,
                                                        encoder_config.hidden_size)

        if labels_encoder:
            config.labels_encoder_config = encoder_config
        else:
            config.encoder_config = encoder_config

        self.config = config

    def forward(self, *args, **kwargs):
        if self.config.fuse_layers:
            output_hidden_states = True
        else:
            output_hidden_states = False
        output = self.model(*args, output_hidden_states = output_hidden_states, 
                                            return_dict = True,  **kwargs)
        if self.config.fuse_layers:
            encoder_layer = self.layers_fuser(output.hidden_states)
        else:
            encoder_layer = output[0]

        return encoder_layer
    
class Encoder(nn.Module):
    def __init__(self, config, from_pretrained: bool = False):
        super().__init__()

        self.bert_layer = Transformer( #transformer_model
            config.model_name, config, from_pretrained,
        )

        bert_hidden_size = self.bert_layer.model.config.hidden_size

        if config.hidden_size != bert_hidden_size:
            self.projection = nn.Linear(bert_hidden_size, config.hidden_size)

    def resize_token_embeddings(self, new_num_tokens, pad_to_multiple_of=None):
        return self.bert_layer.model.resize_token_embeddings(new_num_tokens, 
                                                                pad_to_multiple_of)

    def get_input_embeddings(self):
        return self.bert_layer.model.get_input_embeddings()
    
    def encode_text(self, input_ids, attention_mask, *args, **kwargs):
        token_embeddings = self.bert_layer(input_ids, attention_mask, *args, **kwargs)
        if hasattr(self, "projection"):
            token_embeddings = self.projection(token_embeddings)
        return token_embeddings
    
    def forward(self, *args, **kwargs) -> torch.Tensor:
        token_embeddings = self.encode_text(*args, **kwargs)
        return token_embeddings

class BiEncoder(Encoder):
    def __init__(self, config, from_pretrained: bool = False):
        super().__init__(config, from_pretrained)
        if config.labels_encoder is not None:
            self.labels_encoder = Transformer( #transformer_model
                config.labels_encoder, config, from_pretrained, True
            )
            le_hidden_size = self.labels_encoder.model.config.hidden_size

            if config.hidden_size != le_hidden_size:
                self.labels_projection = nn.Linear(le_hidden_size, config.hidden_size)
    
    def mean_pooling(self, token_embeddings, attention_mask):
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)

    def encode_labels(self, input_ids, attention_mask, *args, **kwargs):
        labels_embeddings = self.labels_encoder(input_ids, attention_mask, *args, **kwargs)
        if hasattr(self, "labels_projection"):
            labels_embeddings = self.labels_projection(labels_embeddings)
        labels_embeddings = self.mean_pooling(labels_embeddings, attention_mask)
        return labels_embeddings

    def forward(self, input_ids, attention_mask, 
                    labels_input_ids = None, labels_attention_mask=None, 
                                            *args, **kwargs) -> torch.Tensor:
        token_embeddings = self.encode_text(input_ids, attention_mask, *args, **kwargs)

        labels_embeddings = self.encode_labels(labels_input_ids, labels_attention_mask, *args, **kwargs)
        return token_embeddings, labels_embeddings
```

## File: gliner/training/__init__.py

<a name='file-gliner-training-__init__.py'></a>
*Description*: This is a Python script.

```python
from .trainer import Trainer, TrainingArguments
```

## File: gliner/training/trainer.py

<a name='file-gliner-training-trainer.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional, Union, Any, Dict, Tuple, List
from dataclasses import dataclass, field

import torch
import transformers
from transformers.training_args import OptimizerNames
from transformers.trainer import (
    is_sagemaker_mp_enabled,
    get_parameter_names,
    ALL_LAYERNORM_LAYERS,
)
from transformers.trainer_utils import seed_worker

if transformers.utils.is_apex_available():
    from apex import amp

if is_sagemaker_mp_enabled():
    from transformers.trainer_pt_utils import smp_forward_backward
from torch.utils.data import DataLoader, Dataset

@dataclass
class TrainingArguments(transformers.TrainingArguments):
    cache_dir: Optional[str] = field(default=None)
    optim: str = field(default="adamw_torch")
    others_lr: Optional[float] = None
    others_weight_decay: Optional[float] = 0.0
    focal_loss_alpha: Optional[float] = -1
    focal_loss_gamma: Optional[float] = 0
    label_smoothing: Optional[float] = 0
    loss_reduction: Optional[str] = 'sum' 

class Trainer(transformers.Trainer):
    def training_step(self, model, inputs, *args, **kwargs) -> torch.Tensor:
        """
        Perform a training step on a batch of inputs.

        Subclass and override to inject custom behavior.

        Args:
            model (`nn.Module`):
                The model to train.
            inputs (`Dict[str, Union[torch.Tensor, Any]]`):
                The inputs and targets of the model.

                The dictionary will be unpacked before being fed to the model. Most models expect the targets under the
                argument `labels`. Check your model's documentation for all accepted arguments.

        Return:
            `torch.Tensor`: The tensor with training loss on this batch.
        """
        model.train()
        try:
            inputs = self._prepare_inputs(inputs)
            if is_sagemaker_mp_enabled():
                loss_mb = smp_forward_backward(model, inputs, self.args.gradient_accumulation_steps)
                return loss_mb.reduce_mean().detach().to(self.args.device)

            with self.compute_loss_context_manager():
                loss = self.compute_loss(model, inputs)

            del inputs
            torch.cuda.empty_cache()

            kwargs = {}

            # For LOMO optimizers you need to explicitly use the learnign rate
            # if self.args.optim in [OptimizerNames.LOMO, OptimizerNames.ADALOMO]:
            #     kwargs["learning_rate"] = self._get_learning_rate()

            if self.args.n_gpu > 1:
                loss = loss.mean()  # mean() to average on multi-gpu parallel training

            if self.use_apex:
                with amp.scale_loss(loss, self.optimizer) as scaled_loss:
                    scaled_loss.backward()
            else:
                self.accelerator.backward(loss, **kwargs)

            return loss.detach() / self.args.gradient_accumulation_steps
        except Exception as e:
            print(f"Skipping iteration due to error: {e}")
            model.zero_grad(set_to_none=True)
            torch.cuda.empty_cache()
            return torch.tensor(0.0, requires_grad=True).to(model.device) 

    def save_model(self, output_dir: Optional[str] = None, _internal_call: bool = False):
        self.model.save_pretrained(output_dir)
        
    def compute_loss(self, model, inputs):
        """
        Override compute_loss to use a custom loss function.
        """
        # Forward pass
        outputs = model(alpha = self.args.focal_loss_alpha,
                        gamma = self.args.focal_loss_gamma,
                        label_smoothing = self.args.label_smoothing,
                        reduction = self.args.loss_reduction,
                        **inputs)
        loss = outputs.loss
        return loss
    
    def create_optimizer(self):
        """
        Setup the optimizer.

        We provide a reasonable default that works well. If you want to use something else, you can pass a tuple in the
        Trainer's init through `optimizers`, or subclass and override this method in a subclass.
        """
        if is_sagemaker_mp_enabled():
            return super().create_optimizer()

        opt_model = self.model

        if self.optimizer is None:
            decay_parameters = get_parameter_names(opt_model, ALL_LAYERNORM_LAYERS)
            decay_parameters = [name for name in decay_parameters if "bias" not in name]
            if self.args.others_lr is not None:
                encoder_parameters = [name for name, _ in opt_model.named_parameters() if "token_rep_layer" in name]
                optimizer_grouped_parameters = [
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n in decay_parameters and n not in encoder_parameters and p.requires_grad)
                        ],
                        "weight_decay": self.args.others_weight_decay,
                        "lr": self.args.others_lr,
                    },
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n not in decay_parameters and n not in encoder_parameters and p.requires_grad)
                        ],
                        "weight_decay": 0.0,
                        "lr": self.args.others_lr,
                    },
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n in decay_parameters and n in encoder_parameters and p.requires_grad)
                        ],
                        "weight_decay": self.args.weight_decay,
                    },
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n not in decay_parameters and n in encoder_parameters and p.requires_grad)
                        ],
                        "weight_decay": 0.0,
                    },
                ]
            else:
                optimizer_grouped_parameters = [
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n in decay_parameters and p.requires_grad)
                        ],
                        "weight_decay": self.args.weight_decay,
                    },
                    {
                        "params": [
                            p for n, p in opt_model.named_parameters() if (n not in decay_parameters and p.requires_grad)
                        ],
                        "weight_decay": 0.0,
                    },
                ]

            optimizer_cls, optimizer_kwargs = Trainer.get_optimizer_cls_and_kwargs(self.args)

            self.optimizer = optimizer_cls(optimizer_grouped_parameters, **optimizer_kwargs)

        return self.optimizer

    def prediction_step(
        self,
        model: torch.nn.Module,
        inputs: Dict[str, Union[torch.Tensor, Any]],
        prediction_loss_only: bool,
        ignore_keys: Optional[List[str]] = None,
    ) -> Tuple[Optional[torch.Tensor], Optional[torch.Tensor], Optional[torch.Tensor]]:
        """
        Perform an evaluation step on model using inputs.

        Subclass and override to inject custom behavior.

        Args:
            model (nn.Module):
                The model to evaluate.
            inputs (Dict[str, Union[torch.Tensor, Any]]):
                The inputs and targets of the model.

                The dictionary will be unpacked before being fed to the model. Most models expect the targets under the
                argument labels. Check your model's documentation for all accepted arguments.
            prediction_loss_only (bool):
                Whether or not to return the loss only.
            ignore_keys (List[str], *optional*):
                A list of keys in the output of your model (if it is a dictionary) that should be ignored when
                gathering predictions.

        Return:
            Tuple[Optional[torch.Tensor], Optional[torch.Tensor], Optional[torch.Tensor]]: A tuple with the loss,
            logits and labels (each being optional).
        """
        with torch.no_grad():
            loss = None
            with self.compute_loss_context_manager():
                outputs = model(**inputs)
            loss = outputs.loss
            logits = outputs.logits
            labels = inputs['labels']
        if prediction_loss_only:
            return (loss, None, None)
        return (loss, logits, labels)


    def get_train_dataloader(self) -> DataLoader:
        """
        Returns the training [`~torch.utils.data.DataLoader`].

        Will use no sampler if `train_dataset` does not implement `__len__`, a random sampler (adapted to distributed
        training if necessary) otherwise.

        Subclass and override this method if you want to inject some custom behavior.
        """
        if self.train_dataset is None:
            raise ValueError("Trainer: training requires a train_dataset.")

        train_dataset = self.train_dataset
        data_collator = self.data_collator

        dataloader_params = {
            "batch_size": self._train_batch_size,
            "collate_fn": data_collator,
            "num_workers": self.args.dataloader_num_workers,
            "pin_memory": self.args.dataloader_pin_memory,
            "persistent_workers": self.args.dataloader_persistent_workers,
        }

        if not isinstance(train_dataset, torch.utils.data.IterableDataset):
            dataloader_params["sampler"] = self._get_train_sampler()
            dataloader_params["drop_last"] = self.args.dataloader_drop_last
            dataloader_params["worker_init_fn"] = seed_worker
            dataloader_params["prefetch_factor"] = self.args.dataloader_prefetch_factor

        return self.accelerator.prepare(DataLoader(train_dataset, **dataloader_params))

    def get_eval_dataloader(self, eval_dataset: Optional[Union[str, Dataset]] = None) -> DataLoader:
        """
        Returns the evaluation [`~torch.utils.data.DataLoader`].

        Subclass and override this method if you want to inject some custom behavior.

        Args:
            eval_dataset (`str` or `torch.utils.data.Dataset`, *optional*):
                If a `str`, will use `self.eval_dataset[eval_dataset]` as the evaluation dataset. If a `Dataset`, will override `self.eval_dataset` and must implement `__len__`. If it is a [`~datasets.Dataset`], columns not accepted by the `model.forward()` method are automatically removed.
        """
        if eval_dataset is None and self.eval_dataset is None:
            raise ValueError("Trainer: evaluation requires an eval_dataset.")

        # If we have persistent workers, don't do a fork bomb especially as eval datasets
        # don't change during training
        dataloader_key = eval_dataset if isinstance(eval_dataset, str) else "eval"
        if (
            hasattr(self, "_eval_dataloaders")
            and dataloader_key in self._eval_dataloaders
            and self.args.dataloader_persistent_workers
        ):
            return self.accelerator.prepare(self._eval_dataloaders[dataloader_key])

        eval_dataset = (
            self.eval_dataset[eval_dataset]
            if isinstance(eval_dataset, str)
            else eval_dataset
            if eval_dataset is not None
            else self.eval_dataset
        )
        data_collator = self.data_collator

        dataloader_params = {
            "batch_size": self.args.eval_batch_size,
            "collate_fn": data_collator,
            "num_workers": self.args.dataloader_num_workers,
            "pin_memory": self.args.dataloader_pin_memory,
            "persistent_workers": self.args.dataloader_persistent_workers,
        }

        if not isinstance(eval_dataset, torch.utils.data.IterableDataset):
            dataloader_params["sampler"] = self._get_eval_sampler(eval_dataset)
            dataloader_params["drop_last"] = self.args.dataloader_drop_last
            dataloader_params["prefetch_factor"] = self.args.dataloader_prefetch_factor

        # accelerator.free_memory() will destroy the references, so
        # we need to store the non-prepared version
        eval_dataloader = DataLoader(eval_dataset, **dataloader_params)
        if self.args.dataloader_persistent_workers:
            if hasattr(self, "_eval_dataloaders"):
                self._eval_dataloaders[dataloader_key] = eval_dataloader
            else:
                self._eval_dataloaders = {dataloader_key: eval_dataloader}

        return self.accelerator.prepare(eval_dataloader)

```

## File: gliner/multitask/open_extraction.py

<a name='file-gliner-multitask-open_extraction.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional, List, Union
import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"
import torch
from datasets import load_dataset, Dataset
from gliner import GLiNER

from .base import GLiNERBasePipeline

class GLiNEROpenExtractor(GLiNERBasePipeline):
    """
    A class to use GLiNER for open information extraction inference and evaluation.

    Attributes:
        device (str): Device to run the model on, e.g., 'cuda:0' or 'cpu'.
        model (GLiNER): Loaded GLiNER model instance.
        prompt (str): Template prompt for open information extraction.

    Methods:
        process_predictions(predictions):
            Processes model predictions to extract the most likely labels.
        prepare_texts(texts, labels):
            Creates open information extraction prompts for each input text.
        __call__(texts, labels, threshold=0.5):
            Runs the model on the given texts and returns predicted labels.
        evaluate(dataset_id, labels=None, threshold=0.5, max_examples=-1):
            Evaluates the model on a dataset and computes F1 scores.
    """

    prompt = ""

    def __init__(self, model_id: str = None, model: GLiNER = None, device: str = 'cuda:0', prompt: Optional[str] = None):
        """
        Initializes the GLiNEROpenExtractor.

        Args:
            model_id (str, optional): Identifier for the model to be loaded. Defaults to None.
            model (GLiNER, optional): Preloaded GLiNER model. Defaults to None.
            device (str, optional): Device to run the model on ('cpu' or 'cuda:X'). Defaults to 'cuda:0'.
            prompt (str, optional): Template prompt for open information extraction.
        """
        # Use the provided prompt or default to the class-level prompt
        prompt = prompt if prompt is not None else self.prompt
        super().__init__(model_id=model_id, model=model, prompt=prompt, device=device)


    def process_predictions(self, predictions, **kwargs):
        """
        Processes predictions to extract the highest-scoring label(s).

        Args:
            predictions (list): List of predictions with scores.

        Returns:
            list: List of predicted labels for each input.
        """
        return predictions

    def prepare_texts(self, texts: List[str], **kwargs):
        """
        Prepares prompts for open-information extraction.

        Args:
            texts (list): List of input texts.

        Returns:
            list: List of formatted prompts.
        """
        prompts = []

        for id, text in enumerate(texts):
            prompt = f"{self.prompt} \n {text}"
            prompts.append(prompt)
        return prompts

    
    def evaluate(self, dataset_id: Optional[str] = None, dataset: Optional[Dataset] = None, 
                    labels: Optional[List[str]]=None, threshold: float =0.5, max_examples: float =-1):
        """
        Evaluates the model on a specified dataset and computes evaluation metrics.

        Args:
            dataset_id (str, optional): Identifier for the dataset to load (e.g., from Hugging Face datasets).
            dataset (Dataset, optional): A pre-loaded dataset to evaluate. If provided, `dataset_id` is ignored.
            labels (list, optional): List of target labels to consider for extraction. Defaults to None (use all).
            threshold (float): Confidence threshold for predictions. Defaults to 0.5.
            max_examples (int): Maximum number of examples to evaluate. Defaults to -1 (use all available examples).

        Returns:
            dict: A dictionary containing evaluation metrics.
        
        Raises:
            ValueError: If neither `dataset_id` nor `dataset` is provided.
        """
        raise NotImplementedError("Currently `evaluate` method is not implemented.")
```

## File: gliner/multitask/classification.py

<a name='file-gliner-multitask-classification.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional, List
import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"
import torch
from datasets import load_dataset, Dataset
from sklearn.metrics import f1_score
from gliner import GLiNER

from .base import GLiNERBasePipeline

class GLiNERClassifier(GLiNERBasePipeline):
    """
    A class to evaluate the GLiNER model for classification tasks using F1 scores.

    Attributes:
        device (str): Device to run the model on, e.g., 'cuda:0' or 'cpu'.
        model (GLiNER): Loaded GLiNER model instance.
        prompt (str): Template prompt for text classification.

    Methods:
        compute_f_score(predicts, true_labels):
            Computes micro, macro, and weighted F1 scores.
        prepare_dataset(dataset, classes=None, text_column='text', label_column='label', split=None, max_examples=-1):
            Prepares texts and true labels from the given dataset.
        process_predictions(predictions):
            Processes model predictions to extract the most likely labels.
        prepare_texts(texts, labels):
            Creates classification prompts for each input text.
        __call__(texts, labels, threshold=0.5):
            Runs the model on the given texts and returns predicted labels.
        evaluate(dataset_id, labels=None, threshold=0.5, max_examples=-1):
            Evaluates the model on a dataset and computes F1 scores.
    """

    prompt = "Classify text into the following classes: {}"

    def __init__(self, model_id: str = None, model: GLiNER = None, device: str = 'cuda:0', prompt: Optional[str] = None):
        """
        Initializes the GLiNERClassifier.

        Args:
            model_id (str, optional): Identifier for the model to be loaded. Defaults to None.
            model (GLiNER, optional): Preloaded GLiNER model. Defaults to None.
            device (str, optional): Device to run the model on ('cpu' or 'cuda:X'). Defaults to 'cuda:0'.
            prompt (str, optional): Template prompt for text classification. Defaults to the class-level prompt.
        """
        # Use the provided prompt or default to the class-level prompt
        prompt = prompt if prompt is not None else self.prompt
        super().__init__(model_id=model_id, model=model, prompt=prompt, device=device)


    def compute_f_score(self, predicts, true_labels):
        """
        Computes the micro, macro, and weighted F1 scores.

        Args:
            predicts (list): List of predicted labels.
            true_labels (list): List of true labels.

        Returns:
            dict: Dictionary with micro, macro, and weighted F1 scores.
        """
        micro = f1_score(true_labels, predicts, average="micro")
        macro = f1_score(true_labels, predicts, average="macro")
        weighted = f1_score(true_labels, predicts, average="weighted")
        return {"micro": micro, "macro": macro, "weighted": weighted}

    def prepare_dataset(self, dataset: Dataset, classes=None, text_column='text', label_column="label", split=None, max_examples=-1):
        """
        Prepares the dataset by extracting texts and true labels.

        Args:
            dataset (Dataset or dict): The dataset to prepare.
            classes (list, optional): List of class labels. Defaults to None.
            text_column (str): Name of the text column. Defaults to 'text'.
            label_column (str): Name of the label column. Defaults to 'label'.
            split (str, optional): Delimiter for splitting class names. Defaults to None.
            max_examples (int): Maximum number of examples to use. Defaults to -1 (use all).

        Returns:
            tuple: Texts, classes, and true labels.
        """
        if 'test' in dataset:
            test_dataset = dataset['test']
        elif isinstance(dataset, Dataset):
            test_dataset = dataset
        else:
            test_dataset = dataset['train']
        
        if classes is None:
            classes = test_dataset.features[label_column].names
            if split is not None:
                classes = [' '.join(class_.split(split)) for class_ in classes]

        texts = test_dataset[text_column]
        true_labels = test_dataset[label_column]

        if isinstance(test_dataset[label_column][0], int):
            true_labels = [classes[label] for label in true_labels]

        if max_examples > 0:
            texts = texts[:max_examples]
            true_labels = true_labels[:max_examples]

        return texts, classes, true_labels

    def process_predictions(self, predictions, multi_label=False, **kwargs):
        """
        Processes predictions to extract the highest-scoring label(s).

        Args:
            predictions (list): List of predictions with scores.
            multi_label (bool): Whether to allow multiple labels per input. Defaults to False.

        Returns:
            list: List of predicted labels for each input.
        """
        batch_predicted_labels = []

        for prediction in predictions:
            # Sort predictions by score in descending order
            sorted_predictions = sorted(prediction, key=lambda entity: entity["score"], reverse=True)

            if not sorted_predictions:
                # Default prediction if no valid predictions are found
                batch_predicted_labels.append([{'label': 'other', 'score': 1.0}])
                continue

            if not multi_label:
                # Single-label mode: select the top prediction and compute softmax score
                scores = [item['score'] for item in sorted_predictions]
                softmax_scores = torch.softmax(torch.tensor(scores), dim=0).tolist()
                top_prediction = {'label': sorted_predictions[0]['text'], 'score': softmax_scores[0]}
                batch_predicted_labels.append([top_prediction])
            else:
                # Multi-label mode: retain all predictions with original scores
                predicted_labels = [{'label': pred['text'], 'score': pred['score']} for pred in sorted_predictions]
                batch_predicted_labels.append(predicted_labels)

        return batch_predicted_labels

    def prepare_texts(self, texts, classes, **kwargs):
        """
        Prepares prompts for classification by appending labels to texts.

        Args:
            texts (list): List of input texts.
            classes (list): List of classification labels.

        Returns:
            list: List of formatted prompts.
        """
        prompts = []
        labels_ = ', '.join(classes)
        for text in texts:
            prompt = f"{self.prompt.format(labels_)} \n {text}"
            prompts.append(prompt)
        return prompts

    def evaluate(self, dataset_id: Optional[str] = None, dataset: Optional[Dataset] = None, 
                    labels: Optional[List[str]]=None, threshold: float =0.5, max_examples: float =-1):
        """
        Evaluates the model on a specified dataset and computes evaluation metrics.

        Args:
            dataset_id (str, optional): Identifier for the dataset to load (e.g., from Hugging Face datasets).
            dataset (Dataset, optional): A pre-loaded dataset to evaluate. If provided, `dataset_id` is ignored.
            labels (list, optional): List of target labels to consider for classification. Defaults to None (use all).
            threshold (float): Confidence threshold for predictions. Defaults to 0.5.
            max_examples (int): Maximum number of examples to evaluate. Defaults to -1 (use all available examples).

        Returns:
            dict: A dictionary containing evaluation metrics such as F1 scores (micro, macro, and weighted).
        
        Raises:
            ValueError: If neither `dataset_id` nor `dataset` is provided.
        """
        if dataset is None and dataset_id is not None:
            dataset = load_dataset(dataset_id)
        else:
            raise ValueError("Either 'dataset_id' or 'dataset' must be provided to start evaluation.")
        
        test_texts, classes, true_labels = self.prepare_dataset(dataset, labels, max_examples=max_examples)
        
        predictions = self.__call__(test_texts, classes=classes, threshold=threshold)
        predicted_labels = [pred[0]['label'] for pred in predictions]

        return self.compute_f_score(predicted_labels, true_labels)
```

## File: gliner/multitask/question_answering.py

<a name='file-gliner-multitask-question_answering.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional, List, Union
import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"
import torch
from datasets import load_dataset, Dataset
from gliner import GLiNER

from .base import GLiNERBasePipeline

class GLiNERQuestionAnswerer(GLiNERBasePipeline):
    """
    A class to use GLiNER for question-answering inference and evaluation.

    Attributes:
        device (str): Device to run the model on, e.g., 'cuda:0' or 'cpu'.
        model (GLiNER): Loaded GLiNER model instance.
        prompt (str): Template prompt for text question-asnwering.

    Methods:
        process_predictions(predictions):
            Processes model predictions to extract the most likely labels.
        prepare_texts(texts, labels):
            Creates Q&A prompts for each input text.
        __call__(texts, labels, threshold=0.5):
            Runs the model on the given texts and returns predicted labels.
        evaluate(dataset_id, labels=None, threshold=0.5, max_examples=-1):
            Evaluates the model on a dataset and computes F1 scores.
    """

    prompt = "Answer the following question: {}"

    def __init__(self, model_id: str = None, model: GLiNER = None, device: str = 'cuda:0', prompt: Optional[str] = None):
        """
        Initializes the GLiNERQuestionAnswerer.

        Args:
            model_id (str, optional): Identifier for the model to be loaded. Defaults to None.
            model (GLiNER, optional): Preloaded GLiNER model. Defaults to None.
            device (str, optional): Device to run the model on ('cpu' or 'cuda:X'). Defaults to 'cuda:0'.
            prompt (str, optional): Template prompt for question-answering.
        """
        # Use the provided prompt or default to the class-level prompt
        prompt = prompt if prompt is not None else self.prompt
        super().__init__(model_id=model_id, model=model, prompt=prompt, device=device)


    def process_predictions(self, predictions, **kwargs):
        """
        Processes predictions to extract the highest-scoring answer(s).

        Args:
            predictions (list): List of predictions with scores.

        Returns:
            list: List of predicted labels for each input.
        """
        batch_predicted_labels = []

        for prediction in predictions:
            # Sort predictions by score in descending order
            sorted_predictions = sorted(prediction, key=lambda entity: entity["score"], reverse=True)

            predicted_labels = [{'answer': pred['text'], 'score': pred['score']} for pred in sorted_predictions]
            batch_predicted_labels.append(predicted_labels)

        return batch_predicted_labels

    def prepare_texts(self, texts: List[str], questions: Union[List[str], str], **kwargs):
        """
        Prepares prompts for question-answering by appending questions to texts.

        Args:
            texts (list): List of input texts.
            questions (list|str): Question or list of questions.

        Returns:
            list: List of formatted prompts.
        """
        prompts = []

        for id, text in enumerate(texts):
            if isinstance(questions, str):
                question = questions
            else:
                question = questions[0]
            prompt = f"{self.prompt.format(question)} \n {text}"
            prompts.append(prompt)
        return prompts

    def __call__(self, texts: Union[str, List[str]], questions: Union[str, List[str]], 
                                labels: List[str] = ['answer'], threshold: float = 0.5,
                                                            batch_size: int = 8, **kwargs):
        return super().__call__(texts, labels, threshold, batch_size, questions=questions)
    
    def evaluate(self, dataset_id: Optional[str] = None, dataset: Optional[Dataset] = None, 
                    labels: Optional[List[str]]=None, threshold: float =0.5, max_examples: float =-1):
        """
        Evaluates the model on a specified dataset and computes evaluation metrics.

        Args:
            dataset_id (str, optional): Identifier for the dataset to load (e.g., from Hugging Face datasets).
            dataset (Dataset, optional): A pre-loaded dataset to evaluate. If provided, `dataset_id` is ignored.
            labels (list, optional): List of target labels to consider for classification. Defaults to None (use all).
            threshold (float): Confidence threshold for predictions. Defaults to 0.5.
            max_examples (int): Maximum number of examples to evaluate. Defaults to -1 (use all available examples).

        Returns:
            dict: A dictionary containing evaluation metrics such as F1 scores.
        
        Raises:
            ValueError: If neither `dataset_id` nor `dataset` is provided.
        """
        raise NotImplementedError("Currently `evaluate` method is not implemented.")

class GLiNERSquadEvaluator(GLiNERQuestionAnswerer):
    def evaluate(self, dataset_id: str = 'rajpurkar/squad_v2', dataset: Optional[Dataset] = None, 
                    labels: Optional[List[str]] = ['answer'], threshold: float = 0.5, max_examples: int = -1):
        """
        Evaluates the model on a specified dataset and computes evaluation metrics.

        Args:
            dataset_id (str, optional): Identifier for the dataset to load (e.g., from Hugging Face datasets).
            dataset (Dataset, optional): A pre-loaded dataset to evaluate. If provided, `dataset_id` is ignored.
            labels (list, optional): List of target labels to consider for classification. Defaults to ['answer'].
            threshold (float): Confidence threshold for predictions. Defaults to 0.5.
            max_examples (int): Maximum number of examples to evaluate. Defaults to -1 (use all available examples).

        Returns:
            dict: A dictionary containing evaluation metrics such as F1 Scores.

        Raises:
            ValueError: If neither `dataset_id` nor `dataset` is provided.
        """
        from evaluate import load

        # Validate input
        if not dataset and not dataset_id:
            raise ValueError("Either `dataset` or `dataset_id` must be provided.")

        # Load the dataset if not provided
        if not dataset:
            dataset = load_dataset(dataset_id, split="validation")

        if not isinstance(dataset, Dataset):
            dataset = dataset['validation']

        # Truncate dataset if max_examples is specified
        if max_examples > 0:
            dataset = dataset.shuffle().select(range(min(len(dataset), max_examples)))

        # Load evaluation metric for SQuAD
        squad_metric = load("squad_v2" if "squad_v2" in dataset_id else "squad")

        # Prepare predictions and references
        contexts = dataset['context']
        questions = dataset['question']

        raw_predictions = self(contexts, questions, labels=labels, threshold=threshold)

        predictions = []
        references = []
        for id, prediction in enumerate(raw_predictions):
            example = dataset[id]

            if len(prediction):
                predicted_answer = prediction[0]["answer"]
                no_answer_probability=0.0
            else:
                predicted_answer = ""
                no_answer_probability=1.0

            # Append to predictions and references
            predictions.append({
                "id": example["id"],
                "prediction_text": predicted_answer,
                "no_answer_probability": no_answer_probability
            })

            references.append({
                "id": example["id"],
                "answers": {"text": example["answers"]["text"], "answer_start": example["answers"]["answer_start"]}
            })

        # Compute metrics
        results = squad_metric.compute(predictions=predictions, references=references)
        return results
```

## File: gliner/multitask/__init__.py

<a name='file-gliner-multitask-__init__.py'></a>
*Description*: This is a Python script.

```python
from .classification import GLiNERClassifier
from .question_answering import GLiNERQuestionAnswerer, GLiNERSquadEvaluator
from .open_extraction import GLiNEROpenExtractor
from .relation_extraction import GLiNERRelationExtractor, GLiNERDocREDEvaluator
from .summarization import GLiNERSummarizer
```

## File: gliner/multitask/base.py

<a name='file-gliner-multitask-base.py'></a>
*Description*: This is a Python script.

```python
from abc import ABC, abstractmethod
from typing import List, Union, Optional
import torch
import warnings

from ..model import GLiNER

class GLiNERBasePipeline(ABC):
    """
    Base class for GLiNER pipelines. Provides an interface for preparing texts,
    processing predictions, and evaluating the model.

    Args:
        model_id (str): Identifier for the model to be loaded.
        prompt (str, optional): Prompt template for text preparation. Defaults to None.
        device (str, optional): Device to run the model on ('cpu' or 'cuda:X'). Defaults to 'cuda:0'.

    Attributes:
        model (GLiNER): The loaded GLiNER model.
        device (str): The device being used for computation.
        prompt (str): The prompt template for text preparation.
    """

    def __init__(self, model_id: str = None, model: GLiNER = None, prompt=None, device='cuda:0'):
        """
        Initializes the GLiNERBasePipeline.

        Args:
            model_id (str): Identifier for the model to be loaded.
            prompt (str, optional): Prompt template for text preparation. Defaults to None.
            device (str, optional): Device to run the model on ('cpu' or 'cuda:X'). Defaults to 'cuda:0'.
        """
        if 'cuda' in device and not torch.cuda.is_available():
            warnings.warn(f"{device} is not available, setting device as 'cpu'.")
            device = 'cpu'
        self.device = device

        if model is not None:
            self.model = model.to(self.device)
        elif model_id is not None:
            self.model = GLiNER.from_pretrained(model_id).to(self.device)
        else:
            raise ValueError("Either 'model_id' or 'model' must be provided to initialize the pipeline.")
        
        self.prompt = prompt

    @abstractmethod
    def prepare_texts(self, texts: List[str], *args, **kwargs):
        """
        Prepares texts for input to the model.

        Args:
            texts (List[str]): List of input texts.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Any: The processed texts ready for model input.
        """
        pass

    @abstractmethod
    def process_predictions(self, predictions: List[dict]):
        """
        Processes model predictions into the desired format.

        Args:
            predictions (List[dict]): Raw predictions from the model.

        Returns:
            Any: Processed predictions in the desired format.
        """
        pass

    @abstractmethod
    def evaluate(self, dataset_id: str, labels: Optional[List[str]] = None, threshold: float = 0.5):
        """
        Evaluates the model on a given dataset.

        Args:
            dataset_id (str): Identifier for the evaluation dataset.
            labels (Optional[List[str]]): List of labels to evaluate. Defaults to None.
            threshold (float): Threshold for prediction confidence. Defaults to 0.5.

        Returns:
            Any: Evaluation results.
        """
        pass

    def __call__(self, texts: Union[str, List[str]], labels: List[str] = ['match'], 
                             threshold: float = 0.5, batch_size: int = 8, **kwargs):
        """
        Runs the model on the provided texts and returns processed results.

        Args:
            texts (Union[str, List[str]]): Single or list of input texts.
            labels (Optional[List[str]]): List of class labels for text preparation. Defaults to None.
            threshold (float): Threshold for prediction confidence. Defaults to 0.5.
            batch_size (int): Batch size for processing. Defaults to 8.

        Returns:
            Any: Processed results from the model.
        """
        if isinstance(texts, str):
            texts = [texts]
        
        prompts = self.prepare_texts(texts, **kwargs)

        predictions = self.model.run(prompts, labels, threshold=threshold, batch_size=batch_size)

        results = self.process_predictions(predictions, **kwargs)

        return results
```

## File: gliner/multitask/summarization.py

<a name='file-gliner-multitask-summarization.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional, List, Union
import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"
import torch
from datasets import load_dataset, Dataset
from gliner import GLiNER

from .base import GLiNERBasePipeline

class GLiNERSummarizer(GLiNERBasePipeline):
    """
    A class to use GLiNER for summarization inference and evaluation.

    Attributes:
        device (str): Device to run the model on, e.g., 'cuda:0' or 'cpu'.
        model (GLiNER): Loaded GLiNER model instance.
        prompt (str): Template prompt for text summarization.

    Methods:
        process_predictions(predictions):
            Processes model predictions to extract the most likely labels.
        prepare_texts(texts, labels):
            Creates summarization prompts for each input text.
        __call__(texts, labels, threshold=0.5):
            Runs the model on the given texts and returns predicted labels.
        evaluate(dataset_id, labels=None, threshold=0.5, max_examples=-1):
            Evaluates the model on a dataset and computes F1 scores.
    """

    prompt = "Summarize the following text highlighting the most important information:"

    def __init__(self, model_id: str = None, model: GLiNER = None, device: str = 'cuda:0', prompt: Optional[str] = None):
        """
        Initializes the GLiNERSummarizer.

        Args:
            model_id (str, optional): Identifier for the model to be loaded. Defaults to None.
            model (GLiNER, optional): Preloaded GLiNER model. Defaults to None.
            device (str, optional): Device to run the model on ('cpu' or 'cuda:X'). Defaults to 'cuda:0'.
            prompt (str, optional): Template prompt for summarization.
        """
        # Use the provided prompt or default to the class-level prompt
        prompt = prompt if prompt is not None else self.prompt
        super().__init__(model_id=model_id, model=model, prompt=prompt, device=device)


    def process_predictions(self, predictions, **kwargs):
        """
        Processes predictions to extract the highest-scoring text chunk(s).

        Args:
            predictions (list): List of predictions with scores.

        Returns:
            list: List of predicted labels for each input.
        """
        batch_predicted_labels = []

        for prediction in predictions:
            # Sort predictions by score in descending order
            sorted_predictions = sorted(prediction, key=lambda entity: entity["start"], reverse=False)

            extracted_text = [pred['text'] for pred in sorted_predictions]
            batch_predicted_labels.append(' '.join(extracted_text))

        return batch_predicted_labels

    def prepare_texts(self, texts: List[str], **kwargs):
        """
        Prepares prompts for summarization by appending prompt to texts.

        Args:
            texts (list): List of input texts.

        Returns:
            list: List of formatted prompts.
        """
        prompts = []

        for id, text in enumerate(texts):
            prompt = f"{self.prompt} \n {text}"
            prompts.append(prompt)
        return prompts

    def __call__(self, texts: Union[str, List[str]], labels: List[str] = ['summary'], 
                                    threshold: float = 0.25, batch_size: int = 8, **kwargs):
        return super().__call__(texts, labels, threshold, batch_size)
    
    def evaluate(self, dataset_id: Optional[str] = None, dataset: Optional[Dataset] = None, 
                    labels: Optional[List[str]]=None, threshold: float =0.5, max_examples: float =-1):
        """
        Evaluates the model on a specified dataset and computes evaluation metrics.

        Args:
            dataset_id (str, optional): Identifier for the dataset to load (e.g., from Hugging Face datasets).
            dataset (Dataset, optional): A pre-loaded dataset to evaluate. If provided, `dataset_id` is ignored.
            labels (list, optional): List of target labels to consider for summarization. Defaults to None (use all).
            threshold (float): Confidence threshold for predictions. Defaults to 0.5.
            max_examples (int): Maximum number of examples to evaluate. Defaults to -1 (use all available examples).

        Returns:
            dict: A dictionary containing evaluation metrics.
        
        Raises:
            ValueError: If neither `dataset_id` nor `dataset` is provided.
        """
        raise NotImplementedError("Currently `evaluate` method is not implemented.")
```

## File: gliner/multitask/relation_extraction.py

<a name='file-gliner-multitask-relation_extraction.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional, List, Union
import os
os.environ["TOKENIZERS_PARALLELISM"] = "true"
import torch
from datasets import load_dataset, Dataset
from gliner import GLiNER

from .base import GLiNERBasePipeline

class GLiNERRelationExtractor(GLiNERBasePipeline):
    """
    A class to use GLiNER for relation extraction inference and evaluation.

    Attributes:
        device (str): Device to run the model on, e.g., 'cuda:0' or 'cpu'.
        model (GLiNER): Loaded GLiNER model instance.
        prompt (str): Template prompt for relation extraction.

    Methods:
        process_predictions(predictions):
            Processes model predictions to extract the most likely labels.
        prepare_texts(texts, labels):
            Creates relation extraction prompts for each input text.
        __call__(texts, labels, threshold=0.5):
            Runs the model on the given texts and returns predicted labels.
        evaluate(dataset_id, labels=None, threshold=0.5, max_examples=-1):
            Evaluates the model on a dataset and computes F1 scores.
    """

    prompt = "Extract relationships between entities from the text: "

    def __init__(self, model_id: str = None, model: GLiNER = None, device: str = 'cuda:0', prompt: Optional[str] = None):
        """
        Initializes the GLiNERRelationExtractor.

        Args:
            model_id (str, optional): Identifier for the model to be loaded. Defaults to None.
            model (GLiNER, optional): Preloaded GLiNER model. Defaults to None.
            device (str, optional): Device to run the model on ('cpu' or 'cuda:X'). Defaults to 'cuda:0'.
            prompt (str, optional): Template prompt for question-answering.
        """
        # Use the provided prompt or default to the class-level prompt
        prompt = prompt if prompt is not None else self.prompt
        super().__init__(model_id=model_id, model=model, prompt=prompt, device=device)

    def prepare_texts(self, texts: List[str], **kwargs):
        """
        Prepares prompts for relation extraction to texts.

        Args:
            texts (list): List of input texts.

        Returns:
            list: List of formatted prompts.
        """
        prompts = []

        for id, text in enumerate(texts):
            prompt = f"{self.prompt} \n {text}"
            prompts.append(prompt)
        return prompts

    def prepare_source_relation(self, ner_predictions: List[dict], relations: List[str]):
        relation_labels = []
        for prediction in ner_predictions:
            curr_labels = []
            unique_entities = {ent['text'] for ent in prediction}
            for relation in relations:
                for ent in unique_entities:
                    curr_labels.append(f"{ent} <> {relation}")
            relation_labels.append(curr_labels)
        return relation_labels

    def process_predictions(self, predictions, **kwargs):
        """
        Processes predictions to extract the highest-scoring relation(s).

        Args:
            predictions (list): List of predictions with scores.

        Returns:
            list: List of predicted labels for each input.
        """
        batch_predicted_relations = []

        for prediction in predictions:
            # Sort predictions by score in descending order
            curr_relations = []

            for target in prediction:
                target_ent = target['text']
                score = target['score']
                source, relation = target['label'].split('<>')
                relation = {
                    "source": source.strip(),
                    "relation": relation.strip(),
                    "target": target_ent.strip(),
                    "score": score
                }
                curr_relations.append(relation)
            batch_predicted_relations.append(curr_relations)

        return batch_predicted_relations
    
    def __call__(self, texts: Union[str, List[str]], relations: List[str]=None, 
                                entities: List[str] = ['named entity'], 
                                relation_labels: Optional[List[List[str]]]=None, 
                                threshold: float = 0.5, batch_size: int = 8, **kwargs):
        if isinstance(texts, str):
            texts = [texts]
        
        prompts = self.prepare_texts(texts, **kwargs)

        if relation_labels is None:
            # ner
            ner_predictions = self.model.run(texts, entities, threshold=threshold, batch_size=batch_size)
            #rex
            relation_labels = self.prepare_source_relation(ner_predictions, relations)

        predictions = self.model.run(prompts, relation_labels, threshold=threshold, batch_size=batch_size)

        results = self.process_predictions(predictions, **kwargs)

        return results
    
    def evaluate(self, dataset_id: Optional[str] = None, dataset: Optional[Dataset] = None, 
                    labels: Optional[List[str]]=None, threshold: float =0.5, max_examples: float =-1):
        """
        Evaluates the model on a specified dataset and computes evaluation metrics.

        Args:
            dataset_id (str, optional): Identifier for the dataset to load (e.g., from Hugging Face datasets).
            dataset (Dataset, optional): A pre-loaded dataset to evaluate. If provided, `dataset_id` is ignored.
            labels (list, optional): List of target labels to consider for relation extraction. Defaults to None (use all).
            threshold (float): Confidence threshold for predictions. Defaults to 0.5.
            max_examples (int): Maximum number of examples to evaluate. Defaults to -1 (use all available examples).

        Returns:
            dict: A dictionary containing evaluation metrics such as F1 scores.
        
        Raises:
            ValueError: If neither `dataset_id` nor `dataset` is provided.
        """
        raise NotImplementedError("Currently `evaluate` method is not implemented.")

class GLiNERDocREDEvaluator(GLiNERRelationExtractor):
    """
    Evaluator class for document-level relation extraction tasks using the GLiNER framework.

    This class includes methods for preparing datasets, processing predictions, computing F1 scores,
    and evaluating the model's performance on document-level relation extraction tasks such as DocRED.
    """

    def prepare_dataset(self, raw_data: Dataset, text_column='sents', rel_column='labels', *args, **kwargs):
        """
        Prepares the dataset for evaluation by extracting labeled relations and corresponding text.

        Args:
            raw_data (Dataset): A list of raw dataset examples where each example contains sentences,
                            entity mentions, and relation annotations.
            text_column (str, optional): Column name in the dataset containing sentences. Defaults to 'sents'.
            rel_column (str, optional): Column name in the dataset containing relation labels. Defaults to 'labels'.

        Returns:
            tuple: A tuple containing:
                - texts_by_line (list of str): Flattened and concatenated text for each document.
                - grouped_labels (list of list of str): Grouped relation labels for each document.
                - true_labels (list of str): True relation labels in "source <> relation <> target" format.
        """
        grouped_labels = []
        true_labels = []
        texts_by_line = []

        for item in raw_data:

            vertex_set = item.get('vertexSet')
            sents = item.get(text_column, [])
            labels = item.get(rel_column, [])

            current_labels=[]

            for head_id, tail_id, relation in zip(labels['head'], labels['tail'], labels['relation_text']):
                current_index = 0
                head_data = None
                tail_data = None

                for sublist in vertex_set:
                      if current_index == head_id:
                          head_data = sublist
                      current_index += 1

                current_index = 0

                for sublist in vertex_set:
                      if current_index == tail_id:
                          tail_data = sublist
                      current_index += 1

                head_name = head_data[0]['name'] if head_data else None
                tail_name = tail_data[0]['name'] if tail_data else None

                true_labels.append(f'{head_name} <> {relation} <> {tail_name}')
                current_labels.append(f'{head_name} <> {relation}')

            grouped_labels.append(current_labels)
            result = " ".join(string for sublist in  sents for string in sublist)
            texts_by_line.append(result)

        return texts_by_line, grouped_labels, true_labels

    def process_results(self, predictions: List[dict]):
        """
        Processes model predictions into the standard "source <> relation <> target" format.

        Args:
            predictions (list of dict): List of prediction dictionaries containing 'source', 'relation', and 'target'.

        Returns:
            list of str: Processed predictions in "source <> relation <> target" format.
        """
        preds = []
        preds = []
        for predict in predictions:
            print(predict)
            for pred_ in predict:
                result = f"{pred_['source']} <> {pred_['relation']} <> {pred_['target']}"
                preds.append(result)
        return preds

    def compute_f_score(self, predicts: List[str], true_labels: List[str]):
        """
        Computes precision, recall, F1 score, and other metrics for the relation extraction task.

        Args:
            predicts (list of str): Predicted relation labels in "source <> relation <> target" format.
            true_labels (list of str): True relation labels in "source <> relation <> target" format.

        Returns:
            tuple: A tuple containing:
                - precision (float): Precision of predictions.
                - recall (float): Recall of predictions.
                - f1 (float): F1 score of predictions.
                - tp (int): Number of true positives.
                - fp (int): Number of false positives.
                - fn (int): Number of false negatives.
        """
        true_set = set(true_labels)
        pred_set = set(predicts)

        tp = len(true_set.intersection(pred_set))
        fp = len(pred_set - true_set)
        fn = len(true_set - pred_set)

        precision = tp / (tp + fp) if tp + fp > 0 else 0
        recall = tp / (tp + fn) if tp + fn > 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if precision + recall > 0 else 0

        return {'precision': precision, 'recall': recall, 'f1': f1, 
                    'true positives': tp, 'false positives': fp,  'false negatives': fn}

    def evaluate(self, dataset_id: str = 'thunlp/docred', dataset: Optional[Dataset] = None, 
                    labels: Optional[List[str]] = None, threshold: float = 0.5, max_examples: int = -1):

        """
        Evaluates the model on a specified dataset and computes evaluation metrics.

        Args:
            dataset_id (str, optional): Identifier for the dataset to load (e.g., from Hugging Face datasets).
            dataset (Dataset, optional): A pre-loaded dataset to evaluate. If provided, `dataset_id` is ignored.
            labels (list, optional): List of target relation labels to consider. Defaults to None (use all).
            threshold (float): Confidence threshold for predictions. Defaults to 0.5.
            max_examples (int): Maximum number of examples to evaluate. Defaults to -1 (use all available examples).

        Returns:
            tuple: Evaluation metrics including precision, recall, F1 score, true positives, false positives,
                   and false negatives.

        Raises:
            ValueError: If neither `dataset_id` nor `dataset` is provided.
        """

        if not dataset and not dataset_id:
            raise ValueError("Either `dataset` or `dataset_id` must be provided.")

        # Load the dataset if not provided
        if not dataset:
            dataset = load_dataset(dataset_id, split="validation")

        if not isinstance(dataset, Dataset):
            dataset = dataset['validation']

        if max_examples > 0:
            dataset = dataset.shuffle().select(range(min(len(dataset), max_examples)))

        test_texts, labels, true_labels = self.prepare_dataset(dataset)
        predictions = self(test_texts, relation_labels=labels)
        preds = self.process_results(predictions)
        return self.compute_f_score(preds, true_labels)
```

## File: gliner/decoding/decoder.py

<a name='file-gliner-decoding-decoder.py'></a>
*Description*: This is a Python script.

```python
from typing import Optional
from abc import ABC, abstractmethod
from functools import partial
import torch

from .utils import has_overlapping, has_overlapping_nested


class BaseDecoder(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def decode(self, *args, **kwargs):
        pass

    def greedy_search(self, spans, flat_ner=True, multi_label=False):
        if flat_ner:
            has_ov = partial(has_overlapping, multi_label=multi_label)
        else:
            has_ov = partial(has_overlapping_nested, multi_label=multi_label)

        new_list = []
        span_prob = sorted(spans, key=lambda x: -x[-1])

        for i in range(len(spans)):
            b = span_prob[i]
            flag = False
            for new in new_list:
                if has_ov(b[:-1], new):
                    flag = True
                    break
            if not flag:
                new_list.append(b)

        new_list = sorted(new_list, key=lambda x: x[0])
        return new_list


class SpanDecoder(BaseDecoder):
    def decode(self, tokens, id_to_classes, model_output, flat_ner=False, threshold=0.5, multi_label=False):
        probs = torch.sigmoid(model_output)
        spans = []
        for i, _ in enumerate(tokens):
            probs_i = probs[i]
            
            # Support for id_to_classes being a list of dictionaries
            id_to_class_i = id_to_classes[i] if isinstance(id_to_classes, list) else id_to_classes
            
            wh_i = [i.tolist() for i in torch.where(probs_i > threshold)]
            span_i = []
            for s, k, c in zip(*wh_i):
                if s + k < len(tokens[i]):
                    span_i.append((s, s + k, id_to_class_i[c + 1], probs_i[s, k, c].item()))

            span_i = self.greedy_search(span_i, flat_ner, multi_label=multi_label)
            spans.append(span_i)
        return spans


class TokenDecoder(BaseDecoder):
    def get_indices_above_threshold(self, scores, threshold):
        scores = torch.sigmoid(scores)
        return [k.tolist() for k in torch.where(scores > threshold)]

    def calculate_span_score(self, start_idx, end_idx, scores_inside_i, start_i, end_i, id_to_classes, threshold):
        span_i = []
        for st, cls_st in zip(*start_idx):
            for ed, cls_ed in zip(*end_idx):
                if ed >= st and cls_st == cls_ed:
                    ins = scores_inside_i[st:ed + 1, cls_st]
                    if (ins < threshold).any():
                        continue
                    spn_score = ins.mean().item()
                    span_i.append((st, ed, id_to_classes[cls_st + 1], spn_score))
        return span_i

    def decode(self, tokens, id_to_classes, model_output, flat_ner=False, threshold=0.5, multi_label=False):
        scores_start, scores_end, scores_inside = model_output
        spans = []
        for i, _ in enumerate(tokens):
            id_to_class_i = id_to_classes[i] if isinstance(id_to_classes, list) else id_to_classes
            span_scores = self.calculate_span_score(
                self.get_indices_above_threshold(scores_start[i], threshold),
                self.get_indices_above_threshold(scores_end[i], threshold),
                torch.sigmoid(scores_inside[i]),
                torch.sigmoid(scores_start[i]),
                torch.sigmoid(scores_end[i]),
                id_to_class_i,
                threshold
            )
            span_i = self.greedy_search(span_scores, flat_ner, multi_label)
            spans.append(span_i)
        return spans
```

## File: gliner/decoding/__init__.py

<a name='file-gliner-decoding-__init__.py'></a>
*Description*: This is a Python script.

```python
from .decoder import SpanDecoder, TokenDecoder
```

## File: gliner/decoding/utils.py

<a name='file-gliner-decoding-utils.py'></a>
*Description*: This is a Python script.

```python
def is_nested(idx1, idx2):
    # Return True if idx2 is nested inside idx1 or vice versa
    return (idx1[0] <= idx2[0] and idx1[1] >= idx2[1]) or (idx2[0] <= idx1[0] and idx2[1] >= idx1[1])

def has_overlapping(idx1, idx2, multi_label=False):
    # Check for any overlap between two spans
    if idx1[:2] == idx2[:2]:  # Exact same boundaries can be considered as overlapping
        return not multi_label
    if idx1[0] > idx2[1] or idx2[0] > idx1[1]:
        return False
    return True


def has_overlapping_nested(idx1, idx2, multi_label=False):
    # Return True if idx1 and idx2 overlap, but neither is nested inside the other
    if idx1[:2] == idx2[:2]:  # Exact same boundaries, not considering labels here
        return not multi_label
    if (idx1[0] > idx2[1] or idx2[0] > idx1[1]) or is_nested(idx1, idx2):
        return False
    return True

```

## File: tests/test_models.py

<a name='file-tests-test_models.py'></a>
*Description*: This is a Python script.

```python
from gliner import GLiNER


def test_span_model():
    model = GLiNER.from_pretrained("gliner-community/gliner_small-v2.5")

    text = """
    Cristiano Ronaldo dos Santos Aveiro (Portuguese pronunciation: [kɾiʃˈtjɐnu ʁɔˈnaldu]; born 5 February 1985) is a Portuguese professional footballer who plays as a forward for and captains both Saudi Pro League club Al Nassr and the Portugal national team. Widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon d'Or awards,[note 3] a record three UEFA Men's Player of the Year Awards, and four European Golden Shoes, the most by a European player. He has won 33 trophies in his career, including seven league titles, five UEFA Champions Leagues, the UEFA European Championship and the UEFA Nations League. Ronaldo holds the records for most appearances (183), goals (140) and assists (42) in the Champions League, goals in the European Championship (14), international goals (128) and international appearances (205). He is one of the few players to have made over 1,200 professional career appearances, the most by an outfield player, and has scored over 850 official senior career goals for club and country, making him the top goalscorer of all time.
    """

    labels = ["person", "award", "date", "competitions", "teams", "person"]

    entities = model.predict_entities(text, labels)

    assert len(entities) > 0

```

## File: tests/test_features_selection.py

<a name='file-tests-test_features_selection.py'></a>
*Description*: This is a Python script.

```python
import pytest
import torch
from transformers import AutoTokenizer
from gliner import GLiNERConfig
from gliner.modeling.base import extract_prompt_features_and_word_embeddings
from gliner.data_processing import SpanProcessor, WordsSplitter

class TestFeaturesExtractor:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.config = GLiNERConfig()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.model_name)
        self.config.class_token_index=len(self.tokenizer)
        self.tokenizer.add_tokens([self.config.ent_token, self.config.sep_token])
        self.splitter = WordsSplitter()
        self.base_tokens = [['Hello', 'world', '!']]
        self.tokens_with_missed = [['Hello', '', 'world', '']]
        self.labels = ['world']
        self.processor = SpanProcessor(self.config, self.tokenizer, self.splitter)

    def test_base_extraction(self):
        input_x = [{"tokenized_text": tk, "ner": None} for tk in self.base_tokens]
        raw_batch = self.processor.collate_raw_batch(input_x, self.labels)
        model_input = self.processor.collate_fn(raw_batch, prepare_labels=False)
        model_input['text_lengths'] = raw_batch['seq_length']
        token_embeds = torch.rand(model_input['words_mask'].shape + (self.config.hidden_size,))
        
        (prompts_embedding,
         prompts_embedding_mask,
         words_embedding,
         mask) = extract_prompt_features_and_word_embeddings(self.config, token_embeds, **model_input)
        
        assert prompts_embedding_mask.shape == (1, 1)
        assert prompts_embedding.shape == (1, 1, self.config.hidden_size)
        assert words_embedding.shape == (1, len(self.base_tokens[0]), self.config.hidden_size)
        
    def test_extraction_with_missed_tokens(self):
        input_x = [{"tokenized_text": tk, "ner": None} for tk in self.tokens_with_missed]
        raw_batch = self.processor.collate_raw_batch(input_x, self.labels)
        model_input = self.processor.collate_fn(raw_batch, prepare_labels=False)
        model_input['text_lengths'] = raw_batch['seq_length']
        token_embeds = torch.rand(model_input['words_mask'].shape + (self.config.hidden_size,))
        
        (prompts_embedding,
         prompts_embedding_mask,
         words_embedding,
         mask) = extract_prompt_features_and_word_embeddings(self.config, token_embeds, **model_input)
        
        assert prompts_embedding_mask.shape == (1, 1)
        assert prompts_embedding.shape == (1, 1, self.config.hidden_size)
        assert words_embedding.shape == (1, len(self.tokens_with_missed[0]), self.config.hidden_size)
        

```

