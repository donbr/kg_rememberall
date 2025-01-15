# Combined Context for LLM

Source Directory: ../data/raw/smolagents
Generated On: 2025-01-14 14:59:11

## Directory Summary

* .Dockerfile: 1 files
* .toml: 2 files
* .md: 28 files
* No extension: 3 files
* .json: 2 files
* .yaml: 1 files
* .py: 34 files
* .yml: 2 files
* .png: 1 files

## Table of Contents

* [e2b.Dockerfile](#file-e2b.Dockerfile)
* [pyproject.toml](#file-pyproject.toml)
* [README.md](#file-README.md)
* [Makefile](#file-Makefile)
* [LICENSE](#file-LICENSE)
* [package-lock.json](#file-package-lock.json)
* [CONTRIBUTING.md](#file-CONTRIBUTING.md)
* [CODE_OF_CONDUCT.md](#file-CODE_OF_CONDUCT.md)
* [e2b.toml](#file-e2b.toml)
* [Dockerfile](#file-Dockerfile)
* [package.json](#file-package.json)
* [.pre-commit-config.yaml](#file-.pre-commit-config.yaml)
* [src/smolagents/prompts.py](#file-src-smolagents-prompts.py)
* [src/smolagents/__init__.py](#file-src-smolagents-__init__.py)
* [src/smolagents/agents.py](#file-src-smolagents-agents.py)
* [src/smolagents/default_tools.py](#file-src-smolagents-default_tools.py)
* [src/smolagents/utils.py](#file-src-smolagents-utils.py)
* [src/smolagents/types.py](#file-src-smolagents-types.py)
* [src/smolagents/local_python_executor.py](#file-src-smolagents-local_python_executor.py)
* [src/smolagents/tools.py](#file-src-smolagents-tools.py)
* [src/smolagents/e2b_executor.py](#file-src-smolagents-e2b_executor.py)
* [src/smolagents/tool_validation.py](#file-src-smolagents-tool_validation.py)
* [src/smolagents/models.py](#file-src-smolagents-models.py)
* [src/smolagents/monitoring.py](#file-src-smolagents-monitoring.py)
* [src/smolagents/gradio_ui.py](#file-src-smolagents-gradio_ui.py)
* [examples/tool_calling_agent_ollama.py](#file-examples-tool_calling_agent_ollama.py)
* [examples/benchmark.py](#file-examples-benchmark.py)
* [examples/e2b_example.py](#file-examples-e2b_example.py)
* [examples/gradio_upload.py](#file-examples-gradio_upload.py)
* [examples/text_to_sql.py](#file-examples-text_to_sql.py)
* [examples/rag.py](#file-examples-rag.py)
* [examples/tool_calling_agent_from_any_llm.py](#file-examples-tool_calling_agent_from_any_llm.py)
* [docs/README.md](#file-docs-README.md)
* [docs/source/en/_config.py](#file-docs-source-en-_config.py)
* [docs/source/en/guided_tour.md](#file-docs-source-en-guided_tour.md)
* [docs/source/en/_toctree.yml](#file-docs-source-en-_toctree.yml)
* [docs/source/en/index.md](#file-docs-source-en-index.md)
* [docs/source/en/reference/tools.md](#file-docs-source-en-reference-tools.md)
* [docs/source/en/reference/agents.md](#file-docs-source-en-reference-agents.md)
* [docs/source/en/conceptual_guides/react.md](#file-docs-source-en-conceptual_guides-react.md)
* [docs/source/en/conceptual_guides/intro_agents.md](#file-docs-source-en-conceptual_guides-intro_agents.md)
* [docs/source/en/examples/text_to_sql.md](#file-docs-source-en-examples-text_to_sql.md)
* [docs/source/en/examples/multiagents.md](#file-docs-source-en-examples-multiagents.md)
* [docs/source/en/examples/rag.md](#file-docs-source-en-examples-rag.md)
* [docs/source/en/tutorials/secure_code_execution.md](#file-docs-source-en-tutorials-secure_code_execution.md)
* [docs/source/en/tutorials/tools.md](#file-docs-source-en-tutorials-tools.md)
* [docs/source/en/tutorials/building_good_agents.md](#file-docs-source-en-tutorials-building_good_agents.md)
* [docs/source/zh/_config.py](#file-docs-source-zh-_config.py)
* [docs/source/zh/guided_tour.md](#file-docs-source-zh-guided_tour.md)
* [docs/source/zh/_toctree.yml](#file-docs-source-zh-_toctree.yml)
* [docs/source/zh/index.md](#file-docs-source-zh-index.md)
* [docs/source/zh/reference/tools.md](#file-docs-source-zh-reference-tools.md)
* [docs/source/zh/reference/agents.md](#file-docs-source-zh-reference-agents.md)
* [docs/source/zh/conceptual_guides/react.md](#file-docs-source-zh-conceptual_guides-react.md)
* [docs/source/zh/conceptual_guides/intro_agents.md](#file-docs-source-zh-conceptual_guides-intro_agents.md)
* [docs/source/zh/examples/text_to_sql.md](#file-docs-source-zh-examples-text_to_sql.md)
* [docs/source/zh/examples/multiagents.md](#file-docs-source-zh-examples-multiagents.md)
* [docs/source/zh/examples/rag.md](#file-docs-source-zh-examples-rag.md)
* [docs/source/zh/tutorials/secure_code_execution.md](#file-docs-source-zh-tutorials-secure_code_execution.md)
* [docs/source/zh/tutorials/tools.md](#file-docs-source-zh-tutorials-tools.md)
* [docs/source/zh/tutorials/building_good_agents.md](#file-docs-source-zh-tutorials-building_good_agents.md)
* [tests/__init__.py](#file-tests-__init__.py)
* [tests/test_python_interpreter.py](#file-tests-test_python_interpreter.py)
* [tests/test_tools.py](#file-tests-test_tools.py)
* [tests/test_all_docs.py](#file-tests-test_all_docs.py)
* [tests/test_final_answer.py](#file-tests-test_final_answer.py)
* [tests/test_monitoring.py](#file-tests-test_monitoring.py)
* [tests/test_utils.py](#file-tests-test_utils.py)
* [tests/test_agents.py](#file-tests-test_agents.py)
* [tests/test_default_tools.py](#file-tests-test_default_tools.py)
* [tests/test_types.py](#file-tests-test_types.py)
* [tests/test_models.py](#file-tests-test_models.py)
* [tests/test_search.py](#file-tests-test_search.py)
* [tests/fixtures/000000039769.png](#file-tests-fixtures-000000039769.png)

## File: e2b.Dockerfile

<a name='file-e2b.Dockerfile'></a>
*Description*: No specific description available.

```plaintext
# You can use most Debian-based base images
FROM e2bdev/code-interpreter:latest 

# Install dependencies and customize sandbox
RUN pip install git+https://github.com/huggingface/smolagents.git
```

## File: pyproject.toml

<a name='file-pyproject.toml'></a>
*Description*: No specific description available.

```plaintext
[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"

[project]
name = "smolagents"
version = "1.3.0.dev"
description = "🤗 smolagents: a barebones library for agents. Agents write python code to call tools or orchestrate other agents."
authors = [
  { name="Aymeric Roucher", email="aymeric@hf.co" }, { name="Thomas Wolf"},
]
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
  "transformers>=4.0.0",
  "requests>=2.32.3",
  "rich>=13.9.4",
  "pandas>=2.2.3",
  "jinja2>=3.1.4",
  "pillow>=11.0.0",
  "markdownify>=0.14.1",
  "gradio>=5.8.0",
  "duckduckgo-search>=6.3.7",
  "python-dotenv>=1.0.1",
  "e2b-code-interpreter>=1.0.3",
  "openai>=1.58.1",
]

[tool.ruff]
lint.ignore = ["F403"]

[project.optional-dependencies]
dev = [
  "torch",
  "torchaudio",
  "torchvision",
  "sqlalchemy",
  "accelerate",
  "soundfile",
  "litellm>=1.55.10",
]
test = [
  "torch",
  "torchaudio",
  "torchvision",
  "pytest>=8.1.0",
  "sqlalchemy",
  "ruff>=0.5.0",
  "accelerate",
  "soundfile",
  "litellm>=1.55.10",
]

```

## File: README.md

<a name='file-README.md'></a>
*Description*: No specific description available.

```plaintext
<!---
Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->
<p align="center">
    <!-- Uncomment when CircleCI is set up
    <a href="https://circleci.com/gh/huggingface/accelerate"><img alt="Build" src="https://img.shields.io/circleci/build/github/huggingface/transformers/master"></a>
    -->
    <a href="https://github.com/huggingface/smolagents/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/huggingface/smolagents.svg?color=blue"></a>
    <a href="https://huggingface.co/docs/smolagents"><img alt="Documentation" src="https://img.shields.io/website/http/huggingface.co/docs/smolagents/index.html.svg?down_color=red&down_message=offline&up_message=online"></a>
    <a href="https://github.com/huggingface/smolagents/releases"><img alt="GitHub release" src="https://img.shields.io/github/release/huggingface/smolagents.svg"></a>
    <a href="https://github.com/huggingface/smolagents/blob/main/CODE_OF_CONDUCT.md"><img alt="Contributor Covenant" src="https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg"></a>
</p>

<h3 align="center">
  <p>🤗 smolagents - a smol library to build great agents!</p>
</h3>

`smolagents` is a library that enables you to run powerful agents in a few lines of code. It offers:

✨ **Simplicity**: the logic for agents fits in ~thousand lines of code (see [agents.py](https://github.com/huggingface/smolagents/blob/main/src/smolagents/agents.py)). We kept abstractions to their minimal shape above raw code!

🧑‍💻 **First-class support for Code Agents**, i.e. agents that write their actions in code (as opposed to "agents being used to write code"). To make it secure, we support executing in sandboxed environments via [E2B](https://e2b.dev/).
 - On top of this [`CodeAgent`](https://huggingface.co/docs/smolagents/reference/agents#smolagents.CodeAgent) class, we still support the standard [`ToolCallingAgent`](https://huggingface.co/docs/smolagents/reference/agents#smolagents.ToolCallingAgent) that writes actions as JSON/text blobs.

🤗 **Hub integrations**: you can share and load tools to/from the Hub, and more is to come!

🌐 **Support for any LLM**: it supports models hosted on the Hub loaded in their `transformers` version or through our inference API, but also supports models from OpenAI, Anthropic and many others via our [LiteLLM](https://www.litellm.ai/) integration.

Full documentation can be found [here](https://huggingface.co/docs/smolagents/index).

> [!NOTE]  
> Check the our [launch blog post](https://huggingface.co/blog/smolagents) to learn more about `smolagents`!

## Quick demo

First install the package.
```bash
pip install smolagents
```
Then define your agent, give it the tools it needs and run it!
```py
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=HfApiModel())

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
```

https://github.com/user-attachments/assets/cd0226e2-7479-4102-aea0-57c22ca47884

## Code agents?

In our `CodeAgent`,  the LLM engine writes its actions in code. This approach is demonstrated to work better than the current industry practice of letting the LLM output a dictionary of the tools it wants to calls: [uses 30% fewer steps](https://huggingface.co/papers/2402.01030) (thus 30% fewer LLM calls)
and [reaches higher performance on difficult benchmarks](https://huggingface.co/papers/2411.01747). Head to [our high-level intro to agents](https://huggingface.co/docs/smolagents/conceptual_guides/intro_agents) to learn more on that.

Especially, since code execution can be a security concern (arbitrary code execution!), we provide options at runtime:
  - a secure python interpreter to run code more safely in your environment
  - a sandboxed environment using [E2B](https://e2b.dev/).

## How smol is it really?

We strived to keep abstractions to a strict minimum: the main code in `agents.py` is only ~1,000 lines of code.
Still, we implement several types of agents: `CodeAgent` writes its actions as Python code snippets, and the more classic `ToolCallingAgent` leverages built-in tool calling methods.

By the way, why use a framework at all? Well, because a big part of this stuff is non-trivial. For instance, the code agent has to keep a consistent format for code throughout its system prompt, its parser, the execution. So our framework handles this complexity for you. But of course we still encourage you to hack into the source code and use only the bits that you need, to the exclusion of everything else!

## How strong are open models for agentic workflows?

We've created [`CodeAgent`](https://huggingface.co/docs/smolagents/reference/agents#smolagents.CodeAgent) instances with some leading models, and compared them on [this benchmark](https://huggingface.co/datasets/m-ric/agents_medium_benchmark_2) that gathers questions from a few different benchmarks to propose a varied blend of challenges.

[Find the benchmarking code here](https://github.com/huggingface/smolagents/blob/main/examples/benchmark.ipynb) for more detail on the agentic setup used, and see a comparison of using LLMs code agents compared to vanilla (spoilers: code agents works better).

<p align="center">
    <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/smolagents/benchmark_code_agents.png" alt="benchmark of different models on agentic workflows" width=70%>
</p>

This comparison shows that open source models can now take on the best closed models!

## Citing smolagents

If you use `smolagents` in your publication, please cite it by using the following BibTeX entry.

```bibtex
@Misc{smolagents,
  title =        {`smolagents`: The easiest way to build efficient agentic systems.},
  author =       {Aymeric Roucher and Thomas Wolf and Leandro von Werra and Erik Kaunismäki},
  howpublished = {\url{https://github.com/huggingface/smolagents}},
  year =         {2025}
}
```

```

## File: Makefile

<a name='file-Makefile'></a>
*Description*: No specific description available.

```plaintext
.PHONY: quality style test docs utils

check_dirs := .

# Check that source code meets quality standards

extra_quality_checks:
	python utils/check_copies.py
	python utils/check_dummies.py
	python utils/check_repo.py
	doc-builder style smolagents docs/source --max_len 119

# this target runs checks on all files
quality:
	ruff check $(check_dirs)
	ruff format --check $(check_dirs)
	doc-builder style smolagents docs/source --max_len 119 --check_only

# Format source code automatically and check is there are any problems left that need manual fixing
style:
	ruff check $(check_dirs) --fix
	ruff format $(check_dirs)
	doc-builder style smolagents docs/source --max_len 119
	
# Run tests for the library
test_big_modeling:
	python -m pytest -s -v ./tests/test_big_modeling.py ./tests/test_modeling_utils.py $(if $(IS_GITHUB_CI),--report-log "$(PYTORCH_VERSION)_big_modeling.log",)

test_core:
	python -m pytest -s -v ./tests/ --ignore=./tests/test_examples.py $(if $(IS_GITHUB_CI),--report-log "$(PYTORCH_VERSION)_core.log",)

test_cli:
	python -m pytest -s -v ./tests/test_cli.py $(if $(IS_GITHUB_CI),--report-log "$(PYTORCH_VERSION)_cli.log",)


# Since the new version of pytest will *change* how things are collected, we need `deepspeed` to 
# run after test_core and test_cli
test:
	$(MAKE) test_core
	$(MAKE) test_cli
	$(MAKE) test_big_modeling
	$(MAKE) test_deepspeed
	$(MAKE) test_fsdp

test_examples:
	python -m pytest -s -v ./tests/test_examples.py $(if $(IS_GITHUB_CI),--report-log "$(PYTORCH_VERSION)_examples.log",)

# Same as test but used to install only the base dependencies
test_prod:
	$(MAKE) test_core

test_rest:
	python -m pytest -s -v ./tests/test_examples.py::FeatureExamplesTests $(if $(IS_GITHUB_CI),--report-log "$(PYTORCH_VERSION)_rest.log",)

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

## File: package-lock.json

<a name='file-package-lock.json'></a>
*Description*: This JSON file contains structured data.

```json
{
  "name": "smolagents",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "dependencies": {
        "@e2b/cli": "^1.0.9"
      }
    },
    "node_modules/@bufbuild/protobuf": {
      "version": "2.2.3",
      "resolved": "https://registry.npmjs.org/@bufbuild/protobuf/-/protobuf-2.2.3.tgz",
      "integrity": "sha512-tFQoXHJdkEOSwj5tRIZSPNUuXK3RaR7T1nUrPgbYX1pUbvqqaaZAsfo+NXBPsz5rZMSKVFrgK1WL8Q/MSLvprg==",
      "license": "(Apache-2.0 AND BSD-3-Clause)"
    },
    "node_modules/@connectrpc/connect": {
      "version": "2.0.0-rc.3",
      "resolved": "https://registry.npmjs.org/@connectrpc/connect/-/connect-2.0.0-rc.3.tgz",
      "integrity": "sha512-ARBt64yEyKbanyRETTjcjJuHr2YXorzQo0etyS5+P6oSeW8xEuzajA9g+zDnMcj1hlX2dQE93foIWQGfpru7gQ==",
      "license": "Apache-2.0",
      "peerDependencies": {
        "@bufbuild/protobuf": "^2.2.0"
      }
    },
    "node_modules/@connectrpc/connect-web": {
      "version": "2.0.0-rc.3",
      "resolved": "https://registry.npmjs.org/@connectrpc/connect-web/-/connect-web-2.0.0-rc.3.tgz",
      "integrity": "sha512-w88P8Lsn5CCsA7MFRl2e6oLY4J/5toiNtJns/YJrlyQaWOy3RO8pDgkz+iIkG98RPMhj2thuBvsd3Cn4DKKCkw==",
      "license": "Apache-2.0",
      "peerDependencies": {
        "@bufbuild/protobuf": "^2.2.0",
        "@connectrpc/connect": "2.0.0-rc.3"
      }
    },
    "node_modules/@e2b/cli": {
      "version": "1.0.9",
      "resolved": "https://registry.npmjs.org/@e2b/cli/-/cli-1.0.9.tgz",
      "integrity": "sha512-TNxW0O/y8GqfDfPGS2tC4jtHUcP6IHAKUxT5fc2y0KWhiJ3Za8Xrn4ZehfkDrvGd5ImjsXkvABHs1RJeioEGjQ==",
      "license": "MIT",
      "dependencies": {
        "@iarna/toml": "^2.2.5",
        "async-listen": "^3.0.1",
        "boxen": "^7.1.1",
        "chalk": "^5.3.0",
        "cli-highlight": "^2.1.11",
        "command-exists": "^1.2.9",
        "commander": "^11.1.0",
        "console-table-printer": "^2.11.2",
        "e2b": "^1.0.1",
        "inquirer": "^9.2.12",
        "open": "^9.1.0",
        "strip-ansi": "^7.1.0",
        "update-notifier": "5.1.0",
        "yup": "^1.3.2"
      },
      "bin": {
        "e2b": "dist/index.js"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@iarna/toml": {
      "version": "2.2.5",
      "resolved": "https://registry.npmjs.org/@iarna/toml/-/toml-2.2.5.tgz",
      "integrity": "sha512-trnsAYxU3xnS1gPHPyU961coFyLkh4gAD/0zQ5mymY4yOZ+CYvsPqUbOFSw0aDM4y0tV7tiFxL/1XfXPNC6IPg==",
      "license": "ISC"
    },
    "node_modules/@inquirer/figures": {
      "version": "1.0.8",
      "resolved": "https://registry.npmjs.org/@inquirer/figures/-/figures-1.0.8.tgz",
      "integrity": "sha512-tKd+jsmhq21AP1LhexC0pPwsCxEhGgAkg28byjJAd+xhmIs8LUX8JbUc3vBf3PhLxWiB5EvyBE5X7JSPAqMAqg==",
      "license": "MIT",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@sindresorhus/is": {
      "version": "0.14.0",
      "resolved": "https://registry.npmjs.org/@sindresorhus/is/-/is-0.14.0.tgz",
      "integrity": "sha512-9NET910DNaIPngYnLLPeg+Ogzqsi9uM4mSboU5y6p8S5DzMTVEsJZrawi+BoDNUVBa2DhJqQYUFvMDfgU062LQ==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/@szmarczak/http-timer": {
      "version": "1.1.2",
      "resolved": "https://registry.npmjs.org/@szmarczak/http-timer/-/http-timer-1.1.2.tgz",
      "integrity": "sha512-XIB2XbzHTN6ieIjfIMV9hlVcfPU26s2vafYWQcZHWXHOxiaRZYEDKEwdl129Zyg50+foYV2jCgtrqSA6qNuNSA==",
      "license": "MIT",
      "dependencies": {
        "defer-to-connect": "^1.0.1"
      },
      "engines": {
        "node": ">=6"
      }
    },
    "node_modules/ansi-align": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/ansi-align/-/ansi-align-3.0.1.tgz",
      "integrity": "sha512-IOfwwBF5iczOjp/WeY4YxyjqAFMQoZufdQWDd19SEExbVLNXqvpzSJ/M7Za4/sCPmQ0+GRquoA7bGcINcxew6w==",
      "license": "ISC",
      "dependencies": {
        "string-width": "^4.1.0"
      }
    },
    "node_modules/ansi-align/node_modules/ansi-regex": {
      "version": "5.0.1",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
      "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-align/node_modules/emoji-regex": {
      "version": "8.0.0",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
      "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
      "license": "MIT"
    },
    "node_modules/ansi-align/node_modules/string-width": {
      "version": "4.2.3",
      "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
      "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
      "license": "MIT",
      "dependencies": {
        "emoji-regex": "^8.0.0",
        "is-fullwidth-code-point": "^3.0.0",
        "strip-ansi": "^6.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-align/node_modules/strip-ansi": {
      "version": "6.0.1",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
      "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/ansi-escapes": {
      "version": "4.3.2",
      "resolved": "https://registry.npmjs.org/ansi-escapes/-/ansi-escapes-4.3.2.tgz",
      "integrity": "sha512-gKXj5ALrKWQLsYG9jlTRmR/xKluxHV+Z9QEwNIgCfM1/uwPMCuzVVnh5mwTd+OuBZcwSIMbqssNWRm1lE51QaQ==",
      "license": "MIT",
      "dependencies": {
        "type-fest": "^0.21.3"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/ansi-escapes/node_modules/type-fest": {
      "version": "0.21.3",
      "resolved": "https://registry.npmjs.org/type-fest/-/type-fest-0.21.3.tgz",
      "integrity": "sha512-t0rzBq87m3fVcduHDUFhKmyyX+9eo6WQjZvf51Ea/M0Q7+T374Jp1aUiyUl0GKxp8M/OETVHSDvmkyPgvX+X2w==",
      "license": "(MIT OR CC0-1.0)",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/ansi-regex": {
      "version": "6.1.0",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.1.0.tgz",
      "integrity": "sha512-7HSX4QQb4CspciLpVFwyRe79O3xsIZDDLER21kERQ71oaPodF8jL725AgJMFAYbooIqolJoRLuM81SpeUkpkvA==",
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-regex?sponsor=1"
      }
    },
    "node_modules/ansi-styles": {
      "version": "6.2.1",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-6.2.1.tgz",
      "integrity": "sha512-bN798gFfQX+viw3R7yrGWRqnrN2oRkEkUjjl4JNn4E8GxxbjtG3FbrEIIY3l8/hrwUwIeCZvi4QuOTP4MErVug==",
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/any-promise": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/any-promise/-/any-promise-1.3.0.tgz",
      "integrity": "sha512-7UvmKalWRt1wgjL1RrGxoSJW/0QZFIegpeGvZG9kjp8vrRu55XTHbwnqq2GpXm9uLbcuhxm3IqX9OB4MZR1b2A==",
      "license": "MIT"
    },
    "node_modules/async-listen": {
      "version": "3.0.1",
      "resolved": "https://registry.npmjs.org/async-listen/-/async-listen-3.0.1.tgz",
      "integrity": "sha512-cWMaNwUJnf37C/S5TfCkk/15MwbPRwVYALA2jtjkbHjCmAPiDXyNJy2q3p1KAZzDLHAWyarUWSujUoHR4pEgrA==",
      "license": "MIT",
      "engines": {
        "node": ">= 14"
      }
    },
    "node_modules/base64-js": {
      "version": "1.5.1",
      "resolved": "https://registry.npmjs.org/base64-js/-/base64-js-1.5.1.tgz",
      "integrity": "sha512-AKpaYlHn8t4SVbOHCy+b5+KKgvR4vrsD8vbvrbiQJps7fKDTkjkDry6ji0rUJjC0kzbNePLwzxq8iypo41qeWA==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT"
    },
    "node_modules/big-integer": {
      "version": "1.6.52",
      "resolved": "https://registry.npmjs.org/big-integer/-/big-integer-1.6.52.tgz",
      "integrity": "sha512-QxD8cf2eVqJOOz63z6JIN9BzvVs/dlySa5HGSBH5xtR8dPteIRQnBxxKqkNTiT6jbDTF6jAfrd4oMcND9RGbQg==",
      "license": "Unlicense",
      "engines": {
        "node": ">=0.6"
      }
    },
    "node_modules/bl": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/bl/-/bl-4.1.0.tgz",
      "integrity": "sha512-1W07cM9gS6DcLperZfFSj+bWLtaPGSOHWhPiGzXmvVJbRLdG82sH/Kn8EtW1VqWVA54AKf2h5k5BbnIbwF3h6w==",
      "license": "MIT",
      "dependencies": {
        "buffer": "^5.5.0",
        "inherits": "^2.0.4",
        "readable-stream": "^3.4.0"
      }
    },
    "node_modules/boxen": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/boxen/-/boxen-7.1.1.tgz",
      "integrity": "sha512-2hCgjEmP8YLWQ130n2FerGv7rYpfBmnmp9Uy2Le1vge6X3gZIfSmEzP5QTDElFxcvVcXlEn8Aq6MU/PZygIOog==",
      "license": "MIT",
      "dependencies": {
        "ansi-align": "^3.0.1",
        "camelcase": "^7.0.1",
        "chalk": "^5.2.0",
        "cli-boxes": "^3.0.0",
        "string-width": "^5.1.2",
        "type-fest": "^2.13.0",
        "widest-line": "^4.0.1",
        "wrap-ansi": "^8.1.0"
      },
      "engines": {
        "node": ">=14.16"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/bplist-parser": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/bplist-parser/-/bplist-parser-0.2.0.tgz",
      "integrity": "sha512-z0M+byMThzQmD9NILRniCUXYsYpjwnlO8N5uCFaCqIOpqRsJCrQL9NK3JsD67CN5a08nF5oIL2bD6loTdHOuKw==",
      "license": "MIT",
      "dependencies": {
        "big-integer": "^1.6.44"
      },
      "engines": {
        "node": ">= 5.10.0"
      }
    },
    "node_modules/buffer": {
      "version": "5.7.1",
      "resolved": "https://registry.npmjs.org/buffer/-/buffer-5.7.1.tgz",
      "integrity": "sha512-EHcyIPBQ4BSGlvjB16k5KgAJ27CIsHY/2JBmCRReo48y9rQ3MaUzWX3KVlBa4U7MyX02HdVj0K7C3WaB3ju7FQ==",
      "funding": [
        {
          "type": "github",
          "url": "https://github.com/sponsors/feross"
        },
        {
          "type": "patreon",
          "url": "https://www.patreon.com/feross"
        },
        {
          "type": "consulting",
          "url": "https://feross.org/support"
        }
      ],
      "license": "MIT",
      "dependencies": {
        "base64-js": "^1.3.1",
        "ieee754": "^1.1.13"
      }
    },
    "node_modules/bundle-name": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/bundle-name/-/bundle-name-3.0.0.tgz",
      "integrity": "sha512-PKA4BeSvBpQKQ8iPOGCSiell+N8P+Tf1DlwqmYhpe2gAhKPHn8EYOxVT+ShuGmhg8lN8XiSlS80yiExKXrURlw==",
      "license": "MIT",
      "dependencies": {
        "run-applescript": "^5.0.0"
      },
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/cacheable-request": {
      "version": "6.1.0",
      "resolved": "https://registry.npmjs.org/cacheable-request/-/cacheable-request-6.1.0.tgz",
      "integrity": "sha512-Oj3cAGPCqOZX7Rz64Uny2GYAZNliQSqfbePrgAQ1wKAihYmCUnraBtJtKcGR4xz7wF+LoJC+ssFZvv5BgF9Igg==",
      "license": "MIT",
      "dependencies": {
        "clone-response": "^1.0.2",
        "get-stream": "^5.1.0",
        "http-cache-semantics": "^4.0.0",
        "keyv": "^3.0.0",
        "lowercase-keys": "^2.0.0",
        "normalize-url": "^4.1.0",
        "responselike": "^1.0.2"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/cacheable-request/node_modules/get-stream": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/get-stream/-/get-stream-5.2.0.tgz",
      "integrity": "sha512-nBF+F1rAZVCu/p7rjzgA+Yb4lfYXrpl7a6VmJrU8wF9I1CKvP/QwPNZHnOlwbTkY6dvtFIzFMSyQXbLoTQPRpA==",
      "license": "MIT",
      "dependencies": {
        "pump": "^3.0.0"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/cacheable-request/node_modules/lowercase-keys": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/lowercase-keys/-/lowercase-keys-2.0.0.tgz",
      "integrity": "sha512-tqNXrS78oMOE73NMxK4EMLQsQowWf8jKooH9g7xPavRT706R6bkQJ6DY2Te7QukaZsulxa30wQ7bk0pm4XiHmA==",
      "license": "MIT",
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/camelcase": {
      "version": "7.0.1",
      "resolved": "https://registry.npmjs.org/camelcase/-/camelcase-7.0.1.tgz",
      "integrity": "sha512-xlx1yCK2Oc1APsPXDL2LdlNP6+uu8OCDdhOBSVT279M/S+y75O30C2VuD8T2ogdePBBl7PfPF4504tnLgX3zfw==",
      "license": "MIT",
      "engines": {
        "node": ">=14.16"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/chalk": {
      "version": "5.4.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-5.4.0.tgz",
      "integrity": "sha512-ZkD35Mx92acjB2yNJgziGqT9oKHEOxjTBTDRpOsRWtdecL/0jM3z5kM/CTzHWvHIen1GvkM85p6TuFfDGfc8/Q==",
      "license": "MIT",
      "engines": {
        "node": "^12.17.0 || ^14.13 || >=16.0.0"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/chardet": {
      "version": "0.7.0",
      "resolved": "https://registry.npmjs.org/chardet/-/chardet-0.7.0.tgz",
      "integrity": "sha512-mT8iDcrh03qDGRRmoA2hmBJnxpllMR+0/0qlzjqZES6NdiWDcZkCNAk4rPFZ9Q85r27unkiNNg8ZOiwZXBHwcA==",
      "license": "MIT"
    },
    "node_modules/ci-info": {
      "version": "2.0.0",
      "resolved": "https://registry.npmjs.org/ci-info/-/ci-info-2.0.0.tgz",
      "integrity": "sha512-5tK7EtrZ0N+OLFMthtqOj4fI2Jeb88C4CAZPu25LDVUgXJ0A3Js4PMGqrn0JU1W0Mh1/Z8wZzYPxqUrXeBboCQ==",
      "license": "MIT"
    },
    "node_modules/cli-boxes": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/cli-boxes/-/cli-boxes-3.0.0.tgz",
      "integrity": "sha512-/lzGpEWL/8PfI0BmBOPRwp0c/wFNX1RdUML3jK/RcSBA9T8mZDdQpqYBKtCFTOfQbwPqWEOpjqW+Fnayc0969g==",
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/cli-cursor": {
      "version": "3.1.0",
      "resolved": "https://registry.npmjs.org/cli-cursor/-/cli-cursor-3.1.0.tgz",
      "integrity": "sha512-I/zHAwsKf9FqGoXM4WWRACob9+SNukZTd94DWF57E4toouRulbCxcUh6RKUEOQlYTHJnzkPMySvPNaaSLNfLZw==",
      "license": "MIT",
      "dependencies": {
        "restore-cursor": "^3.1.0"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/cli-highlight": {
      "version": "2.1.11",
      "resolved": "https://registry.npmjs.org/cli-highlight/-/cli-highlight-2.1.11.tgz",
      "integrity": "sha512-9KDcoEVwyUXrjcJNvHD0NFc/hiwe/WPVYIleQh2O1N2Zro5gWJZ/K+3DGn8w8P/F6FxOgzyC5bxDyHIgCSPhGg==",
      "license": "ISC",
      "dependencies": {
        "chalk": "^4.0.0",
        "highlight.js": "^10.7.1",
        "mz": "^2.4.0",
        "parse5": "^5.1.1",
        "parse5-htmlparser2-tree-adapter": "^6.0.0",
        "yargs": "^16.0.0"
      },
      "bin": {
        "highlight": "bin/highlight"
      },
      "engines": {
        "node": ">=8.0.0",
        "npm": ">=5.0.0"
      }
    },
    "node_modules/cli-highlight/node_modules/ansi-styles": {
      "version": "4.3.0",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
      "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
      "license": "MIT",
      "dependencies": {
        "color-convert": "^2.0.1"
      },
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/cli-highlight/node_modules/chalk": {
      "version": "4.1.2",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-4.1.2.tgz",
      "integrity": "sha512-oKnbhFyRIXpUuez8iBMmyEa4nbj4IOQyuhc/wy9kY7/WVPcwIO9VA668Pu8RkO7+0G76SLROeyw9CpQ061i4mA==",
      "license": "MIT",
      "dependencies": {
        "ansi-styles": "^4.1.0",
        "supports-color": "^7.1.0"
      },
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/chalk/chalk?sponsor=1"
      }
    },
    "node_modules/cli-spinners": {
      "version": "2.9.2",
      "resolved": "https://registry.npmjs.org/cli-spinners/-/cli-spinners-2.9.2.tgz",
      "integrity": "sha512-ywqV+5MmyL4E7ybXgKys4DugZbX0FC6LnwrhjuykIjnK9k8OQacQ7axGKnjDXWNhns0xot3bZI5h55H8yo9cJg==",
      "license": "MIT",
      "engines": {
        "node": ">=6"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/cli-width": {
      "version": "4.1.0",
      "resolved": "https://registry.npmjs.org/cli-width/-/cli-width-4.1.0.tgz",
      "integrity": "sha512-ouuZd4/dm2Sw5Gmqy6bGyNNNe1qt9RpmxveLSO7KcgsTnU7RXfsw+/bukWGo1abgBiMAic068rclZsO4IWmmxQ==",
      "license": "ISC",
      "engines": {
        "node": ">= 12"
      }
    },
    "node_modules/cliui": {
      "version": "7.0.4",
      "resolved": "https://registry.npmjs.org/cliui/-/cliui-7.0.4.tgz",
      "integrity": "sha512-OcRE68cOsVMXp1Yvonl/fzkQOyjLSu/8bhPDfQt0e0/Eb283TKP20Fs2MqoPsr9SwA595rRCA+QMzYc9nBP+JQ==",
      "license": "ISC",
      "dependencies": {
        "string-width": "^4.2.0",
        "strip-ansi": "^6.0.0",
        "wrap-ansi": "^7.0.0"

*Content truncated for brevity.*

```

## File: CONTRIBUTING.md

<a name='file-CONTRIBUTING.md'></a>
*Description*: No specific description available.

```plaintext
<!---
Copyright 2025 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Contribute to smolagents

Everyone is welcome to contribute, and we value everybody's contribution. Code
contributions are not the only way to help the community. Answering questions, helping
others, and improving the documentation are also immensely valuable.

It also helps us if you spread the word! Reference the library in blog posts
about the awesome projects it made possible, shout out on Twitter every time it has
helped you, or simply ⭐️ the repository to say thank you.

However you choose to contribute, please be mindful and respect our
[code of conduct](https://github.com/huggingface/smolagents/blob/main/CODE_OF_CONDUCT.md).

**This guide was heavily inspired by the awesome [scikit-learn guide to contributing](https://github.com/scikit-learn/scikit-learn/blob/main/CONTRIBUTING.md).**

## Ways to contribute

There are several ways you can contribute to smolagents.

* Fix outstanding issues with the existing code.
* Submit issues related to bugs or desired new features.
* Contribute to the examples or to the documentation.

> All contributions are equally valuable to the community. 🥰

## Fixing outstanding issues

If you notice an issue with the existing code and have a fix in mind, feel free to [start contributing](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) and open
a Pull Request!

## Submitting a bug-related issue or feature request

Do your best to follow these guidelines when submitting a bug-related issue or a feature
request. It will make it easier for us to come back to you quickly and with good
feedback.

### Did you find a bug?

The smolagents library is robust and reliable thanks to users who report the problems they encounter.

Before you report an issue, we would really appreciate it if you could **make sure the bug was not
already reported** (use the search bar on GitHub under Issues). Your issue should also be related to bugs in the 
library itself, and not your code. 

Once you've confirmed the bug hasn't already been reported, please include the following information in your issue so 
we can quickly resolve it:

* Your **OS type and version**, as well as your environment versions (versions of rust, python, and dependencies).
* A short, self-contained, code snippet that allows us to reproduce the bug.
* The *full* traceback if an exception is raised.
* Attach any other additional information, like screenshots, you think may help.

### Do you want a new feature?

If there is a new feature you'd like to see in smolagents, please open an issue and describe:

1. What is the *motivation* behind this feature? Is it related to a problem or frustration with the library? Is it 
   a feature related to something you need for a project? Is it something you worked on and think it could benefit 
   the community?

   Whatever it is, we'd love to hear about it!

2. Describe your requested feature in as much detail as possible. The more you can tell us about it, the better 
   we'll be able to help you.
3. Provide a *code snippet* that demonstrates the feature's usage.
4. If the feature is related to a paper, please include a link.

If your issue is well written we're already 80% of the way there by the time you create it.

## Do you want to add documentation?

We're always looking for improvements to the documentation that make it more clear and accurate. Please let us know 
how the documentation can be improved such as typos and any content that is missing, unclear or inaccurate. We'll be 
happy to make the changes or help you make a contribution if you're interested!

## I want to become a maintainer of the project. How do I get there?

Smolagents is a project led and managed by Hugging Face as an initial fork of Transformers Agents. We are  more than 
happy to have motivated individuals from other organizations join us as maintainers with the goal of helping Smolagents
make a dent in the world of Agents.

If you are such an individual (or organization), please reach out to us and let's collaborate.
```

## File: CODE_OF_CONDUCT.md

<a name='file-CODE_OF_CONDUCT.md'></a>
*Description*: No specific description available.

```plaintext

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall
  community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of
  any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email address,
  without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
feedback@huggingface.co.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series of
actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations
```

## File: e2b.toml

<a name='file-e2b.toml'></a>
*Description*: No specific description available.

```plaintext
# This is a config for E2B sandbox template.
# You can use template ID (qywp2ctmu2q7jzprcf4j) to create a sandbox:

# Python SDK
# from e2b import Sandbox, AsyncSandbox
# sandbox = Sandbox("qywp2ctmu2q7jzprcf4j") # Sync sandbox
# sandbox = await AsyncSandbox.create("qywp2ctmu2q7jzprcf4j") # Async sandbox

# JS SDK
# import { Sandbox } from 'e2b'
# const sandbox = await Sandbox.create('qywp2ctmu2q7jzprcf4j')

team_id = "f8776d3a-df2f-4a1d-af48-68c2e13b3b87"
start_cmd = "/root/.jupyter/start-up.sh"
dockerfile = "e2b.Dockerfile"
template_id = "qywp2ctmu2q7jzprcf4j"

```

## File: Dockerfile

<a name='file-Dockerfile'></a>
*Description*: No specific description available.

```plaintext
# Base Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libjpeg-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy package files
COPY . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the package
RUN pip install -e .

COPY server.py /app/server.py

# Expose the port your server will run on
EXPOSE 65432

CMD ["python", "/app/server.py"]

```

## File: package.json

<a name='file-package.json'></a>
*Description*: This JSON file contains structured data.

```json
{
  "dependencies": {
    "@e2b/cli": "^1.0.9"
  }
}

```

## File: .pre-commit-config.yaml

<a name='file-.pre-commit-config.yaml'></a>
*Description*: No specific description available.

```plaintext
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.1
    hooks:
      - id: ruff
        args:
          - --fix
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-merge-conflict
      - id: check-yaml

```

## File: src/smolagents/prompts.py

<a name='file-src-smolagents-prompts.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
SINGLE_STEP_CODE_SYSTEM_PROMPT = """You will be given a task to solve, your job is to come up with a series of simple commands in Python that will perform the task.
To help you, I will give you access to a set of tools that you can use. Each tool is a Python function and has a description explaining the task it performs, the inputs it expects and the outputs it returns.
You should first explain which tool you will use to perform the task and for what reason, then write the code in Python.
Each instruction in Python should be a simple assignment. You can print intermediate results if it makes sense to do so.
In the end, use tool 'final_answer' to return your answer, its argument will be what gets returned.
You can use imports in your code, but only from the following list of modules: <<authorized_imports>>
Be sure to provide a 'Code:' token, else the run will fail.

Tools:
{{tool_descriptions}}

Examples:
---
Task:
"Answer the question in the variable `question` about the image stored in the variable `image`. The question is in French.
You have been provided with these additional arguments, that you can access using the keys as variables in your python code:
{'question': 'Quel est l'animal sur l'image?', 'image': 'path/to/image.jpg'}"

Thought: I will use the following tools: `translator` to translate the question into English and then `image_qa` to answer the question on the input image.
Code:
```py
translated_question = translator(question=question, src_lang="French", tgt_lang="English")
print(f"The translated question is {translated_question}.")
answer = image_qa(image=image, question=translated_question)
final_answer(f"The answer is {answer}")
```<end_code>

---
Task: "Identify the oldest person in the `document` and create an image showcasing the result."

Thought: I will use the following tools: `document_qa` to find the oldest person in the document, then `image_generator` to generate an image according to the answer.
Code:
```py
answer = document_qa(document, question="What is the oldest person?")
print(f"The answer is {answer}.")
image = image_generator(answer)
final_answer(image)
```<end_code>

---
Task: "Generate an image using the text given in the variable `caption`."

Thought: I will use the following tool: `image_generator` to generate an image.
Code:
```py
image = image_generator(prompt=caption)
final_answer(image)
```<end_code>

---
Task: "Summarize the text given in the variable `text` and read it out loud."

Thought: I will use the following tools: `summarizer` to create a summary of the input text, then `text_reader` to read it out loud.
Code:
```py
summarized_text = summarizer(text)
print(f"Summary: {summarized_text}")
audio_summary = text_reader(summarized_text)
final_answer(audio_summary)
```<end_code>

---
Task: "Answer the question in the variable `question` about the text in the variable `text`. Use the answer to generate an image."

Thought: I will use the following tools: `text_qa` to create the answer, then `image_generator` to generate an image according to the answer.
Code:
```py
answer = text_qa(text=text, question=question)
print(f"The answer is {answer}.")
image = image_generator(answer)
final_answer(image)
```<end_code>

---
Task: "Caption the following `image`."

Thought: I will use the following tool: `image_captioner` to generate a caption for the image.
Code:
```py
caption = image_captioner(image)
final_answer(caption)
```<end_code>

---
Above example were using tools that might not exist for you. You only have access to these tools:
{{tool_names}}

{{managed_agents_descriptions}}

Remember to make sure that variables you use are all defined. In particular don't import packages!
Be sure to provide a 'Code:\n```' sequence before the code and '```<end_code>' after, else you will get an error.
DO NOT pass the arguments as a dict as in 'answer = ask_search_agent({'query': "What is the place where James Bond lives?"})', but use the arguments directly as in 'answer = ask_search_agent(query="What is the place where James Bond lives?")'.

Now Begin! If you solve the task correctly, you will receive a reward of $1,000,000.
"""


TOOL_CALLING_SYSTEM_PROMPT = """You are an expert assistant who can solve any task using  tool calls. You will be given a task to solve as best you can.
To do so, you have been given access to the following tools: {{tool_names}}

The tool call you write is an action: after the tool is executed, you will get the result of the tool call as an "observation".
This Action/Observation can repeat N times, you should take several steps when needed.

You can use the result of the previous action as input for the next action.
The observation will always be a string: it can represent a file, like "image_1.jpg".
Then you can use it as input for the next action. You can do it for instance as follows:

Observation: "image_1.jpg"

Action:
{
  "tool_name": "image_transformer",
  "tool_arguments": {"image": "image_1.jpg"}
}

To provide the final answer to the task, use an action blob with "tool_name": "final_answer" tool. It is the only way to complete the task, else you will be stuck on a loop. So your final output should look like this:
Action:
{
  "tool_name": "final_answer",
  "tool_arguments": {"answer": "insert your final answer here"}
}


Here are a few examples using notional tools:
---
Task: "Generate an image of the oldest person in this document."

Action:
{
  "tool_name": "document_qa",
  "tool_arguments": {"document": "document.pdf", "question": "Who is the oldest person mentioned?"}
}
Observation: "The oldest person in the document is John Doe, a 55 year old lumberjack living in Newfoundland."

Action:
{
  "tool_name": "image_generator",
  "tool_arguments": {"prompt": "A portrait of John Doe, a 55-year-old man living in Canada."}
}
Observation: "image.png"

Action:
{
  "tool_name": "final_answer",
  "tool_arguments": "image.png"
}

---
Task: "What is the result of the following operation: 5 + 3 + 1294.678?"

Action:
{
    "tool_name": "python_interpreter",
    "tool_arguments": {"code": "5 + 3 + 1294.678"}
}
Observation: 1302.678

Action:
{
  "tool_name": "final_answer",
  "tool_arguments": "1302.678"
}

---
Task: "Which city has the highest population , Guangzhou or Shanghai?"

Action:
{
    "tool_name": "search",
    "tool_arguments": "Population Guangzhou"
}
Observation: ['Guangzhou has a population of 15 million inhabitants as of 2021.']


Action:
{
    "tool_name": "search",
    "tool_arguments": "Population Shanghai"
}
Observation: '26 million (2019)'

Action:
{
  "tool_name": "final_answer",
  "tool_arguments": "Shanghai"
}


Above example were using notional tools that might not exist for you. You only have access to these tools:

{{tool_descriptions}}

{{managed_agents_descriptions}}

Here are the rules you should always follow to solve your task:
1. ALWAYS provide a tool call, else you will fail.
2. Always use the right arguments for the tools. Never use variable names as the action arguments, use the value instead.
3. Call a tool only when needed: do not call the search agent if you do not need information, try to solve the task yourself.
If no tool call is needed, use final_answer tool to return your answer.
4. Never re-do a tool call that you previously did with the exact same parameters.

Now Begin! If you solve the task correctly, you will receive a reward of $1,000,000.
"""

CODE_SYSTEM_PROMPT = """You are an expert assistant who can solve any task using code blobs. You will be given a task to solve as best you can.
To do so, you have been given access to a list of tools: these tools are basically Python functions which you can call with code.
To solve the task, you must plan forward to proceed in a series of steps, in a cycle of 'Thought:', 'Code:', and 'Observation:' sequences.

At each step, in the 'Thought:' sequence, you should first explain your reasoning towards solving the task and the tools that you want to use.
Then in the 'Code:' sequence, you should write the code in simple Python. The code sequence must end with '<end_code>' sequence.
During each intermediate step, you can use 'print()' to save whatever important information you will then need.
These print outputs will then appear in the 'Observation:' field, which will be available as input for the next step.
In the end you have to return a final answer using the `final_answer` tool.

Here are a few examples using notional tools:
---
Task: "Generate an image of the oldest person in this document."

Thought: I will proceed step by step and use the following tools: `document_qa` to find the oldest person in the document, then `image_generator` to generate an image according to the answer.
Code:
```py
answer = document_qa(document=document, question="Who is the oldest person mentioned?")
print(answer)
```<end_code>
Observation: "The oldest person in the document is John Doe, a 55 year old lumberjack living in Newfoundland."

Thought: I will now generate an image showcasing the oldest person.
Code:
```py
image = image_generator("A portrait of John Doe, a 55-year-old man living in Canada.")
final_answer(image)
```<end_code>

---
Task: "What is the result of the following operation: 5 + 3 + 1294.678?"

Thought: I will use python code to compute the result of the operation and then return the final answer using the `final_answer` tool
Code:
```py
result = 5 + 3 + 1294.678
final_answer(result)
```<end_code>

---
Task:
"Answer the question in the variable `question` about the image stored in the variable `image`. The question is in French.
You have been provided with these additional arguments, that you can access using the keys as variables in your python code:
{'question': 'Quel est l'animal sur l'image?', 'image': 'path/to/image.jpg'}"

Thought: I will use the following tools: `translator` to translate the question into English and then `image_qa` to answer the question on the input image.
Code:
```py
translated_question = translator(question=question, src_lang="French", tgt_lang="English")
print(f"The translated question is {translated_question}.")
answer = image_qa(image=image, question=translated_question)
final_answer(f"The answer is {answer}")
```<end_code>

---
Task:
In a 1979 interview, Stanislaus Ulam discusses with Martin Sherwin about other great physicists of his time, including Oppenheimer.
What does he say was the consequence of Einstein learning too much math on his creativity, in one word?

Thought: I need to find and read the 1979 interview of Stanislaus Ulam with Martin Sherwin.
Code:
```py
pages = search(query="1979 interview Stanislaus Ulam Martin Sherwin physicists Einstein")
print(pages)
```<end_code>
Observation:
No result found for query "1979 interview Stanislaus Ulam Martin Sherwin physicists Einstein".

Thought: The query was maybe too restrictive and did not find any results. Let's try again with a broader query.
Code:
```py
pages = search(query="1979 interview Stanislaus Ulam")
print(pages)
```<end_code>
Observation:
Found 6 pages:
[Stanislaus Ulam 1979 interview](https://ahf.nuclearmuseum.org/voices/oral-histories/stanislaus-ulams-interview-1979/)

[Ulam discusses Manhattan Project](https://ahf.nuclearmuseum.org/manhattan-project/ulam-manhattan-project/)

(truncated)

Thought: I will read the first 2 pages to know more.
Code:
```py
for url in ["https://ahf.nuclearmuseum.org/voices/oral-histories/stanislaus-ulams-interview-1979/", "https://ahf.nuclearmuseum.org/manhattan-project/ulam-manhattan-project/"]:
    whole_page = visit_webpage(url)
    print(whole_page)
    print("\n" + "="*80 + "\n")  # Print separator between pages
```<end_code>
Observation:
Manhattan Project Locations:
Los Alamos, NM
Stanislaus Ulam was a Polish-American mathematician. He worked on the Manhattan Project at Los Alamos and later helped design the hydrogen bomb. In this interview, he discusses his work at
(truncated)

Thought: I now have the final answer: from the webpages visited, Stanislaus Ulam says of Einstein: "He learned too much mathematics and sort of diminished, it seems to me personally, it seems to me his purely physics creativity." Let's answer in one word.
Code:
```py
final_answer("diminished")
```<end_code>

---
Task: "Which city has the highest population: Guangzhou or Shanghai?"

Thought: I need to get the populations for both cities and compare them: I will use the tool `search` to get the population of both cities.
Code:
```py
for city in ["Guangzhou", "Shanghai"]:
    print(f"Population {city}:", search(f"{city} population")
```<end_code>
Observation:
Population Guangzhou: ['Guangzhou has a population of 15 million inhabitants as of 2021.']
Population Shanghai: '26 million (2019)'

Thought: Now I know that Shanghai has the highest population.
Code:
```py
final_answer("Shanghai")
```<end_code>

---
Task: "What is the current age of the pope, raised to the power 0.36?"

Thought: I will use the tool `wiki` to get the age of the pope, and confirm that with a web search.
Code:
```py
pope_age_wiki = wiki(query="current pope age")
print("Pope age as per wikipedia:", pope_age_wiki)
pope_age_search = web_search(query="current pope age")
print("Pope age as per google search:", pope_age_search)
```<end_code>
Observation:
Pope age: "The pope Francis is currently 88 years old."

Thought: I know that the pope is 88 years old. Let's compute the result using python code.
Code:
```py
pope_current_age = 88 ** 0.36
final_answer(pope_current_age)
```<end_code>

Above example were using notional tools that might not exist for you. On top of performing computations in the Python code snippets that you create, you only have access to these tools:

{{tool_descriptions}}

{{managed_agents_descriptions}}

Here are the rules you should always follow to solve your task:
1. Always provide a 'Thought:' sequence, and a 'Code:\n```py' sequence ending with '```<end_code>' sequence, else you will fail.
2. Use only variables that you have defined!
3. Always use the right arguments for the tools. DO NOT pass the arguments as a dict as in 'answer = wiki({'query': "What is the place where James Bond lives?"})', but use the arguments directly as in 'answer = wiki(query="What is the place where James Bond lives?")'.
4. Take care to not chain too many sequential tool calls in the same code block, especially when the output format is unpredictable. For instance, a call to search has an unpredictable return format, so do not have another tool call that depends on its output in the same block: rather output results with print() to use them in the next block.
5. Call a tool only when needed, and never re-do a tool call that you previously did with the exact same parameters.
6. Don't name any new variable with the same name as a tool: for instance don't name a variable 'final_answer'.
7. Never create any notional variables in our code, as having these in your logs will derail you from the true variables.
8. You can use imports in your code, but only from the following list of modules: {{authorized_imports}}
9. The state persists between code executions: so if in one step you've created variables or imported modules, these will all persist.
10. Don't give up! You're in charge of solving the task, not providing directions to solve it.

Now Begin! If you solve the task correctly, you will receive a reward of $1,000,000.
"""

SYSTEM_PROMPT_FACTS = """Below I will present you a task.

You will now build a comprehensive preparatory survey of which facts we have at our disposal and which ones we still need.
To do so, you will have to read the task and identify things that must be discovered in order to successfully complete it.
Don't make any assumptions. For each item, provide a thorough reasoning. Here is how you will structure this survey:

---
### 1. Facts given in the task
List here the specific facts given in the task that could help you (there might be nothing here).

### 2. Facts to look up
List here any facts that we may need to look up.
Also list where to find each of these, for instance a website, a file... - maybe the task contains some sources that you should re-use here.

### 3. Facts to derive
List here anything that we want to derive from the above by logical reasoning, for instance computation or simulation.

Keep in mind that "facts" will typically be specific names, dates, values, etc. Your answer should use the below headings:
### 1. Facts given in the task
### 2. Facts to look up
### 3. Facts to derive
Do not add anything else."""

SYSTEM_PROMPT_PLAN = """You are a world expert at making efficient plans to solve any task using a set of carefully crafted tools.

Now for the given task, develop a step-by-step high-level plan taking into account the above inputs and list of facts.
This plan should involve individual tasks based on the available tools, that if executed correctly will yield the correct answer.
Do not skip steps, do not add any superfluous steps. Only write the high-level plan, DO NOT DETAIL INDIVIDUAL TOOL CALLS.
After writing the final step of the plan, write the '\n<end_plan>' tag and stop there."""

USER_PROMPT_PLAN = """
Here is your task:

Task:
```
{task}
```

Your plan can leverage any of these tools:
{tool_descriptions}

{managed_agents_descriptions}

List of facts that you know:
```
{answer_facts}
```

Now begin! Write your plan below."""

SYSTEM_PROMPT_FACTS_UPDATE = """
You are a world expert at gathering known and unknown facts based on a conversation.
Below you will find a task, and ahistory of attempts made to solve the task. You will have to produce a list of these:
### 1. Facts given in the task
### 2. Facts that we have learned
### 3. Facts still to look up
### 4. Facts still to derive
Find the task and history below."""

USER_PROMPT_FACTS_UPDATE = """Earlier we've built a list of facts.
But since in your previous steps you may have learned useful new facts or invalidated some false ones.
Please update your list of facts based on the previous history, and provide these headings:
### 1. Facts given in the task
### 2. Facts that we have learned
### 3. Facts still to look up
### 4. Facts still to derive

Now write your new list of facts below."""

SYSTEM_PROMPT_PLAN_UPDATE = """You are a world expert at making efficient plans to solve any task using a set of carefully crafted tools.

You have been given a task:
```
{task}
```

Find below the record of what has been tried so far to solve it. Then you will be asked to make an updated plan to solve the task.
If the previous tries so far have met some success, you can make an updated plan based on these actions.
If you are stalled, you can make a completely new plan starting from scratch.
"""

USER_PROMPT_PLAN_UPDATE = """You're still working towards solving this task:
```
{task}
```

You have access to these tools and only these:
{tool_descriptions}

{managed_agents_descriptions}

Here is the up to date list of facts that you know:
```
{facts_update}
```

Now for the given task, develop a step-by-step high-level plan taking into account the above inputs and list of facts.
This plan should involve individual tasks based on the available tools, that if executed correctly will yield the correct answer.
Beware that you have {remaining_steps} steps remaining.
Do not skip steps, do not add any superfluous steps. Only write the high-level plan, DO NOT DETAIL INDIVIDUAL TOOL CALLS.
After writing the final step of the plan, write the '\n<end_plan>' tag and stop there.

Now write your new plan below."""

PLAN_UPDATE_FINAL_PLAN_REDACTION = """I still need to solve the task I was given:
```
{task}
```

Here is my new/updated plan of action to solve the task:
```
{plan_update}
```"""

MANAGED_AGENT_PROMPT = """You're a helpful agent named '{name}'.
You have been submitted this task by your manager.
---
Task:
{task}
---
You're helping your manager solve a wider task: so make sure to not provide a one-line answer, but give as much information as possible to give them a clear understanding of the answer.

Your final_answer WILL HAVE to contain these parts:
### 1. Task outcome (short version):
### 2. Task outcome (extremely detailed version):
### 3. Additional context (if relevant):

Put all these in your final_answer tool, everything that you do not pass as an argument to final_answer will be lost.
And even if your task resolution is not successful, please return as much context as possible, so that your manager can act upon this feedback.

*Content truncated for brevity.*

```

## File: src/smolagents/__init__.py

<a name='file-src-smolagents-__init__.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
__version__ = "1.3.0.dev"

from typing import TYPE_CHECKING

from transformers.utils import _LazyModule
from transformers.utils.import_utils import define_import_structure

if TYPE_CHECKING:
    from .agents import *
    from .default_tools import *
    from .e2b_executor import *
    from .gradio_ui import *
    from .local_python_executor import *
    from .models import *
    from .monitoring import *
    from .prompts import *
    from .tools import *
    from .types import *
    from .utils import *


else:
    import sys

    _file = globals()["__file__"]
    import_structure = define_import_structure(_file)
    import_structure[""] = {"__version__": __version__}
    sys.modules[__name__] = _LazyModule(
        __name__,
        _file,
        import_structure,
        module_spec=__spec__,
        extra_objects={"__version__": __version__},
    )

```

## File: src/smolagents/agents.py

<a name='file-src-smolagents-agents.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from enum import IntEnum
from rich import box
from rich.console import Group
from rich.panel import Panel
from rich.rule import Rule
from rich.syntax import Syntax
from rich.text import Text
from rich.console import Console

from .default_tools import FinalAnswerTool, TOOL_MAPPING
from .e2b_executor import E2BExecutor
from .local_python_executor import (
    BASE_BUILTIN_MODULES,
    LocalPythonInterpreter,
    fix_final_answer_code,
)
from .models import MessageRole
from .monitoring import Monitor
from .prompts import (
    CODE_SYSTEM_PROMPT,
    MANAGED_AGENT_PROMPT,
    PLAN_UPDATE_FINAL_PLAN_REDACTION,
    SYSTEM_PROMPT_FACTS,
    SYSTEM_PROMPT_FACTS_UPDATE,
    SYSTEM_PROMPT_PLAN,
    SYSTEM_PROMPT_PLAN_UPDATE,
    TOOL_CALLING_SYSTEM_PROMPT,
    USER_PROMPT_FACTS_UPDATE,
    USER_PROMPT_PLAN,
    USER_PROMPT_PLAN_UPDATE,
)
from .tools import (
    DEFAULT_TOOL_DESCRIPTION_TEMPLATE,
    Tool,
    get_tool_description_with_args,
)
from .types import AgentAudio, AgentImage, handle_agent_output_types
from .utils import (
    AgentError,
    AgentExecutionError,
    AgentGenerationError,
    AgentMaxStepsError,
    AgentParsingError,
    console,
    parse_code_blobs,
    parse_json_tool_call,
    truncate_content,
)


@dataclass
class ToolCall:
    name: str
    arguments: Any
    id: str


class AgentStep:
    pass


@dataclass
class ActionStep(AgentStep):
    agent_memory: List[Dict[str, str]] | None = None
    tool_calls: List[ToolCall] | None = None
    start_time: float | None = None
    end_time: float | None = None
    step: int | None = None
    error: AgentError | None = None
    duration: float | None = None
    llm_output: str | None = None
    observations: str | None = None
    action_output: Any = None


@dataclass
class PlanningStep(AgentStep):
    plan: str
    facts: str


@dataclass
class TaskStep(AgentStep):
    task: str


@dataclass
class SystemPromptStep(AgentStep):
    system_prompt: str


def get_tool_descriptions(
    tools: Dict[str, Tool], tool_description_template: str
) -> str:
    return "\n".join(
        [
            get_tool_description_with_args(tool, tool_description_template)
            for tool in tools.values()
        ]
    )


def format_prompt_with_tools(
    tools: Dict[str, Tool], prompt_template: str, tool_description_template: str
) -> str:
    tool_descriptions = get_tool_descriptions(tools, tool_description_template)
    prompt = prompt_template.replace("{{tool_descriptions}}", tool_descriptions)
    if "{{tool_names}}" in prompt:
        prompt = prompt.replace(
            "{{tool_names}}",
            ", ".join([f"'{tool.name}'" for tool in tools.values()]),
        )
    return prompt


def show_agents_descriptions(managed_agents: Dict):
    managed_agents_descriptions = """
You can also give requests to team members.
Calling a team member works the same as for calling a tool: simply, the only argument you can give in the call is 'request', a long string explaining your request.
Given that this team member is a real human, you should be very verbose in your request.
Here is a list of the team members that you can call:"""
    for agent in managed_agents.values():
        managed_agents_descriptions += f"\n- {agent.name}: {agent.description}"
    return managed_agents_descriptions


def format_prompt_with_managed_agents_descriptions(
    prompt_template,
    managed_agents,
    agent_descriptions_placeholder: Optional[str] = None,
) -> str:
    if agent_descriptions_placeholder is None:
        agent_descriptions_placeholder = "{{managed_agents_descriptions}}"
    if agent_descriptions_placeholder not in prompt_template:
        raise ValueError(
            f"Provided prompt template does not contain the managed agents descriptions placeholder '{agent_descriptions_placeholder}'"
        )
    if len(managed_agents.keys()) > 0:
        return prompt_template.replace(
            agent_descriptions_placeholder, show_agents_descriptions(managed_agents)
        )
    else:
        return prompt_template.replace(agent_descriptions_placeholder, "")


YELLOW_HEX = "#d4b702"


class LogLevel(IntEnum):
    ERROR = 0  # Only errors
    INFO = 1  # Normal output (default)
    DEBUG = 2  # Detailed output


class AgentLogger:
    def __init__(self, level: LogLevel = LogLevel.INFO):
        self.level = level
        self.console = Console()

    def log(self, *args, level: LogLevel = LogLevel.INFO, **kwargs):
        if level <= self.level:
            console.print(*args, **kwargs)


class MultiStepAgent:
    """
    Agent class that solves the given task step by step, using the ReAct framework:
    While the objective is not reached, the agent will perform a cycle of action (given by the LLM) and observation (obtained from the environment).
    """

    def __init__(
        self,
        tools: List[Tool],
        model: Callable[[List[Dict[str, str]]], str],
        system_prompt: Optional[str] = None,
        tool_description_template: Optional[str] = None,
        max_steps: int = 6,
        tool_parser: Optional[Callable] = None,
        add_base_tools: bool = False,
        verbosity_level: int = 1,
        grammar: Optional[Dict[str, str]] = None,
        managed_agents: Optional[List] = None,
        step_callbacks: Optional[List[Callable]] = None,
        planning_interval: Optional[int] = None,
    ):
        if system_prompt is None:
            system_prompt = CODE_SYSTEM_PROMPT
        if tool_parser is None:
            tool_parser = parse_json_tool_call
        self.agent_name = self.__class__.__name__
        self.model = model
        self.system_prompt_template = system_prompt
        self.tool_description_template = (
            tool_description_template
            if tool_description_template
            else DEFAULT_TOOL_DESCRIPTION_TEMPLATE
        )
        self.max_steps = max_steps
        self.tool_parser = tool_parser
        self.grammar = grammar
        self.planning_interval = planning_interval
        self.state = {}

        self.managed_agents = {}
        if managed_agents is not None:
            self.managed_agents = {agent.name: agent for agent in managed_agents}

        self.tools = {tool.name: tool for tool in tools}
        if add_base_tools:
            for tool_name, tool_class in TOOL_MAPPING.items():
                if (
                    tool_name != "python_interpreter"
                    or self.__class__.__name__ == "ToolCallingAgent"
                ):
                    self.tools[tool_name] = tool_class()
        self.tools["final_answer"] = FinalAnswerTool()

        self.system_prompt = self.initialize_system_prompt()
        self.input_messages = None
        self.logs = []
        self.task = None
        self.logger = AgentLogger(level=verbosity_level)
        self.monitor = Monitor(self.model, self.logger)
        self.step_callbacks = step_callbacks if step_callbacks is not None else []
        self.step_callbacks.append(self.monitor.update_metrics)

    def initialize_system_prompt(self):
        self.system_prompt = format_prompt_with_tools(
            self.tools,
            self.system_prompt_template,
            self.tool_description_template,
        )
        self.system_prompt = format_prompt_with_managed_agents_descriptions(
            self.system_prompt, self.managed_agents
        )

        return self.system_prompt

    def write_inner_memory_from_logs(
        self, summary_mode: Optional[bool] = False
    ) -> List[Dict[str, str]]:
        """
        Reads past llm_outputs, actions, and observations or errors from the logs into a series of messages
        that can be used as input to the LLM.
        """
        memory = []
        for i, step_log in enumerate(self.logs):
            if isinstance(step_log, SystemPromptStep):
                if not summary_mode:
                    thought_message = {
                        "role": MessageRole.SYSTEM,
                        "content": step_log.system_prompt.strip(),
                    }
                    memory.append(thought_message)

            elif isinstance(step_log, PlanningStep):
                thought_message = {
                    "role": MessageRole.ASSISTANT,
                    "content": "[FACTS LIST]:\n" + step_log.facts.strip(),
                }
                memory.append(thought_message)

                if not summary_mode:
                    thought_message = {
                        "role": MessageRole.ASSISTANT,
                        "content": "[PLAN]:\n" + step_log.plan.strip(),
                    }
                    memory.append(thought_message)

            elif isinstance(step_log, TaskStep):
                task_message = {
                    "role": MessageRole.USER,
                    "content": "New task:\n" + step_log.task,
                }
                memory.append(task_message)

            elif isinstance(step_log, ActionStep):
                if step_log.llm_output is not None and not summary_mode:
                    thought_message = {
                        "role": MessageRole.ASSISTANT,
                        "content": step_log.llm_output.strip(),
                    }
                    memory.append(thought_message)

                if step_log.tool_calls is not None:
                    tool_call_message = {
                        "role": MessageRole.ASSISTANT,
                        "content": str(
                            [
                                {
                                    "id": tool_call.id,
                                    "type": "function",
                                    "function": {
                                        "name": tool_call.name,
                                        "arguments": tool_call.arguments,
                                    },
                                }
                                for tool_call in step_log.tool_calls
                            ]
                        ),
                    }
                    memory.append(tool_call_message)

                if step_log.tool_calls is None and step_log.error is not None:
                    message_content = (
                        "Error:\n"
                        + str(step_log.error)
                        + "\nNow let's retry: take care not to repeat previous errors! If you have retried several times, try a completely different approach.\n"
                    )
                    tool_response_message = {
                        "role": MessageRole.ASSISTANT,
                        "content": message_content,
                    }
                if step_log.tool_calls is not None and (
                    step_log.error is not None or step_log.observations is not None
                ):
                    if step_log.error is not None:
                        message_content = (
                            "Error:\n"
                            + str(step_log.error)
                            + "\nNow let's retry: take care not to repeat previous errors! If you have retried several times, try a completely different approach.\n"
                        )
                    elif step_log.observations is not None:
                        message_content = f"Observation:\n{step_log.observations}"
                    tool_response_message = {
                        "role": MessageRole.TOOL_RESPONSE,
                        "content": f"Call id: {(step_log.tool_calls[0].id if getattr(step_log.tool_calls[0], 'id') else 'call_0')}\n"
                        + message_content,
                    }
                    memory.append(tool_response_message)

        return memory

    def get_succinct_logs(self):
        return [
            {key: value for key, value in log.items() if key != "agent_memory"}
            for log in self.logs
        ]

    def extract_action(self, llm_output: str, split_token: str) -> Tuple[str, str]:
        """
        Parse action from the LLM output

        Args:
            llm_output (`str`): Output of the LLM
            split_token (`str`): Separator for the action. Should match the example in the system prompt.
        """
        try:
            split = llm_output.split(split_token)
            rationale, action = (
                split[-2],
                split[-1],
            )  # NOTE: using indexes starting from the end solves for when you have more than one split_token in the output
        except Exception:
            raise AgentParsingError(
                f"No '{split_token}' token provided in your output.\nYour output:\n{llm_output}\n. Be sure to include an action, prefaced with '{split_token}'!"
            )
        return rationale.strip(), action.strip()

    def provide_final_answer(self, task) -> str:
        """
        This method provides a final answer to the task, based on the logs of the agent's interactions.
        """
        self.input_messages = [
            {
                "role": MessageRole.SYSTEM,
                "content": "An agent tried to answer a user query but it got stuck and failed to do so. You are tasked with providing an answer instead. Here is the agent's memory:",
            }
        ]
        self.input_messages += self.write_inner_memory_from_logs()[1:]
        self.input_messages += [
            {
                "role": MessageRole.USER,
                "content": f"Based on the above, please provide an answer to the following user request:\n{task}",
            }
        ]
        try:
            return self.model(self.input_messages).content
        except Exception as e:
            return f"Error in generating final LLM output:\n{e}"

    def execute_tool_call(
        self, tool_name: str, arguments: Union[Dict[str, str], str]
    ) -> Any:
        """
        Execute tool with the provided input and returns the result.
        This method replaces arguments with the actual values from the state if they refer to state variables.

        Args:
            tool_name (`str`): Name of the Tool to execute (should be one from self.tools).
            arguments (Dict[str, str]): Arguments passed to the Tool.
        """
        available_tools = {**self.tools, **self.managed_agents}
        if tool_name not in available_tools:
            error_msg = f"Unknown tool {tool_name}, should be instead one of {list(available_tools.keys())}."
            raise AgentExecutionError(error_msg)

        try:
            if isinstance(arguments, str):
                if tool_name in self.managed_agents:
                    observation = available_tools[tool_name].__call__(arguments)
                else:
                    observation = available_tools[tool_name].__call__(
                        arguments, sanitize_inputs_outputs=True
                    )
            elif isinstance(arguments, dict):
                for key, value in arguments.items():
                    if isinstance(value, str) and value in self.state:
                        arguments[key] = self.state[value]
                if tool_name in self.managed_agents:
                    observation = available_tools[tool_name].__call__(**arguments)
                else:
                    observation = available_tools[tool_name].__call__(
                        **arguments, sanitize_inputs_outputs=True
                    )
            else:
                error_msg = f"Arguments passed to tool should be a dict or string: got a {type(arguments)}."
                raise AgentExecutionError(error_msg)
            return observation
        except Exception as e:
            if tool_name in self.tools:
                tool_description = get_tool_description_with_args(
                    available_tools[tool_name]
                )
                error_msg = (
                    f"Error in tool call execution: {e}\nYou should only use this tool with a correct input.\n"
                    f"As a reminder, this tool's description is the following:\n{tool_description}"
                )
                raise AgentExecutionError(error_msg)
            elif tool_name in self.managed_agents:
                error_msg = (
                    f"Error in calling team member: {e}\nYou should only ask this team member with a correct request.\n"
                    f"As a reminder, this team member's description is the following:\n{available_tools[tool_name]}"
                )
                raise AgentExecutionError(error_msg)

    def step(self, log_entry: ActionStep) -> Union[None, Any]:
        """To be implemented in children classes. Should return either None if the step is not final."""
        pass

    def run(
        self,
        task: str,
        stream: bool = False,
        reset: bool = True,
        single_step: bool = False,
        additional_args: Optional[Dict] = None,
    ):
        """
        Runs the agent for the given task.

        Args:
            task (`str`): The task to perform.
            stream (`bool`): Whether to run in a streaming way.
            reset (`bool`): Whether to reset the conversation or keep it going from previous run.
            single_step (`bool`): Whether to run the agent in one-shot fashion.
            additional_args (`dict`): Any other variables that you want to pass to the agent run, for instance images or dataframes. Give them clear names!

        Example:
        ```py
        from smolagents import CodeAgent
        agent = CodeAgent(tools=[])
        agent.run("What is the result of 2 power 3.7384?")
        ```
        """
        self.task = task
        if additional_args is not None:
            self.state.update(additional_args)
            self.task += f"""
You have been provided with these additional arguments, that you can access using the keys as variables in your python code:
{str(additional_args)}."""

        self.initialize_system_prompt()
        system_prompt_step = SystemPromptStep(system_prompt=self.system_prompt)

        if reset:
            self.logs = []
            self.logs.append(system_prompt_step)
            self.monitor.reset()
        else:
            if len(self.logs) > 0:
                self.logs[0] = system_prompt_step
            else:
                self.logs.append(system_prompt_step)

        self.logger.log(
            Panel(
                f"\n[bold]{self.task.strip()}\n",
                title="[bold]New run",
                subtitle=f"{type(self.model).__name__} - {(self.model.model_id if hasattr(self.model, 'model_id') else '')}",
                border_style=YELLOW_HEX,
                subtitle_align="left",

*Content truncated for brevity.*

```

## File: src/smolagents/default_tools.py

<a name='file-src-smolagents-default_tools.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import json
import re
from dataclasses import dataclass
from typing import Dict, Optional

from huggingface_hub import hf_hub_download, list_spaces


from transformers.utils import is_offline_mode, is_torch_available

from .local_python_executor import (
    BASE_BUILTIN_MODULES,
    BASE_PYTHON_TOOLS,
    evaluate_python_code,
)
from .tools import TOOL_CONFIG_FILE, PipelineTool, Tool
from .types import AgentAudio
from .utils import truncate_content

if is_torch_available():
    from transformers.models.whisper import (
        WhisperForConditionalGeneration,
        WhisperProcessor,
    )
else:
    WhisperForConditionalGeneration = object
    WhisperProcessor = object


@dataclass
class PreTool:
    name: str
    inputs: Dict[str, str]
    output_type: type
    task: str
    description: str
    repo_id: str


def get_remote_tools(logger, organization="huggingface-tools"):
    if is_offline_mode():
        logger.info("You are in offline mode, so remote tools are not available.")
        return {}

    spaces = list_spaces(author=organization)
    tools = {}
    for space_info in spaces:
        repo_id = space_info.id
        resolved_config_file = hf_hub_download(
            repo_id, TOOL_CONFIG_FILE, repo_type="space"
        )
        with open(resolved_config_file, encoding="utf-8") as reader:
            config = json.load(reader)
        task = repo_id.split("/")[-1]
        tools[config["name"]] = PreTool(
            task=task,
            description=config["description"],
            repo_id=repo_id,
            name=task,
            inputs=config["inputs"],
            output_type=config["output_type"],
        )

    return tools


class PythonInterpreterTool(Tool):
    name = "python_interpreter"
    description = "This is a tool that evaluates python code. It can be used to perform calculations."
    inputs = {
        "code": {
            "type": "string",
            "description": "The python code to run in interpreter",
        }
    }
    output_type = "string"

    def __init__(self, *args, authorized_imports=None, **kwargs):
        if authorized_imports is None:
            self.authorized_imports = list(set(BASE_BUILTIN_MODULES))
        else:
            self.authorized_imports = list(
                set(BASE_BUILTIN_MODULES) | set(authorized_imports)
            )
        self.inputs = {
            "code": {
                "type": "string",
                "description": (
                    "The code snippet to evaluate. All variables used in this snippet must be defined in this same snippet, "
                    f"else you will get an error. This code can only import the following python libraries: {authorized_imports}."
                ),
            }
        }
        self.base_python_tools = BASE_PYTHON_TOOLS
        self.python_evaluator = evaluate_python_code
        super().__init__(*args, **kwargs)

    def forward(self, code: str) -> str:
        state = {}
        output = str(
            self.python_evaluator(
                code,
                state=state,
                static_tools=self.base_python_tools,
                authorized_imports=self.authorized_imports,
            )[0]  # The second element is boolean is_final_answer
        )
        return f"Stdout:\n{state['print_outputs']}\nOutput: {output}"


class FinalAnswerTool(Tool):
    name = "final_answer"
    description = "Provides a final answer to the given problem."
    inputs = {
        "answer": {"type": "any", "description": "The final answer to the problem"}
    }
    output_type = "any"

    def forward(self, answer):
        return answer


class UserInputTool(Tool):
    name = "user_input"
    description = "Asks for user's input on a specific question"
    inputs = {
        "question": {"type": "string", "description": "The question to ask the user"}
    }
    output_type = "string"

    def forward(self, question):
        user_input = input(f"{question} => ")
        return user_input


class DuckDuckGoSearchTool(Tool):
    name = "web_search"
    description = """Performs a duckduckgo web search based on your query (think a Google search) then returns the top search results."""
    inputs = {
        "query": {"type": "string", "description": "The search query to perform."}
    }
    output_type = "string"

    def __init__(self, *args, max_results=10, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_results = max_results
        try:
            from duckduckgo_search import DDGS
        except ImportError:
            raise ImportError(
                "You must install package `duckduckgo_search` to run this tool: for instance run `pip install duckduckgo-search`."
            )
        self.ddgs = DDGS()

    def forward(self, query: str) -> str:
        results = self.ddgs.text(query, max_results=self.max_results)
        postprocessed_results = [
            f"[{result['title']}]({result['href']})\n{result['body']}"
            for result in results
        ]
        return "## Search Results\n\n" + "\n\n".join(postprocessed_results)


class GoogleSearchTool(Tool):
    name = "web_search"
    description = """Performs a google web search for your query then returns a string of the top search results."""
    inputs = {
        "query": {"type": "string", "description": "The search query to perform."},
        "filter_year": {
            "type": "integer",
            "description": "Optionally restrict results to a certain year",
            "nullable": True,
        },
    }
    output_type = "string"

    def __init__(self):
        super().__init__(self)
        import os

        self.serpapi_key = os.getenv("SERPAPI_API_KEY")

    def forward(self, query: str, filter_year: Optional[int] = None) -> str:
        import requests

        if self.serpapi_key is None:
            raise ValueError(
                "Missing SerpAPI key. Make sure you have 'SERPAPI_API_KEY' in your env variables."
            )

        params = {
            "engine": "google",
            "q": query,
            "api_key": self.serpapi_key,
            "google_domain": "google.com",
        }
        if filter_year is not None:
            params["tbs"] = (
                f"cdr:1,cd_min:01/01/{filter_year},cd_max:12/31/{filter_year}"
            )

        response = requests.get("https://serpapi.com/search.json", params=params)

        if response.status_code == 200:
            results = response.json()
        else:
            raise ValueError(response.json())

        if "organic_results" not in results.keys():
            if filter_year is not None:
                raise Exception(
                    f"'organic_results' key not found for query: '{query}' with filtering on year={filter_year}. Use a less restrictive query or do not filter on year."
                )
            else:
                raise Exception(
                    f"'organic_results' key not found for query: '{query}'. Use a less restrictive query."
                )
        if len(results["organic_results"]) == 0:
            year_filter_message = (
                f" with filter year={filter_year}" if filter_year is not None else ""
            )
            return f"No results found for '{query}'{year_filter_message}. Try with a more general query, or remove the year filter."

        web_snippets = []
        if "organic_results" in results:
            for idx, page in enumerate(results["organic_results"]):
                date_published = ""
                if "date" in page:
                    date_published = "\nDate published: " + page["date"]

                source = ""
                if "source" in page:
                    source = "\nSource: " + page["source"]

                snippet = ""
                if "snippet" in page:
                    snippet = "\n" + page["snippet"]

                redacted_version = f"{idx}. [{page['title']}]({page['link']}){date_published}{source}\n{snippet}"

                redacted_version = redacted_version.replace(
                    "Your browser can't play this video.", ""
                )
                web_snippets.append(redacted_version)

        return "## Search Results\n" + "\n\n".join(web_snippets)


class VisitWebpageTool(Tool):
    name = "visit_webpage"
    description = "Visits a webpage at the given url and reads its content as a markdown string. Use this to browse webpages."
    inputs = {
        "url": {
            "type": "string",
            "description": "The url of the webpage to visit.",
        }
    }
    output_type = "string"

    def forward(self, url: str) -> str:
        try:
            import requests
            from markdownify import markdownify
            from requests.exceptions import RequestException
        except ImportError:
            raise ImportError(
                "You must install packages `markdownify` and `requests` to run this tool: for instance run `pip install markdownify requests`."
            )
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes

            # Convert the HTML content to Markdown
            markdown_content = markdownify(response.text).strip()

            # Remove multiple line breaks
            markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

            return truncate_content(markdown_content)

        except RequestException as e:
            return f"Error fetching the webpage: {str(e)}"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"


class SpeechToTextTool(PipelineTool):
    default_checkpoint = "openai/whisper-large-v3-turbo"
    description = "This is a tool that transcribes an audio into text. It returns the transcribed text."
    name = "transcriber"
    pre_processor_class = WhisperProcessor
    model_class = WhisperForConditionalGeneration

    inputs = {
        "audio": {
            "type": "audio",
            "description": "The audio to transcribe. Can be a local path, an url, or a tensor.",
        }
    }
    output_type = "string"

    def encode(self, audio):
        audio = AgentAudio(audio).to_raw()
        return self.pre_processor(audio, return_tensors="pt")

    def forward(self, inputs):
        return self.model.generate(inputs["input_features"])

    def decode(self, outputs):
        return self.pre_processor.batch_decode(outputs, skip_special_tokens=True)[0]


TOOL_MAPPING = {
    tool_class.name: tool_class
    for tool_class in [
        PythonInterpreterTool,
        DuckDuckGoSearchTool,
        VisitWebpageTool,
    ]
}

__all__ = [
    "PythonInterpreterTool",
    "FinalAnswerTool",
    "UserInputTool",
    "DuckDuckGoSearchTool",
    "GoogleSearchTool",
    "VisitWebpageTool",
    "SpeechToTextTool",
]

```

## File: src/smolagents/utils.py

<a name='file-src-smolagents-utils.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import ast
import inspect
import json
import re
import types
from typing import Dict, Tuple, Union

from rich.console import Console
from transformers.utils.import_utils import _is_package_available

_pygments_available = _is_package_available("pygments")


def is_pygments_available():
    return _pygments_available


console = Console(width=200)

BASE_BUILTIN_MODULES = [
    "collections",
    "datetime",
    "itertools",
    "math",
    "queue",
    "random",
    "re",
    "stat",
    "statistics",
    "time",
    "unicodedata",
]


class AgentError(Exception):
    """Base class for other agent-related exceptions"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message
        console.print(f"[bold red]{message}[/bold red]")


class AgentParsingError(AgentError):
    """Exception raised for errors in parsing in the agent"""

    pass


class AgentExecutionError(AgentError):
    """Exception raised for errors in execution in the agent"""

    pass


class AgentMaxStepsError(AgentError):
    """Exception raised for errors in execution in the agent"""

    pass


class AgentGenerationError(AgentError):
    """Exception raised for errors in generation in the agent"""

    pass


def parse_json_blob(json_blob: str) -> Dict[str, str]:
    try:
        first_accolade_index = json_blob.find("{")
        last_accolade_index = [a.start() for a in list(re.finditer("}", json_blob))][-1]
        json_blob = json_blob[first_accolade_index : last_accolade_index + 1].replace(
            '\\"', "'"
        )
        json_data = json.loads(json_blob, strict=False)
        return json_data
    except json.JSONDecodeError as e:
        place = e.pos
        if json_blob[place - 1 : place + 2] == "},\n":
            raise ValueError(
                "JSON is invalid: you probably tried to provide multiple tool calls in one action. PROVIDE ONLY ONE TOOL CALL."
            )
        raise ValueError(
            f"The JSON blob you used is invalid due to the following error: {e}.\n"
            f"JSON blob was: {json_blob}, decoding failed on that specific part of the blob:\n"
            f"'{json_blob[place - 4 : place + 5]}'."
        )
    except Exception as e:
        raise ValueError(f"Error in parsing the JSON blob: {e}")


def parse_code_blobs(code_blob: str) -> str:
    """Parses the LLM's output to get any code blob inside. Will return the code directly if it's code."""
    pattern = r"```(?:py|python)?\n(.*?)\n```"
    matches = re.findall(pattern, code_blob, re.DOTALL)
    if len(matches) == 0:
        try:  # Maybe the LLM outputted a code blob directly
            ast.parse(code_blob)
            return code_blob
        except SyntaxError:
            pass

        if "final" in code_blob and "answer" in code_blob:
            raise ValueError(
                f"""
The code blob is invalid, because the regex pattern {pattern} was not found in {code_blob=}. It seems like you're trying to return the final answer, you can do it as follows:
Code:
```py
final_answer("YOUR FINAL ANSWER HERE")
```<end_code>""".strip()
            )
        raise ValueError(
            f"""
The code blob is invalid, because the regex pattern {pattern} was not found in {code_blob=}. Make sure to include code with the correct pattern, for instance:
Thoughts: Your thoughts
Code:
```py
# Your python code here
```<end_code>""".strip()
        )
    return "\n\n".join(match.strip() for match in matches)


def parse_json_tool_call(json_blob: str) -> Tuple[str, Union[str, None]]:
    json_blob = json_blob.replace("```json", "").replace("```", "")
    tool_call = parse_json_blob(json_blob)
    tool_name_key, tool_arguments_key = None, None
    for possible_tool_name_key in ["action", "tool_name", "tool", "name", "function"]:
        if possible_tool_name_key in tool_call:
            tool_name_key = possible_tool_name_key
    for possible_tool_arguments_key in [
        "action_input",
        "tool_arguments",
        "tool_args",
        "parameters",
    ]:
        if possible_tool_arguments_key in tool_call:
            tool_arguments_key = possible_tool_arguments_key
    if tool_name_key is not None:
        if tool_arguments_key is not None:
            return tool_call[tool_name_key], tool_call[tool_arguments_key]
        else:
            return tool_call[tool_name_key], None
    error_msg = "No tool name key found in tool call!" + f" Tool call: {json_blob}"
    raise AgentParsingError(error_msg)


MAX_LENGTH_TRUNCATE_CONTENT = 20000


def truncate_content(
    content: str, max_length: int = MAX_LENGTH_TRUNCATE_CONTENT
) -> str:
    if len(content) <= max_length:
        return content
    else:
        return (
            content[: MAX_LENGTH_TRUNCATE_CONTENT // 2]
            + f"\n..._This content has been truncated to stay below {max_length} characters_...\n"
            + content[-MAX_LENGTH_TRUNCATE_CONTENT // 2 :]
        )


class ImportFinder(ast.NodeVisitor):
    def __init__(self):
        self.packages = set()

    def visit_Import(self, node):
        for alias in node.names:
            # Get the base package name (before any dots)
            base_package = alias.name.split(".")[0]
            self.packages.add(base_package)

    def visit_ImportFrom(self, node):
        if node.module:  # for "from x import y" statements
            # Get the base package name (before any dots)
            base_package = node.module.split(".")[0]
            self.packages.add(base_package)


def get_method_source(method):
    """Get source code for a method, including bound methods."""
    if isinstance(method, types.MethodType):
        method = method.__func__
    return inspect.getsource(method).strip()


def is_same_method(method1, method2):
    """Compare two methods by their source code."""
    try:
        source1 = get_method_source(method1)
        source2 = get_method_source(method2)

        # Remove method decorators if any
        source1 = "\n".join(
            line for line in source1.split("\n") if not line.strip().startswith("@")
        )
        source2 = "\n".join(
            line for line in source2.split("\n") if not line.strip().startswith("@")
        )

        return source1 == source2
    except (TypeError, OSError):
        return False


def is_same_item(item1, item2):
    """Compare two class items (methods or attributes) for equality."""
    if callable(item1) and callable(item2):
        return is_same_method(item1, item2)
    else:
        return item1 == item2


def instance_to_source(instance, base_cls=None):
    """Convert an instance to its class source code representation."""
    cls = instance.__class__
    class_name = cls.__name__

    # Start building class lines
    class_lines = []
    if base_cls:
        class_lines.append(f"class {class_name}({base_cls.__name__}):")
    else:
        class_lines.append(f"class {class_name}:")

    # Add docstring if it exists and differs from base
    if cls.__doc__ and (not base_cls or cls.__doc__ != base_cls.__doc__):
        class_lines.append(f'    """{cls.__doc__}"""')

    # Add class-level attributes
    class_attrs = {
        name: value
        for name, value in cls.__dict__.items()
        if not name.startswith("__")
        and not callable(value)
        and not (
            base_cls and hasattr(base_cls, name) and getattr(base_cls, name) == value
        )
    }

    for name, value in class_attrs.items():
        if isinstance(value, str):
            if "\n" in value:
                class_lines.append(f'    {name} = """{value}"""')
            else:
                class_lines.append(f'    {name} = "{value}"')
        else:
            class_lines.append(f"    {name} = {repr(value)}")

    if class_attrs:
        class_lines.append("")

    # Add methods
    methods = {
        name: func
        for name, func in cls.__dict__.items()
        if callable(func)
        and not (
            base_cls
            and hasattr(base_cls, name)
            and getattr(base_cls, name).__code__.co_code == func.__code__.co_code
        )
    }

    for name, method in methods.items():
        method_source = inspect.getsource(method)
        # Clean up the indentation
        method_lines = method_source.split("\n")
        first_line = method_lines[0]
        indent = len(first_line) - len(first_line.lstrip())
        method_lines = [line[indent:] for line in method_lines]
        method_source = "\n".join(
            ["    " + line if line.strip() else line for line in method_lines]
        )
        class_lines.append(method_source)
        class_lines.append("")

    # Find required imports using ImportFinder
    import_finder = ImportFinder()
    import_finder.visit(ast.parse("\n".join(class_lines)))
    required_imports = import_finder.packages

    # Build final code with imports
    final_lines = []

    # Add base class import if needed
    if base_cls:
        final_lines.append(f"from {base_cls.__module__} import {base_cls.__name__}")

    # Add discovered imports
    for package in required_imports:
        final_lines.append(f"import {package}")

    if final_lines:  # Add empty line after imports
        final_lines.append("")

    # Add the class code
    final_lines.extend(class_lines)

    return "\n".join(final_lines)


__all__ = ["AgentError"]

```

## File: src/smolagents/types.py

<a name='file-src-smolagents-types.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import os
import pathlib
import tempfile
import uuid
from io import BytesIO

import numpy as np
import requests
from transformers.utils import (
    is_torch_available,
    is_vision_available,
)
from transformers.utils.import_utils import _is_package_available

logger = logging.getLogger(__name__)

if is_vision_available():
    from PIL import Image
    from PIL.Image import Image as ImageType
else:
    ImageType = object

if is_torch_available():
    import torch
    from torch import Tensor
else:
    Tensor = object

if _is_package_available("soundfile"):
    import soundfile as sf


class AgentType:
    """
    Abstract class to be reimplemented to define types that can be returned by agents.

    These objects serve three purposes:

    - They behave as they were the type they're meant to be, e.g., a string for text, a PIL.Image for images
    - They can be stringified: str(object) in order to return a string defining the object
    - They should be displayed correctly in ipython notebooks/colab/jupyter
    """

    def __init__(self, value):
        self._value = value

    def __str__(self):
        return self.to_string()

    def to_raw(self):
        logger.error(
            "This is a raw AgentType of unknown type. Display in notebooks and string conversion will be unreliable"
        )
        return self._value

    def to_string(self) -> str:
        logger.error(
            "This is a raw AgentType of unknown type. Display in notebooks and string conversion will be unreliable"
        )
        return str(self._value)


class AgentText(AgentType, str):
    """
    Text type returned by the agent. Behaves as a string.
    """

    def to_raw(self):
        return self._value

    def to_string(self):
        return str(self._value)


class AgentImage(AgentType, ImageType):
    """
    Image type returned by the agent. Behaves as a PIL.Image.
    """

    def __init__(self, value):
        AgentType.__init__(self, value)
        ImageType.__init__(self)

        if not is_vision_available():
            raise ImportError("PIL must be installed in order to handle images.")

        self._path = None
        self._raw = None
        self._tensor = None

        if isinstance(value, AgentImage):
            self._raw, self._path, self._tensor = value._raw, value._path, value._tensor
        elif isinstance(value, ImageType):
            self._raw = value
        elif isinstance(value, bytes):
            self._raw = Image.open(BytesIO(value))
        elif isinstance(value, (str, pathlib.Path)):
            self._path = value
        elif isinstance(value, torch.Tensor):
            self._tensor = value
        elif isinstance(value, np.ndarray):
            self._tensor = torch.from_numpy(value)
        else:
            raise TypeError(
                f"Unsupported type for {self.__class__.__name__}: {type(value)}"
            )

    def _ipython_display_(self, include=None, exclude=None):
        """
        Displays correctly this type in an ipython notebook (ipython, colab, jupyter, ...)
        """
        from IPython.display import Image, display

        display(Image(self.to_string()))

    def to_raw(self):
        """
        Returns the "raw" version of that object. In the case of an AgentImage, it is a PIL.Image.
        """
        if self._raw is not None:
            return self._raw

        if self._path is not None:
            self._raw = Image.open(self._path)
            return self._raw

        if self._tensor is not None:
            array = self._tensor.cpu().detach().numpy()
            return Image.fromarray((255 - array * 255).astype(np.uint8))

    def to_string(self):
        """
        Returns the stringified version of that object. In the case of an AgentImage, it is a path to the serialized
        version of the image.
        """
        if self._path is not None:
            return self._path

        if self._raw is not None:
            directory = tempfile.mkdtemp()
            self._path = os.path.join(directory, str(uuid.uuid4()) + ".png")
            self._raw.save(self._path, format="png")
            return self._path

        if self._tensor is not None:
            array = self._tensor.cpu().detach().numpy()

            # There is likely simpler than load into image into save
            img = Image.fromarray((255 - array * 255).astype(np.uint8))

            directory = tempfile.mkdtemp()
            self._path = os.path.join(directory, str(uuid.uuid4()) + ".png")
            img.save(self._path, format="png")

            return self._path

    def save(self, output_bytes, format: str = None, **params):
        """
        Saves the image to a file.
        Args:
            output_bytes (bytes): The output bytes to save the image to.
            format (str): The format to use for the output image. The format is the same as in PIL.Image.save.
            **params: Additional parameters to pass to PIL.Image.save.
        """
        img = self.to_raw()
        img.save(output_bytes, format=format, **params)


class AgentAudio(AgentType, str):
    """
    Audio type returned by the agent.
    """

    def __init__(self, value, samplerate=16_000):
        super().__init__(value)

        if not _is_package_available("soundfile"):
            raise ImportError("soundfile must be installed in order to handle audio.")

        self._path = None
        self._tensor = None

        self.samplerate = samplerate
        if isinstance(value, (str, pathlib.Path)):
            self._path = value
        elif is_torch_available() and isinstance(value, torch.Tensor):
            self._tensor = value
        elif isinstance(value, tuple):
            self.samplerate = value[0]
            if isinstance(value[1], np.ndarray):
                self._tensor = torch.from_numpy(value[1])
            else:
                self._tensor = torch.tensor(value[1])
        else:
            raise ValueError(f"Unsupported audio type: {type(value)}")

    def _ipython_display_(self, include=None, exclude=None):
        """
        Displays correctly this type in an ipython notebook (ipython, colab, jupyter, ...)
        """
        from IPython.display import Audio, display

        display(Audio(self.to_string(), rate=self.samplerate))

    def to_raw(self):
        """
        Returns the "raw" version of that object. It is a `torch.Tensor` object.
        """
        if self._tensor is not None:
            return self._tensor

        if self._path is not None:
            if "://" in str(self._path):
                response = requests.get(self._path)
                response.raise_for_status()
                tensor, self.samplerate = sf.read(BytesIO(response.content))
            else:
                tensor, self.samplerate = sf.read(self._path)
            self._tensor = torch.tensor(tensor)
            return self._tensor

    def to_string(self):
        """
        Returns the stringified version of that object. In the case of an AgentAudio, it is a path to the serialized
        version of the audio.
        """
        if self._path is not None:
            return self._path

        if self._tensor is not None:
            directory = tempfile.mkdtemp()
            self._path = os.path.join(directory, str(uuid.uuid4()) + ".wav")
            sf.write(self._path, self._tensor, samplerate=self.samplerate)
            return self._path


AGENT_TYPE_MAPPING = {"string": AgentText, "image": AgentImage, "audio": AgentAudio}
INSTANCE_TYPE_MAPPING = {
    str: AgentText,
    ImageType: AgentImage,
    Tensor: AgentAudio,
}

if is_torch_available():
    INSTANCE_TYPE_MAPPING[Tensor] = AgentAudio


def handle_agent_input_types(*args, **kwargs):
    args = [(arg.to_raw() if isinstance(arg, AgentType) else arg) for arg in args]
    kwargs = {
        k: (v.to_raw() if isinstance(v, AgentType) else v) for k, v in kwargs.items()
    }
    return args, kwargs


def handle_agent_output_types(output, output_type=None):
    if output_type in AGENT_TYPE_MAPPING:
        # If the class has defined outputs, we can map directly according to the class definition
        decoded_outputs = AGENT_TYPE_MAPPING[output_type](output)
        return decoded_outputs
    else:
        # If the class does not have defined output, then we map according to the type
        for _k, _v in INSTANCE_TYPE_MAPPING.items():
            if isinstance(output, _k):
                if (
                    _k is not object
                ):  # avoid converting to audio if torch is not installed
                    return _v(output)
        return output


__all__ = ["AgentType", "AgentImage", "AgentText", "AgentAudio"]

```

## File: src/smolagents/local_python_executor.py

<a name='file-src-smolagents-local_python_executor.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import ast
import builtins
import difflib
import math
import re
from collections.abc import Mapping
from importlib import import_module
from typing import Any, Callable, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

from .utils import BASE_BUILTIN_MODULES, truncate_content


class InterpreterError(ValueError):
    """
    An error raised when the interpreter cannot evaluate a Python expression, due to syntax error or unsupported
    operations.
    """

    pass


ERRORS = {
    name: getattr(builtins, name)
    for name in dir(builtins)
    if isinstance(getattr(builtins, name), type)
    and issubclass(getattr(builtins, name), BaseException)
}

PRINT_OUTPUTS, MAX_LEN_OUTPUT = "", 50000
OPERATIONS_COUNT, MAX_OPERATIONS = 0, 10000000


def custom_print(*args):
    return None


BASE_PYTHON_TOOLS = {
    "print": custom_print,
    "isinstance": isinstance,
    "range": range,
    "float": float,
    "int": int,
    "bool": bool,
    "str": str,
    "set": set,
    "list": list,
    "dict": dict,
    "tuple": tuple,
    "round": round,
    "ceil": math.ceil,
    "floor": math.floor,
    "log": math.log,
    "exp": math.exp,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "atan2": math.atan2,
    "degrees": math.degrees,
    "radians": math.radians,
    "pow": math.pow,
    "sqrt": math.sqrt,
    "len": len,
    "sum": sum,
    "max": max,
    "min": min,
    "abs": abs,
    "enumerate": enumerate,
    "zip": zip,
    "reversed": reversed,
    "sorted": sorted,
    "all": all,
    "any": any,
    "map": map,
    "filter": filter,
    "ord": ord,
    "chr": chr,
    "next": next,
    "iter": iter,
    "divmod": divmod,
    "callable": callable,
    "getattr": getattr,
    "hasattr": hasattr,
    "setattr": setattr,
    "issubclass": issubclass,
    "type": type,
    "complex": complex,
}


class BreakException(Exception):
    pass


class ContinueException(Exception):
    pass


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value


def get_iterable(obj):
    if isinstance(obj, list):
        return obj
    elif hasattr(obj, "__iter__"):
        return list(obj)
    else:
        raise InterpreterError("Object is not iterable")


def fix_final_answer_code(code: str) -> str:
    """
    Sometimes an LLM can try to assign a variable to final_answer, which would break the final_answer() tool.
    This function fixes this behaviour by replacing variable assignments to final_answer with final_answer_variable,
    while preserving function calls to final_answer().
    """
    # First, find if there's a direct assignment to final_answer
    # Use word boundary and negative lookbehind to ensure it's not an object attribute
    assignment_pattern = r"(?<!\.)(?<!\w)\bfinal_answer\s*="
    if "final_answer(" not in code or not re.search(assignment_pattern, code):
        # If final_answer tool is not called in this blob, then doing the replacement is hazardous because it could false the model's memory for next steps.
        # Let's not modify the code and leave the subsequent assignment error happen.
        return code

    # Pattern for replacing variable assignments
    # Looks for 'final_answer' followed by '=' with optional whitespace
    # Negative lookbehind ensures we don't match object attributes
    assignment_regex = r"(?<!\.)(?<!\w)(\bfinal_answer)(\s*=)"
    code = re.sub(assignment_regex, r"final_answer_variable\2", code)

    # Pattern for replacing variable usage but not function calls
    # Negative lookahead (?!\s*\() ensures we don't match function calls
    # Negative lookbehind (?<!\.|\w) ensures we don't match object methods or other variables
    variable_regex = r"(?<!\.)(?<!\w)(\bfinal_answer\b)(?!\s*\()"
    code = re.sub(variable_regex, "final_answer_variable", code)
    return code


def evaluate_unaryop(
    expression: ast.UnaryOp,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> Any:
    operand = evaluate_ast(
        expression.operand, state, static_tools, custom_tools, authorized_imports
    )
    if isinstance(expression.op, ast.USub):
        return -operand
    elif isinstance(expression.op, ast.UAdd):
        return operand
    elif isinstance(expression.op, ast.Not):
        return not operand
    elif isinstance(expression.op, ast.Invert):
        return ~operand
    else:
        raise InterpreterError(
            f"Unary operation {expression.op.__class__.__name__} is not supported."
        )


def evaluate_lambda(
    lambda_expression: ast.Lambda,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> Callable:
    args = [arg.arg for arg in lambda_expression.args.args]

    def lambda_func(*values: Any) -> Any:
        new_state = state.copy()
        for arg, value in zip(args, values):
            new_state[arg] = value
        return evaluate_ast(
            lambda_expression.body,
            new_state,
            static_tools,
            custom_tools,
            authorized_imports,
        )

    return lambda_func


def evaluate_while(
    while_loop: ast.While,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> None:
    max_iterations = 1000
    iterations = 0
    while evaluate_ast(
        while_loop.test, state, static_tools, custom_tools, authorized_imports
    ):
        for node in while_loop.body:
            try:
                evaluate_ast(
                    node, state, static_tools, custom_tools, authorized_imports
                )
            except BreakException:
                return None
            except ContinueException:
                break
        iterations += 1
        if iterations > max_iterations:
            raise InterpreterError(
                f"Maximum number of {max_iterations} iterations in While loop exceeded"
            )
    return None


def create_function(
    func_def: ast.FunctionDef,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> Callable:
    def new_func(*args: Any, **kwargs: Any) -> Any:
        func_state = state.copy()
        arg_names = [arg.arg for arg in func_def.args.args]
        default_values = [
            evaluate_ast(d, state, static_tools, custom_tools, authorized_imports)
            for d in func_def.args.defaults
        ]

        # Apply default values
        defaults = dict(zip(arg_names[-len(default_values) :], default_values))

        # Set positional arguments
        for name, value in zip(arg_names, args):
            func_state[name] = value

        # Set keyword arguments
        for name, value in kwargs.items():
            func_state[name] = value

        # Handle variable arguments
        if func_def.args.vararg:
            vararg_name = func_def.args.vararg.arg
            func_state[vararg_name] = args

        if func_def.args.kwarg:
            kwarg_name = func_def.args.kwarg.arg
            func_state[kwarg_name] = kwargs

        # Set default values for arguments that were not provided
        for name, value in defaults.items():
            if name not in func_state:
                func_state[name] = value

        # Update function state with self and __class__
        if func_def.args.args and func_def.args.args[0].arg == "self":
            if args:
                func_state["self"] = args[0]
                func_state["__class__"] = args[0].__class__

        result = None
        try:
            for stmt in func_def.body:
                result = evaluate_ast(
                    stmt, func_state, static_tools, custom_tools, authorized_imports
                )
        except ReturnException as e:
            result = e.value

        if func_def.name == "__init__":
            return None

        return result

    return new_func


def evaluate_function_def(
    func_def: ast.FunctionDef,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> Callable:
    custom_tools[func_def.name] = create_function(
        func_def, state, static_tools, custom_tools, authorized_imports
    )
    return custom_tools[func_def.name]


def evaluate_class_def(
    class_def: ast.ClassDef,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> type:
    class_name = class_def.name
    bases = [
        evaluate_ast(base, state, static_tools, custom_tools, authorized_imports)
        for base in class_def.bases
    ]
    class_dict = {}

    for stmt in class_def.body:
        if isinstance(stmt, ast.FunctionDef):
            class_dict[stmt.name] = evaluate_function_def(
                stmt, state, static_tools, custom_tools, authorized_imports
            )
        elif isinstance(stmt, ast.Assign):
            for target in stmt.targets:
                if isinstance(target, ast.Name):
                    class_dict[target.id] = evaluate_ast(
                        stmt.value,
                        state,
                        static_tools,
                        custom_tools,
                        authorized_imports,
                    )
                elif isinstance(target, ast.Attribute):
                    class_dict[target.attr] = evaluate_ast(
                        stmt.value,
                        state,
                        static_tools,
                        custom_tools,
                        authorized_imports,
                    )
        else:
            raise InterpreterError(
                f"Unsupported statement in class body: {stmt.__class__.__name__}"
            )

    new_class = type(class_name, tuple(bases), class_dict)
    state[class_name] = new_class
    return new_class


def evaluate_augassign(
    expression: ast.AugAssign,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> Any:
    def get_current_value(target: ast.AST) -> Any:
        if isinstance(target, ast.Name):
            return state.get(target.id, 0)
        elif isinstance(target, ast.Subscript):
            obj = evaluate_ast(
                target.value, state, static_tools, custom_tools, authorized_imports
            )
            key = evaluate_ast(
                target.slice, state, static_tools, custom_tools, authorized_imports
            )
            return obj[key]
        elif isinstance(target, ast.Attribute):
            obj = evaluate_ast(
                target.value, state, static_tools, custom_tools, authorized_imports
            )
            return getattr(obj, target.attr)
        elif isinstance(target, ast.Tuple):
            return tuple(get_current_value(elt) for elt in target.elts)
        elif isinstance(target, ast.List):
            return [get_current_value(elt) for elt in target.elts]
        else:
            raise InterpreterError(
                "AugAssign not supported for {type(target)} targets."
            )

    current_value = get_current_value(expression.target)
    value_to_add = evaluate_ast(
        expression.value, state, static_tools, custom_tools, authorized_imports
    )

    if isinstance(expression.op, ast.Add):
        if isinstance(current_value, list):
            if not isinstance(value_to_add, list):
                raise InterpreterError(
                    f"Cannot add non-list value {value_to_add} to a list."
                )
            updated_value = current_value + value_to_add
        else:
            updated_value = current_value + value_to_add
    elif isinstance(expression.op, ast.Sub):
        updated_value = current_value - value_to_add
    elif isinstance(expression.op, ast.Mult):
        updated_value = current_value * value_to_add
    elif isinstance(expression.op, ast.Div):
        updated_value = current_value / value_to_add
    elif isinstance(expression.op, ast.Mod):
        updated_value = current_value % value_to_add
    elif isinstance(expression.op, ast.Pow):
        updated_value = current_value**value_to_add
    elif isinstance(expression.op, ast.FloorDiv):
        updated_value = current_value // value_to_add
    elif isinstance(expression.op, ast.BitAnd):
        updated_value = current_value & value_to_add
    elif isinstance(expression.op, ast.BitOr):
        updated_value = current_value | value_to_add
    elif isinstance(expression.op, ast.BitXor):
        updated_value = current_value ^ value_to_add
    elif isinstance(expression.op, ast.LShift):
        updated_value = current_value << value_to_add
    elif isinstance(expression.op, ast.RShift):
        updated_value = current_value >> value_to_add
    else:
        raise InterpreterError(
            f"Operation {type(expression.op).__name__} is not supported."
        )

    # Update the state
    set_value(
        expression.target,
        updated_value,
        state,
        static_tools,
        custom_tools,
        authorized_imports,
    )

    return updated_value


def evaluate_boolop(
    node: ast.BoolOp,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> bool:
    if isinstance(node.op, ast.And):
        for value in node.values:
            if not evaluate_ast(
                value, state, static_tools, custom_tools, authorized_imports
            ):
                return False
        return True
    elif isinstance(node.op, ast.Or):
        for value in node.values:
            if evaluate_ast(
                value, state, static_tools, custom_tools, authorized_imports
            ):
                return True
        return False


def evaluate_binop(
    binop: ast.BinOp,
    state: Dict[str, Any],
    static_tools: Dict[str, Callable],
    custom_tools: Dict[str, Callable],
    authorized_imports: List[str],
) -> Any:
    # Recursively evaluate the left and right operands
    left_val = evaluate_ast(
        binop.left, state, static_tools, custom_tools, authorized_imports
    )
    right_val = evaluate_ast(
        binop.right, state, static_tools, custom_tools, authorized_imports
    )

    # Determine the operation based on the type of the operator in the BinOp
    if isinstance(binop.op, ast.Add):
        return left_val + right_val
    elif isinstance(binop.op, ast.Sub):
        return left_val - right_val
    elif isinstance(binop.op, ast.Mult):
        return left_val * right_val
    elif isinstance(binop.op, ast.Div):
        return left_val / right_val
    elif isinstance(binop.op, ast.Mod):
        return left_val % right_val
    elif isinstance(binop.op, ast.Pow):
        return left_val**right_val
    elif isinstance(binop.op, ast.FloorDiv):
        return left_val // right_val
    elif isinstance(binop.op, ast.BitAnd):
        return left_val & right_val
    elif isinstance(binop.op, ast.BitOr):
        return left_val | right_val
    elif isinstance(binop.op, ast.BitXor):
        return left_val ^ right_val
    elif isinstance(binop.op, ast.LShift):
        return left_val << right_val
    elif isinstance(binop.op, ast.RShift):
        return left_val >> right_val
    else:
        raise NotImplementedError(

*Content truncated for brevity.*

```

## File: src/smolagents/tools.py

<a name='file-src-smolagents-tools.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import ast
import importlib
import inspect
import json
import logging
import os
import sys
import tempfile
import textwrap
from functools import lru_cache, wraps
from pathlib import Path
from typing import Callable, Dict, Optional, Union, get_type_hints

from huggingface_hub import (
    create_repo,
    get_collection,
    hf_hub_download,
    metadata_update,
    upload_folder,
)
from huggingface_hub.utils import RepositoryNotFoundError
from packaging import version
from transformers.dynamic_module_utils import get_imports
from transformers.utils import (
    TypeHintParsingException,
    cached_file,
    get_json_schema,
    is_accelerate_available,
    is_torch_available,
)
from transformers.utils.chat_template_utils import _parse_type_hint

from .tool_validation import MethodChecker, validate_tool_attributes
from .types import ImageType, handle_agent_input_types, handle_agent_output_types
from .utils import instance_to_source

logger = logging.getLogger(__name__)

if is_accelerate_available():
    from accelerate import PartialState
    from accelerate.utils import send_to_device

if is_torch_available():
    from transformers import AutoProcessor
else:
    AutoProcessor = object

TOOL_CONFIG_FILE = "tool_config.json"


def get_repo_type(repo_id, repo_type=None, **hub_kwargs):
    if repo_type is not None:
        return repo_type
    try:
        hf_hub_download(repo_id, TOOL_CONFIG_FILE, repo_type="space", **hub_kwargs)
        return "space"
    except RepositoryNotFoundError:
        try:
            hf_hub_download(repo_id, TOOL_CONFIG_FILE, repo_type="model", **hub_kwargs)
            return "model"
        except RepositoryNotFoundError:
            raise EnvironmentError(
                f"`{repo_id}` does not seem to be a valid repo identifier on the Hub."
            )
        except Exception:
            return "model"
    except Exception:
        return "space"


def validate_after_init(cls):
    original_init = cls.__init__

    @wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.validate_arguments()

    cls.__init__ = new_init
    return cls


def _convert_type_hints_to_json_schema(func: Callable) -> Dict:
    type_hints = get_type_hints(func)
    signature = inspect.signature(func)
    properties = {}
    for param_name, param_type in type_hints.items():
        if param_name != "return":
            properties[param_name] = _parse_type_hint(param_type)
            if signature.parameters[param_name].default != inspect.Parameter.empty:
                properties[param_name]["nullable"] = True
    for param_name in signature.parameters.keys():
        if signature.parameters[param_name].default != inspect.Parameter.empty:
            if (
                param_name not in properties
            ):  # this can happen if the param has no type hint but a default value
                properties[param_name] = {"nullable": True}
    return properties


AUTHORIZED_TYPES = [
    "string",
    "boolean",
    "integer",
    "number",
    "image",
    "audio",
    "any",
    "object",
]

CONVERSION_DICT = {"str": "string", "int": "integer", "float": "number"}


class Tool:
    """
    A base class for the functions used by the agent. Subclass this and implement the `forward` method as well as the
    following class attributes:

    - **description** (`str`) -- A short description of what your tool does, the inputs it expects and the output(s) it
      will return. For instance 'This is a tool that downloads a file from a `url`. It takes the `url` as input, and
      returns the text contained in the file'.
    - **name** (`str`) -- A performative name that will be used for your tool in the prompt to the agent. For instance
      `"text-classifier"` or `"image_generator"`.
    - **inputs** (`Dict[str, Dict[str, Union[str, type]]]`) -- The dict of modalities expected for the inputs.
      It has one `type`key and a `description`key.
      This is used by `launch_gradio_demo` or to make a nice space from your tool, and also can be used in the generated
      description for your tool.
    - **output_type** (`type`) -- The type of the tool output. This is used by `launch_gradio_demo`
      or to make a nice space from your tool, and also can be used in the generated description for your tool.

    You can also override the method [`~Tool.setup`] if your tool has an expensive operation to perform before being
    usable (such as loading a model). [`~Tool.setup`] will be called the first time you use your tool, but not at
    instantiation.
    """

    name: str
    description: str
    inputs: Dict[str, Dict[str, Union[str, type, bool]]]
    output_type: str

    def __init__(self, *args, **kwargs):
        self.is_initialized = False

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        validate_after_init(cls)

    def validate_arguments(self):
        required_attributes = {
            "description": str,
            "name": str,
            "inputs": dict,
            "output_type": str,
        }

        for attr, expected_type in required_attributes.items():
            attr_value = getattr(self, attr, None)
            if attr_value is None:
                raise TypeError(f"You must set an attribute {attr}.")
            if not isinstance(attr_value, expected_type):
                raise TypeError(
                    f"Attribute {attr} should have type {expected_type.__name__}, got {type(attr_value)} instead."
                )
        for input_name, input_content in self.inputs.items():
            assert isinstance(input_content, dict), (
                f"Input '{input_name}' should be a dictionary."
            )
            assert "type" in input_content and "description" in input_content, (
                f"Input '{input_name}' should have keys 'type' and 'description', has only {list(input_content.keys())}."
            )
            if input_content["type"] not in AUTHORIZED_TYPES:
                raise Exception(
                    f"Input '{input_name}': type '{input_content['type']}' is not an authorized value, should be one of {AUTHORIZED_TYPES}."
                )

        assert getattr(self, "output_type", None) in AUTHORIZED_TYPES

        # Validate forward function signature, except for Tools that use a "generic" signature (PipelineTool, SpaceToolWrapper)
        if not (
            hasattr(self, "skip_forward_signature_validation")
            and getattr(self, "skip_forward_signature_validation") is True
        ):
            signature = inspect.signature(self.forward)

            if not set(signature.parameters.keys()) == set(self.inputs.keys()):
                raise Exception(
                    "Tool's 'forward' method should take 'self' as its first argument, then its next arguments should match the keys of tool attribute 'inputs'."
                )

            json_schema = _convert_type_hints_to_json_schema(self.forward)
            for key, value in self.inputs.items():
                if "nullable" in value:
                    assert key in json_schema and "nullable" in json_schema[key], (
                        f"Nullable argument '{key}' in inputs should have key 'nullable' set to True in function signature."
                    )
                if key in json_schema and "nullable" in json_schema[key]:
                    assert "nullable" in value, (
                        f"Nullable argument '{key}' in function signature should have key 'nullable' set to True in inputs."
                    )

    def forward(self, *args, **kwargs):
        return NotImplementedError("Write this method in your subclass of `Tool`.")

    def __call__(self, *args, sanitize_inputs_outputs: bool = False, **kwargs):
        if not self.is_initialized:
            self.setup()

        # Handle the arguments might be passed as a single dictionary
        if len(args) == 1 and len(kwargs) == 0 and isinstance(args[0], dict):
            potential_kwargs = args[0]

            # If the dictionary keys match our input parameters, convert it to kwargs
            if all(key in self.inputs for key in potential_kwargs):
                args = ()
                kwargs = potential_kwargs

        if sanitize_inputs_outputs:
            args, kwargs = handle_agent_input_types(*args, **kwargs)
        outputs = self.forward(*args, **kwargs)
        if sanitize_inputs_outputs:
            outputs = handle_agent_output_types(outputs, self.output_type)
        return outputs

    def setup(self):
        """
        Overwrite this method here for any operation that is expensive and needs to be executed before you start using
        your tool. Such as loading a big model.
        """
        self.is_initialized = True

    def save(self, output_dir):
        """
        Saves the relevant code files for your tool so it can be pushed to the Hub. This will copy the code of your
        tool in `output_dir` as well as autogenerate:

        - a `tool.py` file containing the logic for your tool.
        - an `app.py` file providing an UI for your tool when it is exported to a Space with `tool.push_to_hub()`
        - a `requirements.txt` containing the names of the module used by your tool (as detected when inspecting its
          code)

        Args:
            output_dir (`str`): The folder in which you want to save your tool.
        """
        os.makedirs(output_dir, exist_ok=True)
        class_name = self.__class__.__name__
        tool_file = os.path.join(output_dir, "tool.py")

        # Save tool file
        if type(self).__name__ == "SimpleTool":
            # Check that imports are self-contained
            source_code = inspect.getsource(self.forward).replace("@tool", "")
            forward_node = ast.parse(textwrap.dedent(source_code))
            # If tool was created using '@tool' decorator, it has only a forward pass, so it's simpler to just get its code
            method_checker = MethodChecker(set())
            method_checker.visit(forward_node)

            if len(method_checker.errors) > 0:
                raise (ValueError("\n".join(method_checker.errors)))

            forward_source_code = inspect.getsource(self.forward)
            tool_code = textwrap.dedent(f"""
            from smolagents import Tool
            from typing import Optional

            class {class_name}(Tool):
                name = "{self.name}"
                description = "{self.description}"
                inputs = {json.dumps(self.inputs, separators=(",", ":"))}
                output_type = "{self.output_type}"
            """).strip()
            import re

            def add_self_argument(source_code: str) -> str:
                """Add 'self' as first argument to a function definition if not present."""
                pattern = r"def forward\(((?!self)[^)]*)\)"

                def replacement(match):
                    args = match.group(1).strip()
                    if args:  # If there are other arguments
                        return f"def forward(self, {args})"
                    return "def forward(self)"

                return re.sub(pattern, replacement, source_code)

            forward_source_code = forward_source_code.replace(self.name, "forward")
            forward_source_code = add_self_argument(forward_source_code)
            forward_source_code = forward_source_code.replace("@tool", "").strip()
            tool_code += "\n\n" + textwrap.indent(forward_source_code, "    ")

        else:  # If the tool was not created by the @tool decorator, it was made by subclassing Tool
            if type(self).__name__ in [
                "SpaceToolWrapper",
                "LangChainToolWrapper",
                "GradioToolWrapper",
            ]:
                raise ValueError(
                    "Cannot save objects created with from_space, from_langchain or from_gradio, as this would create errors."
                )

            validate_tool_attributes(self.__class__)

            tool_code = instance_to_source(self, base_cls=Tool)

        with open(tool_file, "w", encoding="utf-8") as f:
            f.write(tool_code.replace(":true,", ":True,").replace(":true}", ":True}"))

        # Save app file
        app_file = os.path.join(output_dir, "app.py")
        with open(app_file, "w", encoding="utf-8") as f:
            f.write(
                textwrap.dedent(f"""
            from smolagents import launch_gradio_demo
            from typing import Optional
            from tool import {class_name}

            tool = {class_name}()

            launch_gradio_demo(tool)
            """).lstrip()
            )

        # Save requirements file
        requirements_file = os.path.join(output_dir, "requirements.txt")

        imports = []
        for module in [tool_file]:
            imports.extend(get_imports(module))
        imports = list(
            set(
                [
                    el
                    for el in imports + ["smolagents"]
                    if el not in sys.stdlib_module_names
                ]
            )
        )
        with open(requirements_file, "w", encoding="utf-8") as f:
            f.write("\n".join(imports) + "\n")

    def push_to_hub(
        self,
        repo_id: str,
        commit_message: str = "Upload tool",
        private: Optional[bool] = None,
        token: Optional[Union[bool, str]] = None,
        create_pr: bool = False,
    ) -> str:
        """
        Upload the tool to the Hub.

        For this method to work properly, your tool must have been defined in a separate module (not `__main__`).
        For instance:
        ```
        from my_tool_module import MyTool
        my_tool = MyTool()
        my_tool.push_to_hub("my-username/my-space")
        ```

        Parameters:
            repo_id (`str`):
                The name of the repository you want to push your tool to. It should contain your organization name when
                pushing to a given organization.
            commit_message (`str`, *optional*, defaults to `"Upload tool"`):
                Message to commit while pushing.
            private (`bool`, *optional*):
                Whether to make the repo private. If `None` (default), the repo will be public unless the organization's default is private. This value is ignored if the repo already exists.
            token (`bool` or `str`, *optional*):
                The token to use as HTTP bearer authorization for remote files. If unset, will use the token generated
                when running `huggingface-cli login` (stored in `~/.huggingface`).
            create_pr (`bool`, *optional*, defaults to `False`):
                Whether or not to create a PR with the uploaded files or directly commit.
        """
        repo_url = create_repo(
            repo_id=repo_id,
            token=token,
            private=private,
            exist_ok=True,
            repo_type="space",
            space_sdk="gradio",
        )
        repo_id = repo_url.repo_id
        metadata_update(repo_id, {"tags": ["tool"]}, repo_type="space")

        with tempfile.TemporaryDirectory() as work_dir:
            # Save all files.
            self.save(work_dir)
            print(work_dir)
            with open(work_dir + "/tool.py", "r") as f:
                print("\n".join(f.readlines()))
            logger.info(
                f"Uploading the following files to {repo_id}: {','.join(os.listdir(work_dir))}"
            )
            return upload_folder(
                repo_id=repo_id,
                commit_message=commit_message,
                folder_path=work_dir,
                token=token,
                create_pr=create_pr,
                repo_type="space",
            )

    @classmethod
    def from_hub(
        cls,
        repo_id: str,
        token: Optional[str] = None,
        trust_remote_code: bool = False,
        **kwargs,
    ):
        """
        Loads a tool defined on the Hub.

        <Tip warning={true}>

        Loading a tool from the Hub means that you'll download the tool and execute it locally.
        ALWAYS inspect the tool you're downloading before loading it within your runtime, as you would do when
        installing a package using pip/npm/apt.

        </Tip>

        Args:
            repo_id (`str`):
                The name of the repo on the Hub where your tool is defined.
            token (`str`, *optional*):
                The token to identify you on hf.co. If unset, will use the token generated when running
                `huggingface-cli login` (stored in `~/.huggingface`).
            trust_remote_code(`str`, *optional*, defaults to False):
                This flags marks that you understand the risk of running remote code and that you trust this tool.
                If not setting this to True, loading the tool from Hub will fail.
            kwargs (additional keyword arguments, *optional*):
                Additional keyword arguments that will be split in two: all arguments relevant to the Hub (such as
                `cache_dir`, `revision`, `subfolder`) will be used when downloading the files for your tool, and the
                others will be passed along to its init.
        """
        assert trust_remote_code, (
            "Loading a tool from Hub requires to trust remote code. Make sure you've inspected the repo and pass `trust_remote_code=True` to load the tool."
        )

        hub_kwargs_names = [
            "cache_dir",
            "force_download",
            "resume_download",
            "proxies",
            "revision",
            "repo_type",
            "subfolder",
            "local_files_only",
        ]
        hub_kwargs = {k: v for k, v in kwargs.items() if k in hub_kwargs_names}

        tool_file = "tool.py"

        # Get the tool's tool.py file.
        hub_kwargs["repo_type"] = get_repo_type(repo_id, **hub_kwargs)
        resolved_tool_file = cached_file(
            repo_id,
            tool_file,
            token=token,
            **hub_kwargs,
            _raise_exceptions_for_gated_repo=False,
            _raise_exceptions_for_missing_entries=False,
            _raise_exceptions_for_connection_errors=False,
        )
        tool_code = resolved_tool_file is not None
        if resolved_tool_file is None:
            resolved_tool_file = cached_file(
                repo_id,
                tool_file,
                token=token,
                **hub_kwargs,
                _raise_exceptions_for_gated_repo=False,
                _raise_exceptions_for_missing_entries=False,
                _raise_exceptions_for_connection_errors=False,
            )
        if resolved_tool_file is None:
            raise EnvironmentError(
                f"{repo_id} does not appear to provide a valid configuration in `tool_config.json` or `config.json`."
            )

        with open(resolved_tool_file, encoding="utf-8") as reader:
            tool_code = "".join(reader.readlines())

        # Find the Tool subclass in the namespace
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save the code to a file
            module_path = os.path.join(temp_dir, "tool.py")
            with open(module_path, "w") as f:
                f.write(tool_code)

            print("TOOL CODE:\n", tool_code)

            # Load module from file path
            spec = importlib.util.spec_from_file_location("tool", module_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

*Content truncated for brevity.*

```

## File: src/smolagents/e2b_executor.py

<a name='file-src-smolagents-e2b_executor.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import base64
import pickle
import textwrap
from io import BytesIO
from typing import Any, List, Tuple

from dotenv import load_dotenv
from e2b_code_interpreter import Sandbox
from PIL import Image

from .tool_validation import validate_tool_attributes
from .tools import Tool
from .utils import BASE_BUILTIN_MODULES, instance_to_source

load_dotenv()


class E2BExecutor:
    def __init__(self, additional_imports: List[str], tools: List[Tool], logger):
        self.custom_tools = {}
        self.sbx = Sandbox()  # "qywp2ctmu2q7jzprcf4j")
        # TODO: validate installing agents package or not
        # print("Installing agents package on remote executor...")
        # self.sbx.commands.run(
        #     "pip install git+https://github.com/huggingface/smolagents.git",
        #     timeout=300
        # )
        # print("Installation of agents package finished.")
        self.logger = logger
        additional_imports = additional_imports + ["pickle5"]
        if len(additional_imports) > 0:
            execution = self.sbx.commands.run(
                "pip install " + " ".join(additional_imports)
            )
            if execution.error:
                raise Exception(f"Error installing dependencies: {execution.error}")
            else:
                logger.log(f"Installation of {additional_imports} succeeded!", 0)

        tool_codes = []
        for tool in tools:
            validate_tool_attributes(tool.__class__, check_imports=False)
            tool_code = instance_to_source(tool, base_cls=Tool)
            tool_code = tool_code.replace("from smolagents.tools import Tool", "")
            tool_code += f"\n{tool.name} = {tool.__class__.__name__}()\n"
            tool_codes.append(tool_code)

        tool_definition_code = "\n".join(
            [f"import {module}" for module in BASE_BUILTIN_MODULES]
        )
        tool_definition_code += textwrap.dedent("""
        class Tool:
            def __call__(self, *args, **kwargs):
                return self.forward(*args, **kwargs)

            def forward(self, *args, **kwargs):
                pass # to be implemented in child class
        """)
        tool_definition_code += "\n\n".join(tool_codes)

        tool_definition_execution = self.run_code_raise_errors(tool_definition_code)
        self.logger.log(tool_definition_execution.logs)

    def run_code_raise_errors(self, code: str):
        execution = self.sbx.run_code(
            code,
        )
        if execution.error:
            execution_logs = "\n".join([str(log) for log in execution.logs.stdout])
            logs = execution_logs
            logs += "Executing code yielded an error:"
            logs += execution.error.name
            logs += execution.error.value
            logs += execution.error.traceback
            raise ValueError(logs)
        return execution

    def __call__(self, code_action: str, additional_args: dict) -> Tuple[Any, Any]:
        if len(additional_args) > 0:
            # Pickle additional_args to server
            import tempfile

            with tempfile.NamedTemporaryFile() as f:
                pickle.dump(additional_args, f)
                f.flush()
                with open(f.name, "rb") as file:
                    self.sbx.files.write("/home/state.pkl", file)
            remote_unloading_code = """import pickle
import os
print("File path", os.path.getsize('/home/state.pkl'))
with open('/home/state.pkl', 'rb') as f:
    pickle_dict = pickle.load(f)
locals().update({key: value for key, value in pickle_dict.items()})
"""
            execution = self.run_code_raise_errors(remote_unloading_code)
            execution_logs = "\n".join([str(log) for log in execution.logs.stdout])
            self.logger.log(execution_logs, 1)

        execution = self.run_code_raise_errors(code_action)
        execution_logs = "\n".join([str(log) for log in execution.logs.stdout])
        if not execution.results:
            return None, execution_logs
        else:
            for result in execution.results:
                if result.is_main_result:
                    for attribute_name in ["jpeg", "png"]:
                        if getattr(result, attribute_name) is not None:
                            image_output = getattr(result, attribute_name)
                            decoded_bytes = base64.b64decode(
                                image_output.encode("utf-8")
                            )
                            return Image.open(BytesIO(decoded_bytes)), execution_logs
                    for attribute_name in [
                        "chart",
                        "data",
                        "html",
                        "javascript",
                        "json",
                        "latex",
                        "markdown",
                        "pdf",
                        "svg",
                        "text",
                    ]:
                        if getattr(result, attribute_name) is not None:
                            return getattr(result, attribute_name), execution_logs
            raise ValueError("No main result returned by executor!")


__all__ = ["E2BExecutor"]

```

## File: src/smolagents/tool_validation.py

<a name='file-src-smolagents-tool_validation.py'></a>
*Description*: This is a Python script.

```python
import ast
import builtins
import inspect
import textwrap
from typing import Set

from .utils import BASE_BUILTIN_MODULES

_BUILTIN_NAMES = set(vars(builtins))


class MethodChecker(ast.NodeVisitor):
    """
    Checks that a method
    - only uses defined names
    - contains no local imports (e.g. numpy is ok but local_script is not)
    """

    def __init__(self, class_attributes: Set[str], check_imports: bool = True):
        self.undefined_names = set()
        self.imports = {}
        self.from_imports = {}
        self.assigned_names = set()
        self.arg_names = set()
        self.class_attributes = class_attributes
        self.errors = []
        self.check_imports = check_imports

    def visit_arguments(self, node):
        """Collect function arguments"""
        self.arg_names = {arg.arg for arg in node.args}
        if node.kwarg:
            self.arg_names.add(node.kwarg.arg)
        if node.vararg:
            self.arg_names.add(node.vararg.arg)

    def visit_Import(self, node):
        for name in node.names:
            actual_name = name.asname or name.name
            self.imports[actual_name] = name.name

    def visit_ImportFrom(self, node):
        module = node.module or ""
        for name in node.names:
            actual_name = name.asname or name.name
            self.from_imports[actual_name] = (module, name.name)

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.assigned_names.add(target.id)
        self.visit(node.value)

    def visit_With(self, node):
        """Track aliases in 'with' statements (the 'y' in 'with X as y')"""
        for item in node.items:
            if item.optional_vars:  # This is the 'y' in 'with X as y'
                if isinstance(item.optional_vars, ast.Name):
                    self.assigned_names.add(item.optional_vars.id)
        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        """Track exception aliases (the 'e' in 'except Exception as e')"""
        if node.name:  # This is the 'e' in 'except Exception as e'
            self.assigned_names.add(node.name)
        self.generic_visit(node)

    def visit_AnnAssign(self, node):
        """Track annotated assignments."""
        if isinstance(node.target, ast.Name):
            self.assigned_names.add(node.target.id)
        if node.value:
            self.visit(node.value)

    def visit_For(self, node):
        target = node.target
        if isinstance(target, ast.Name):
            self.assigned_names.add(target.id)
        elif isinstance(target, ast.Tuple):
            for elt in target.elts:
                if isinstance(elt, ast.Name):
                    self.assigned_names.add(elt.id)
        self.generic_visit(node)

    def visit_Attribute(self, node):
        if not (isinstance(node.value, ast.Name) and node.value.id == "self"):
            self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            if not (
                node.id in _BUILTIN_NAMES
                or node.id in BASE_BUILTIN_MODULES
                or node.id in self.arg_names
                or node.id == "self"
                or node.id in self.class_attributes
                or node.id in self.imports
                or node.id in self.from_imports
                or node.id in self.assigned_names
            ):
                self.errors.append(f"Name '{node.id}' is undefined.")

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if not (
                node.func.id in _BUILTIN_NAMES
                or node.func.id in BASE_BUILTIN_MODULES
                or node.func.id in self.arg_names
                or node.func.id == "self"
                or node.func.id in self.class_attributes
                or node.func.id in self.imports
                or node.func.id in self.from_imports
                or node.func.id in self.assigned_names
            ):
                self.errors.append(f"Name '{node.func.id}' is undefined.")
        self.generic_visit(node)


def validate_tool_attributes(cls, check_imports: bool = True) -> None:
    """
    Validates that a Tool class follows the proper patterns:
    0. __init__ takes no argument (args chosen at init are not traceable so we cannot rebuild the source code for them, make them class attributes!).
    1. About the class:
        - Class attributes should only be strings or dicts
        - Class attributes cannot be complex attributes
    2. About all class methods:
        - Imports must be from packages, not local files
        - All methods must be self-contained

    Raises all errors encountered, if no error returns None.
    """
    errors = []

    source = textwrap.dedent(inspect.getsource(cls))

    tree = ast.parse(source)

    if not isinstance(tree.body[0], ast.ClassDef):
        raise ValueError("Source code must define a class")

    # Check that __init__ method takes no arguments
    if not cls.__init__.__qualname__ == "Tool.__init__":
        sig = inspect.signature(cls.__init__)
        non_self_params = list(
            [arg_name for arg_name in sig.parameters.keys() if arg_name != "self"]
        )
        if len(non_self_params) > 0:
            errors.append(
                f"This tool has additional args specified in __init__(self): {non_self_params}. Make sure it does not, all values should be hardcoded!"
            )

    class_node = tree.body[0]

    class ClassLevelChecker(ast.NodeVisitor):
        def __init__(self):
            self.imported_names = set()
            self.complex_attributes = set()
            self.class_attributes = set()
            self.in_method = False

        def visit_FunctionDef(self, node):
            old_context = self.in_method
            self.in_method = True
            self.generic_visit(node)
            self.in_method = old_context

        def visit_Assign(self, node):
            if self.in_method:
                return
            # Track class attributes
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.class_attributes.add(target.id)

            # Check if the assignment is more complex than simple literals
            if not all(
                isinstance(
                    val, (ast.Str, ast.Num, ast.Constant, ast.Dict, ast.List, ast.Set)
                )
                for val in ast.walk(node.value)
            ):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        self.complex_attributes.add(target.id)

    class_level_checker = ClassLevelChecker()
    class_level_checker.visit(class_node)

    if class_level_checker.complex_attributes:
        errors.append(
            f"Complex attributes should be defined in __init__, not as class attributes: "
            f"{', '.join(class_level_checker.complex_attributes)}"
        )

    # Run checks on all methods
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef):
            method_checker = MethodChecker(
                class_level_checker.class_attributes, check_imports=check_imports
            )
            method_checker.visit(node)
            errors += [f"- {node.name}: {error}" for error in method_checker.errors]

    if errors:
        raise ValueError("Tool validation failed:\n" + "\n".join(errors))
    return

```

## File: src/smolagents/models.py

<a name='file-src-smolagents-models.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from dataclasses import dataclass
import json
import logging
import os
import random
from copy import deepcopy
from enum import Enum
from typing import Dict, List, Optional, Union, Any

from huggingface_hub import InferenceClient

from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    StoppingCriteria,
    StoppingCriteriaList,
    is_torch_available,
)
from transformers.utils.import_utils import _is_package_available

import openai

from .tools import Tool

logger = logging.getLogger(__name__)

DEFAULT_JSONAGENT_REGEX_GRAMMAR = {
    "type": "regex",
    "value": 'Thought: .+?\\nAction:\\n\\{\\n\\s{4}"action":\\s"[^"\\n]+",\\n\\s{4}"action_input":\\s"[^"\\n]+"\\n\\}\\n<end_code>',
}

DEFAULT_CODEAGENT_REGEX_GRAMMAR = {
    "type": "regex",
    "value": "Thought: .+?\\nCode:\\n```(?:py|python)?\\n(?:.|\\s)+?\\n```<end_code>",
}

if _is_package_available("litellm"):
    import litellm


@dataclass
class ChatMessageToolCallDefinition:
    arguments: Any
    name: str
    description: Optional[str] = None


@dataclass
class ChatMessageToolCall:
    function: ChatMessageToolCallDefinition
    id: str
    type: str


@dataclass
class ChatMessage:
    role: str
    content: Optional[str] = None
    tool_calls: Optional[List[ChatMessageToolCall]] = None


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL_CALL = "tool-call"
    TOOL_RESPONSE = "tool-response"

    @classmethod
    def roles(cls):
        return [r.value for r in cls]


tool_role_conversions = {
    MessageRole.TOOL_CALL: MessageRole.ASSISTANT,
    MessageRole.TOOL_RESPONSE: MessageRole.USER,
}


def get_json_schema(tool: Tool) -> Dict:
    properties = deepcopy(tool.inputs)
    required = []
    for key, value in properties.items():
        if value["type"] == "any":
            value["type"] = "string"
        if not ("nullable" in value and value["nullable"]):
            required.append(key)
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required,
            },
        },
    }


def remove_stop_sequences(content: str, stop_sequences: List[str]) -> str:
    for stop_seq in stop_sequences:
        if content[-len(stop_seq) :] == stop_seq:
            content = content[: -len(stop_seq)]
    return content


def get_clean_message_list(
    message_list: List[Dict[str, str]],
    role_conversions: Dict[MessageRole, MessageRole] = {},
) -> List[Dict[str, str]]:
    """
    Subsequent messages with the same role will be concatenated to a single message.

    Args:
        message_list (`List[Dict[str, str]]`): List of chat messages.
    """
    final_message_list = []
    message_list = deepcopy(message_list)  # Avoid modifying the original list
    for message in message_list:
        # if not set(message.keys()) == {"role", "content"}:
        #     raise ValueError("Message should contain only 'role' and 'content' keys!")

        role = message["role"]
        if role not in MessageRole.roles():
            raise ValueError(
                f"Incorrect role {role}, only {MessageRole.roles()} are supported for now."
            )

        if role in role_conversions:
            message["role"] = role_conversions[role]

        if (
            len(final_message_list) > 0
            and message["role"] == final_message_list[-1]["role"]
        ):
            final_message_list[-1]["content"] += "\n=======\n" + message["content"]
        else:
            final_message_list.append(message)
    return final_message_list


def parse_dictionary(possible_dictionary: str) -> Union[Dict, str]:
    try:
        start, end = (
            possible_dictionary.find("{"),
            possible_dictionary.rfind("}") + 1,
        )
        return json.loads(possible_dictionary[start:end])
    except Exception:
        return possible_dictionary


class Model:
    def __init__(self):
        self.last_input_token_count = None
        self.last_output_token_count = None

    def get_token_counts(self) -> Dict[str, int]:
        return {
            "input_token_count": self.last_input_token_count,
            "output_token_count": self.last_output_token_count,
        }

    def __call__(
        self,
        messages: List[Dict[str, str]],
        stop_sequences: Optional[List[str]] = None,
        grammar: Optional[str] = None,
        max_tokens: int = 1500,
    ) -> ChatMessage:
        """Process the input messages and return the model's response.

        Parameters:
            messages (`List[Dict[str, str]]`):
                A list of message dictionaries to be processed. Each dictionary should have the structure `{"role": "user/system", "content": "message content"}`.
            stop_sequences (`List[str]`, *optional*):
                A list of strings that will stop the generation if encountered in the model's output.
            grammar (`str`, *optional*):
                The grammar or formatting structure to use in the model's response.
            max_tokens (`int`, *optional*):
                The maximum count of tokens to generate.
        Returns:
            `str`: The text content of the model's response.
        """
        pass  # To be implemented in child classes!


class HfApiModel(Model):
    """A class to interact with Hugging Face's Inference API for language model interaction.

    This engine allows you to communicate with Hugging Face's models using the Inference API. It can be used in both serverless mode or with a dedicated endpoint, supporting features like stop sequences and grammar customization.

    Parameters:
        model_id (`str`, *optional*, defaults to `"Qwen/Qwen2.5-Coder-32B-Instruct"`):
            The Hugging Face model ID to be used for inference. This can be a path or model identifier from the Hugging Face model hub.
        token (`str`, *optional*):
            Token used by the Hugging Face API for authentication. This token need to be authorized 'Make calls to the serverless Inference API'.
            If the model is gated (like Llama-3 models), the token also needs 'Read access to contents of all public gated repos you can access'.
            If not provided, the class will try to use environment variable 'HF_TOKEN', else use the token stored in the Hugging Face CLI configuration.
        timeout (`int`, *optional*, defaults to 120):
            Timeout for the API request, in seconds.

    Raises:
        ValueError:
            If the model name is not provided.

    Example:
    ```python
    >>> engine = HfApiModel(
    ...     model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
    ...     token="your_hf_token_here",
    ... )
    >>> messages = [{"role": "user", "content": "Explain quantum mechanics in simple terms."}]
    >>> response = engine(messages, stop_sequences=["END"], max_tokens=1500)
    >>> print(response)
    "Quantum mechanics is the branch of physics that studies..."
    ```
    """

    def __init__(
        self,
        model_id: str = "Qwen/Qwen2.5-Coder-32B-Instruct",
        token: Optional[str] = None,
        timeout: Optional[int] = 120,
        temperature: float = 0.5,
    ):
        super().__init__()
        self.model_id = model_id
        if token is None:
            token = os.getenv("HF_TOKEN")
        self.client = InferenceClient(self.model_id, token=token, timeout=timeout)
        self.temperature = temperature

    def __call__(
        self,
        messages: List[Dict[str, str]],
        stop_sequences: Optional[List[str]] = None,
        grammar: Optional[str] = None,
        max_tokens: int = 1500,
        tools_to_call_from: Optional[List[Tool]] = None,
    ) -> ChatMessage:
        """
        Gets an LLM output message for the given list of input messages.
        If argument `tools_to_call_from` is passed, the model's tool calling options will be used to return a tool call.
        """
        messages = get_clean_message_list(
            messages, role_conversions=tool_role_conversions
        )
        if tools_to_call_from:
            response = self.client.chat.completions.create(
                messages=messages,
                tools=[get_json_schema(tool) for tool in tools_to_call_from],
                tool_choice="auto",
                stop=stop_sequences,
                max_tokens=max_tokens,
                temperature=self.temperature,
            )
        else:
            response = self.client.chat.completions.create(
                model=self.model_id,
                messages=messages,
                stop=stop_sequences,
                max_tokens=max_tokens,
                temperature=self.temperature,
            )
        self.last_input_token_count = response.usage.prompt_tokens
        self.last_output_token_count = response.usage.completion_tokens
        return response.choices[0].message


class TransformersModel(Model):
    """This engine initializes a model and tokenizer from the given `model_id`.

    Parameters:
        model_id (`str`, *optional*, defaults to `"HuggingFaceTB/SmolLM2-1.7B-Instruct"`):
            The Hugging Face model ID to be used for inference. This can be a path or model identifier from the Hugging Face model hub.
        device (`str`, optional, defaults to `"cuda"` if available, else `"cpu"`.):
            The device to load the model on (`"cpu"` or `"cuda"`).
    """

    def __init__(self, model_id: Optional[str] = None, device: Optional[str] = None):
        super().__init__()
        if not is_torch_available():
            raise ImportError("Please install torch in order to use TransformersModel.")
        import torch

        default_model_id = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
        if model_id is None:
            model_id = default_model_id
            logger.warning(
                f"`model_id`not provided, using this default tokenizer for token counts: '{model_id}'"
            )
        self.model_id = model_id
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        self.device = device
        logger.info(f"Using device: {self.device}")
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_id)
            self.model = AutoModelForCausalLM.from_pretrained(model_id, device_map=self.device)
        except Exception as e:
            logger.warning(
                f"Failed to load tokenizer and model for {model_id=}: {e}. Loading default tokenizer and model instead from {default_model_id=}."
            )
            self.model_id = default_model_id
            self.tokenizer = AutoTokenizer.from_pretrained(default_model_id)
            self.model = AutoModelForCausalLM.from_pretrained(model_id, device_map=self.device)

    def make_stopping_criteria(self, stop_sequences: List[str]) -> StoppingCriteriaList:
        class StopOnStrings(StoppingCriteria):
            def __init__(self, stop_strings: List[str], tokenizer):
                self.stop_strings = stop_strings
                self.tokenizer = tokenizer
                self.stream = ""

            def reset(self):
                self.stream = ""

            def __call__(self, input_ids, scores, **kwargs):
                generated = self.tokenizer.decode(
                    input_ids[0][-1], skip_special_tokens=True
                )
                self.stream += generated
                if any(
                    [
                        self.stream.endswith(stop_string)
                        for stop_string in self.stop_strings
                    ]
                ):
                    return True
                return False

        return StoppingCriteriaList([StopOnStrings(stop_sequences, self.tokenizer)])

    def __call__(
        self,
        messages: List[Dict[str, str]],
        stop_sequences: Optional[List[str]] = None,
        grammar: Optional[str] = None,
        max_tokens: int = 1500,
        tools_to_call_from: Optional[List[Tool]] = None,
    ) -> ChatMessage:
        messages = get_clean_message_list(
            messages, role_conversions=tool_role_conversions
        )
        if tools_to_call_from is not None:
            prompt_tensor = self.tokenizer.apply_chat_template(
                messages,
                tools=[get_json_schema(tool) for tool in tools_to_call_from],
                return_tensors="pt",
                return_dict=True,
                add_generation_prompt=True,
            )
        else:
            prompt_tensor = self.tokenizer.apply_chat_template(
                messages,
                return_tensors="pt",
                return_dict=True,
            )
        prompt_tensor = prompt_tensor.to(self.model.device)
        count_prompt_tokens = prompt_tensor["input_ids"].shape[1]

        out = self.model.generate(
            **prompt_tensor,
            max_new_tokens=max_tokens,
            stopping_criteria=(
                self.make_stopping_criteria(stop_sequences) if stop_sequences else None
            ),
        )
        generated_tokens = out[0, count_prompt_tokens:]
        output = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        self.last_input_token_count = count_prompt_tokens
        self.last_output_token_count = len(generated_tokens)

        if stop_sequences is not None:
            output = remove_stop_sequences(output, stop_sequences)
        if tools_to_call_from is None:
            return ChatMessage(role="assistant", content=output)
        else:
            if "Action:" in output:
                output = output.split("Action:", 1)[1].strip()
            parsed_output = json.loads(output)
            tool_name = parsed_output.get("tool_name")
            tool_arguments = parsed_output.get("tool_arguments")
            return ChatMessage(
                role="assistant",
                content="",
                tool_calls=[
                    ChatMessageToolCall(
                        id="".join(random.choices("0123456789", k=5)),
                        type="function",
                        function=ChatMessageToolCallDefinition(
                            name=tool_name, arguments=tool_arguments
                        ),
                    )
                ],
            )


class LiteLLMModel(Model):
    def __init__(
        self,
        model_id="anthropic/claude-3-5-sonnet-20240620",
        api_base=None,
        api_key=None,
        **kwargs,
    ):
        if not _is_package_available("litellm"):
            raise ImportError(
                "litellm not found. Install it with `pip install litellm`"
            )
        super().__init__()
        self.model_id = model_id
        # IMPORTANT - Set this to TRUE to add the function to the prompt for Non OpenAI LLMs
        litellm.add_function_to_prompt = True
        self.api_base = api_base
        self.api_key = api_key
        self.kwargs = kwargs

    def __call__(
        self,
        messages: List[Dict[str, str]],
        stop_sequences: Optional[List[str]] = None,
        grammar: Optional[str] = None,
        max_tokens: int = 1500,
        tools_to_call_from: Optional[List[Tool]] = None,
    ) -> ChatMessage:
        messages = get_clean_message_list(
            messages, role_conversions=tool_role_conversions
        )
        if tools_to_call_from:
            response = litellm.completion(
                model=self.model_id,
                messages=messages,
                tools=[get_json_schema(tool) for tool in tools_to_call_from],
                tool_choice="required",
                stop=stop_sequences,
                max_tokens=max_tokens,
                api_base=self.api_base,
                api_key=self.api_key,
                **self.kwargs,
            )
        else:
            response = litellm.completion(
                model=self.model_id,
                messages=messages,
                stop=stop_sequences,
                max_tokens=max_tokens,
                api_base=self.api_base,
                api_key=self.api_key,
                **self.kwargs,
            )
        self.last_input_token_count = response.usage.prompt_tokens
        self.last_output_token_count = response.usage.completion_tokens
        return response.choices[0].message


class OpenAIServerModel(Model):
    """This engine connects to an OpenAI-compatible API server.

    Parameters:
        model_id (`str`):
            The model identifier to use on the server (e.g. "gpt-3.5-turbo").
        api_base (`str`):
            The base URL of the OpenAI-compatible API server.
        api_key (`str`):
            The API key to use for authentication.
        temperature (`float`, *optional*, defaults to 0.7):
            Controls randomness in the model's responses. Values between 0 and 2.
        **kwargs:
            Additional keyword arguments to pass to the OpenAI API.
    """

    def __init__(
        self,
        model_id: str,
        api_base: str,
        api_key: str,
        temperature: float = 0.7,
        **kwargs,
    ):
        super().__init__()
        self.model_id = model_id
        self.client = openai.OpenAI(
            base_url=api_base,
            api_key=api_key,
        )
        self.temperature = temperature
        self.kwargs = kwargs

    def __call__(
        self,
        messages: List[Dict[str, str]],
        stop_sequences: Optional[List[str]] = None,

*Content truncated for brevity.*

```

## File: src/smolagents/monitoring.py

<a name='file-src-smolagents-monitoring.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from rich.text import Text


class Monitor:
    def __init__(self, tracked_model, logger):
        self.step_durations = []
        self.tracked_model = tracked_model
        self.logger = logger
        if (
            getattr(self.tracked_model, "last_input_token_count", "Not found")
            != "Not found"
        ):
            self.total_input_token_count = 0
            self.total_output_token_count = 0

    def get_total_token_counts(self):
        return {
            "input": self.total_input_token_count,
            "output": self.total_output_token_count,
        }

    def reset(self):
        self.step_durations = []
        self.total_input_token_count = 0
        self.total_output_token_count = 0

    def update_metrics(self, step_log):
        step_duration = step_log.duration
        self.step_durations.append(step_duration)
        console_outputs = f"[Step {len(self.step_durations) - 1}: Duration {step_duration:.2f} seconds"

        if getattr(self.tracked_model, "last_input_token_count", None) is not None:
            self.total_input_token_count += self.tracked_model.last_input_token_count
            self.total_output_token_count += self.tracked_model.last_output_token_count
            console_outputs += f"| Input tokens: {self.total_input_token_count:,} | Output tokens: {self.total_output_token_count:,}"
        console_outputs += "]"
        self.logger.log(Text(console_outputs, style="dim"), level=1)


__all__ = ["Monitor"]

```

## File: src/smolagents/gradio_ui.py

<a name='file-src-smolagents-gradio_ui.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding=utf-8
# Copyright 2024 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import gradio as gr
import shutil
import os
import mimetypes
import re

from .agents import ActionStep, AgentStep, MultiStepAgent
from .types import AgentAudio, AgentImage, AgentText, handle_agent_output_types


def pull_messages_from_step(step_log: AgentStep, test_mode: bool = True):
    """Extract ChatMessage objects from agent steps"""
    if isinstance(step_log, ActionStep):
        yield gr.ChatMessage(role="assistant", content=step_log.llm_output or "")
        if step_log.tool_calls is not None:
            first_tool_call = step_log.tool_calls[0]
            used_code = first_tool_call.name == "code interpreter"
            content = first_tool_call.arguments
            if used_code:
                content = f"```py\n{content}\n```"
            yield gr.ChatMessage(
                role="assistant",
                metadata={"title": f"🛠️ Used tool {first_tool_call.name}"},
                content=str(content),
            )
        if step_log.observations is not None:
            yield gr.ChatMessage(role="assistant", content=step_log.observations)
        if step_log.error is not None:
            yield gr.ChatMessage(
                role="assistant",
                content=str(step_log.error),
                metadata={"title": "💥 Error"},
            )


def stream_to_gradio(
    agent,
    task: str,
    test_mode: bool = False,
    reset_agent_memory: bool = False,
    **kwargs,
):
    """Runs an agent with the given task and streams the messages from the agent as gradio ChatMessages."""

    for step_log in agent.run(task, stream=True, reset=reset_agent_memory, **kwargs):
        for message in pull_messages_from_step(step_log, test_mode=test_mode):
            yield message

    final_answer = step_log  # Last log is the run's final_answer
    final_answer = handle_agent_output_types(final_answer)

    if isinstance(final_answer, AgentText):
        yield gr.ChatMessage(
            role="assistant",
            content=f"**Final answer:**\n{final_answer.to_string()}\n",
        )
    elif isinstance(final_answer, AgentImage):
        yield gr.ChatMessage(
            role="assistant",
            content={"path": final_answer.to_string(), "mime_type": "image/png"},
        )
    elif isinstance(final_answer, AgentAudio):
        yield gr.ChatMessage(
            role="assistant",
            content={"path": final_answer.to_string(), "mime_type": "audio/wav"},
        )
    else:
        yield gr.ChatMessage(role="assistant", content=str(final_answer))


class GradioUI:
    """A one-line interface to launch your agent in Gradio"""

    def __init__(self, agent: MultiStepAgent, file_upload_folder: str | None = None):
        self.agent = agent
        self.file_upload_folder = file_upload_folder
        if self.file_upload_folder is not None:
            if not os.path.exists(file_upload_folder):
                os.mkdir(file_upload_folder)

    def interact_with_agent(self, prompt, messages):
        messages.append(gr.ChatMessage(role="user", content=prompt))
        yield messages
        for msg in stream_to_gradio(self.agent, task=prompt, reset_agent_memory=False):
            messages.append(msg)
            yield messages
        yield messages

    def upload_file(
        self,
        file,
        file_uploads_log,
        allowed_file_types=[
            "application/pdf",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "text/plain",
        ],
    ):
        """
        Handle file uploads, default allowed types are .pdf, .docx, and .txt
        """

        if file is None:
            return "No file uploaded"

        try:
            mime_type, _ = mimetypes.guess_type(file.name)
        except Exception as e:
            return f"Error: {e}"

        if mime_type not in allowed_file_types:
            return "File type disallowed"

        # Sanitize file name
        original_name = os.path.basename(file.name)
        sanitized_name = re.sub(
            r"[^\w\-.]", "_", original_name
        )  # Replace any non-alphanumeric, non-dash, or non-dot characters with underscores

        type_to_ext = {}
        for ext, t in mimetypes.types_map.items():
            if t not in type_to_ext:
                type_to_ext[t] = ext

        # Ensure the extension correlates to the mime type
        sanitized_name = sanitized_name.split(".")[:-1]
        sanitized_name.append("" + type_to_ext[mime_type])
        sanitized_name = "".join(sanitized_name)

        # Save the uploaded file to the specified folder
        file_path = os.path.join(
            self.file_upload_folder, os.path.basename(sanitized_name)
        )
        shutil.copy(file.name, file_path)

        return gr.Textbox(
            f"File uploaded: {file_path}", visible=True
        ), file_uploads_log + [file_path]

    def log_user_message(self, text_input, file_uploads_log):
        return (
            text_input
            + f"\nYou have been provided with these files, which might be helpful or not: {file_uploads_log}"
            if len(file_uploads_log) > 0
            else "",
            "",
        )

    def launch(self):
        with gr.Blocks() as demo:
            stored_messages = gr.State([])
            file_uploads_log = gr.State([])
            chatbot = gr.Chatbot(
                label="Agent",
                type="messages",
                avatar_images=(
                    None,
                    "https://em-content.zobj.net/source/twitter/53/robot-face_1f916.png",
                ),
            )
            # If an upload folder is provided, enable the upload feature
            if self.file_upload_folder is not None:
                upload_file = gr.File(label="Upload a file", height=1)
                upload_status = gr.Textbox(
                    label="Upload Status", interactive=False, visible=False
                )
                upload_file.change(
                    self.upload_file,
                    [upload_file, file_uploads_log],
                    [upload_status, file_uploads_log],
                )
            text_input = gr.Textbox(lines=1, label="Chat Message")
            text_input.submit(
                self.log_user_message,
                [text_input, file_uploads_log],
                [stored_messages, text_input],
            ).then(self.interact_with_agent, [stored_messages, chatbot], [chatbot])

        demo.launch()


__all__ = ["stream_to_gradio", "GradioUI"]

```

## File: examples/tool_calling_agent_ollama.py

<a name='file-examples-tool_calling_agent_ollama.py'></a>
*Description*: This is a Python script.

```python
from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel
from typing import Optional

model = LiteLLMModel(
    model_id="ollama_chat/llama3.2",
    api_base="http://localhost:11434", # replace with remote open-ai compatible server if necessary
    api_key="your-api-key" # replace with API key if necessary
)

@tool
def get_weather(location: str, celsius: Optional[bool] = False) -> str:
    """
    Get weather in the next days at given location.
    Secretly this tool does not care about the location, it hates the weather everywhere.

    Args:
        location: the location
        celsius: the temperature
    """
    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

agent = ToolCallingAgent(tools=[get_weather], model=model)

print(agent.run("What's the weather like in Paris?"))

```

## File: examples/benchmark.py

<a name='file-examples-benchmark.py'></a>
*Description*: This is a Python script.

```python
#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install -e .. datasets sympy numpy matplotlib seaborn -q # Install dev version of smolagents + some packages')


# In[4]:


import datasets
import pandas as pd

eval_ds = datasets.load_dataset("m-ric/smol_agents_benchmark")["train"]
pd.DataFrame(eval_ds)


# ### Define utilities and tools
# To run the SERPAPI tool, you will need to have a [SerpAPI](https://serpapi.com/dashboard) API key: for this you need a paid account.

# In[7]:


import time
import json
import os
import re
import string
import warnings
from tqdm import tqdm
from typing import List

from smolagents import (
    GoogleSearchTool,
    CodeAgent,
    ToolCallingAgent,
    HfApiModel,
    AgentError,
    VisitWebpageTool,
    PythonInterpreterTool,
)
from smolagents.agents import ActionStep
from dotenv import load_dotenv

load_dotenv()
os.makedirs("output", exist_ok=True)


def serialize_agent_error(obj):
    if isinstance(obj, AgentError):
        return {"error_type": obj.__class__.__name__, "message": obj.message}
    else:
        return str(obj)


def answer_questions(
    eval_ds, file_name, agent, model_id, action_type, is_vanilla_llm=False
):
    answered_questions = []
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            for line in f:
                answered_questions.append(json.loads(line)["question"])

    for _, example in tqdm(enumerate(eval_ds), total=len(eval_ds)):
        try:
            question = example["question"]
            if example["source"] == "SimpleQA":
                question += " Answer with only the final number."
            if example["source"] == "MATH":
                question += " Write code, not latex."
            if question in answered_questions:
                continue
            start_time = time.time()

            if is_vanilla_llm:
                llm = agent
                answer = llm([{"role": "user", "content": question}])
                token_count = llm.last_input_token_count + llm.last_output_token_count
                intermediate_steps = []
            else:
                answer = agent.run(question)
                token_count = agent.monitor.get_total_token_counts()
                intermediate_steps = str(agent.logs)
                # Remove memory from logs to make them more compact.
                for step in agent.logs:
                    if isinstance(step, ActionStep):
                        step.agent_memory = None

            end_time = time.time()
            annotated_example = {
                "model_id": model_id,
                "agent_action_type": action_type,
                "question": question,
                "answer": answer,
                "true_answer": example["true_answer"],
                "source": example["source"],
                "intermediate_steps": intermediate_steps,
                "start_time": start_time,
                "end_time": end_time,
                "token_counts": token_count,
            }

            with open(file_name, "a") as f:
                json.dump(annotated_example, f, default=serialize_agent_error)
                f.write("\n")  # add a newline for JSONL format
        except Exception as e:
            print("Failed:", e)


def normalize_number_str(number_str: str) -> float:
    # we replace these common units and commas to allow
    # conversion to float
    for char in ["$", "%", ","]:
        number_str = number_str.replace(char, "")
    try:
        return float(number_str)
    except ValueError:
        return float("inf")


def split_string(
    s: str,
    char_list: list[str] = [",", ";"],
) -> list[str]:
    pattern = f"[{''.join(char_list)}]"
    return re.split(pattern, s)


def is_float(element: any) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


def normalize_str(input_str, remove_punct=True) -> str:
    """
    Normalize a string by:
    - Removing all white spaces
    - Optionally removing punctuation (if remove_punct is True)
    - Converting to lowercase
    Parameters:
    - input_str: str, the string to normalize
    - remove_punct: bool, whether to remove punctuation (default: True)
    Returns:
    - str, the normalized string
    """
    # Remove all white spaces. Required e.g for seagull vs. sea gull
    no_spaces = re.sub(r"\s", "", input_str)

    # Remove punctuation, if specified.
    if remove_punct:
        translator = str.maketrans("", "", string.punctuation)
        return no_spaces.lower().translate(translator)
    else:
        return no_spaces.lower()


def extract_numbers(text: str) -> List[str]:
    """This pattern matches:
    - Optional negative sign
    - Numbers with optional comma thousand separators
    - Optional decimal points with decimal numbers
    """
    pattern = r"-?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?"

    return [el.replace(",", "") for el in re.findall(pattern, text)]


def get_question_score_gaia(
    model_answer: str,
    ground_truth: str,
) -> bool:
    """Scoring function used to score functions from the GAIA benchmark"""
    if is_float(ground_truth):
        normalized_answer = normalize_number_str(str(model_answer))
        return normalized_answer == float(ground_truth)

    elif any(char in ground_truth for char in [",", ";"]):  # if gt is a list
        # question with the fish: normalization removes punct
        gt_elems = split_string(ground_truth)
        ma_elems = split_string(model_answer)

        if len(gt_elems) != len(ma_elems):  # check length is the same
            warnings.warn(
                "Answer lists have different lengths, returning False.", UserWarning
            )
            return False

        comparisons = []
        for ma_elem, gt_elem in zip(
            ma_elems, gt_elems
        ):  # compare each element as float or str
            if is_float(gt_elem):
                normalized_ma_elem = normalize_number_str(ma_elem)
                comparisons.append(normalized_ma_elem == float(gt_elem))
            else:
                # we do not remove punct since comparisons can include punct
                comparisons.append(
                    normalize_str(ma_elem, remove_punct=False)
                    == normalize_str(gt_elem, remove_punct=False)
                )
        return all(comparisons)

    else:  # if gt is a str
        return normalize_str(model_answer) == normalize_str(ground_truth)


# ## Benchmark agents
# 
# ### Open models

# In[ ]:


open_model_ids = [
    "meta-llama/Llama-3.3-70B-Instruct",
    # "Qwen/QwQ-32B-Preview",
    "Qwen/Qwen2.5-72B-Instruct",
    "Qwen/Qwen2.5-Coder-32B-Instruct",
    "meta-llama/Llama-3.2-3B-Instruct",
    "meta-llama/Llama-3.1-8B-Instruct",
    "mistralai/Mistral-Nemo-Instruct-2407",
    # "HuggingFaceTB/SmolLM2-1.7B-Instruct",
    # "meta-llama/Llama-3.1-70B-Instruct",
]

for model_id in open_model_ids:
    print(f"Evaluating '{model_id}'...")
    # action_type = "tool_calling"
    # agent = ToolCallingAgent(
    #     tools=[GoogleSearchTool(), VisitWebpageTool(), PythonInterpreterTool()],
    #     model=HfApiModel(model_id),
    #     max_steps=10,
    # )
    # file_name = f"output/{model_id.replace('/', '_')}-{action_type}-26-dec-2024.jsonl"
    # answer_questions(eval_ds, file_name, agent, model_id, action_type)

    action_type = "code"
    agent = CodeAgent(
        tools=[GoogleSearchTool(), VisitWebpageTool()],
        model=HfApiModel(model_id),
        additional_authorized_imports=["numpy", "sympy"],
        max_steps=10,
    )
    file_name = f"output/{model_id.replace('/', '_')}-{action_type}-26-dec-2024.jsonl"
    answer_questions(eval_ds, file_name, agent, model_id, action_type)

    # Also evaluate vanilla model
    action_type = "vanilla"
    llm = HfApiModel(model_id)
    file_name = f"output/{model_id.replace('/', '_')}-{action_type}-26-dec-2024.jsonl"
    answer_questions(
        eval_ds, file_name, llm, model_id, action_type, is_vanilla_llm=True
    )


# ## Closed models

# In[ ]:


from smolagents import LiteLLMModel

litellm_model_ids = ["gpt-4o", "anthropic/claude-3-5-sonnet-latest"]

for model_id in litellm_model_ids:
    print(f"Evaluating '{model_id}'...")
    action_type = "tool_calling"
    agent = ToolCallingAgent(
        tools=[
            GoogleSearchTool(),
            VisitWebpageTool(),
            PythonInterpreterTool(["numpy", "sympy"]),
        ],
        model=LiteLLMModel(model_id),
        max_steps=10,
    )
    file_name = f"output/{model_id.replace('/', '_')}-{action_type}-26-dec-2024.jsonl"
    answer_questions(eval_ds, file_name, agent, model_id, action_type)

    action_type = "code"
    agent = CodeAgent(
        tools=[GoogleSearchTool(), VisitWebpageTool()],
        model=LiteLLMModel(model_id),
        additional_authorized_imports=["numpy", "sympy"],
        max_steps=10,
    )
    file_name = f"output/{model_id.replace('/', '_')}-{action_type}-26-dec-2024.jsonl"
    answer_questions(eval_ds, file_name, agent, model_id, action_type)

    # Also evaluate vanilla model
    action_type = "vanilla"
    llm = LiteLLMModel(model_id)
    file_name = f"output/{model_id.replace('/', '_')}-{action_type}-26-dec-2024.jsonl"
    answer_questions(
        eval_ds, file_name, llm, model_id, action_type, is_vanilla_llm=True
    )


# In[8]:


# import glob
# import json

# jsonl_files = glob.glob(f"output/*.jsonl")

# for file_path in jsonl_files:
#     if "-Nemo-" in file_path and "-vanilla-" in file_path:
#         print(file_path)
#         # Read all lines and filter out SimpleQA sources
#         filtered_lines = []
#         removed = 0
#         with open(file_path, "r", encoding="utf-8") as f:
#             for line in f:
#                 try:
#                     data = json.loads(line.strip())
#                     data["answer"] = data["answer"]["content"]
#                     # if not any([question in data["question"] for question in eval_ds["question"]]):
#                     #     removed +=1
#                     # else:
#                     filtered_lines.append(json.dumps(data) + "\n")
#                 except json.JSONDecodeError:
#                     print("Invalid line:", line)
#                     continue  # Skip invalid JSON lines
#         print(f"Removed {removed} lines.")
#         # Write filtered content back to the same file
#         with open(
#             str(file_path).replace("-vanilla-", "-vanilla2-"), "w", encoding="utf-8"
#         ) as f:
#             f.writelines(filtered_lines)


# ## Score answers

# In[9]:


import pandas as pd
import glob

res = []
for file_path in glob.glob("output/*.jsonl"):
    data = []
    with open(file_path) as f:
        for line in f:
            try:
                # Use standard json module instead of pandas.json to handle large numbers better
                record = json.loads(line)
                data.append(record)
            except json.JSONDecodeError as e:
                print(f"Error parsing line in {file_path}: {e}")
                continue

    try:
        smoldf = pd.DataFrame(data)
        smoldf["action_type"] = "vanilla" if "-vanilla-" in file_path else "code"
        res.append(smoldf)
    except Exception as e:
        print(f"Error creating DataFrame from {file_path}: {e}")
        continue

result_df = pd.concat(res)


def get_correct(row):
    if row["source"] == "MATH":  # Checks the last number in answer
        numbers_answer = extract_numbers(str(row["answer"]))
        if len(numbers_answer) == 0:
            return False
        return float(numbers_answer[-1]) == float(row["true_answer"])
    else:
        return get_question_score_gaia(str(row["answer"]), str(row["true_answer"]))


result_df["correct"] = result_df.apply(get_correct, axis=1)

result_df = (
    (result_df.groupby(["model_id", "source", "action_type"])[["correct"]].mean() * 100)
    .round(1)
    .reset_index()
)


# In[10]:


pivot_df = result_df.pivot_table(
    index=["model_id", "source"],
    columns=["action_type"],
    values="correct",
    fill_value=float("nan"),
).reset_index()


# ### Display results

# In[11]:


display(pivot_df)


# In[16]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.legend_handler import HandlerTuple  # Added import

# Assuming pivot_df is your original dataframe
models = pivot_df["model_id"].unique()
sources = pivot_df["source"].unique()

# Create figure and axis
plt.style.use("seaborn-v0_8-white")
fig, ax = plt.subplots(figsize=(15, 6))

# Set the width of each bar group and positions of the bars
width = 0.15  # width of each bar
spacing = 0.02  # space between bars within a group
group_spacing = 0.2  # space between model groups

# Calculate positions for the bars
num_sources = len(sources)
total_width_per_group = (width + spacing) * num_sources * 2  # *2 for agent and vanilla
x = np.arange(len(models)) * (total_width_per_group + group_spacing)

# Plot bars for each source
for i, source in enumerate(sources):
    source_data = pivot_df[pivot_df["source"] == source]
    agent_scores = [
        source_data[source_data["model_id"] == model]["code"].values[0]
        if len(source_data[source_data["model_id"] == model]) > 0
        else np.nan
        for model in models
    ]
    vanilla_scores = [
        source_data[source_data["model_id"] == model]["vanilla"].values[0]
        if len(source_data[source_data["model_id"] == model]) > 0
        else np.nan
        for model in models
    ]

    # Position calculation for each pair of bars
    pos = x + i * (width * 2 + spacing)

    agent_bars = ax.bar(pos, agent_scores, width, label=f"{source} (Agent)", alpha=0.8)
    vanilla_bars = ax.bar(
        pos + width * 0.6,
        vanilla_scores,
        width,
        hatch="////",
        alpha=0.5,
        hatch_linewidth=2,
        label=f"{source} (Vanilla)",
        color="white",
        edgecolor=agent_bars[0].get_facecolor(),
    )

# Customize the plot
ax.set_ylabel("Score")
ax.set_title("Model Performance Comparison")

# Set x-axis ticks in the middle of each group
group_centers = x + (total_width_per_group - spacing) / 2
ax.set_xticks(group_centers)

# Wrap long model names to prevent overlap
wrapped_labels = ["\n".join(model.split("/")) for model in models]
ax.set_xticklabels(wrapped_labels, rotation=0, ha="center")

# Modify legend to combine agent and vanilla entries
handles, labels = ax.get_legend_handles_labels()
unique_sources = sources
legend_elements = [
    (handles[i * 2], handles[i * 2 + 1], labels[i * 2].replace(" (Agent)", ""))
    for i in range(len(unique_sources))
]
custom_legend = ax.legend(
    [
        (agent_handle, vanilla_handle)
        for agent_handle, vanilla_handle, _ in legend_elements
    ],
    [label for _, _, label in legend_elements],
    handler_map={tuple: HandlerTuple(ndivide=None)},
    bbox_to_anchor=(1.05, 1),
    loc="upper left",
)

ax.yaxis.grid(True, linestyle="--", alpha=0.3)
ax.set_ylim(bottom=0)
plt.tight_layout()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.show()


# In[12]:


def create_mathjax_table(pivot_df, formatted_df):
    # Start the matrix environment with 4 columns
    # l for left-aligned model and task, c for centered numbers
    mathjax_table = "\\begin{array}{llcc}\n"

*Content truncated for brevity.*

```

## File: examples/e2b_example.py

<a name='file-examples-e2b_example.py'></a>
*Description*: This is a Python script.

```python
from smolagents import Tool, CodeAgent, HfApiModel
from smolagents.default_tools import VisitWebpageTool
from dotenv import load_dotenv

load_dotenv()

class GetCatImageTool(Tool):
    name="get_cat_image"
    description = "Get a cat image"
    inputs = {}
    output_type = "image"

    def __init__(self):
        super().__init__()
        self.url = "https://em-content.zobj.net/source/twitter/53/robot-face_1f916.png"

    def forward(self):
        from PIL import Image
        import requests
        from io import BytesIO

        response = requests.get(self.url)

        return Image.open(BytesIO(response.content))


get_cat_image = GetCatImageTool()

agent = CodeAgent(
    tools = [get_cat_image, VisitWebpageTool()],
    model=HfApiModel(),
    additional_authorized_imports=["Pillow", "requests", "markdownify"], # "duckduckgo-search", 
    use_e2b_executor=True
)

agent.run(
    "Return me an image of a cat. Directly use the image provided in your state.", additional_args={"cat_image":get_cat_image()}
) # Asking to directly return the image from state tests that additional_args are properly sent to server.

# Try the agent in a Gradio UI
from smolagents import GradioUI

GradioUI(agent).launch()
```

## File: examples/gradio_upload.py

<a name='file-examples-gradio_upload.py'></a>
*Description*: This is a Python script.

```python
from smolagents import (
    CodeAgent,
    HfApiModel,
    GradioUI
)

agent = CodeAgent(
    tools=[], model=HfApiModel(), max_steps=4, verbosity_level=0
)

GradioUI(agent, file_upload_folder='./data').launch()

```

## File: examples/text_to_sql.py

<a name='file-examples-text_to_sql.py'></a>
*Description*: This is a Python script.

```python
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Float,
    insert,
    inspect,
    text,
)

engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# create city SQL table
table_name = "receipts"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("customer_name", String(16), primary_key=True),
    Column("price", Float),
    Column("tip", Float),
)
metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
    {"receipt_id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
    {"receipt_id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
    {"receipt_id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
]
for row in rows:
    stmt = insert(receipts).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)

inspector = inspect(engine)
columns_info = [(col["name"], col["type"]) for col in inspector.get_columns("receipts")]

table_description = "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
print(table_description)

from smolagents import tool

@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'receipts'. Its description is as follows:
        Columns:
        - receipt_id: INTEGER
        - customer_name: VARCHAR(16)
        - price: FLOAT
        - tip: FLOAT

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output

from smolagents import CodeAgent, HfApiModel

agent = CodeAgent(
    tools=[sql_engine],
    model=HfApiModel("meta-llama/Meta-Llama-3.1-8B-Instruct"),
)
agent.run("Can you give me the name of the client who got the most expensive receipt?")
```

## File: examples/rag.py

<a name='file-examples-rag.py'></a>
*Description*: This is a Python script.

```python
# from huggingface_hub import login

# login()
import datasets
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever


knowledge_base = datasets.load_dataset("m-ric/huggingface_doc", split="train")
knowledge_base = knowledge_base.filter(lambda row: row["source"].startswith("huggingface/transformers"))

source_docs = [
    Document(page_content=doc["text"], metadata={"source": doc["source"].split("/")[1]})
    for doc in knowledge_base
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    add_start_index=True,
    strip_whitespace=True,
    separators=["\n\n", "\n", ".", " ", ""],
)
docs_processed = text_splitter.split_documents(source_docs)

from smolagents import Tool

class RetrieverTool(Tool):
    name = "retriever"
    description = "Uses semantic search to retrieve the parts of transformers documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question.",
        }
    }
    output_type = "string"

    def __init__(self, docs, **kwargs):
        super().__init__(**kwargs)
        self.retriever = BM25Retriever.from_documents(
            docs, k=10
        )

    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"

        docs = self.retriever.invoke(
            query,
        )
        return "\nRetrieved documents:\n" + "".join(
            [
                f"\n\n===== Document {str(i)} =====\n" + doc.page_content
                for i, doc in enumerate(docs)
            ]
        )

from smolagents import HfApiModel, CodeAgent

retriever_tool = RetrieverTool(docs_processed)
agent = CodeAgent(
    tools=[retriever_tool], model=HfApiModel("meta-llama/Llama-3.3-70B-Instruct"), max_steps=4, verbosity_level=2
)

agent_output = agent.run("For a transformers model training, which is slower, the forward or the backward pass?")

print("Final output:")
print(agent_output)

```

## File: examples/tool_calling_agent_from_any_llm.py

<a name='file-examples-tool_calling_agent_from_any_llm.py'></a>
*Description*: This is a Python script.

```python
from smolagents.agents import ToolCallingAgent
from smolagents import tool, LiteLLMModel
from typing import Optional

# Choose which LLM engine to use!
# model = HfApiModel(model_id="meta-llama/Llama-3.3-70B-Instruct")
# model = TransformersModel(model_id="meta-llama/Llama-3.2-2B-Instruct")

# For anthropic: change model_id below to 'anthropic/claude-3-5-sonnet-20240620'
model = LiteLLMModel(model_id="gpt-4o")

@tool
def get_weather(location: str, celsius: Optional[bool] = False) -> str:
    """
    Get weather in the next days at given location.
    Secretly this tool does not care about the location, it hates the weather everywhere.

    Args:
        location: the location
        celsius: the temperature
    """
    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

agent = ToolCallingAgent(tools=[get_weather], model=model)

print(agent.run("What's the weather like in Paris?"))
```

## File: docs/README.md

<a name='file-docs-README.md'></a>
*Description*: No specific description available.

```plaintext
<!---
Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->

# Generating the documentation

To generate the documentation, you have to build it. Several packages are necessary to build the doc.

First, you need to install the project itself by running the following command at the root of the code repository:

```bash
pip install -e .
```

You also need to install 2 extra packages:

```bash
# `hf-doc-builder` to build the docs
pip install git+https://github.com/huggingface/doc-builder@main
# `watchdog` for live reloads
pip install watchdog
```

---
**NOTE**

You only need to generate the documentation to inspect it locally (if you're planning changes and want to
check how they look before committing for instance). You don't have to commit the built documentation.

---

## Building the documentation

Once you have setup the `doc-builder` and additional packages with the pip install command above,
you can generate the documentation by typing the following command:

```bash
doc-builder build smolagents docs/source/en/ --build_dir ~/tmp/test-build
```

You can adapt the `--build_dir` to set any temporary folder that you prefer. This command will create it and generate
the MDX files that will be rendered as the documentation on the main website. You can inspect them in your favorite
Markdown editor.

## Previewing the documentation

To preview the docs, run the following command:

```bash
doc-builder preview smolagents docs/source/en/
```

The docs will be viewable at [http://localhost:5173](http://localhost:5173). You can also preview the docs once you
have opened a PR. You will see a bot add a comment to a link where the documentation with your changes lives.

---
**NOTE**

The `preview` command only works with existing doc files. When you add a completely new file, you need to update
`_toctree.yml` & restart `preview` command (`ctrl-c` to stop it & call `doc-builder preview ...` again).

---

## Adding a new element to the navigation bar

Accepted files are Markdown (.md).

Create a file with its extension and put it in the source directory. You can then link it to the toc-tree by putting
the filename without the extension in the [`_toctree.yml`](https://github.com/huggingface/smolagents/blob/main/docs/source/_toctree.yml) file.

## Renaming section headers and moving sections

It helps to keep the old links working when renaming the section header and/or moving sections from one document to another. This is because the old links are likely to be used in Issues, Forums, and Social media and it'd make for a much more superior user experience if users reading those months later could still easily navigate to the originally intended information.

Therefore, we simply keep a little map of moved sections at the end of the document where the original section was. The key is to preserve the original anchor.

So if you renamed a section from: "Section A" to "Section B", then you can add at the end of the file:

```
Sections that were moved:

[ <a href="#section-b">Section A</a><a id="section-a"></a> ]
```
and of course, if you moved it to another file, then:

```
Sections that were moved:

[ <a href="../new-file#section-b">Section A</a><a id="section-a"></a> ]
```

Use the relative style to link to the new file so that the versioned docs continue to work.

For an example of a rich moved section set please see the very end of [the transformers Trainer doc](https://github.com/huggingface/transformers/blob/main/docs/source/en/main_classes/trainer.md).


## Writing Documentation - Specification

The `huggingface/smolagents` documentation follows the
[Google documentation](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) style for docstrings,
although we can write them directly in Markdown.

### Adding a new tutorial

Adding a new tutorial or section is done in two steps:

- Add a new Markdown (.md) file under `./source`.
- Link that file in `./source/_toctree.yml` on the correct toc-tree.

Make sure to put your new file under the proper section. If you have a doubt, feel free to ask in a Github Issue or PR.

### Translating

When translating, refer to the guide at [./TRANSLATING.md](https://github.com/huggingface/smolagents/blob/main/docs/TRANSLATING.md).

### Writing source documentation

Values that should be put in `code` should either be surrounded by backticks: \`like so\`. Note that argument names
and objects like True, None, or any strings should usually be put in `code`.

When mentioning a class, function, or method, it is recommended to use our syntax for internal links so that our tool
adds a link to its documentation with this syntax: \[\`XXXClass\`\] or \[\`function\`\]. This requires the class or
function to be in the main package.

If you want to create a link to some internal class or function, you need to
provide its path. For instance: \[\`utils.ModelOutput\`\]. This will be converted into a link with
`utils.ModelOutput` in the description. To get rid of the path and only keep the name of the object you are
linking to in the description, add a ~: \[\`~utils.ModelOutput\`\] will generate a link with `ModelOutput` in the description.

The same works for methods so you can either use \[\`XXXClass.method\`\] or \[~\`XXXClass.method\`\].

#### Defining arguments in a method

Arguments should be defined with the `Args:` (or `Arguments:` or `Parameters:`) prefix, followed by a line return and
an indentation. The argument should be followed by its type, with its shape if it is a tensor, a colon, and its
description:

```
    Args:
        n_layers (`int`): The number of layers of the model.
```

If the description is too long to fit in one line, another indentation is necessary before writing the description
after the argument.

Here's an example showcasing everything so far:

```
    Args:
        input_ids (`torch.LongTensor` of shape `(batch_size, sequence_length)`):
            Indices of input sequence tokens in the vocabulary.

            Indices can be obtained using [`AlbertTokenizer`]. See [`~PreTrainedTokenizer.encode`] and
            [`~PreTrainedTokenizer.__call__`] for details.

            [What are input IDs?](../glossary#input-ids)
```

For optional arguments or arguments with defaults we follow the following syntax: imagine we have a function with the
following signature:

```
def my_function(x: str = None, a: float = 1):
```

then its documentation should look like this:

```
    Args:
        x (`str`, *optional*):
            This argument controls ...
        a (`float`, *optional*, defaults to 1):
            This argument is used to ...
```

Note that we always omit the "defaults to \`None\`" when None is the default for any argument. Also note that even
if the first line describing your argument type and its default gets long, you can't break it on several lines. You can
however write as many lines as you want in the indented description (see the example above with `input_ids`).

#### Writing a multi-line code block

Multi-line code blocks can be useful for displaying examples. They are done between two lines of three backticks as usual in Markdown:


````
```
# first line of code
# second line
# etc
```
````

#### Writing a return block

The return block should be introduced with the `Returns:` prefix, followed by a line return and an indentation.
The first line should be the type of the return, followed by a line return. No need to indent further for the elements
building the return.

Here's an example of a single value return:

```
    Returns:
        `List[int]`: A list of integers in the range [0, 1] --- 1 for a special token, 0 for a sequence token.
```

Here's an example of a tuple return, comprising several objects:

```
    Returns:
        `tuple(torch.FloatTensor)` comprising various elements depending on the configuration ([`BertConfig`]) and inputs:
        - ** loss** (*optional*, returned when `masked_lm_labels` is provided) `torch.FloatTensor` of shape `(1,)` --
          Total loss is the sum of the masked language modeling loss and the next sequence prediction (classification) loss.
        - **prediction_scores** (`torch.FloatTensor` of shape `(batch_size, sequence_length, config.vocab_size)`) --
          Prediction scores of the language modeling head (scores for each vocabulary token before SoftMax).
```

#### Adding an image

Due to the rapidly growing repository, it is important to make sure that no files that would significantly weigh down the repository are added. This includes images, videos, and other non-text files. We prefer to leverage a hf.co hosted `dataset` like
the ones hosted on [`hf-internal-testing`](https://huggingface.co/hf-internal-testing) in which to place these files and reference
them by URL. We recommend putting them in the following dataset: [huggingface/documentation-images](https://huggingface.co/datasets/huggingface/documentation-images).
If an external contribution, feel free to add the images to your PR and ask a Hugging Face member to migrate your images
to this dataset.

#### Writing documentation examples

The syntax for Example docstrings can look as follows:

```
    Example:

    ```python
    >>> from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
    >>> from datasets import load_dataset
    >>> import torch

    >>> dataset = load_dataset("hf-internal-testing/librispeech_asr_demo", "clean", split="validation")
    >>> dataset = dataset.sort("id")
    >>> sampling_rate = dataset.features["audio"].sampling_rate

    >>> processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
    >>> model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    >>> # audio file is decoded on the fly
    >>> inputs = processor(dataset[0]["audio"]["array"], sampling_rate=sampling_rate, return_tensors="pt")
    >>> with torch.no_grad():
    ...     logits = model(**inputs).logits
    >>> predicted_ids = torch.argmax(logits, dim=-1)

    >>> # transcribe speech
    >>> transcription = processor.batch_decode(predicted_ids)
    >>> transcription[0]
    'MISTER QUILTER IS THE APOSTLE OF THE MIDDLE CLASSES AND WE ARE GLAD TO WELCOME HIS GOSPEL'
    ```
```

The docstring should give a minimal, clear example of how the respective model
is to be used in inference and also include the expected (ideally sensible)
output.
Often, readers will try out the example before even going through the function
or class definitions. Therefore, it is of utmost importance that the example
works as expected.
```

## File: docs/source/en/_config.py

<a name='file-docs-source-en-_config.py'></a>
*Description*: This is a Python script.

```python
# docstyle-ignore
INSTALL_CONTENT = """
# Installation
! pip install smolagents
# To install from source instead of the last release, comment the command above and uncomment the following one.
# ! pip install git+https://github.com/huggingface/smolagents.git
"""

notebook_first_cells = [{"type": "code", "content": INSTALL_CONTENT}]
black_avoid_patterns = {
    "{processor_class}": "FakeProcessorClass",
    "{model_class}": "FakeModelClass",
    "{object_class}": "FakeObjectClass",
}

```

## File: docs/source/en/guided_tour.md

<a name='file-docs-source-en-guided_tour.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Agents - Guided tour

[[open-in-colab]]

In this guided visit, you will learn how to build an agent, how to run it, and how to customize it to make it work better for your use-case.

### Building your agent

To initialize a minimal agent, you need at least these two arguments:

- `model`, a text-generation model to power your agent - because the agent is different from a simple LLM, it is a system that uses a LLM as its engine. You can use any of these options:
    - [`TransformersModel`] takes a pre-initialized `transformers` pipeline to run inference on your local machine using `transformers`.
    - [`HfApiModel`] leverages a `huggingface_hub.InferenceClient` under the hood.
    - [`LiteLLMModel`] lets you call 100+ different models through [LiteLLM](https://docs.litellm.ai/)!

- `tools`, a list of `Tools` that the agent can use to solve the task. It can be an empty list. You can also add the default toolbox on top of your `tools` list by defining the optional argument `add_base_tools=True`.

Once you have these two arguments, `tools` and `model`,  you can create an agent and run it. You can use any LLM you'd like, either through [Hugging Face API](https://huggingface.co/docs/api-inference/en/index), [transformers](https://github.com/huggingface/transformers/), [ollama](https://ollama.com/), or [LiteLLM](https://www.litellm.ai/).

<hfoptions id="Pick a LLM">
<hfoption id="Hugging Face API">

Hugging Face API is free to use without a token, but then it will have a rate limitation.

To access gated models or rise your rate limits with a PRO account, you need to set the environment variable `HF_TOKEN` or pass `token` variable upon initialization of `HfApiModel`.

```python
from smolagents import CodeAgent, HfApiModel

model_id = "meta-llama/Llama-3.3-70B-Instruct"

model = HfApiModel(model_id=model_id, token="<YOUR_HUGGINGFACEHUB_API_TOKEN>")
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```
</hfoption>
<hfoption id="Local Transformers Model">

```python
from smolagents import CodeAgent, TransformersModel

model_id = "meta-llama/Llama-3.2-3B-Instruct"

model = TransformersModel(model_id=model_id)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```
</hfoption>
<hfoption id="OpenAI or Anthropic API">

To use `LiteLLMModel`, you need to set the environment variable `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`, or pass `api_key` variable upon initialization.

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key="YOUR_ANTHROPIC_API_KEY") # Could use 'gpt-4o'
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```
</hfoption>
<hfoption id="Ollama">

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/llama3.2", # This model is a bit weak for agentic behaviours though
    api_base="http://localhost:11434", # replace with remote open-ai compatible server if necessary
    api_key="YOUR_API_KEY" # replace with API key if necessary
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```
</hfoption>
</hfoptions>

#### CodeAgent and ToolCallingAgent

The [`CodeAgent`] is our default agent. It will write and execute python code snippets at each step.

By default, the execution is done in your local environment.
This should be safe because the only functions that can be called are the tools you provided (especially if it's only tools by Hugging Face) and a set of predefined safe functions like `print` or functions from the `math` module, so you're already limited in what can be executed.

The Python interpreter also doesn't allow imports by default outside of a safe list, so all the most obvious attacks shouldn't be an issue.
You can authorize additional imports by passing the authorized modules as a list of strings in argument `additional_authorized_imports` upon initialization of your [`CodeAgent`]:

```py
model = HfApiModel()
agent = CodeAgent(tools=[], model=model, additional_authorized_imports=['requests', 'bs4'])
agent.run("Could you get me the title of the page at url 'https://huggingface.co/blog'?")
```

> [!WARNING]
> The LLM can generate arbitrary code that will then be executed: do not add any unsafe imports!

The execution will stop at any code trying to perform an illegal operation or if there is a regular Python error with the code generated by the agent.

You can also use [E2B code executor](https://e2b.dev/docs#what-is-e2-b) instead of a local Python interpreter by first [setting the `E2B_API_KEY` environment variable](https://e2b.dev/dashboard?tab=keys) and then passing `use_e2b_executor=True` upon agent initialization.

> [!TIP]
> Learn more about code execution [in this tutorial](tutorials/secure_code_execution).

We also support the widely-used way of writing actions as JSON-like blobs: this is [`ToolCallingAgent`], it works much in the same way like [`CodeAgent`], of course without `additional_authorized_imports` since it doesn't execute code:

```py
from smolagents import ToolCallingAgent

agent = ToolCallingAgent(tools=[], model=model)
agent.run("Could you get me the title of the page at url 'https://huggingface.co/blog'?")
```

### Inspecting an agent run

Here are a few useful attributes to inspect what happened after a run:
- `agent.logs` stores the fine-grained logs of the agent. At every step of the agent's run, everything gets stored in a dictionary that then is appended to `agent.logs`.
- Running `agent.write_inner_memory_from_logs()` creates an inner memory of the agent's logs for the LLM to view, as a list of chat messages. This method goes over each step of the log and only stores what it's interested in as a message: for instance, it will save the system prompt and task in separate messages, then for each step it will store the LLM output as a message, and the tool call output as another message. Use this if you want a higher-level view of what has happened - but not every log will be transcripted by this method.

## Tools

A tool is an atomic function to be used by an agent. To be used by an LLM, it also needs a few attributes that constitute its API and will be used to describe to the LLM how to call this tool:
- A name
- A description
- Input types and descriptions
- An output type

You can for instance check the [`PythonInterpreterTool`]: it has a name, a description, input descriptions, an output type, and a `forward` method to perform the action.

When the agent is initialized, the tool attributes are used to generate a tool description which is baked into the agent's system prompt. This lets the agent know which tools it can use and why.

### Default toolbox

Transformers comes with a default toolbox for empowering agents, that you can add to your agent upon initialization with argument `add_base_tools = True`:

- **DuckDuckGo web search***: performs a web search using DuckDuckGo browser.
- **Python code interpreter**: runs your LLM generated Python code in a secure environment. This tool will only be added to [`ToolCallingAgent`] if you initialize it with `add_base_tools=True`, since code-based agent can already natively execute Python code
- **Transcriber**: a speech-to-text pipeline built on Whisper-Turbo that transcribes an audio to text.

You can manually use a tool by calling it with its arguments.

```python
from smolagents import DuckDuckGoSearchTool

search_tool = DuckDuckGoSearchTool()
print(search_tool("Who's the current president of Russia?"))
```

### Create a new tool

You can create your own tool for use cases not covered by the default tools from Hugging Face.
For example, let's create a tool that returns the most downloaded model for a given task from the Hub.

You'll start with the code below.

```python
from huggingface_hub import list_models

task = "text-classification"

most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
print(most_downloaded_model.id)
```

This code can quickly be converted into a tool, just by wrapping it in a function and adding the `tool` decorator:
This is not the only way to build the tool: you can directly define it as a subclass of [`Tool`], which gives you more flexibility, for instance the possibility to initialize heavy class attributes.

Let's see how it works for both options:

<hfoptions id="build-a-tool">
<hfoption id="Decorate a function with @tool">

```py
from smolagents import tool

@tool
def model_download_tool(task: str) -> str:
    """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which to get the download count.
    """
    most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
    return most_downloaded_model.id
```

The function needs:
- A clear name. The name should be descriptive enough of what this tool does to help the LLM brain powering the agent. Since this tool returns the model with the most downloads for a task, let's name it `model_download_tool`.
- Type hints on both inputs and output
- A description, that includes an 'Args:' part where each argument is described (without a type indication this time, it will be pulled from the type hint). Same as for the tool name, this description is an instruction manual for the LLM powering you agent, so do not neglect it.
All these elements will be automatically baked into the agent's system prompt upon initialization: so strive to make them as clear as possible!

> [!TIP]
> This definition format is the same as tool schemas used in `apply_chat_template`, the only difference is the added `tool` decorator: read more on our tool use API [here](https://huggingface.co/blog/unified-tool-use#passing-tools-to-a-chat-template).
</hfoption>
<hfoption id="Subclass Tool">

```py
from smolagents import Tool

class ModelDownloadTool(Tool):
    name = "model_download_tool"
    description = "This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub. It returns the name of the checkpoint."
    inputs = {"task": {"type": "string", "description": "The task for which to get the download count."}}
    output_type = "string"

    def forward(self, task: str) -> str:
        most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
        return most_downloaded_model.id
```

The subclass needs the following attributes:
- A clear `name`. The name should be descriptive enough of what this tool does to help the LLM brain powering the agent. Since this tool returns the model with the most downloads for a task, let's name it `model_download_tool`.
- A `description`. Same as for the `name`, this description is an instruction manual for the LLM powering you agent, so do not neglect it.
- Input types and descriptions
- Output type
All these attributes will be automatically baked into the agent's system prompt upon initialization: so strive to make them as clear as possible!
</hfoption>
</hfoptions>


Then you can directly initialize your agent:
```py
from smolagents import CodeAgent, HfApiModel
agent = CodeAgent(tools=[model_download_tool], model=HfApiModel())
agent.run(
    "Can you give me the name of the model that has the most downloads in the 'text-to-video' task on the Hugging Face Hub?"
)
```

You get the following logs:
```text
╭──────────────────────────────────────── New run ─────────────────────────────────────────╮
│                                                                                          │
│ Can you give me the name of the model that has the most downloads in the 'text-to-video' │
│ task on the Hugging Face Hub?                                                            │
│                                                                                          │
╰─ HfApiModel - Qwen/Qwen2.5-Coder-32B-Instruct ───────────────────────────────────────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 0 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
╭─ Executing this code: ───────────────────────────────────────────────────────────────────╮
│   1 model_name = model_download_tool(task="text-to-video")                               │
│   2 print(model_name)                                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
Execution logs:
ByteDance/AnimateDiff-Lightning

Out: None
[Step 0: Duration 0.27 seconds| Input tokens: 2,069 | Output tokens: 60]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
╭─ Executing this code: ───────────────────────────────────────────────────────────────────╮
│   1 final_answer("ByteDance/AnimateDiff-Lightning")                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
Out - Final answer: ByteDance/AnimateDiff-Lightning
[Step 1: Duration 0.10 seconds| Input tokens: 4,288 | Output tokens: 148]
Out[20]: 'ByteDance/AnimateDiff-Lightning'
```

> [!TIP]
> Read more on tools in the [dedicated tutorial](./tutorials/tools#what-is-a-tool-and-how-to-build-one).

## Multi-agents

Multi-agent systems have been introduced with Microsoft's framework [Autogen](https://huggingface.co/papers/2308.08155).

In this type of framework, you have several agents working together to solve your task instead of only one.
It empirically yields better performance on most benchmarks. The reason for this better performance is conceptually simple: for many tasks, rather than using a do-it-all system, you would prefer to specialize units on sub-tasks. Here, having agents with separate tool sets and memories allows to achieve efficient specialization. For instance, why fill the memory of the code generating agent with all the content of webpages visited by the web search agent? It's better to keep them separate.

You can easily build hierarchical multi-agent systems with `smolagents`.

To do so, encapsulate the agent in a [`ManagedAgent`] object. This object needs arguments `agent`, `name`, and a `description`, which will then be embedded in the manager agent's system prompt to let it know how to call this managed agent, as we also do for tools.

Here's an example of making an agent that managed a specific web search agent using our [`DuckDuckGoSearchTool`]:

```py
from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool, ManagedAgent

model = HfApiModel()

web_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="web_search",
    description="Runs web searches for you. Give it your query as an argument."
)

manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[managed_web_agent]
)

manager_agent.run("Who is the CEO of Hugging Face?")
```

> [!TIP]
> For an in-depth example of an efficient multi-agent implementation, see [how we pushed our multi-agent system to the top of the GAIA leaderboard](https://huggingface.co/blog/beating-gaia).


## Talk with your agent and visualize its thoughts in a cool Gradio interface

You can use `GradioUI` to interactively submit tasks to your agent and observe its thought and execution process, here is an example:

```py
from smolagents import (
    load_tool,
    CodeAgent,
    HfApiModel,
    GradioUI
)

# Import tool from Hub
image_generation_tool = load_tool("m-ric/text-to-image")

model = HfApiModel(model_id)

# Initialize the agent with the image generation tool
agent = CodeAgent(tools=[image_generation_tool], model=model)

GradioUI(agent).launch()
```

Under the hood, when the user types a new answer, the agent is launched with `agent.run(user_request, reset=False)`.
The `reset=False` flag means the agent's memory is not flushed before launching this new task, which lets the conversation go on.

You can also use this `reset=False` argument to keep the conversation going in any other agentic application.

## Next steps

For more in-depth usage, you will then want to check out our tutorials:
- [the explanation of how our code agents work](./tutorials/secure_code_execution)
- [this guide on how to build good agents](./tutorials/building_good_agents).
- [the in-depth guide for tool usage](./tutorials/building_good_agents).

```

## File: docs/source/en/_toctree.yml

<a name='file-docs-source-en-_toctree.yml'></a>
*Description*: No specific description available.

```plaintext
- title: Get started
  sections:
  - local: index
    title: 🤗 Agents
  - local: guided_tour
    title: Guided tour
- title: Tutorials
  sections:
  - local: tutorials/building_good_agents
    title: ✨ Building good agents
  - local: tutorials/tools
    title: 🛠️ Tools - in-depth guide
  - local: tutorials/secure_code_execution
    title: 🛡️ Secure your code execution with E2B
- title: Conceptual guides
  sections:
  - local: conceptual_guides/intro_agents
    title: 🤖 An introduction to agentic systems
  - local: conceptual_guides/react
    title: 🤔 How do Multi-step agents work?
- title: Examples
  sections:
  - local: examples/text_to_sql
    title: Self-correcting Text-to-SQL
  - local: examples/rag
    title: Master you knowledge base with agentic RAG
  - local: examples/multiagents
    title: Orchestrate a multi-agent system
- title: Reference
  sections:
  - local: reference/agents
    title: Agent-related objects
  - local: reference/tools
    title: Tool-related objects

```

## File: docs/source/en/index.md

<a name='file-docs-source-en-index.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# `smolagents`

This library is the simplest framework out there to build powerful agents! By the way, wtf are "agents"? We provide our definition [in this page](conceptual_guides/intro_agents), where you'll also find tips for when to use them or not (spoilers: you'll often be better off without agents).

This library offers:

✨ **Simplicity**: the logic for agents fits in ~thousand lines of code. We kept abstractions to their minimal shape above raw code!

🌐 **Support for any LLM**: it supports models hosted on the Hub loaded in their `transformers` version or through our inference API, but also models from OpenAI, Anthropic... it's really easy to power an agent with any LLM.

🧑‍💻 **First-class support for Code Agents**, i.e. agents that write their actions in code (as opposed to "agents being used to write code"), [read more here](tutorials/secure_code_execution).

🤗 **Hub integrations**: you can share and load tools to/from the Hub, and more is to come!

<div class="mt-10">
  <div class="w-full flex flex-col space-y-4 md:space-y-0 md:grid md:grid-cols-2 md:gap-y-4 md:gap-x-5">
    <a class="!no-underline border dark:border-gray-700 p-5 rounded-lg shadow hover:shadow-lg" href="./guided_tour"
      ><div class="w-full text-center bg-gradient-to-br from-blue-400 to-blue-500 rounded-lg py-1.5 font-semibold mb-5 text-white text-lg leading-relaxed">Guided tour</div>
      <p class="text-gray-700">Learn the basics and become familiar with using Agents. Start here if you are using Agents for the first time!</p>
    </a>
    <a class="!no-underline border dark:border-gray-700 p-5 rounded-lg shadow hover:shadow-lg" href="./examples/text_to_sql"
      ><div class="w-full text-center bg-gradient-to-br from-indigo-400 to-indigo-500 rounded-lg py-1.5 font-semibold mb-5 text-white text-lg leading-relaxed">How-to guides</div>
      <p class="text-gray-700">Practical guides to help you achieve a specific goal: create an agent to generate and test SQL queries!</p>
    </a>
    <a class="!no-underline border dark:border-gray-700 p-5 rounded-lg shadow hover:shadow-lg" href="./conceptual_guides/intro_agents"
      ><div class="w-full text-center bg-gradient-to-br from-pink-400 to-pink-500 rounded-lg py-1.5 font-semibold mb-5 text-white text-lg leading-relaxed">Conceptual guides</div>
      <p class="text-gray-700">High-level explanations for building a better understanding of important topics.</p>
   </a>
    <a class="!no-underline border dark:border-gray-700 p-5 rounded-lg shadow hover:shadow-lg" href="./tutorials/building_good_agents"
      ><div class="w-full text-center bg-gradient-to-br from-purple-400 to-purple-500 rounded-lg py-1.5 font-semibold mb-5 text-white text-lg leading-relaxed">Tutorials</div>
      <p class="text-gray-700">Horizontal tutorials that cover important aspects of building agents.</p>
    </a>
  </div>
</div>

```

## File: docs/source/en/reference/tools.md

<a name='file-docs-source-en-reference-tools.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Tools

<Tip warning={true}>

Smolagents is an experimental API which is subject to change at any time. Results returned by the agents
can vary as the APIs or underlying models are prone to change.

</Tip>

To learn more about agents and tools make sure to read the [introductory guide](../index). This page
contains the API docs for the underlying classes.

## Tools

### load_tool

[[autodoc]] load_tool

### tool

[[autodoc]] tool

### Tool

[[autodoc]] Tool

### launch_gradio_demo

[[autodoc]] launch_gradio_demo

## Default tools

### PythonInterpreterTool

[[autodoc]] PythonInterpreterTool

### DuckDuckGoSearchTool

[[autodoc]] DuckDuckGoSearchTool

### VisitWebpageTool

[[autodoc]] VisitWebpageTool

## ToolCollection

[[autodoc]] ToolCollection

## Agent Types

Agents can handle any type of object in-between tools; tools, being completely multimodal, can accept and return
text, image, audio, video, among other types. In order to increase compatibility between tools, as well as to 
correctly render these returns in ipython (jupyter, colab, ipython notebooks, ...), we implement wrapper classes
around these types.

The wrapped objects should continue behaving as initially; a text object should still behave as a string, an image
object should still behave as a `PIL.Image`.

These types have three specific purposes:

- Calling `to_raw` on the type should return the underlying object
- Calling `to_string` on the type should return the object as a string: that can be the string in case of an `AgentText`
  but will be the path of the serialized version of the object in other instances
- Displaying it in an ipython kernel should display the object correctly

### AgentText

[[autodoc]] smolagents.types.AgentText

### AgentImage

[[autodoc]] smolagents.types.AgentImage

### AgentAudio

[[autodoc]] smolagents.types.AgentAudio

```

## File: docs/source/en/reference/agents.md

<a name='file-docs-source-en-reference-agents.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Agents

<Tip warning={true}>

Smolagents is an experimental API which is subject to change at any time. Results returned by the agents
can vary as the APIs or underlying models are prone to change.

</Tip>

To learn more about agents and tools make sure to read the [introductory guide](../index). This page
contains the API docs for the underlying classes.

## Agents

Our agents inherit from [`MultiStepAgent`], which means they can act in multiple steps, each step consisting of one thought, then one tool call and execution. Read more in [this conceptual guide](../conceptual_guides/react).

We provide two types of agents, based on the main [`Agent`] class.
  - [`CodeAgent`] is the default agent, it writes its tool calls in Python code.
  - [`ToolCallingAgent`] writes its tool calls in JSON.

Both require arguments `model` and list of tools `tools` at initialization.


### Classes of agents

[[autodoc]] MultiStepAgent

[[autodoc]] CodeAgent

[[autodoc]] ToolCallingAgent


### ManagedAgent

[[autodoc]] ManagedAgent

### stream_to_gradio

[[autodoc]] stream_to_gradio

### GradioUI

[[autodoc]] GradioUI

## Models

You're free to create and use your own models to power your agent.

You could use any `model` callable for your agent, as long as:
1. It follows the [messages format](./chat_templating) (`List[Dict[str, str]]`) for its input `messages`, and it returns a `str`.
2. It stops generating outputs *before* the sequences passed in the argument `stop_sequences`

For defining your LLM, you can make a `custom_model` method which accepts a list of [messages](./chat_templating) and returns an object with a .content attribute containing the text. This callable also needs to accept a `stop_sequences` argument that indicates when to stop generating.

```python
from huggingface_hub import login, InferenceClient

login("<YOUR_HUGGINGFACEHUB_API_TOKEN>")

model_id = "meta-llama/Llama-3.3-70B-Instruct"

client = InferenceClient(model=model_id)

def custom_model(messages, stop_sequences=["Task"]):
    response = client.chat_completion(messages, stop=stop_sequences, max_tokens=1000)
    answer = response.choices[0].message
    return answer
```

Additionally, `custom_model` can also take a `grammar` argument. In the case where you specify a `grammar` upon agent initialization, this argument will be passed to the calls to model, with the `grammar` that you defined upon initialization, to allow [constrained generation](https://huggingface.co/docs/text-generation-inference/conceptual/guidance) in order to force properly-formatted agent outputs.

### TransformersModel

For convenience, we have added a `TransformersModel` that implements the points above by building a local `transformers` pipeline for the model_id given at initialization.

```python
from smolagents import TransformersModel

model = TransformersModel(model_id="HuggingFaceTB/SmolLM-135M-Instruct")

print(model([{"role": "user", "content": "Ok!"}], stop_sequences=["great"]))
```
```text
>>> What a
```

[[autodoc]] TransformersModel

### HfApiModel

The `HfApiModel` wraps an [HF Inference API](https://huggingface.co/docs/api-inference/index) client for the execution of the LLM.

```python
from smolagents import HfApiModel

messages = [
  {"role": "user", "content": "Hello, how are you?"},
  {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
  {"role": "user", "content": "No need to help, take it easy."},
]

model = HfApiModel()
print(model(messages))
```
```text
>>> Of course! If you change your mind, feel free to reach out. Take care!
```
[[autodoc]] HfApiModel

### LiteLLMModel

The `LiteLLMModel` leverages [LiteLLM](https://www.litellm.ai/) to support 100+ LLMs from various providers.
You can pass kwargs upon model initialization that will then be used whenever using the model, for instance below we pass `temperature`.

```python
from smolagents import LiteLLMModel

messages = [
  {"role": "user", "content": "Hello, how are you?"},
  {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
  {"role": "user", "content": "No need to help, take it easy."},
]

model = LiteLLMModel("anthropic/claude-3-5-sonnet-latest", temperature=0.2)
print(model(messages, max_tokens=10))
```

[[autodoc]] LiteLLMModel

```

## File: docs/source/en/conceptual_guides/react.md

<a name='file-docs-source-en-conceptual_guides-react.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# How do multi-step agents work?

The ReAct framework ([Yao et al., 2022](https://huggingface.co/papers/2210.03629)) is currently the main approach to building agents.

The name is based on the concatenation of two words, "Reason" and "Act." Indeed, agents following this architecture will solve their task in as many steps as needed, each step consisting of a Reasoning step, then an Action step where it formulates tool calls that will bring it closer to solving the task at hand.

React process involves keeping a memory of past steps.

> [!TIP]
> Read [Open-source LLMs as LangChain Agents](https://huggingface.co/blog/open-source-llms-as-agents) blog post to learn more about multi-step agents.

Here is a video overview of how that works:

<div class="flex justify-center">
    <img
        class="block dark:hidden"
        src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/Agent_ManimCE.gif"
    />
    <img
        class="hidden dark:block"
        src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/Agent_ManimCE.gif"
    />
</div>

![Framework of a React Agent](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/open-source-llms-as-agents/ReAct.png)

We implement two versions of ToolCallingAgent: 
- [`ToolCallingAgent`] generates tool calls as a JSON in its output.
- [`CodeAgent`] is a new type of ToolCallingAgent that generates its tool calls as blobs of code, which works really well for LLMs that have strong coding performance.

> [!TIP]
> We also provide an option to run agents in one-shot: just pass `single_step=True` when launching the agent, like `agent.run(your_task, single_step=True)`
```

## File: docs/source/en/conceptual_guides/intro_agents.md

<a name='file-docs-source-en-conceptual_guides-intro_agents.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Introduction to Agents

## 🤔 What are agents?

Any efficient system using AI will need to provide LLMs some kind of access to the real world: for instance the possibility to call a search tool to get external information, or to act on certain programs in order to solve a task. In other words, LLMs should have ***agency***. Agentic programs are the gateway to the outside world for LLMs.

> [!TIP]
> AI Agents are **programs where LLM outputs control the workflow**.

Any system leveraging LLMs will integrate the LLM outputs into code. The influence of the LLM's input on the code workflow is the level of agency of LLMs in the system.

Note that with this definition, "agent" is not a discrete, 0 or 1 definition: instead, "agency" evolves on a continuous spectrum, as you give more or less power to the LLM on your workflow.

See in the table below how agency can vary across systems:

| Agency Level | Description                                             | How that's called | Example Pattern                                    |
| ------------ | ------------------------------------------------------- | ----------------- | -------------------------------------------------- |
| ☆☆☆          | LLM output has no impact on program flow                | Simple Processor  | `process_llm_output(llm_response)`                 |
| ★☆☆          | LLM output determines an if/else switch                 | Router            | `if llm_decision(): path_a() else: path_b()`       |
| ★★☆          | LLM output determines function execution                | Tool Caller       | `run_function(llm_chosen_tool, llm_chosen_args)`   |
| ★★★          | LLM output controls iteration and program continuation  | Multi-step Agent  | `while llm_should_continue(): execute_next_step()` |
| ★★★          | One agentic workflow can start another agentic workflow | Multi-Agent       | `if llm_trigger(): execute_agent()`                |

The multi-step agent has this code structure:

```python
memory = [user_defined_task]
while llm_should_continue(memory): # this loop is the multi-step part
    action = llm_get_next_action(memory) # this is the tool-calling part
    observations = execute_action(action)
    memory += [action, observations]
```

This agentic system runs in a loop, executing a new action at each step (the action can involve calling some pre-determined *tools* that are just functions), until its observations make it apparent that a satisfactory state has been reached to solve the given task. Here’s an example of how a multi-step agent can solve a simple math question:

<div class="flex justify-center">
    <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/Agent_ManimCE.gif"/>
</div>


## ✅ When to use agents / ⛔ when to avoid them

Agents are useful when you need an LLM to determine the workflow of an app. But they’re often overkill. The question is: do I really need flexibility in the workflow to efficiently solve the task at hand?
If the pre-determined workflow falls short too often, that means you need more flexibility.
Let's take an example: say you're making an app that handles customer requests on a surfing trip website.

You could know in advance that the requests will belong to either of 2 buckets (based on user choice), and you have a predefined workflow for each of these 2 cases.

1. Want some knowledge on the trips? ⇒ give them access to a search bar to search your knowledge base
2. Wants to talk to sales? ⇒ let them type in a contact form.

If that deterministic workflow fits all queries, by all means just code everything! This will give you a 100% reliable system with no risk of error introduced by letting unpredictable LLMs meddle in your workflow. For the sake of simplicity and robustness, it's advised to regularize towards not using any agentic behaviour. 

But what if the workflow can't be determined that well in advance? 

For instance, a user wants to ask : `"I can come on Monday, but I forgot my passport so risk being delayed to Wednesday, is it possible to take me and my stuff to surf on Tuesday morning, with a cancellation insurance?"` This question hinges on many factors, and probably none of the predetermined criteria above will suffice for this request.

If the pre-determined workflow falls short too often, that means you need more flexibility.

That is where an agentic setup helps.

In the above example, you could just make a multi-step agent that has access to a weather API for weather forecasts, Google Maps API to compute travel distance, an employee availability dashboard and a RAG system on your knowledge base.

Until recently, computer programs were restricted to pre-determined workflows, trying to handle complexity by piling up  if/else switches. They focused on extremely narrow tasks, like "compute the sum of these numbers" or "find the shortest path in this graph". But actually, most real-life tasks, like our trip example above, do not fit in pre-determined workflows. Agentic systems open up the vast world of real-world tasks to programs!

## Why `smolagents`?

For some low-level agentic use cases, like chains or routers, you can write all the code yourself. You'll be much better that way, since it will let you control and understand your system better.

But once you start going for more complicated behaviours like letting an LLM call a function (that's "tool calling") or letting an LLM run a while loop ("multi-step agent"), some abstractions become necessary:
- for tool calling, you need to parse the agent's output, so this output needs a predefined format like "Thought: I should call tool 'get_weather'. Action: get_weather(Paris).", that you parse with a predefined function, and system prompt given to the LLM should notify it about this format.
- for a multi-step agent where the LLM output determines the loop, you need to give a different prompt to the LLM based on what happened in the last loop iteration: so you need some kind of memory.

See? With these two examples, we already found the need for a few items to help us:

- Of course, an LLM that acts as the engine powering the system
- A list of tools that the agent can access
- A parser that extracts tool calls from the LLM output
- A system prompt synced with the parser
- A memory

But wait, since we give room to LLMs in decisions, surely they will make mistakes: so we need error logging and retry mechanisms.

All these elements need tight coupling to make a well-functioning system. That's why we decided we needed to make basic building blocks to make all this stuff work together.

## Code agents

In a multi-step agent, at each step, the LLM can write an action, in the form of some calls to external tools. A common format (used by Anthropic, OpenAI, and many others) for writing these actions is generally different shades of "writing actions as a JSON of tools names and arguments to use, which you then parse to know which tool to execute and with which arguments".

[Multiple](https://huggingface.co/papers/2402.01030) [research](https://huggingface.co/papers/2411.01747) [papers](https://huggingface.co/papers/2401.00812) have shown that having the tool calling LLMs in code is much better.

The reason for this simply that *we crafted our code languages specifically to be the best possible way to express actions performed by a computer*. If JSON snippets were a better expression, JSON would be the top programming language and programming would be hell on earth.

The figure below, taken from [Executable Code Actions Elicit Better LLM Agents](https://huggingface.co/papers/2402.01030), illustrate some advantages of writing actions in code:

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/code_vs_json_actions.png">

Writing actions in code rather than JSON-like snippets provides better:

- **Composability:** could you nest JSON actions within each other, or define a set of JSON actions to re-use later, the same way you could just define a python function?
- **Object management:** how do you store the output of an action like `generate_image` in JSON?
- **Generality:** code is built to express simply anything you can have a computer do.
- **Representation in LLM training data:** plenty of quality code actions is already included in LLMs’ training data which means they’re already trained for this!

```

## File: docs/source/en/examples/text_to_sql.md

<a name='file-docs-source-en-examples-text_to_sql.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Text-to-SQL

[[open-in-colab]]

In this tutorial, we’ll see how to implement an agent that leverages SQL using `smolagents`.

> Let's start with the golden question: why not keep it simple and use a standard text-to-SQL pipeline?

A standard text-to-sql pipeline is brittle, since the generated SQL query can be incorrect. Even worse, the query could be incorrect, but not raise an error, instead giving some incorrect/useless outputs without raising an alarm.

👉 Instead, an agent system is able to critically inspect outputs and decide if the query needs to be changed or not, thus giving it a huge performance boost.

Let’s build this agent! 💪

First, we setup the SQL environment:
```py
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Float,
    insert,
    inspect,
    text,
)

engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# create city SQL table
table_name = "receipts"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("customer_name", String(16), primary_key=True),
    Column("price", Float),
    Column("tip", Float),
)
metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
    {"receipt_id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
    {"receipt_id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
    {"receipt_id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
]
for row in rows:
    stmt = insert(receipts).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)
```

### Build our agent

Now let’s make our SQL table retrievable by a tool.

The tool’s description attribute will be embedded in the LLM’s prompt by the agent system: it gives the LLM information about how to use the tool. This is where we want to describe the SQL table.

```py
inspector = inspect(engine)
columns_info = [(col["name"], col["type"]) for col in inspector.get_columns("receipts")]

table_description = "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
print(table_description)
```

```text
Columns:
  - receipt_id: INTEGER
  - customer_name: VARCHAR(16)
  - price: FLOAT
  - tip: FLOAT
```

Now let’s build our tool. It needs the following: (read [the tool doc](../tutorials/tools) for more detail)
- A docstring with an `Args:` part listing arguments.
- Type hints on both inputs and output.

```py
from smolagents import tool

@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'receipts'. Its description is as follows:
        Columns:
        - receipt_id: INTEGER
        - customer_name: VARCHAR(16)
        - price: FLOAT
        - tip: FLOAT

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output
```

Now let us create an agent that leverages this tool.

We use the `CodeAgent`, which is smolagents’ main agent class: an agent that writes actions in code and can iterate on previous output according to the ReAct framework.

The model is the LLM that powers the agent system. `HfApiModel` allows you to call LLMs using HF’s Inference API, either via Serverless or Dedicated endpoint, but you could also use any proprietary API.

```py
from smolagents import CodeAgent, HfApiModel

agent = CodeAgent(
    tools=[sql_engine],
    model=HfApiModel("meta-llama/Meta-Llama-3.1-8B-Instruct"),
)
agent.run("Can you give me the name of the client who got the most expensive receipt?")
```

### Level 2: Table joins

Now let’s make it more challenging! We want our agent to handle joins across multiple tables.

So let’s make a second table recording the names of waiters for each receipt_id!

```py
table_name = "waiters"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("waiter_name", String(16), primary_key=True),
)
metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "waiter_name": "Corey Johnson"},
    {"receipt_id": 2, "waiter_name": "Michael Watts"},
    {"receipt_id": 3, "waiter_name": "Michael Watts"},
    {"receipt_id": 4, "waiter_name": "Margaret James"},
]
for row in rows:
    stmt = insert(receipts).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)
```
Since we changed the table, we update the `SQLExecutorTool` with this table’s description to let the LLM properly leverage information from this table.

```py
updated_description = """Allows you to perform SQL queries on the table. Beware that this tool's output is a string representation of the execution output.
It can use the following tables:"""

inspector = inspect(engine)
for table in ["receipts", "waiters"]:
    columns_info = [(col["name"], col["type"]) for col in inspector.get_columns(table)]

    table_description = f"Table '{table}':\n"

    table_description += "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
    updated_description += "\n\n" + table_description

print(updated_description)
```
Since this request is a bit harder than the previous one, we’ll switch the LLM engine to use the more powerful [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)!

```py
sql_engine.description = updated_description

agent = CodeAgent(
    tools=[sql_engine],
    model=HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct"),
)

agent.run("Which waiter got more total money from tips?")
```
It directly works! The setup was surprisingly simple, wasn’t it?

This example is done! We've touched upon these concepts:
- Building new tools.
- Updating a tool's description.
- Switching to a stronger LLM helps agent reasoning.

✅ Now you can go build this text-to-SQL system you’ve always dreamt of! ✨
```

## File: docs/source/en/examples/multiagents.md

<a name='file-docs-source-en-examples-multiagents.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Orchestrate a multi-agent system 🤖🤝🤖

[[open-in-colab]]

In this notebook we will make a **multi-agent web browser: an agentic system with several agents collaborating to solve problems using the web!**

It will be a simple hierarchy, using a `ManagedAgent` object to wrap the managed web search agent:

```
              +----------------+
              | Manager agent  |
              +----------------+
                       |
        _______________|______________
       |                              |
  Code interpreter   +--------------------------------+
       tool          |         Managed agent          |
                     |      +------------------+      |
                     |      | Web Search agent |      |
                     |      +------------------+      |
                     |         |            |         |
                     |  Web Search tool     |         |
                     |             Visit webpage tool |
                     +--------------------------------+
```
Let's set up this system. 

Run the line below to install the required dependencies:

```
!pip install markdownify duckduckgo-search smolagents --upgrade -q
```

Let's login in order to call the HF Inference API:

```
from huggingface_hub import login

login()
```

⚡️ Our agent will be powered by [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) using `HfApiModel` class that uses HF's Inference API: the Inference API allows to quickly and easily run any OS model.

_Note:_ The Inference API hosts models based on various criteria, and deployed models may be updated or replaced without prior notice. Learn more about it [here](https://huggingface.co/docs/api-inference/supported-models).

```py
model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"
```

## 🔍 Create a web search tool

For web browsing, we can already use our pre-existing [`DuckDuckGoSearchTool`](https://github.com/huggingface/smolagents/blob/main/src/smolagents/default_tools/search.py) tool to provide a Google search equivalent.

But then we will also need to be able to peak into the page found by the `DuckDuckGoSearchTool`.
To do so, we could import the library's built-in `VisitWebpageTool`, but we will build it again to see how it's done.

So let's create our `VisitWebpageTool` tool from scratch using `markdownify`.

```py
import re
import requests
from markdownify import markdownify
from requests.exceptions import RequestException
from smolagents import tool


@tool
def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string.

    Args:
        url: The URL of the webpage to visit.

    Returns:
        The content of the webpage converted to Markdown, or an error message if the request fails.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the HTML content to Markdown
        markdown_content = markdownify(response.text).strip()

        # Remove multiple line breaks
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

        return markdown_content

    except RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
```

Ok, now let's initialize and test our tool!

```py
print(visit_webpage("https://en.wikipedia.org/wiki/Hugging_Face")[:500])
```

## Build our multi-agent system 🤖🤝🤖

Now that we have all the tools `search` and `visit_webpage`, we can use them to create the web agent.

Which configuration to choose for this agent?
- Web browsing is a single-timeline task that does not require parallel tool calls, so JSON tool calling works well for that. We thus choose a `JsonAgent`.
- Also, since sometimes web search requires exploring many pages before finding the correct answer, we prefer to increase the number of `max_steps` to 10.

```py
from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    HfApiModel,
    ManagedAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel,
)

model = HfApiModel(model_id)

web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage],
    model=model,
    max_steps=10,
)
```

We then wrap this agent into a `ManagedAgent` that will make it callable by its manager agent.

```py
managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="search",
    description="Runs web searches for you. Give it your query as an argument.",
)
```

Finally we create a manager agent, and upon initialization we pass our managed agent to it in its `managed_agents` argument.

Since this agent is the one tasked with the planning and thinking, advanced reasoning will be beneficial, so a `CodeAgent` will be the best choice.

Also, we want to ask a question that involves the current year and does additional data calculations: so let us add `additional_authorized_imports=["time", "numpy", "pandas"]`, just in case the agent needs these packages.

```py
manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[managed_web_agent],
    additional_authorized_imports=["time", "numpy", "pandas"],
)
```

That's all! Now let's run our system! We select a question that requires both some calculation and research:

```py
answer = manager_agent.run("If LLM training continues to scale up at the current rhythm until 2030, what would be the electric power in GW required to power the biggest training runs by 2030? What would that correspond to, compared to some countries? Please provide a source for any numbers used.")
```

We get this report as the answer:
```
Based on current growth projections and energy consumption estimates, if LLM trainings continue to scale up at the 
current rhythm until 2030:

1. The electric power required to power the biggest training runs by 2030 would be approximately 303.74 GW, which 
translates to about 2,660,762 GWh/year.

2. Comparing this to countries' electricity consumption:
   - It would be equivalent to about 34% of China's total electricity consumption.
   - It would exceed the total electricity consumption of India (184%), Russia (267%), and Japan (291%).
   - It would be nearly 9 times the electricity consumption of countries like Italy or Mexico.

3. Source of numbers:
   - The initial estimate of 5 GW for future LLM training comes from AWS CEO Matt Garman.
   - The growth projection used a CAGR of 79.80% from market research by Springs.
   - Country electricity consumption data is from the U.S. Energy Information Administration, primarily for the year 
2021.
```

Seems like we'll need some sizeable powerplants if the [scaling hypothesis](https://gwern.net/scaling-hypothesis) continues to hold true.

Our agents managed to efficiently collaborate towards solving the task! ✅

💡 You can easily extend this orchestration to more agents: one does the code execution, one the web search, one handles file loadings...
```

## File: docs/source/en/examples/rag.md

<a name='file-docs-source-en-examples-rag.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Agentic RAG

[[open-in-colab]]

Retrieval-Augmented-Generation (RAG) is “using an LLM to answer a user query, but basing the answer on information retrieved from a knowledge base”. It has many advantages over using a vanilla or fine-tuned LLM: to name a few, it allows to ground the answer on true facts and reduce confabulations, it allows to provide the LLM with domain-specific knowledge, and it allows fine-grained control of access to information from the knowledge base.

But vanilla RAG has limitations, most importantly these two:
- It performs only one retrieval step: if the results are bad, the generation in turn will be bad.
- Semantic similarity is computed with the user query as a reference, which might be suboptimal: for instance, the user query will often be a question and the document containing the true answer will be in affirmative voice, so its similarity score will be downgraded compared to other source documents in the interrogative form, leading to a risk of missing the relevant information.

We can alleviate these problems by making a RAG agent: very simply, an agent armed with a retriever tool!

This agent will: ✅ Formulate the query itself and ✅ Critique to re-retrieve if needed.

So it should naively recover some advanced RAG techniques!
- Instead of directly using the user query as the reference in semantic search, the agent formulates itself a reference sentence that can be closer to the targeted documents, as in [HyDE](https://huggingface.co/papers/2212.10496).
The agent can use the generated snippets and re-retrieve if needed, as in [Self-Query](https://docs.llamaindex.ai/en/stable/examples/evaluation/RetryQuery/).

Let's build this system. 🛠️

Run the line below to install required dependencies:
```bash
!pip install smolagents pandas langchain langchain-community sentence-transformers rank_bm25 --upgrade -q
```
To call the HF Inference API, you will need a valid token as your environment variable `HF_TOKEN`.
We use python-dotenv to load it.
```py
from dotenv import load_dotenv
load_dotenv()
```

We first load a knowledge base on which we want to perform RAG: this dataset is a compilation of the documentation pages for many Hugging Face libraries, stored as markdown. We will keep only the documentation for the `transformers` library.

Then prepare the knowledge base by processing the dataset and storing it into a vector database to be used by the retriever.

We use [LangChain](https://python.langchain.com/docs/introduction/) for its excellent vector database utilities.

```py
import datasets
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever

knowledge_base = datasets.load_dataset("m-ric/huggingface_doc", split="train")
knowledge_base = knowledge_base.filter(lambda row: row["source"].startswith("huggingface/transformers"))

source_docs = [
    Document(page_content=doc["text"], metadata={"source": doc["source"].split("/")[1]})
    for doc in knowledge_base
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    add_start_index=True,
    strip_whitespace=True,
    separators=["\n\n", "\n", ".", " ", ""],
)
docs_processed = text_splitter.split_documents(source_docs)
```

Now the documents are ready.

So let’s build our agentic RAG system!

👉 We only need a RetrieverTool that our agent can leverage to retrieve information from the knowledge base.

Since we need to add a vectordb as an attribute of the tool, we cannot simply use the simple tool constructor with a `@tool` decorator: so we will follow the advanced setup highlighted in the [tools tutorial](../tutorials/tools).

```py
from smolagents import Tool

class RetrieverTool(Tool):
    name = "retriever"
    description = "Uses semantic search to retrieve the parts of transformers documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question.",
        }
    }
    output_type = "string"

    def __init__(self, docs, **kwargs):
        super().__init__(**kwargs)
        self.retriever = BM25Retriever.from_documents(
            docs, k=10
        )

    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"

        docs = self.retriever.invoke(
            query,
        )
        return "\nRetrieved documents:\n" + "".join(
            [
                f"\n\n===== Document {str(i)} =====\n" + doc.page_content
                for i, doc in enumerate(docs)
            ]
        )

retriever_tool = RetrieverTool(docs_processed)
```
We have used BM25, a classic retrieval method, because it's lightning fast to setup.
To improve retrieval accuracy, you could use replace BM25 with semantic search using vector representations for documents: thus you can head to the [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) to select a good embedding model.

Now it’s straightforward to create an agent that leverages this `retriever_tool`!

The agent will need these arguments upon initialization:
- `tools`: a list of tools that the agent will be able to call.
- `model`: the LLM that powers the agent.
Our `model` must be a callable that takes as input a list of messages and returns text. It also needs to accept a stop_sequences argument that indicates when to stop its generation. For convenience, we directly use the HfEngine class provided in the package to get a LLM engine that calls Hugging Face's Inference API.

And we use [meta-llama/Llama-3.3-70B-Instruct](meta-llama/Llama-3.3-70B-Instruct) as the llm engine because:
- It has a long 128k context, which is helpful for processing long source documents
- It is served for free at all times on HF's Inference API!

_Note:_ The Inference API hosts models based on various criteria, and deployed models may be updated or replaced without prior notice. Learn more about it [here](https://huggingface.co/docs/api-inference/supported-models).

```py
from smolagents import HfApiModel, CodeAgent

agent = CodeAgent(
    tools=[retriever_tool], model=HfApiModel("meta-llama/Llama-3.3-70B-Instruct"), max_steps=4, verbosity_level=2
)
```

Upon initializing the CodeAgent, it has been automatically given a default system prompt that tells the LLM engine to process step-by-step and generate tool calls as code snippets, but you could replace this prompt template with your own as needed.

Then when its `.run()` method is launched, the agent takes care of calling the LLM engine, and executing the tool calls, all in a loop that ends only when tool `final_answer` is called with the final answer as its argument.

```py
agent_output = agent.run("For a transformers model training, which is slower, the forward or the backward pass?")

print("Final output:")
print(agent_output)
```




```

## File: docs/source/en/tutorials/secure_code_execution.md

<a name='file-docs-source-en-tutorials-secure_code_execution.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Secure code execution

[[open-in-colab]]

> [!TIP]
> If you're new to building agents, make sure to first read the [intro to agents](../conceptual_guides/intro_agents) and the [guided tour of smolagents](../guided_tour).

### Code agents

[Multiple](https://huggingface.co/papers/2402.01030) [research](https://huggingface.co/papers/2411.01747) [papers](https://huggingface.co/papers/2401.00812) have shown that having the LLM write its actions (the tool calls) in code is much better than the current standard format for tool calling, which is across the industry different shades of "writing actions as a JSON of tools names and arguments to use".

Why is code better? Well, because we crafted our code languages specifically to be great at expressing actions performed by a computer. If JSON snippets was a better way, this package would have been written in JSON snippets and the devil would be laughing at us.

Code is just a better way to express actions on a computer. It has better:
- **Composability:** could you nest JSON actions within each other, or define a set of JSON actions to re-use later, the same way you could just define a python function?
- **Object management:** how do you store the output of an action like `generate_image` in JSON?
- **Generality:** code is built to express simply anything you can do have a computer do.
- **Representation in LLM training corpus:** why not leverage this benediction of the sky that plenty of quality actions have already been included in LLM training corpus?

This is illustrated on the figure below, taken from [Executable Code Actions Elicit Better LLM Agents](https://huggingface.co/papers/2402.01030).

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/code_vs_json_actions.png">

This is why we put emphasis on proposing code agents, in this case python agents, which meant putting higher effort on building secure python interpreters.

### Local python interpreter

By default, the `CodeAgent` runs LLM-generated code in your environment.
This execution is not done by the vanilla Python interpreter: we've re-built a more secure `LocalPythonInterpreter` from the ground up.
This interpreter is designed for security by:
 - Restricting the imports to a list explicitly passed by the user
 - Capping the number of operations to prevent infinite loops and resource bloating.
 - Will not perform any operation that's not pre-defined.

We've used this on many use cases, without ever observing any damage to the environment. 

However this solution is not watertight: one could imagine occasions where LLMs fine-tuned for malignant actions could still hurt your environment. For instance if you've allowed an innocuous package like `Pillow` to process images, the LLM could generate thousands of saves of images to bloat your hard drive.
It's certainly not likely if you've chosen the LLM engine yourself, but it could happen.

So if you want to be extra cautious, you can use the remote code execution option described below.

### E2B code executor

For maximum security, you can use our integration with E2B to run code in a sandboxed environment. This is a remote execution service that runs your code in an isolated container, making it impossible for the code to affect your local environment.

For this, you will need to setup your E2B account and set your `E2B_API_KEY` in your environment variables. Head to [E2B's quickstart documentation](https://e2b.dev/docs/quickstart) for more information.

Then you can install it with `pip install e2b-code-interpreter python-dotenv`.

Now you're set!

To set the code executor to E2B, simply pass the flag `use_e2b_executor=True` when initializing your `CodeAgent`.
Note that you should add all the tool's dependencies in `additional_authorized_imports`, so that the executor installs them.

```py
from smolagents import CodeAgent, VisitWebpageTool, HfApiModel
agent = CodeAgent(
    tools = [VisitWebpageTool()],
    model=HfApiModel(),
    additional_authorized_imports=["requests", "markdownify"],
    use_e2b_executor=True
)

agent.run("What was Abraham Lincoln's preferred pet?")
```

E2B code execution is not compatible with multi-agents at the moment - because having an agent call in a code blob that should be executed remotely is a mess. But we're working on adding it!

```

## File: docs/source/en/tutorials/tools.md

<a name='file-docs-source-en-tutorials-tools.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Tools

[[open-in-colab]]

Here, we're going to see advanced tool usage.

> [!TIP]
> If you're new to building agents, make sure to first read the [intro to agents](../conceptual_guides/intro_agents) and the [guided tour of smolagents](../guided_tour).

- [Tools](#tools)
    - [What is a tool, and how to build one?](#what-is-a-tool-and-how-to-build-one)
    - [Share your tool to the Hub](#share-your-tool-to-the-hub)
    - [Import a Space as a tool](#import-a-space-as-a-tool)
    - [Use LangChain tools](#use-langchain-tools)
    - [Manage your agent's toolbox](#manage-your-agents-toolbox)
    - [Use a collection of tools](#use-a-collection-of-tools)

### What is a tool, and how to build one?

A tool is mostly a function that an LLM can use in an agentic system.

But to use it, the LLM will need to be given an API: name, tool description, input types and descriptions, output type.

So it cannot be only a function. It should be a class.

So at core, the tool is a class that wraps a function with metadata that helps the LLM understand how to use it.

Here's how it looks:

```python
from smolagents import Tool

class HFModelDownloadsTool(Tool):
    name = "model_download_counter"
    description = """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint."""
    inputs = {
        "task": {
            "type": "string",
            "description": "the task category (such as text-classification, depth-estimation, etc)",
        }
    }
    output_type = "string"

    def forward(self, task: str):
        from huggingface_hub import list_models

        model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
        return model.id

model_downloads_tool = HFModelDownloadsTool()
```

The custom tool subclasses [`Tool`] to inherit useful methods. The child class also defines:
- An attribute `name`, which corresponds to the name of the tool itself. The name usually describes what the tool does. Since the code returns the model with the most downloads for a task, let's name it `model_download_counter`.
- An attribute `description` is used to populate the agent's system prompt.
- An `inputs` attribute, which is a dictionary with keys `"type"` and `"description"`. It contains information that helps the Python interpreter make educated choices about the input.
- An `output_type` attribute, which specifies the output type. The types for both `inputs` and `output_type` should be [Pydantic formats](https://docs.pydantic.dev/latest/concepts/json_schema/#generating-json-schema), they can be either of these: [`~AUTHORIZED_TYPES`].
- A `forward` method which contains the inference code to be executed.

And that's all it needs to be used in an agent!

There's another way to build a tool. In the [guided_tour](../guided_tour), we implemented a tool using the `@tool` decorator. The [`tool`] decorator is the recommended way to define simple tools, but sometimes you need more than this: using several methods in a class for more clarity, or using additional class attributes.

In this case, you can build your tool by subclassing [`Tool`] as described above.

### Share your tool to the Hub

You can share your custom tool to the Hub by calling [`~Tool.push_to_hub`] on the tool. Make sure you've created a repository for it on the Hub and are using a token with read access.

```python
model_downloads_tool.push_to_hub("{your_username}/hf-model-downloads", token="<YOUR_HUGGINGFACEHUB_API_TOKEN>")
```

For the push to Hub to work, your tool will need to respect some rules:
- All methods are self-contained, e.g. use variables that come either from their args.
- As per the above point, **all imports should be defined directly within the tool's functions**, else you will get an error when trying to call [`~Tool.save`] or [`~Tool.push_to_hub`] with your custom tool.
- If you subclass the `__init__` method, you can give it no other argument than `self`. This is because arguments set during a specific tool instance's initialization are hard to track, which prevents from sharing them properly to the hub. And anyway, the idea of making a specific class is that you can already set class attributes for anything you need to hard-code (just set `your_variable=(...)` directly under the `class YourTool(Tool):` line). And of course you can still create a class attribute anywhere in your code by assigning stuff to `self.your_variable`.


Once your tool is pushed to Hub, you can visualize it. [Here](https://huggingface.co/spaces/m-ric/hf-model-downloads) is the `model_downloads_tool` that I've pushed. It has a nice gradio interface.

When diving into the tool files, you can find that all the tool's logic is under [tool.py](https://huggingface.co/spaces/m-ric/hf-model-downloads/blob/main/tool.py). That is where you can inspect a tool shared by someone else.

Then you can load the tool with [`load_tool`] or create it with [`~Tool.from_hub`] and pass it to the `tools` parameter in your agent.
Since running tools means running custom code, you need to make sure you trust the repository, thus we require to pass `trust_remote_code=True` to load a tool from the Hub.

```python
from smolagents import load_tool, CodeAgent

model_download_tool = load_tool(
    "{your_username}/hf-model-downloads",
    trust_remote_code=True
)
```

### Import a Space as a tool

You can directly import a Space from the Hub as a tool using the [`Tool.from_space`] method!

You only need to provide the id of the Space on the Hub, its name, and a description that will help you agent understand what the tool does. Under the hood, this will use [`gradio-client`](https://pypi.org/project/gradio-client/) library to call the Space.

For instance, let's import the [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) Space from the Hub and use it to generate an image.

```python
image_generation_tool = Tool.from_space(
    "black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generate an image from a prompt"
)

image_generation_tool("A sunny beach")
```
And voilà, here's your image! 🏖️

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/sunny_beach.webp">

Then you can use this tool just like any other tool.  For example, let's improve the prompt  `a rabbit wearing a space suit` and generate an image of it.

```python
from smolagents import CodeAgent, HfApiModel

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")
agent = CodeAgent(tools=[image_generation_tool], model=model)

agent.run(
    "Improve this prompt, then generate an image of it.", prompt='A rabbit wearing a space suit'
)
```

```text
=== Agent thoughts:
improved_prompt could be "A bright blue space suit wearing rabbit, on the surface of the moon, under a bright orange sunset, with the Earth visible in the background"

Now that I have improved the prompt, I can use the image generator tool to generate an image based on this prompt.
>>> Agent is executing the code below:
image = image_generator(prompt="A bright blue space suit wearing rabbit, on the surface of the moon, under a bright orange sunset, with the Earth visible in the background")
final_answer(image)
```

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/rabbit_spacesuit_flux.webp">

How cool is this? 🤩

### Use LangChain tools

We love Langchain and think it has a very compelling suite of tools.
To import a tool from LangChain, use the `from_langchain()` method.

Here is how you can use it to recreate the intro's search result using a LangChain web search tool.
This tool will need `pip install langchain google-search-results -q` to work properly.
```python
from langchain.agents import load_tools

search_tool = Tool.from_langchain(load_tools(["serpapi"])[0])

agent = CodeAgent(tools=[search_tool], model=model)

agent.run("How many more blocks (also denoted as layers) are in BERT base encoder compared to the encoder from the architecture proposed in Attention is All You Need?")
```

### Manage your agent's toolbox

You can manage an agent's toolbox by adding or replacing a tool in attribute `agent.tools`, since it is a standard dictionary.

Let's add the `model_download_tool` to an existing agent initialized with only the default toolbox.

```python
from smolagents import HfApiModel

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

agent = CodeAgent(tools=[], model=model, add_base_tools=True)
agent.tools[model_download_tool.name] = model_download_tool
```
Now we can leverage the new tool:

```python
agent.run(
    "Can you give me the name of the model that has the most downloads in the 'text-to-video' task on the Hugging Face Hub but reverse the letters?"
)
```


> [!TIP]
> Beware of not adding too many tools to an agent: this can overwhelm weaker LLM engines.


### Use a collection of tools

You can leverage tool collections by using the `ToolCollection` object, with the slug of the collection you want to use.
Then pass them as a list to initialize your agent, and start using them!

```py
from smolagents import ToolCollection, CodeAgent

image_tool_collection = ToolCollection(
    collection_slug="huggingface-tools/diffusion-tools-6630bb19a942c2306a2cdb6f",
    token="<YOUR_HUGGINGFACEHUB_API_TOKEN>"
)
agent = CodeAgent(tools=[*image_tool_collection.tools], model=model, add_base_tools=True)

agent.run("Please draw me a picture of rivers and lakes.")
```

To speed up the start, tools are loaded only if called by the agent.

```

## File: docs/source/en/tutorials/building_good_agents.md

<a name='file-docs-source-en-tutorials-building_good_agents.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Building good agents

[[open-in-colab]]

There's a world of difference between building an agent that works and one that doesn't.
How can we build agents that fall into the latter category?
In this guide, we're going to see best practices for building agents.

> [!TIP]
> If you're new to building agents, make sure to first read the [intro to agents](../conceptual_guides/intro_agents) and the [guided tour of smolagents](../guided_tour).

### The best agentic systems are the simplest: simplify the workflow as much as you can

Giving an LLM some agency in your workflow introduces some risk of errors.

Well-programmed agentic systems have good error logging and retry mechanisms anyway, so the LLM engine has a chance to self-correct their mistake. But to reduce the risk of LLM error to the maximum, you should simplify your workflow!

Let's revisit the example from the [intro to agents](../conceptual_guides/intro_agents): a bot that answers user queries for a surf trip company.
Instead of letting the agent do 2 different calls for "travel distance API" and "weather API" each time they are asked about a new surf spot, you could just make one unified tool "return_spot_information", a function that calls both APIs at once and returns their concatenated outputs to the user.

This will reduce costs, latency, and error risk!

The main guideline is: Reduce the number of LLM calls as much as you can.

This leads to a few takeaways:
- Whenever possible, group 2 tools in one, like in our example of the two APIs.
- Whenever possible, logic should be based on deterministic functions rather than agentic decisions.

### Improve the information flow to the LLM engine

Remember that your LLM engine is like an *intelligent* robot, tapped into a room with the only communication with the outside world being notes passed under a door.

It won't know of anything that happened if you don't explicitly put that into its prompt.

So first start with making your task very clear!
Since an agent is powered by an LLM, minor variations in your task formulation might yield completely different results.

Then, improve the information flow towards your agent in tool use.

Particular guidelines to follow:
- Each tool should log (by simply using `print` statements inside the tool's `forward` method) everything that could be useful for the LLM engine.
  - In particular, logging detail on tool execution errors would help a lot!

For instance, here's a tool that retrieves weather data based on location and date-time:

First, here's a poor version:
```python
import datetime
from smolagents import tool

def get_weather_report_at_coordinates(coordinates, date_time):
    # Dummy function, returns a list of [temperature in °C, risk of rain on a scale 0-1, wave height in m]
    return [28.0, 0.35, 0.85]

def get_coordinates_from_location(location):
    # Returns dummy coordinates
    return [3.3, -42.0]

@tool
def get_weather_api(location: str, date_time: str) -> str:
    """
    Returns the weather report.

    Args:
        location: the name of the place that you want the weather for.
        date_time: the date and time for which you want the report.
    """
    lon, lat = convert_location_to_coordinates(location)
    date_time = datetime.strptime(date_time)
    return str(get_weather_report_at_coordinates((lon, lat), date_time))
```

Why is it bad?
- there's no precision of the format that should be used for `date_time`
- there's no detail on how location should be specified.
- there's no logging mechanism trying to make explicit failure cases like location not being in a proper format, or date_time not being properly formatted.
- the output format is hard to understand

If the tool call fails, the error trace logged in memory can help the LLM reverse engineer the tool to fix the errors. But why leave it with so much heavy lifting to do?

A better way to build this tool would have been the following:
```python
@tool
def get_weather_api(location: str, date_time: str) -> str:
    """
    Returns the weather report.

    Args:
        location: the name of the place that you want the weather for. Should be a place name, followed by possibly a city name, then a country, like "Anchor Point, Taghazout, Morocco".
        date_time: the date and time for which you want the report, formatted as '%m/%d/%y %H:%M:%S'.
    """
    lon, lat = convert_location_to_coordinates(location)
    try:
        date_time = datetime.strptime(date_time)
    except Exception as e:
        raise ValueError("Conversion of `date_time` to datetime format failed, make sure to provide a string in format '%m/%d/%y %H:%M:%S'. Full trace:" + str(e))
    temperature_celsius, risk_of_rain, wave_height = get_weather_report_at_coordinates((lon, lat), date_time)
    return f"Weather report for {location}, {date_time}: Temperature will be {temperature_celsius}°C, risk of rain is {risk_of_rain*100:.0f}%, wave height is {wave_height}m."
```

In general, to ease the load on your LLM, the good question to ask yourself is: "How easy would it be for me, if I was dumb and using this tool for the first time ever, to program with this tool and correct my own errors?".

### Give more arguments to the agent

To pass some additional objects to your agent beyond the simple string describing the task, you can use the `additional_args` argument to pass any type of object:

```py
from smolagents import CodeAgent, HfApiModel

model_id = "meta-llama/Llama-3.3-70B-Instruct"

agent = CodeAgent(tools=[], model=HfApiModel(model_id=model_id), add_base_tools=True)

agent.run(
    "Why does Mike not know many people in New York?",
    additional_args={"mp3_sound_file_url":'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/recording.mp3'}
)
```
For instance, you can use this `additional_args` argument to pass images or strings that you want your agent to leverage.



## How to debug your agent

### 1. Use a stronger LLM

In an agentic workflows, some of the errors are actual errors, some other are the fault of your LLM engine not reasoning properly.
For instance, consider this trace for an `CodeAgent` that I asked to create a car picture:
```
==================================================================================================== New task ====================================================================================================
Make me a cool car picture
──────────────────────────────────────────────────────────────────────────────────────────────────── New step ────────────────────────────────────────────────────────────────────────────────────────────────────
Agent is executing the code below: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
image_generator(prompt="A cool, futuristic sports car with LED headlights, aerodynamic design, and vibrant color, high-res, photorealistic")
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Last output from code snippet: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
/var/folders/6m/9b1tts6d5w960j80wbw9tx3m0000gn/T/tmpx09qfsdd/652f0007-3ee9-44e2-94ac-90dae6bb89a4.png
Step 1:

- Time taken: 16.35 seconds
- Input tokens: 1,383
- Output tokens: 77
──────────────────────────────────────────────────────────────────────────────────────────────────── New step ────────────────────────────────────────────────────────────────────────────────────────────────────
Agent is executing the code below: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
final_answer("/var/folders/6m/9b1tts6d5w960j80wbw9tx3m0000gn/T/tmpx09qfsdd/652f0007-3ee9-44e2-94ac-90dae6bb89a4.png")
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Print outputs:

Last output from code snippet: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
/var/folders/6m/9b1tts6d5w960j80wbw9tx3m0000gn/T/tmpx09qfsdd/652f0007-3ee9-44e2-94ac-90dae6bb89a4.png
Final answer:
/var/folders/6m/9b1tts6d5w960j80wbw9tx3m0000gn/T/tmpx09qfsdd/652f0007-3ee9-44e2-94ac-90dae6bb89a4.png
```
The user sees, instead of an image being returned, a path being returned to them.
It could look like a bug from the system, but actually the agentic system didn't cause the error: it's just that the LLM brain did the mistake of not saving the image output into a variable.
Thus it cannot access the image again except by leveraging the path that was logged while saving the image, so it returns the path instead of an image.

The first step to debugging your agent is thus "Use a more powerful LLM". Alternatives like `Qwen2/5-72B-Instruct` wouldn't have made that mistake.

### 2. Provide more guidance / more information

You can also use less powerful models, provided you guide them more effectively.

Put yourself in the shoes of your model: if you were the model solving the task, would you struggle with the information available to you (from the system prompt + task formulation + tool description) ?

Would you need some added clarifications?

To provide extra information, we do not recommend to change the system prompt right away: the default system prompt has many adjustments that you do not want to mess up except if you understand the prompt very well.
Better ways to guide your LLM engine are:
- If it's about the task to solve: add all these details to the task. The task could be 100s of pages long.
- If it's about how to use tools: the description attribute of your tools.


### 3. Change the system prompt (generally not advised)

If above clarifications are not sufficient, you can change the system prompt.

Let's see how it works. For example, let us check the default system prompt for the [`CodeAgent`] (below version is shortened by skipping zero-shot examples).

```python
print(agent.system_prompt_template)
```
Here is what you get:
```text
You are an expert assistant who can solve any task using code blobs. You will be given a task to solve as best you can.
To do so, you have been given access to a list of tools: these tools are basically Python functions which you can call with code.
To solve the task, you must plan forward to proceed in a series of steps, in a cycle of 'Thought:', 'Code:', and 'Observation:' sequences.

At each step, in the 'Thought:' sequence, you should first explain your reasoning towards solving the task and the tools that you want to use.
Then in the 'Code:' sequence, you should write the code in simple Python. The code sequence must end with '<end_code>' sequence.
During each intermediate step, you can use 'print()' to save whatever important information you will then need.
These print outputs will then appear in the 'Observation:' field, which will be available as input for the next step.
In the end you have to return a final answer using the `final_answer` tool.

Here are a few examples using notional tools:
---
{examples}

Above example were using notional tools that might not exist for you. On top of performing computations in the Python code snippets that you create, you only have access to these tools:

{{tool_descriptions}}

{{managed_agents_descriptions}}

Here are the rules you should always follow to solve your task:
1. Always provide a 'Thought:' sequence, and a 'Code:\n```py' sequence ending with '```<end_code>' sequence, else you will fail.
2. Use only variables that you have defined!
3. Always use the right arguments for the tools. DO NOT pass the arguments as a dict as in 'answer = wiki({'query': "What is the place where James Bond lives?"})', but use the arguments directly as in 'answer = wiki(query="What is the place where James Bond lives?")'.
4. Take care to not chain too many sequential tool calls in the same code block, especially when the output format is unpredictable. For instance, a call to search has an unpredictable return format, so do not have another tool call that depends on its output in the same block: rather output results with print() to use them in the next block.
5. Call a tool only when needed, and never re-do a tool call that you previously did with the exact same parameters.
6. Don't name any new variable with the same name as a tool: for instance don't name a variable 'final_answer'.
7. Never create any notional variables in our code, as having these in your logs might derail you from the true variables.
8. You can use imports in your code, but only from the following list of modules: {{authorized_imports}}
9. The state persists between code executions: so if in one step you've created variables or imported modules, these will all persist.
10. Don't give up! You're in charge of solving the task, not providing directions to solve it.

Now Begin! If you solve the task correctly, you will receive a reward of $1,000,000.
```

As you can see, there are placeholders like `"{{tool_descriptions}}"`: these will be used upon agent initialization to insert certain automatically generated descriptions of tools or managed agents.

So while you can overwrite this system prompt template by passing your custom prompt as an argument to the `system_prompt` parameter, your new system prompt must contain the following placeholders:
- `"{{tool_descriptions}}"` to insert tool descriptions.
- `"{{managed_agents_description}}"` to insert the description for managed agents if there are any.
- For `CodeAgent` only: `"{{authorized_imports}}"` to insert the list of authorized imports.

Then you can change the system prompt as follows:

```py
from smolagents.prompts import CODE_SYSTEM_PROMPT

modified_system_prompt = CODE_SYSTEM_PROMPT + "\nHere you go!" # Change the system prompt here

agent = CodeAgent(
    tools=[], 
    model=HfApiModel(), 
    system_prompt=modified_system_prompt
)
```

This also works with the [`ToolCallingAgent`].


### 4. Extra planning

We provide a model for a supplementary planning step, that an agent can run regularly in-between normal action steps. In this step, there is no tool call, the LLM is simply asked to update a list of facts it knows and to reflect on what steps it should take next based on those facts.

```py
from smolagents import load_tool, CodeAgent, HfApiModel, DuckDuckGoSearchTool
from dotenv import load_dotenv

load_dotenv()

# Import tool from Hub
image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

search_tool = DuckDuckGoSearchTool()

agent = CodeAgent(
    tools=[search_tool],
    model=HfApiModel("Qwen/Qwen2.5-72B-Instruct"),
    planning_interval=3 # This is where you activate planning!
)

# Run it!
result = agent.run(
    "How long would a cheetah at full speed take to run the length of Pont Alexandre III?",
)
```

```

## File: docs/source/zh/_config.py

<a name='file-docs-source-zh-_config.py'></a>
*Description*: This is a Python script.

```python
# docstyle-ignore
INSTALL_CONTENT = """
# Installation
! pip install smolagents
# To install from source instead of the last release, comment the command above and uncomment the following one.
# ! pip install git+https://github.com/huggingface/smolagents.git
"""

notebook_first_cells = [{"type": "code", "content": INSTALL_CONTENT}]
black_avoid_patterns = {
    "{processor_class}": "FakeProcessorClass",
    "{model_class}": "FakeModelClass",
    "{object_class}": "FakeObjectClass",
}

```

## File: docs/source/zh/guided_tour.md

<a name='file-docs-source-zh-guided_tour.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Agents - 导览

[[open-in-colab]]

在本导览中，您将学习如何构建一个 agent（智能体），如何运行它，以及如何自定义它以使其更好地适应您的使用场景。

> [!TIP]
> 译者注：Agent 的业内术语是“智能体”。本译文将保留 agent，不作翻译，以带来更高效的阅读体验。(在中文为主的文章中，It's easier to 注意到英文。Attention Is All You Need!)

> [!TIP]
> 中文社区发布了关于 smolagents 的介绍和实践讲解视频(来源：[Issue#80](https://github.com/huggingface/smolagents/issues/80))，你可以访问[这里](https://www.youtube.com/watch?v=wwN3oAugc4c)进行观看！

### 构建您的 agent

要初始化一个最小化的 agent，您至少需要以下两个参数：

- `model`，一个为您的 agent 提供动力的文本生成模型 - 因为 agent 与简单的 LLM 不同，它是一个使用 LLM 作为引擎的系统。您可以使用以下任一选项：
    - [`TransformersModel`] 使用预初始化的 `transformers` 管道在本地机器上运行推理
    - [`HfApiModel`] 在底层使用 `huggingface_hub.InferenceClient`
    - [`LiteLLMModel`] 让您通过 [LiteLLM](https://docs.litellm.ai/) 调用 100+ 不同的模型！

- `tools`，agent 可以用来解决任务的 `Tools` 列表。它可以是一个空列表。您还可以通过定义可选参数 `add_base_tools=True` 在您的 `tools` 列表之上添加默认工具箱。

一旦有了这两个参数 `tools` 和 `model`，您就可以创建一个 agent 并运行它。您可以使用任何您喜欢的 LLM，无论是通过 [Hugging Face API](https://huggingface.co/docs/api-inference/en/index)、[transformers](https://github.com/huggingface/transformers/)、[ollama](https://ollama.com/)，还是 [LiteLLM](https://www.litellm.ai/)。

<hfoptions id="选择一个LLM">
<hfoption id="Hugging Face API">

Hugging Face API 可以免费使用而无需 token，但会有速率限制。

要访问受限模型或使用 PRO 账户提高速率限制，您需要设置环境变量 `HF_TOKEN` 或在初始化 `HfApiModel` 时传递 `token` 变量。

```python
from smolagents import CodeAgent, HfApiModel

model_id = "meta-llama/Llama-3.3-70B-Instruct"

model = HfApiModel(model_id=model_id, token="<YOUR_HUGGINGFACEHUB_API_TOKEN>")
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```
</hfoption>
<hfoption id="本地Transformers模型">

```python
from smolagents import CodeAgent, TransformersModel

model_id = "meta-llama/Llama-3.2-3B-Instruct"

model = TransformersModel(model_id=model_id)
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```
</hfoption>
<hfoption id="OpenAI或Anthropic API">

要使用 `LiteLLMModel`，您需要设置环境变量 `ANTHROPIC_API_KEY` 或 `OPENAI_API_KEY`，或者在初始化时传递 `api_key` 变量。

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key="YOUR_ANTHROPIC_API_KEY") # 也可以使用 'gpt-4o'
agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```
</hfoption>
<hfoption id="Ollama">

```python
from smolagents import CodeAgent, LiteLLMModel

model = LiteLLMModel(
    model_id="ollama_chat/llama3.2", # 这个模型对于 agent 行为来说有点弱
    api_base="http://localhost:11434", # 如果需要可以替换为远程 open-ai 兼容服务器
    api_key="YOUR_API_KEY" # 如果需要可以替换为 API key
)

agent = CodeAgent(tools=[], model=model, add_base_tools=True)

agent.run(
    "Could you give me the 118th number in the Fibonacci sequence?",
)
```
</hfoption>
</hfoptions>

#### CodeAgent 和 ToolCallingAgent

[`CodeAgent`] 是我们的默认 agent。它将在每一步编写并执行 Python 代码片段。

默认情况下，执行是在您的本地环境中完成的。
这应该是安全的，因为唯一可以调用的函数是您提供的工具（特别是如果只有 Hugging Face 的工具）和一组预定义的安全函数，如 `print` 或 `math` 模块中的函数，所以您已经限制了可以执行的内容。

Python 解释器默认也不允许在安全列表之外导入，所以所有最明显的攻击都不应该成为问题。
您可以通过在初始化 [`CodeAgent`] 时将授权模块作为字符串列表传递给参数 `additional_authorized_imports` 来授权额外的导入：

```py
from smolagents import CodeAgent

agent = CodeAgent(tools=[], model=model, additional_authorized_imports=['requests', 'bs4'])
agent.run("Could you get me the title of the page at url 'https://huggingface.co/blog'?")
```

> [!WARNING]
> LLM 可以生成任意代码然后执行：不要添加任何不安全的导入！

如果生成的代码尝试执行非法操作或出现常规 Python 错误，执行将停止。

您也可以使用 [E2B 代码执行器](https://e2b.dev/docs#what-is-e2-b) 而不是本地 Python 解释器，首先 [设置 `E2B_API_KEY` 环境变量](https://e2b.dev/dashboard?tab=keys)，然后在初始化 agent 时传递 `use_e2b_executor=True`。

> [!TIP]
> 在 [该教程中](tutorials/secure_code_execution) 了解更多关于代码执行的内容。

我们还支持广泛使用的将动作编写为 JSON-like 块的方式：[`ToolCallingAgent`]，它的工作方式与 [`CodeAgent`] 非常相似，当然没有 `additional_authorized_imports`，因为它不执行代码：

```py
from smolagents import ToolCallingAgent

agent = ToolCallingAgent(tools=[], model=model)
agent.run("Could you get me the title of the page at url 'https://huggingface.co/blog'?")
```

### 检查 agent 运行

以下是一些有用的属性，用于检查运行后发生了什么：
- `agent.logs` 存储 agent 的细粒度日志。在 agent 运行的每一步，所有内容都会存储在一个字典中，然后附加到 `agent.logs` 中。
- 运行 `agent.write_inner_memory_from_logs()` 会为 LLM 创建一个 agent 日志的内部内存，作为聊天消息列表。此方法会遍历日志的每一步，并仅存储它感兴趣的内容作为消息：例如，它会将系统提示和任务存储为单独的消息，然后对于每一步，它会将 LLM 输出存储为一条消息，工具调用输出存储为另一条消息。如果您想要更高级别的视图 - 但不是每个日志都会被此方法转录。

## 工具

工具是 agent 使用的原子函数。为了被 LLM 使用，它还需要一些构成其 API 的属性，这些属性将用于向 LLM 描述如何调用此工具：
- 名称
- 描述
- 输入类型和描述
- 输出类型

例如，您可以查看 [`PythonInterpreterTool`]：它有一个名称、描述、输入描述、输出类型和一个执行操作的 `forward` 方法。

当 agent 初始化时，工具属性用于生成工具描述，该描述被嵌入到 agent 的系统提示中。这让 agent 知道它可以使用哪些工具以及为什么。

### 默认工具箱

Transformers 附带了一个用于增强 agent 的默认工具箱，您可以在初始化时通过参数 `add_base_tools = True` 将其添加到您的 agent 中：

- **DuckDuckGo 网页搜索**：使用 DuckDuckGo 浏览器执行网页搜索。
- **Python 代码解释器**：在安全环境中运行 LLM 生成的 Python 代码。只有在使用 `add_base_tools=True` 初始化 [`ToolCallingAgent`] 时才会添加此工具，因为基于代码的 agent 已经可以原生执行 Python 代码
- **转录器**：基于 Whisper-Turbo 构建的语音转文本管道，将音频转录为文本。

您可以通过调用 [`load_tool`] 函数和要执行的任务手动使用工具。

```python
from smolagents import load_tool

search_tool = load_tool("web_search")
print(search_tool("Who's the current president of Russia?"))
```

### 创建一个新工具

您可以创建自己的工具，用于 Hugging Face 默认工具未涵盖的用例。
例如，让我们创建一个工具，返回 Hub 上给定任务下载量最多的模型。

您将从以下代码开始。

```python
from huggingface_hub import list_models

task = "text-classification"

most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
print(most_downloaded_model.id)
```

这段代码可以通过将其包装在一个函数中并添加 `tool` 装饰器快速转换为工具：
这不是构建工具的唯一方法：您可以直接将其定义为 [`Tool`] 的子类，这为您提供了更多的灵活性，例如初始化重型类属性的可能性。

让我们看看这两种选项的工作原理：

<hfoptions id="构建工具">
<hfoption id="使用@tool装饰一个函数">

```py
from smolagents import tool

@tool
def model_download_tool(task: str) -> str:
    """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint.

    Args:
        task: The task for which to get the download count.
    """
    most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
    return most_downloaded_model.id
```

该函数需要：
- 一个清晰的名称。名称应该足够描述此工具的功能，以帮助为 agent 提供动力的 LLM。由于此工具返回任务下载量最多的模型，我们将其命名为 `model_download_tool`。
- 输入和输出的类型提示
- 一个描述，其中包括一个 'Args:' 部分，其中每个参数都被描述（这次没有类型指示，它将从类型提示中提取）。与工具名称一样，此描述是为您的 agent 提供动力的 LLM 的说明书，所以不要忽视它。
所有这些元素将在初始化时自动嵌入到 agent 的系统提示中：因此要努力使它们尽可能清晰！

> [!TIP]
> 此定义格式与 `apply_chat_template` 中使用的工具模式相同，唯一的区别是添加了 `tool` 装饰器：[这里](https://huggingface.co/blog/unified-tool-use#passing-tools-to-a-chat-template) 了解更多关于我们的工具使用 API。
</hfoption>
<hfoption id="子类化Tool">

```py
from smolagents import Tool

class ModelDownloadTool(Tool):
    name = "model_download_tool"
    description = "This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub. It returns the name of the checkpoint."
    inputs = {"task": {"type": "string", "description": "The task for which to get the download count."}}
    output_type = "string"

    def forward(self, task: str) -> str:
        most_downloaded_model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
        return most_downloaded_model.id
```

子类需要以下属性：
- 一个清晰的 `name`。名称应该足够描述此工具的功能，以帮助为 agent 提供动力的 LLM。由于此工具返回任务下载量最多的模型，我们将其命名为 `model_download_tool`。
- 一个 `description`。与 `name` 一样，此描述是为您的 agent 提供动力的 LLM 的说明书，所以不要忽视它。
- 输入类型和描述
- 输出类型
所有这些属性将在初始化时自动嵌入到 agent 的系统提示中：因此要努力使它们尽可能清晰！
</hfoption>
</hfoptions>


然后您可以直接初始化您的 agent：
```py
from smolagents import CodeAgent, HfApiModel
agent = CodeAgent(tools=[model_download_tool], model=HfApiModel())
agent.run(
    "Can you give me the name of the model that has the most downloads in the 'text-to-video' task on the Hugging Face Hub?"
)
```

您将获得以下日志：
```text
╭──────────────────────────────────────── New run ─────────────────────────────────────────╮
│                                                                                          │
│ Can you give me the name of the model that has the most downloads in the 'text-to-video' │
│ task on the Hugging Face Hub?                                                            │
│                                                                                          │
╰─ HfApiModel - Qwen/Qwen2.5-Coder-32B-Instruct ───────────────────────────────────────────╯
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 0 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
╭─ Executing this code: ───────────────────────────────────────────────────────────────────╮
│   1 model_name = model_download_tool(task="text-to-video")                               │
│   2 print(model_name)                                                                    │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
Execution logs:
ByteDance/AnimateDiff-Lightning

Out: None
[Step 0: Duration 0.27 seconds| Input tokens: 2,069 | Output tokens: 60]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Step 1 ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
╭─ Executing this code: ───────────────────────────────────────────────────────────────────╮
│   1 final_answer("ByteDance/AnimateDiff-Lightning")                                      │
╰──────────────────────────────────────────────────────────────────────────────────────────╯
Out - Final answer: ByteDance/AnimateDiff-Lightning
[Step 1: Duration 0.10 seconds| Input tokens: 4,288 | Output tokens: 148]
Out[20]: 'ByteDance/AnimateDiff-Lightning'
```

> [!TIP]
> 在 [专用教程](./tutorials/tools#what-is-a-tool-and-how-to-build-one) 中了解更多关于工具的内容。

## 多 agent

多 agent 系统是随着微软的框架 [Autogen](https://huggingface.co/papers/2308.08155) 引入的。

在这种类型的框架中，您有多个 agent 一起工作来解决您的任务，而不是只有一个。
经验表明，这在大多数基准测试中表现更好。这种更好表现的原因在概念上很简单：对于许多任务，与其使用一个全能系统，您更愿意将单元专门用于子任务。在这里，拥有具有单独工具集和内存的 agent 可以实现高效的专业化。例如，为什么要用网页搜索 agent 访问的所有网页内容填充代码生成 agent 的内存？最好将它们分开。

您可以使用 `smolagents` 轻松构建分层多 agent 系统。

为此，将 agent 封装在 [`ManagedAgent`] 对象中。此对象需要参数 `agent`、`name` 和 `description`，这些参数将嵌入到管理 agent 的系统提示中，以让它知道如何调用此托管 agent，就像我们对工具所做的那样。

以下是一个使用我们的 [`DuckDuckGoSearchTool`] 制作一个管理特定网页搜索 agent 的 agent 的示例：

```py
from smolagents import CodeAgent, HfApiModel, DuckDuckGoSearchTool, ManagedAgent

model = HfApiModel()

web_agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="web_search",
    description="Runs web searches for you. Give it your query as an argument."
)

manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[managed_web_agent]
)

manager_agent.run("Who is the CEO of Hugging Face?")
```

> [!TIP]
> 有关高效多 agent 实现的深入示例，请参阅 [我们如何将多 agent 系统推向 GAIA 排行榜的顶部](https://huggingface.co/blog/beating-gaia)。


## 与您的 agent 交谈并在酷炫的 Gradio 界面中可视化其思考过程

您可以使用 `GradioUI` 交互式地向您的 agent 提交任务并观察其思考和执行过程，以下是一个示例：

```py
from smolagents import (
    load_tool,
    CodeAgent,
    HfApiModel,
    GradioUI
)

# 从 Hub 导入工具
image_generation_tool = load_tool("m-ric/text-to-image")

model = HfApiModel(model_id)

# 使用图像生成工具初始化 agent
agent = CodeAgent(tools=[image_generation_tool], model=model)

GradioUI(agent).launch()
```

在底层，当用户输入新答案时，agent 会以 `agent.run(user_request, reset=False)` 启动。
`reset=False` 标志意味着在启动此新任务之前不会刷新 agent 的内存，这使得对话可以继续。

您也可以在其他 agent 化应用程序中使用此 `reset=False` 参数来保持对话继续。

## 下一步

要更深入地使用，您将需要查看我们的教程：
- [我们的代码 agent 如何工作的解释](./tutorials/secure_code_execution)
- [本指南关于如何构建好的 agent](./tutorials/building_good_agents)。
- [工具使用的深入指南](./tutorials/tools)。

```

## File: docs/source/zh/_toctree.yml

<a name='file-docs-source-zh-_toctree.yml'></a>
*Description*: No specific description available.

```plaintext
- title: 起步
  sections:
  - local: index
    title: 🤗 Agents
  - local: guided_tour
    title: 导览
- title: Tutorials
  sections:
  - local: tutorials/building_good_agents
    title: ✨ 构建好用的 agents
  - local: tutorials/tools
    title: 🛠️ 工具 - 深度指南
  - local: tutorials/secure_code_execution
    title: 🛡️ 使用 E2B 保护你的代码执行
- title: Conceptual guides
  sections:
  - local: conceptual_guides/intro_agents
    title: 🤖 Agent 化系统介绍
  - local: conceptual_guides/react
    title: 🤔 多步骤 Agent 是如何工作的？
- title: Examples
  sections:
  - local: examples/text_to_sql
    title: Self-correcting Text-to-SQL
  - local: examples/rag
    title: Master you knowledge base with agentic RAG
  - local: examples/multiagents
    title: Orchestrate a multi-agent system
- title: Reference
  sections:
  - local: reference/agents
    title: Agent-related objects
  - local: reference/tools
    title: Tool-related objects

```

## File: docs/source/zh/index.md

<a name='file-docs-source-zh-index.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.
-->

# `smolagents`

这是构建强大 agent 的最简单框架！顺便问一下，什么是 "agent"？我们在[此页面](conceptual_guides/intro_agents)提供了我们的定义，您还可以找到关于何时使用或不使用它们的建议（剧透：通常不使用 agent 会更好）。

> [!TIP]
> 译者注：Agent 的业内术语是“智能体”。本译文将保留 agent，不作翻译，以带来更高效的阅读体验。(在中文为主的文章中，It's easier to 注意到英文。Attention Is All You Need!)

本库提供：

✨ **简洁性**：Agent 逻辑仅需约千行代码。我们将抽象保持在原始代码之上的最小形态！

🌐 **支持任何 LLM**：支持通过 Hub 托管的模型，使用其 `transformers` 版本或通过我们的推理 API 加载，也支持 OpenAI、Anthropic 等模型。使用任何 LLM 为 agent 提供动力都非常容易。

🧑‍💻 **一流的代码 agent 支持**，即编写代码作为其操作的 agent（与"用于编写代码的 agent"相对），[在此了解更多](tutorials/secure_code_execution)。

🤗 **Hub 集成**：您可以在 Hub 上共享和加载工具，更多功能即将推出！

<div class="mt-10">
  <div class="w-full flex flex-col space-y-4 md:space-y-0 md:grid md:grid-cols-2 md:gap-y-4 md:gap-x-5">
    <a class="!no-underline border dark:border-gray-700 p-5 rounded-lg shadow hover:shadow-lg" href="./guided_tour"
      ><div class="w-full text-center bg-gradient-to-br from-blue-400 to-blue-500 rounded-lg py-1.5 font-semibold mb-5 text-white text-lg leading-relaxed">导览</div>
      <p class="text-gray-700">学习基础知识并熟悉使用 agent。如果您是第一次使用 agent，请从这里开始！</p>
    </a>
    <a class="!no-underline border dark:border-gray-700 p-5 rounded-lg shadow hover:shadow-lg" href="./examples/text_to_sql"
      ><div class="w-full text-center bg-gradient-to-br from-indigo-400 to-indigo-500 rounded-lg py-1.5 font-semibold mb-5 text-white text-lg leading-relaxed">操作指南</div>
      <p class="text-gray-700">实用指南，帮助您实现特定目标：创建一个生成和测试 SQL 查询的 agent！</p>
    </a>
    <a class="!no-underline border dark:border-gray-700 p-5 rounded-lg shadow hover:shadow-lg" href="./conceptual_guides/intro_agents"
      ><div class="w-full text-center bg-gradient-to-br from-pink-400 to-pink-500 rounded-lg py-1.5 font-semibold mb-5 text-white text-lg leading-relaxed">概念指南</div>
      <p class="text-gray-700">高级解释，帮助您更好地理解重要主题。</p>
   </a>
    <a class="!no-underline border dark:border-gray-700 p-5 rounded-lg shadow hover:shadow-lg" href="./tutorials/building_good_agents"
      ><div class="w-full text-center bg-gradient-to-br from-purple-400 to-purple-500 rounded-lg py-1.5 font-semibold mb-5 text-white text-lg leading-relaxed">教程</div>
      <p class="text-gray-700">涵盖构建 agent 重要方面的横向教程。</p>
    </a>
  </div>
</div>

```

## File: docs/source/zh/reference/tools.md

<a name='file-docs-source-zh-reference-tools.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Tools

<Tip warning={true}>

Smolagents is an experimental API which is subject to change at any time. Results returned by the agents
can vary as the APIs or underlying models are prone to change.

</Tip>

To learn more about agents and tools make sure to read the [introductory guide](../index). This page
contains the API docs for the underlying classes.

## Tools

### load_tool

[[autodoc]] load_tool

### tool

[[autodoc]] tool

### Tool

[[autodoc]] Tool

### launch_gradio_demo

[[autodoc]] launch_gradio_demo

## Default tools

### PythonInterpreterTool

[[autodoc]] PythonInterpreterTool

### DuckDuckGoSearchTool

[[autodoc]] DuckDuckGoSearchTool

### VisitWebpageTool

[[autodoc]] VisitWebpageTool

## ToolCollection

[[autodoc]] ToolCollection

## Agent Types

Agents can handle any type of object in-between tools; tools, being completely multimodal, can accept and return
text, image, audio, video, among other types. In order to increase compatibility between tools, as well as to 
correctly render these returns in ipython (jupyter, colab, ipython notebooks, ...), we implement wrapper classes
around these types.

The wrapped objects should continue behaving as initially; a text object should still behave as a string, an image
object should still behave as a `PIL.Image`.

These types have three specific purposes:

- Calling `to_raw` on the type should return the underlying object
- Calling `to_string` on the type should return the object as a string: that can be the string in case of an `AgentText`
  but will be the path of the serialized version of the object in other instances
- Displaying it in an ipython kernel should display the object correctly

### AgentText

[[autodoc]] smolagents.types.AgentText

### AgentImage

[[autodoc]] smolagents.types.AgentImage

### AgentAudio

[[autodoc]] smolagents.types.AgentAudio

```

## File: docs/source/zh/reference/agents.md

<a name='file-docs-source-zh-reference-agents.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Agents

<Tip warning={true}>

Smolagents is an experimental API which is subject to change at any time. Results returned by the agents
can vary as the APIs or underlying models are prone to change.

</Tip>

To learn more about agents and tools make sure to read the [introductory guide](../index). This page
contains the API docs for the underlying classes.

## Agents

Our agents inherit from [`MultiStepAgent`], which means they can act in multiple steps, each step consisting of one thought, then one tool call and execution. Read more in [this conceptual guide](../conceptual_guides/react).

We provide two types of agents, based on the main [`Agent`] class.
  - [`CodeAgent`] is the default agent, it writes its tool calls in Python code.
  - [`ToolCallingAgent`] writes its tool calls in JSON.

Both require arguments `model` and list of tools `tools` at initialization.


### Classes of agents

[[autodoc]] MultiStepAgent

[[autodoc]] CodeAgent

[[autodoc]] ToolCallingAgent


### ManagedAgent

[[autodoc]] ManagedAgent

### stream_to_gradio

[[autodoc]] stream_to_gradio

### GradioUI

[[autodoc]] GradioUI

## Models

You're free to create and use your own models to power your agent.

You could use any `model` callable for your agent, as long as:
1. It follows the [messages format](./chat_templating) (`List[Dict[str, str]]`) for its input `messages`, and it returns a `str`.
2. It stops generating outputs *before* the sequences passed in the argument `stop_sequences`

For defining your LLM, you can make a `custom_model` method which accepts a list of [messages](./chat_templating) and returns text. This callable also needs to accept a `stop_sequences` argument that indicates when to stop generating.

```python
from huggingface_hub import login, InferenceClient

login("<YOUR_HUGGINGFACEHUB_API_TOKEN>")

model_id = "meta-llama/Llama-3.3-70B-Instruct"

client = InferenceClient(model=model_id)

def custom_model(messages, stop_sequences=["Task"]) -> str:
    response = client.chat_completion(messages, stop=stop_sequences, max_tokens=1000)
    answer = response.choices[0].message.content
    return answer
```

Additionally, `custom_model` can also take a `grammar` argument. In the case where you specify a `grammar` upon agent initialization, this argument will be passed to the calls to model, with the `grammar` that you defined upon initialization, to allow [constrained generation](https://huggingface.co/docs/text-generation-inference/conceptual/guidance) in order to force properly-formatted agent outputs.

### TransformersModel

For convenience, we have added a `TransformersModel` that implements the points above by building a local `transformers` pipeline for the model_id given at initialization.

```python
from smolagents import TransformersModel

model = TransformersModel(model_id="HuggingFaceTB/SmolLM-135M-Instruct")

print(model([{"role": "user", "content": "Ok!"}], stop_sequences=["great"]))
```
```text
>>> What a
```

[[autodoc]] TransformersModel

### HfApiModel

The `HfApiModel` wraps an [HF Inference API](https://huggingface.co/docs/api-inference/index) client for the execution of the LLM.

```python
from smolagents import HfApiModel

messages = [
  {"role": "user", "content": "Hello, how are you?"},
  {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
  {"role": "user", "content": "No need to help, take it easy."},
]

model = HfApiModel()
print(model(messages))
```
```text
>>> Of course! If you change your mind, feel free to reach out. Take care!
```
[[autodoc]] HfApiModel

### LiteLLMModel

The `LiteLLMModel` leverages [LiteLLM](https://www.litellm.ai/) to support 100+ LLMs from various providers.
You can pass kwargs upon model initialization that will then be used whenever using the model, for instance below we pass `temperature`.

```python
from smolagents import LiteLLMModel

messages = [
  {"role": "user", "content": "Hello, how are you?"},
  {"role": "assistant", "content": "I'm doing great. How can I help you today?"},
  {"role": "user", "content": "No need to help, take it easy."},
]

model = LiteLLMModel("anthropic/claude-3-5-sonnet-latest", temperature=0.2)
print(model(messages, max_tokens=10))
```

[[autodoc]] LiteLLMModel
```

## File: docs/source/zh/conceptual_guides/react.md

<a name='file-docs-source-zh-conceptual_guides-react.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# 多步骤 agent 是如何工作的？

ReAct 框架（[Yao et al., 2022](https://huggingface.co/papers/2210.03629)）是目前构建 agent 的主要方法。

该名称基于两个词的组合："Reason" （推理）和 "Act" （行动）。实际上，遵循此架构的 agent 将根据需要尽可能多的步骤来解决其任务，每个步骤包括一个推理步骤，然后是一个行动步骤，在该步骤中，它制定工具调用，使其更接近解决手头的任务。

ReAct 过程涉及保留过去步骤的记忆。

> [!TIP]
> 阅读 [Open-source LLMs as LangChain Agents](https://huggingface.co/blog/open-source-llms-as-agents) 博客文章以了解更多关于多步 agent 的信息。

以下是其工作原理的视频概述：

<div class="flex justify-center">
    <img
        class="block dark:hidden"
        src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/Agent_ManimCE.gif"
    />
    <img
        class="hidden dark:block"
        src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/Agent_ManimCE.gif"
    />
</div>

![ReAct agent 的框架](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/blog/open-source-llms-as-agents/ReAct.png)

我们实现了两个版本的 ToolCallingAgent：
- [`ToolCallingAgent`] 在其输出中生成 JSON 格式的工具调用。
- [`CodeAgent`] 是一种新型的 ToolCallingAgent，它生成代码块形式的工具调用，这对于具有强大编码性能的 LLM 非常有效。

> [!TIP]
> 我们还提供了一个选项来以单步模式运行 agent：只需在启动 agent 时传递 `single_step=True`，例如 `agent.run(your_task, single_step=True)`
```

## File: docs/source/zh/conceptual_guides/intro_agents.md

<a name='file-docs-source-zh-conceptual_guides-intro_agents.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->

# Agent 简介

> [!TIP]
> 译者注：Agent 的业内术语是“智能体”。本译文将保留 agent，不作翻译，以带来更高效的阅读体验。(在中文为主的文章中，It's easier to 注意到英文。Attention Is All You Need!)

## 🤔 什么是 agent？

任何使用 AI 的高效系统都需要为 LLM 提供某种访问现实世界的方式：例如调用搜索工具获取外部信息，或者操作某些程序以完成任务。换句话说，LLM 应该具有 **_Agent 能力_**。Agent 程序是 LLM 通往外部世界的门户。

> [!TIP]
> AI agent 是 **LLM 输出控制工作流的程序**。

任何利用 LLM 的系统都会将 LLM 输出集成到代码中。LLM 输入对代码工作流的影响程度就是 LLM 在系统中的 agent 能力级别。

请注意，根据这个定义，"Agent" 不是一个离散的、非 0 即 1 的定义：相反，"Agent 能力" 是一个连续谱系，随着你在工作流中给予 LLM 更多或更少的权力而变化。

请参见下表中 agent 能力在不同系统中的变化：

| Agent 能力级别 | 描述                                           | 名称       | 示例模式                                           |
| ------------ | ---------------------------------------------- | ---------- | -------------------------------------------------- |
| ☆☆☆          | LLM 输出对程序流程没有影响                     | 简单处理器 | `process_llm_output(llm_response)`                 |
| ★☆☆          | LLM 输出决定 if/else 分支                      | 路由       | `if llm_decision(): path_a() else: path_b()`       |
| ★★☆          | LLM 输出决定函数执行                           | 工具调用者 | `run_function(llm_chosen_tool, llm_chosen_args)`   |
| ★★★          | LLM 输出控制迭代和程序继续                     | 多步 Agent | `while llm_should_continue(): execute_next_step()` |
| ★★★          | 一个 agent 工作流可以启动另一个 agent 工作流 | 多 Agent   | `if llm_trigger(): execute_agent()`                |

多步 agent 具有以下代码结构：

```python
memory = [user_defined_task]
while llm_should_continue(memory): # 这个循环是多步部分
    action = llm_get_next_action(memory) # 这是工具调用部分
    observations = execute_action(action)
    memory += [action, observations]
```

这个 agent 系统在一个循环中运行，每一步执行一个新动作（该动作可能涉及调用一些预定义的 *工具*，这些工具只是函数），直到其观察结果表明已达到解决给定任务的满意状态。以下是一个多步 agent 如何解决简单数学问题的示例：

<div class="flex justify-center">
    <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/Agent_ManimCE.gif"/>
</div>

## ✅ 何时使用 agent / ⛔ 何时避免使用

当你需要 LLM 确定应用程序的工作流时，agent 很有用。但它们通常有些过度。问题是：我真的需要工作流的灵活性来有效解决手头的任务吗？
如果预定义的工作流经常不足，这意味着你需要更多的灵活性。
让我们举个例子：假设你正在开发一个处理冲浪旅行网站客户请求的应用程序。

你可以提前知道请求将属于 2 个类别之一（基于用户选择），并且你为这 2 种情况都有预定义的工作流。

1. 想要了解旅行信息？⇒ 给他们访问搜索栏以搜索你的知识库
2. 想与销售交谈？⇒ 让他们填写联系表单。

如果这个确定性工作流适合所有查询，那就直接编码吧！这将为你提供一个 100% 可靠的系统，没有让不可预测的 LLM 干扰你的工作流而引入错误的风险。为了简单和稳健起见，建议规范化不使用任何 agent 行为。

但如果工作流不能提前确定得那么好呢？

例如，用户想问：`"I can come on Monday, but I forgot my passport so risk being delayed to Wednesday, is it possible to take me and my stuff to surf on Tuesday morning, with a cancellation insurance?"` 这个问题涉及许多因素，可能上述预定的标准都不足以满足这个请求。

如果预定义的工作流经常不足，这意味着你需要更多的灵活性。

这就是 agent 设置发挥作用的地方。

在上面的例子中，你可以创建一个多步 agent，它可以访问天气 API 获取天气预报，Google Maps API 计算旅行距离，员工在线仪表板和你的知识库上的 RAG 系统。

直到最近，计算机程序还局限于预定义的工作流，试图通过堆积 if/else 分支来处理复杂性。它们专注于极其狭窄的任务，如"计算这些数字的总和"或"找到这个图中的最短路径"。但实际上，大多数现实生活中的任务，如我们上面的旅行示例，都不适合预定义的工作流。agent 系统为程序打开了现实世界任务的大门！

## 为什么选择 `smolagents`？

对于一些低级的 agent 用例，如链或路由器，你可以自己编写所有代码。这样会更好，因为它可以让你更好地控制和理解你的系统。

但一旦你开始追求更复杂的行为，比如让 LLM 调用函数（即"工具调用"）或让 LLM 运行 while 循环（"多步 agent"），一些抽象就变得必要：

- 对于工具调用，你需要解析 agent 的输出，因此这个输出需要一个预定义的格式，如"Thought: I should call tool 'get_weather'. Action: get_weather(Paris)."，你用预定义的函数解析它，并且给 LLM 的系统提示应该通知它这个格式。
- 对于 LLM 输出决定循环的多步 agent，你需要根据上次循环迭代中发生的情况给 LLM 不同的提示：所以你需要某种记忆能力。

看到了吗？通过这两个例子，我们已经发现需要一些项目来帮助我们：

- 当然，一个作为系统引擎的 LLM
- agent 可以访问的工具列表
- 从 LLM 输出中提取工具调用的解析器
- 与解析器同步的系统提示
- 记忆能力

但是等等，既然我们给 LLM 在决策中留出了空间，它们肯定会犯错误：所以我们需要错误日志记录和重试机制。

所有这些元素都需要紧密耦合才能形成一个功能良好的系统。这就是为什么我们决定需要制作基本构建块来让所有这些东西协同工作。

## 代码 agent

在多步 agent 中，每一步 LLM 都可以编写一个动作，形式为调用外部工具。编写这些动作的常见格式（由 Anthropic、OpenAI 等使用）通常是"将动作编写为工具名称和要使用的参数的 JSON，然后解析以知道要执行哪个工具以及使用哪些参数"的不同变体。

[多项](https://huggingface.co/papers/2402.01030) [研究](https://huggingface.co/papers/2411.01747) [论文](https://huggingface.co/papers/2401.00812) 表明，在代码中进行工具调用的 LLM 要好得多。

原因很简单，_我们专门设计了我们的代码语言，使其成为表达计算机执行动作的最佳方式_。如果 JSON 片段是更好的表达方式，JSON 将成为顶级编程语言，编程将变得非常困难。

下图取自 [Executable Code Actions Elicit Better LLM Agents](https://huggingface.co/papers/2402.01030)，说明了用代码编写动作的一些优势：

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/code_vs_json_actions.png">

与 JSON 片段相比，用代码编写动作提供了更好的：

- **可组合性：** 你能像定义 python 函数一样，将 JSON 动作嵌套在一起，或定义一组 JSON 动作以供重用吗？
- **对象管理：** 你如何在 JSON 中存储像 `generate_image` 这样的动作的输出？
- **通用性：** 代码被构建为简单地表达任何你可以让计算机做的事情。
- **LLM 训练数据中的表示：** 大量高质量的代码动作已经包含在 LLM 的训练数据中，这意味着它们已经为此进行了训练！

```

## File: docs/source/zh/examples/text_to_sql.md

<a name='file-docs-source-zh-examples-text_to_sql.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Text-to-SQL

[[open-in-colab]]

In this tutorial, we’ll see how to implement an agent that leverages SQL using `smolagents`.

> Let's start with the golden question: why not keep it simple and use a standard text-to-SQL pipeline?

A standard text-to-sql pipeline is brittle, since the generated SQL query can be incorrect. Even worse, the query could be incorrect, but not raise an error, instead giving some incorrect/useless outputs without raising an alarm.

👉 Instead, an agent system is able to critically inspect outputs and decide if the query needs to be changed or not, thus giving it a huge performance boost.

Let’s build this agent! 💪

First, we setup the SQL environment:
```py
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    Float,
    insert,
    inspect,
    text,
)

engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# create city SQL table
table_name = "receipts"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("customer_name", String(16), primary_key=True),
    Column("price", Float),
    Column("tip", Float),
)
metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "customer_name": "Alan Payne", "price": 12.06, "tip": 1.20},
    {"receipt_id": 2, "customer_name": "Alex Mason", "price": 23.86, "tip": 0.24},
    {"receipt_id": 3, "customer_name": "Woodrow Wilson", "price": 53.43, "tip": 5.43},
    {"receipt_id": 4, "customer_name": "Margaret James", "price": 21.11, "tip": 1.00},
]
for row in rows:
    stmt = insert(receipts).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)
```

### Build our agent

Now let’s make our SQL table retrievable by a tool.

The tool’s description attribute will be embedded in the LLM’s prompt by the agent system: it gives the LLM information about how to use the tool. This is where we want to describe the SQL table.

```py
inspector = inspect(engine)
columns_info = [(col["name"], col["type"]) for col in inspector.get_columns("receipts")]

table_description = "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
print(table_description)
```

```text
Columns:
  - receipt_id: INTEGER
  - customer_name: VARCHAR(16)
  - price: FLOAT
  - tip: FLOAT
```

Now let’s build our tool. It needs the following: (read [the tool doc](../tutorials/tools) for more detail)
- A docstring with an `Args:` part listing arguments.
- Type hints on both inputs and output.

```py
from smolagents import tool

@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'receipts'. Its description is as follows:
        Columns:
        - receipt_id: INTEGER
        - customer_name: VARCHAR(16)
        - price: FLOAT
        - tip: FLOAT

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output
```

Now let us create an agent that leverages this tool.

We use the `CodeAgent`, which is smolagents’ main agent class: an agent that writes actions in code and can iterate on previous output according to the ReAct framework.

The model is the LLM that powers the agent system. HfApiModel allows you to call LLMs using HF’s Inference API, either via Serverless or Dedicated endpoint, but you could also use any proprietary API.

```py
from smolagents import CodeAgent, HfApiModel

agent = CodeAgent(
    tools=[sql_engine],
    model=HfApiModel("meta-llama/Meta-Llama-3.1-8B-Instruct"),
)
agent.run("Can you give me the name of the client who got the most expensive receipt?")
```

### Level 2: Table joins

Now let’s make it more challenging! We want our agent to handle joins across multiple tables.

So let’s make a second table recording the names of waiters for each receipt_id!

```py
table_name = "waiters"
receipts = Table(
    table_name,
    metadata_obj,
    Column("receipt_id", Integer, primary_key=True),
    Column("waiter_name", String(16), primary_key=True),
)
metadata_obj.create_all(engine)

rows = [
    {"receipt_id": 1, "waiter_name": "Corey Johnson"},
    {"receipt_id": 2, "waiter_name": "Michael Watts"},
    {"receipt_id": 3, "waiter_name": "Michael Watts"},
    {"receipt_id": 4, "waiter_name": "Margaret James"},
]
for row in rows:
    stmt = insert(receipts).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)
```
Since we changed the table, we update the `SQLExecutorTool` with this table’s description to let the LLM properly leverage information from this table.

```py
updated_description = """Allows you to perform SQL queries on the table. Beware that this tool's output is a string representation of the execution output.
It can use the following tables:"""

inspector = inspect(engine)
for table in ["receipts", "waiters"]:
    columns_info = [(col["name"], col["type"]) for col in inspector.get_columns(table)]

    table_description = f"Table '{table}':\n"

    table_description += "Columns:\n" + "\n".join([f"  - {name}: {col_type}" for name, col_type in columns_info])
    updated_description += "\n\n" + table_description

print(updated_description)
```
Since this request is a bit harder than the previous one, we’ll switch the LLM engine to use the more powerful [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)!

```py
sql_engine.description = updated_description

agent = CodeAgent(
    tools=[sql_engine],
    model=HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct"),
)

agent.run("Which waiter got more total money from tips?")
```
It directly works! The setup was surprisingly simple, wasn’t it?

This example is done! We've touched upon these concepts:
- Building new tools.
- Updating a tool's description.
- Switching to a stronger LLM helps agent reasoning.

✅ Now you can go build this text-to-SQL system you’ve always dreamt of! ✨
```

## File: docs/source/zh/examples/multiagents.md

<a name='file-docs-source-zh-examples-multiagents.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Orchestrate a multi-agent system 🤖🤝🤖

[[open-in-colab]]

In this notebook we will make a **multi-agent web browser: an agentic system with several agents collaborating to solve problems using the web!**

It will be a simple hierarchy, using a `ManagedAgent` object to wrap the managed web search agent:

```
              +----------------+
              | Manager agent  |
              +----------------+
                       |
        _______________|______________
       |                              |
  Code interpreter   +--------------------------------+
       tool          |         Managed agent          |
                     |      +------------------+      |
                     |      | Web Search agent |      |
                     |      +------------------+      |
                     |         |            |         |
                     |  Web Search tool     |         |
                     |             Visit webpage tool |
                     +--------------------------------+
```
Let's set up this system. 

Run the line below to install the required dependencies:

```
!pip install markdownify duckduckgo-search smolagents --upgrade -q
```

Let's login in order to call the HF Inference API:

```py
from huggingface_hub import notebook_login

notebook_login()
```

⚡️ Our agent will be powered by [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) using `HfApiModel` class that uses HF's Inference API: the Inference API allows to quickly and easily run any OS model.

_Note:_ The Inference API hosts models based on various criteria, and deployed models may be updated or replaced without prior notice. Learn more about it [here](https://huggingface.co/docs/api-inference/supported-models).

```py
model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"
```

## 🔍 Create a web search tool

For web browsing, we can already use our pre-existing [`DuckDuckGoSearchTool`](https://github.com/huggingface/smolagents/blob/main/src/smolagents/default_tools/search.py) tool to provide a Google search equivalent.

But then we will also need to be able to peak into the page found by the `DuckDuckGoSearchTool`.
To do so, we could import the library's built-in `VisitWebpageTool`, but we will build it again to see how it's done.

So let's create our `VisitWebpageTool` tool from scratch using `markdownify`.

```py
import re
import requests
from markdownify import markdownify
from requests.exceptions import RequestException
from smolagents import tool


@tool
def visit_webpage(url: str) -> str:
    """Visits a webpage at the given URL and returns its content as a markdown string.

    Args:
        url: The URL of the webpage to visit.

    Returns:
        The content of the webpage converted to Markdown, or an error message if the request fails.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Convert the HTML content to Markdown
        markdown_content = markdownify(response.text).strip()

        # Remove multiple line breaks
        markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

        return markdown_content

    except RequestException as e:
        return f"Error fetching the webpage: {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
```

Ok, now let's initialize and test our tool!

```py
print(visit_webpage("https://en.wikipedia.org/wiki/Hugging_Face")[:500])
```

## Build our multi-agent system 🤖🤝🤖

Now that we have all the tools `search` and `visit_webpage`, we can use them to create the web agent.

Which configuration to choose for this agent?
- Web browsing is a single-timeline task that does not require parallel tool calls, so JSON tool calling works well for that. We thus choose a `JsonAgent`.
- Also, since sometimes web search requires exploring many pages before finding the correct answer, we prefer to increase the number of `max_steps` to 10.

```py
from smolagents import (
    CodeAgent,
    ToolCallingAgent,
    HfApiModel,
    ManagedAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel,
)

model = HfApiModel(model_id)

web_agent = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool(), visit_webpage],
    model=model,
    max_steps=10,
)
```

We then wrap this agent into a `ManagedAgent` that will make it callable by its manager agent.

```py
managed_web_agent = ManagedAgent(
    agent=web_agent,
    name="search",
    description="Runs web searches for you. Give it your query as an argument.",
)
```

Finally we create a manager agent, and upon initialization we pass our managed agent to it in its `managed_agents` argument.

Since this agent is the one tasked with the planning and thinking, advanced reasoning will be beneficial, so a `CodeAgent` will be the best choice.

Also, we want to ask a question that involves the current year and does additional data calculations: so let us add `additional_authorized_imports=["time", "numpy", "pandas"]`, just in case the agent needs these packages.

```py
manager_agent = CodeAgent(
    tools=[],
    model=model,
    managed_agents=[managed_web_agent],
    additional_authorized_imports=["time", "numpy", "pandas"],
)
```

That's all! Now let's run our system! We select a question that requires both some calculation and research:

```py
answer = manager_agent.run("If LLM training continues to scale up at the current rhythm until 2030, what would be the electric power in GW required to power the biggest training runs by 2030? What would that correspond to, compared to some countries? Please provide a source for any numbers used.")
```

We get this report as the answer:
```
Based on current growth projections and energy consumption estimates, if LLM trainings continue to scale up at the 
current rhythm until 2030:

1. The electric power required to power the biggest training runs by 2030 would be approximately 303.74 GW, which 
translates to about 2,660,762 GWh/year.

2. Comparing this to countries' electricity consumption:
   - It would be equivalent to about 34% of China's total electricity consumption.
   - It would exceed the total electricity consumption of India (184%), Russia (267%), and Japan (291%).
   - It would be nearly 9 times the electricity consumption of countries like Italy or Mexico.

3. Source of numbers:
   - The initial estimate of 5 GW for future LLM training comes from AWS CEO Matt Garman.
   - The growth projection used a CAGR of 79.80% from market research by Springs.
   - Country electricity consumption data is from the U.S. Energy Information Administration, primarily for the year 
2021.
```

Seems like we'll need some sizeable powerplants if the [scaling hypothesis](https://gwern.net/scaling-hypothesis) continues to hold true.

Our agents managed to efficiently collaborate towards solving the task! ✅

💡 You can easily extend this orchestration to more agents: one does the code execution, one the web search, one handles file loadings...
```

## File: docs/source/zh/examples/rag.md

<a name='file-docs-source-zh-examples-rag.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# Agentic RAG

[[open-in-colab]]

Retrieval-Augmented-Generation (RAG) is “using an LLM to answer a user query, but basing the answer on information retrieved from a knowledge base”. It has many advantages over using a vanilla or fine-tuned LLM: to name a few, it allows to ground the answer on true facts and reduce confabulations, it allows to provide the LLM with domain-specific knowledge, and it allows fine-grained control of access to information from the knowledge base.

But vanilla RAG has limitations, most importantly these two:
- It performs only one retrieval step: if the results are bad, the generation in turn will be bad.
- Semantic similarity is computed with the user query as a reference, which might be suboptimal: for instance, the user query will often be a question and the document containing the true answer will be in affirmative voice, so its similarity score will be downgraded compared to other source documents in the interrogative form, leading to a risk of missing the relevant information.

We can alleviate these problems by making a RAG agent: very simply, an agent armed with a retriever tool!

This agent will: ✅ Formulate the query itself and ✅ Critique to re-retrieve if needed.

So it should naively recover some advanced RAG techniques!
- Instead of directly using the user query as the reference in semantic search, the agent formulates itself a reference sentence that can be closer to the targeted documents, as in [HyDE](https://huggingface.co/papers/2212.10496).
The agent can use the generated snippets and re-retrieve if needed, as in [Self-Query](https://docs.llamaindex.ai/en/stable/examples/evaluation/RetryQuery/).

Let's build this system. 🛠️

Run the line below to install required dependencies:
```bash
!pip install smolagents pandas langchain langchain-community sentence-transformers rank_bm25 --upgrade -q
```
To call the HF Inference API, you will need a valid token as your environment variable `HF_TOKEN`.
We use python-dotenv to load it.
```py
from dotenv import load_dotenv
load_dotenv()
```

We first load a knowledge base on which we want to perform RAG: this dataset is a compilation of the documentation pages for many Hugging Face libraries, stored as markdown. We will keep only the documentation for the `transformers` library.

Then prepare the knowledge base by processing the dataset and storing it into a vector database to be used by the retriever.

We use [LangChain](https://python.langchain.com/docs/introduction/) for its excellent vector database utilities.

```py
import datasets
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever

knowledge_base = datasets.load_dataset("m-ric/huggingface_doc", split="train")
knowledge_base = knowledge_base.filter(lambda row: row["source"].startswith("huggingface/transformers"))

source_docs = [
    Document(page_content=doc["text"], metadata={"source": doc["source"].split("/")[1]})
    for doc in knowledge_base
]

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    add_start_index=True,
    strip_whitespace=True,
    separators=["\n\n", "\n", ".", " ", ""],
)
docs_processed = text_splitter.split_documents(source_docs)
```

Now the documents are ready.

So let’s build our agentic RAG system!

👉 We only need a RetrieverTool that our agent can leverage to retrieve information from the knowledge base.

Since we need to add a vectordb as an attribute of the tool, we cannot simply use the simple tool constructor with a `@tool` decorator: so we will follow the advanced setup highlighted in the [tools tutorial](../tutorials/tools).

```py
from smolagents import Tool

class RetrieverTool(Tool):
    name = "retriever"
    description = "Uses semantic search to retrieve the parts of transformers documentation that could be most relevant to answer your query."
    inputs = {
        "query": {
            "type": "string",
            "description": "The query to perform. This should be semantically close to your target documents. Use the affirmative form rather than a question.",
        }
    }
    output_type = "string"

    def __init__(self, docs, **kwargs):
        super().__init__(**kwargs)
        self.retriever = BM25Retriever.from_documents(
            docs, k=10
        )

    def forward(self, query: str) -> str:
        assert isinstance(query, str), "Your search query must be a string"

        docs = self.retriever.invoke(
            query,
        )
        return "\nRetrieved documents:\n" + "".join(
            [
                f"\n\n===== Document {str(i)} =====\n" + doc.page_content
                for i, doc in enumerate(docs)
            ]
        )

retriever_tool = RetrieverTool(docs_processed)
```
We have used BM25, a classic retrieval method, because it's lightning fast to setup.
To improve retrieval accuracy, you could use replace BM25 with semantic search using vector representations for documents: thus you can head to the [MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) to select a good embedding model.

Now it’s straightforward to create an agent that leverages this `retriever_tool`!

The agent will need these arguments upon initialization:
- `tools`: a list of tools that the agent will be able to call.
- `model`: the LLM that powers the agent.
Our `model` must be a callable that takes as input a list of messages and returns text. It also needs to accept a stop_sequences argument that indicates when to stop its generation. For convenience, we directly use the HfEngine class provided in the package to get a LLM engine that calls Hugging Face's Inference API.

And we use [meta-llama/Llama-3.3-70B-Instruct](meta-llama/Llama-3.3-70B-Instruct) as the llm engine because:
- It has a long 128k context, which is helpful for processing long source documents
- It is served for free at all times on HF's Inference API!

_Note:_ The Inference API hosts models based on various criteria, and deployed models may be updated or replaced without prior notice. Learn more about it [here](https://huggingface.co/docs/api-inference/supported-models).

```py
from smolagents import HfApiModel, CodeAgent

agent = CodeAgent(
    tools=[retriever_tool], model=HfApiModel("meta-llama/Llama-3.3-70B-Instruct"), max_steps=4, verbose=True
)
```

Upon initializing the CodeAgent, it has been automatically given a default system prompt that tells the LLM engine to process step-by-step and generate tool calls as code snippets, but you could replace this prompt template with your own as needed.

Then when its `.run()` method is launched, the agent takes care of calling the LLM engine, and executing the tool calls, all in a loop that ends only when tool `final_answer` is called with the final answer as its argument.

```py
agent_output = agent.run("For a transformers model training, which is slower, the forward or the backward pass?")

print("Final output:")
print(agent_output)
```




```

## File: docs/source/zh/tutorials/secure_code_execution.md

<a name='file-docs-source-zh-tutorials-secure_code_execution.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# 安全代码执行

[[open-in-colab]]

> [!TIP]
> 如果你是第一次构建 agent，请先阅读 [agent 介绍](../conceptual_guides/intro_agents) 和 [smolagents 导览](../guided_tour)。

### 代码智能体

[多项](https://huggingface.co/papers/2402.01030) [研究](https://huggingface.co/papers/2411.01747) [表明](https://huggingface.co/papers/2401.00812)，让大语言模型用代码编写其动作（工具调用）比当前标准的工具调用格式要好得多，目前行业标准是 "将动作写成包含工具名称和参数的 JSON" 的各种变体。

为什么代码更好？因为我们专门为计算机执行的动作而设计编程语言。如果 JSON 片段是更好的方式，那么这个工具包就应该是用 JSON 片段编写的，魔鬼就会嘲笑我们。

代码就是表达计算机动作的更好方式。它具有更好的：
- **组合性**：你能像定义 Python 函数那样，在 JSON 动作中嵌套其他 JSON 动作，或者定义一组 JSON 动作以便以后重用吗？
- **对象管理**：你如何在 JSON 中存储像 `generate_image` 这样的动作的输出？
- **通用性**：代码是为了简单地表达任何可以让计算机做的事情而构建的。
- **在 LLM 训练语料库中的表示**：天赐良机，为什么不利用已经包含在 LLM 训练语料库中的大量高质量动作呢？

下图展示了这一点，取自 [可执行代码动作引出更好的 LLM 智能体](https://huggingface.co/papers/2402.01030)。

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/code_vs_json_actions.png">

这就是为什么我们强调提出代码智能体，在本例中是 Python 智能体，这意味着我们要在构建安全的 Python 解释器上投入更多精力。

### 本地 Python 解释器

默认情况下，`CodeAgent` 会在你的环境中运行 LLM 生成的代码。
这个执行不是由普通的 Python 解释器完成的：我们从零开始重新构建了一个更安全的 `LocalPythonInterpreter`。
这个解释器通过以下方式设计以确保安全：
  - 将导入限制为用户显式传递的列表
  - 限制操作次数以防止无限循环和资源膨胀
  - 不会执行任何未预定义的操作

我们已经在许多用例中使用了这个解释器，从未观察到对环境造成任何损害。

然而，这个解决方案并不是万无一失的：可以想象，如果 LLM 被微调用于恶意操作，仍然可能损害你的环境。例如，如果你允许像 `Pillow` 这样无害的包处理图像，LLM 可能会生成数千张图像保存以膨胀你的硬盘。
如果你自己选择了 LLM 引擎，这当然不太可能，但它可能会发生。

所以如果你想格外谨慎，可以使用下面描述的远程代码执行选项。

### E2B 代码执行器

为了最大程度的安全性，你可以使用我们与 E2B 的集成在沙盒环境中运行代码。这是一个远程执行服务，可以在隔离的容器中运行你的代码，使代码无法影响你的本地环境。

为此，你需要设置你的 E2B 账户并在环境变量中设置 `E2B_API_KEY`。请前往 [E2B 快速入门文档](https://e2b.dev/docs/quickstart) 了解更多信息。

然后你可以通过 `pip install e2b-code-interpreter python-dotenv` 安装它。

现在你已经准备好了！

要将代码执行器设置为 E2B，只需在初始化 `CodeAgent` 时传递标志 `use_e2b_executor=True`。
请注意，你应该将所有工具的依赖项添加到 `additional_authorized_imports` 中，以便执行器安装它们。

```py
from smolagents import CodeAgent, VisitWebpageTool, HfApiModel
agent = CodeAgent(
    tools = [VisitWebpageTool()],
    model=HfApiModel(),
    additional_authorized_imports=["requests", "markdownify"],
    use_e2b_executor=True
)

agent.run("What was Abraham Lincoln's preferred pet?")
```

目前 E2B 代码执行暂不兼容多 agent——因为把 agent 调用放在应该在远程执行的代码块里，是非常混乱的。但我们正在努力做到这件事！

```

## File: docs/source/zh/tutorials/tools.md

<a name='file-docs-source-zh-tutorials-tools.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# 工具

[[open-in-colab]]

在这里，我们将学习高级工具的使用。

> [!TIP]
> 如果你是构建 agent 的新手，请确保先阅读 [agent 介绍](../conceptual_guides/intro_agents) 和 [smolagents 导览](../guided_tour)。

- [工具](#工具)
    - [什么是工具，如何构建一个工具？](#什么是工具如何构建一个工具)
    - [将你的工具分享到 Hub](#将你的工具分享到-hub)
    - [将 Space 导入为工具](#将-space-导入为工具)
    - [使用 LangChain 工具](#使用-langchain-工具)
    - [管理你的 agent 工具箱](#管理你的-agent-工具箱)
    - [使用工具集合](#使用工具集合)

### 什么是工具，如何构建一个工具？

工具主要是 LLM 可以在 agent 系统中使用的函数。

但要使用它，LLM 需要被提供一个 API：名称、工具描述、输入类型和描述、输出类型。

所以它不能仅仅是一个函数。它应该是一个类。

因此，核心上，工具是一个类，它包装了一个函数，并带有帮助 LLM 理解如何使用它的元数据。

以下是它的结构：

```python
from smolagents import Tool

class HFModelDownloadsTool(Tool):
    name = "model_download_counter"
    description = """
    This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
    It returns the name of the checkpoint."""
    inputs = {
        "task": {
            "type": "string",
            "description": "the task category (such as text-classification, depth-estimation, etc)",
        }
    }
    output_type = "string"

    def forward(self, task: str):
        from huggingface_hub import list_models

        model = next(iter(list_models(filter=task, sort="downloads", direction=-1)))
        return model.id

model_downloads_tool = HFModelDownloadsTool()
```

自定义工具继承 [`Tool`] 以继承有用的方法。子类还定义了：
- 一个属性 `name`，对应于工具本身的名称。名称通常描述工具的功能。由于代码返回任务中下载量最多的模型，我们将其命名为 `model_download_counter`。
- 一个属性 `description`，用于填充 agent 的系统提示。
- 一个 `inputs` 属性，它是一个带有键 `"type"` 和 `"description"` 的字典。它包含帮助 Python 解释器对输入做出明智选择的信息。
- 一个 `output_type` 属性，指定输出类型。`inputs` 和 `output_type` 的类型应为 [Pydantic 格式](https://docs.pydantic.dev/latest/concepts/json_schema/#generating-json-schema)，它们可以是以下之一：[`~AUTHORIZED_TYPES`]。
- 一个 `forward` 方法，包含要执行的推理代码。

这就是它在 agent 中使用所需的全部内容！

还有另一种构建工具的方法。在 [guided_tour](../guided_tour) 中，我们使用 `@tool` 装饰器实现了一个工具。[`tool`] 装饰器是定义简单工具的推荐方式，但有时你需要更多：在类中使用多个方法以获得更清晰的代码，或使用额外的类属性。

在这种情况下，你可以通过如上所述继承 [`Tool`] 来构建你的工具。

### 将你的工具分享到 Hub

你可以通过调用 [`~Tool.push_to_hub`] 将你的自定义工具分享到 Hub。确保你已经在 Hub 上为其创建了一个仓库，并且使用的是具有读取权限的 token。

```python
model_downloads_tool.push_to_hub("{your_username}/hf-model-downloads", token="<YOUR_HUGGINGFACEHUB_API_TOKEN>")
```

为了使推送到 Hub 正常工作，你的工具需要遵守一些规则：
- 所有方法都是自包含的，例如使用来自其参数中的变量。
- 根据上述要点，**所有导入应直接在工具的函数中定义**，否则在尝试使用 [`~Tool.save`] 或 [`~Tool.push_to_hub`] 调用你的自定义工具时会出现错误。
- 如果你继承了 `__init__` 方法，除了 `self` 之外，你不能给它任何其他参数。这是因为在特定工具实例初始化期间设置的参数很难跟踪，这阻碍了将它们正确分享到 Hub。无论如何，创建特定类的想法是你已经可以为任何需要硬编码的内容设置类属性（只需在 `class YourTool(Tool):` 行下直接设置 `your_variable=(...)`）。当然，你仍然可以通过将内容分配给 `self.your_variable` 在代码中的任何地方创建类属性。

一旦你的工具被推送到 Hub，你就可以查看它。[这里](https://huggingface.co/spaces/m-ric/hf-model-downloads) 是我推送的 `model_downloads_tool`。它有一个漂亮的 gradio 界面。

在深入工具文件时，你可以发现所有工具的逻辑都在 [tool.py](https://huggingface.co/spaces/m-ric/hf-model-downloads/blob/main/tool.py) 下。这是你可以检查其他人分享的工具的地方。

然后你可以使用 [`load_tool`] 加载工具或使用 [`~Tool.from_hub`] 创建它，并将其传递给 agent 中的 `tools` 参数。
由于运行工具意味着运行自定义代码，你需要确保你信任该仓库，因此我们需要传递 `trust_remote_code=True` 来从 Hub 加载工具。

```python
from smolagents import load_tool, CodeAgent

model_download_tool = load_tool(
    "{your_username}/hf-model-downloads",
    trust_remote_code=True
)
```

### 将 Space 导入为工具

你可以使用 [`Tool.from_space`] 方法直接从 Hub 导入一个 Space 作为工具！

你只需要提供 Hub 上 Space 的 id、它的名称和一个帮助你的 agent 理解工具功能的描述。在底层，这将使用 [`gradio-client`](https://pypi.org/project/gradio-client/) 库来调用 Space。

例如，让我们从 Hub 导入 [FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) Space 并使用它生成一张图片。

```python
image_generation_tool = Tool.from_space(
    "black-forest-labs/FLUX.1-schnell",
    name="image_generator",
    description="Generate an image from a prompt"
)

image_generation_tool("A sunny beach")
```
瞧，这是你的图片！🏖️

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/sunny_beach.webp">

然后你可以像使用任何其他工具一样使用这个工具。例如，让我们改进提示 `A rabbit wearing a space suit` 并生成它的图片。

```python
from smolagents import CodeAgent, HfApiModel

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")
agent = CodeAgent(tools=[image_generation_tool], model=model)

agent.run(
    "Improve this prompt, then generate an image of it.", prompt='A rabbit wearing a space suit'
)
```

```text
=== Agent thoughts:
improved_prompt could be "A bright blue space suit wearing rabbit, on the surface of the moon, under a bright orange sunset, with the Earth visible in the background"

Now that I have improved the prompt, I can use the image generator tool to generate an image based on this prompt.
>>> Agent is executing the code below:
image = image_generator(prompt="A bright blue space suit wearing rabbit, on the surface of the moon, under a bright orange sunset, with the Earth visible in the background")
final_answer(image)
```

<img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/rabbit_spacesuit_flux.webp">

这得有多酷？🤩

### 使用 LangChain 工具

我们喜欢 Langchain，并认为它有一套非常吸引人的工具。
要从 LangChain 导入工具，请使用 `from_langchain()` 方法。

以下是如何使用它来重现介绍中的搜索结果，使用 LangChain 的 web 搜索工具。
这个工具需要 `pip install langchain google-search-results -q` 才能正常工作。
```python
from langchain.agents import load_tools

search_tool = Tool.from_langchain(load_tools(["serpapi"])[0])

agent = CodeAgent(tools=[search_tool], model=model)

agent.run("How many more blocks (also denoted as layers) are in BERT base encoder compared to the encoder from the architecture proposed in Attention is All You Need?")
```

### 管理你的 agent 工具箱

你可以通过添加或替换工具来管理 agent 的工具箱。

让我们将 `model_download_tool` 添加到一个仅使用默认工具箱初始化的现有 agent 中。

```python
from smolagents import HfApiModel

model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")

agent = CodeAgent(tools=[], model=model, add_base_tools=True)
agent.tools.append(model_download_tool)
```
现在我们可以利用新工具：

```python
agent.run(
    "Can you give me the name of the model that has the most downloads in the 'text-to-video' task on the Hugging Face Hub but reverse the letters?"
)
```


> [!TIP]
> 注意不要向 agent 添加太多工具：这可能会让较弱的 LLM 引擎不堪重负。


### 使用工具集合

你可以通过使用 ToolCollection 对象来利用工具集合，使用你想要使用的集合的 slug。
然后将它们作为列表传递给 agent 初始化，并开始使用它们！

```py
from smolagents import ToolCollection, CodeAgent

image_tool_collection = ToolCollection(
    collection_slug="huggingface-tools/diffusion-tools-6630bb19a942c2306a2cdb6f",
    token="<YOUR_HUGGINGFACEHUB_API_TOKEN>"
)
agent = CodeAgent(tools=[*image_tool_collection.tools], model=model, add_base_tools=True)

agent.run("Please draw me a picture of rivers and lakes.")
```

为了加快启动速度，工具仅在 agent 调用时加载。

```

## File: docs/source/zh/tutorials/building_good_agents.md

<a name='file-docs-source-zh-tutorials-building_good_agents.md'></a>
*Description*: No specific description available.

```plaintext
<!--Copyright 2024 The HuggingFace Team. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

⚠️ Note that this file is in Markdown but contain specific syntax for our doc-builder (similar to MDX) that may not be
rendered properly in your Markdown viewer.

-->
# 构建好用的 agent

[[open-in-colab]]

能良好工作的 agent 和不能工作的 agent 之间，有天壤之别。
我们怎么样才能构建出属于前者的 agent 呢？
在本指南中，我们将看到构建 agent 的最佳实践。

> [!TIP]
> 如果你是 agent 构建的新手，请确保首先阅读 [agent 介绍](../conceptual_guides/intro_agents) 和 [smolagents 导览](../guided_tour)。

### 最好的 agent 系统是最简单的：尽可能简化工作流

在你的工作流中赋予 LLM 一些自主权，会引入一些错误风险。

经过良好编程的 agent 系统，通常具有良好的错误日志记录和重试机制，因此 LLM 引擎有机会自我纠错。但为了最大限度地降低 LLM 错误的风险，你应该简化你的工作流！

让我们回顾一下 [agent 介绍](../conceptual_guides/intro_agents) 中的例子：一个为冲浪旅行公司回答用户咨询的机器人。
与其让 agent 每次被问及新的冲浪地点时，都分别调用 "旅行距离 API" 和 "天气 API"，你可以只创建一个统一的工具 "return_spot_information"，一个同时调用这两个 API，并返回它们连接输出的函数。

这可以降低成本、延迟和错误风险！

主要的指导原则是：尽可能减少 LLM 调用的次数。

这可以带来一些启发：
- 尽可能把两个工具合并为一个，就像我们两个 API 的例子。
- 尽可能基于确定性函数，而不是 agent 决策，来实现逻辑。

### 改善流向 LLM 引擎的信息流

记住，你的 LLM 引擎就像一个 ~智能~ 机器人，被关在一个房间里，与外界唯一的交流方式是通过门缝传递的纸条。

如果你没有明确地将信息放入其提示中，它将不知道发生的任何事情。

所以首先要让你的任务非常清晰！
由于 agent 由 LLM 驱动，任务表述的微小变化可能会产生完全不同的结果。

然后，改善工具使用中流向 agent 的信息流。

需要遵循的具体指南：
- 每个工具都应该记录（只需在工具的 `forward` 方法中使用 `print` 语句）对 LLM 引擎可能有用的所有信息。
  - 特别是，记录工具执行错误的详细信息会很有帮助！

例如，这里有一个根据位置和日期时间检索天气数据的工具：

首先，这是一个糟糕的版本：
```python
import datetime
from smolagents import tool

def get_weather_report_at_coordinates(coordinates, date_time):
    # 虚拟函数，返回 [温度（°C），降雨风险（0-1），浪高（m）]
    return [28.0, 0.35, 0.85]

def get_coordinates_from_location(location):
    # 返回虚拟坐标
    return [3.3, -42.0]

@tool
def get_weather_api(location: str, date_time: str) -> str:
    """
    Returns the weather report.

    Args:
        location: the name of the place that you want the weather for.
        date_time: the date and time for which you want the report.
    """
    lon, lat = convert_location_to_coordinates(location)
    date_time = datetime.strptime(date_time)
    return str(get_weather_report_at_coordinates((lon, lat), date_time))
```

为什么它不好？
- 没有说明 `date_time` 应该使用的格式
- 没有说明位置应该如何指定
- 没有记录机制来处理明确的报错情况，如位置格式不正确或 date_time 格式不正确
- 输出格式难以理解

如果工具调用失败，内存中记录的错误跟踪，可以帮助 LLM 逆向工程工具来修复错误。但为什么要让它做这么多繁重的工作呢？

构建这个工具的更好方式如下：
```python
@tool
def get_weather_api(location: str, date_time: str) -> str:
    """
    Returns the weather report.

    Args:
        location: the name of the place that you want the weather for. Should be a place name, followed by possibly a city name, then a country, like "Anchor Point, Taghazout, Morocco".
        date_time: the date and time for which you want the report, formatted as '%m/%d/%y %H:%M:%S'.
    """
    lon, lat = convert_location_to_coordinates(location)
    try:
        date_time = datetime.strptime(date_time)
    except Exception as e:
        raise ValueError("Conversion of `date_time` to datetime format failed, make sure to provide a string in format '%m/%d/%y %H:%M:%S'. Full trace:" + str(e))
    temperature_celsius, risk_of_rain, wave_height = get_weather_report_at_coordinates((lon, lat), date_time)
    return f"Weather report for {location}, {date_time}: Temperature will be {temperature_celsius}°C, risk of rain is {risk_of_rain*100:.0f}%, wave height is {wave_height}m."
```

一般来说，为了减轻 LLM 的负担，要问自己的好问题是："如果我是一个第一次使用这个工具的傻瓜，使用这个工具编程并纠正自己的错误有多容易？"。

### 给 agent 更多参数

除了简单的任务描述字符串外，你还可以使用 `additional_args` 参数传递任何类型的对象：

```py
from smolagents import CodeAgent, HfApiModel

model_id = "meta-llama/Llama-3.3-70B-Instruct"

agent = CodeAgent(tools=[], model=HfApiModel(model_id=model_id), add_base_tools=True)

agent.run(
    "Why does Mike not know many people in New York?",
    additional_args={"mp3_sound_file_url":'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/recording.mp3'}
)
```
例如，你可以使用这个 `additional_args` 参数传递你希望 agent 利用的图像或字符串。


## 如何调试你的 agent

### 1. 使用更强大的 LLM

在 agent 工作流中，有些错误是实际错误，有些则是你的 LLM 引擎没有正确推理的结果。
例如，参考这个我要求创建一个汽车图片的 `CodeAgent` 的运行记录：
```text
==================================================================================================== New task ====================================================================================================
Make me a cool car picture
──────────────────────────────────────────────────────────────────────────────────────────────────── New step ─────────────────────────────────────────────────────────────────────────────────────────────────────
Agent is executing the code below: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
image_generator(prompt="A cool, futuristic sports car with LED headlights, aerodynamic design, and vibrant color, high-res, photorealistic")
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Last output from code snippet: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
/var/folders/6m/9b1tts6d5w960j80wbw9tx3m0000gn/T/tmpx09qfsdd/652f0007-3ee9-44e2-94ac-90dae6bb89a4.png
Step 1:

- Time taken: 16.35 seconds
- Input tokens: 1,383
- Output tokens: 77
──────────────────────────────────────────────────────────────────────────────────────────────────── New step ─────────────────────────────────────────────────────────────────────────────────────────────────────
Agent is executing the code below: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
final_answer("/var/folders/6m/9b1tts6d5w960j80wbw9tx3m0000gn/T/tmpx09qfsdd/652f0007-3ee9-44e2-94ac-90dae6bb89a4.png")
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Print outputs:

Last output from code snippet: ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
/var/folders/6m/9b1tts6d5w960j80wbw9tx3m0000gn/T/tmpx09qfsdd/652f0007-3ee9-44e2-94ac-90dae6bb89a4.png
Final answer:
/var/folders/6m/9b1tts6d5w960j80wbw9tx3m0000gn/T/tmpx09qfsdd/652f0007-3ee9-44e2-94ac-90dae6bb89a4.png
```
用户看到的是返回了一个路径，而不是图像。
这看起来像是系统的错误，但实际上 agent 系统并没有导致错误：只是 LLM 大脑犯了一个错误，没有把图像输出，保存到变量中。
因此，它无法再次访问图像，只能利用保存图像时记录的路径，所以它返回的是路径，而不是图像。

调试 agent 的第一步是"使用更强大的 LLM"。像 `Qwen2.5-72B-Instruct` 这样的替代方案不会犯这种错误。

### 2. 提供更多指导/更多信息

你也可以使用不太强大的模型，只要你更有效地指导它们。

站在模型的角度思考：如果你是模型在解决任务，你会因为系统提示+任务表述+工具描述中提供的信息而挣扎吗？

你需要一些额外的说明吗？

为了提供额外信息，我们不建议立即更改系统提示：默认系统提示有许多调整，除非你非常了解提示，否则你很容易翻车。
更好的指导 LLM 引擎的方法是：
- 如果是关于要解决的任务：把所有细节添加到任务中。任务可以有几百页长。
- 如果是关于如何使用工具：你的工具的 description 属性。


### 3. 更改系统提示（通常不建议）

如果上述说明不够，你可以更改系统提示。

让我们看看它是如何工作的。例如，让我们检查 [`CodeAgent`] 的默认系统提示（下面的版本通过跳过零样本示例进行了缩短）。

```python
print(agent.system_prompt_template)
```
你会得到：
```text
You are an expert assistant who can solve any task using code blobs. You will be given a task to solve as best you can.
To do so, you have been given access to a list of tools: these tools are basically Python functions which you can call with code.
To solve the task, you must plan forward to proceed in a series of steps, in a cycle of 'Thought:', 'Code:', and 'Observation:' sequences.

At each step, in the 'Thought:' sequence, you should first explain your reasoning towards solving the task and the tools that you want to use.
Then in the 'Code:' sequence, you should write the code in simple Python. The code sequence must end with '<end_code>' sequence.
During each intermediate step, you can use 'print()' to save whatever important information you will then need.
These print outputs will then appear in the 'Observation:' field, which will be available as input for the next step.
In the end you have to return a final answer using the `final_answer` tool.

Here are a few examples using notional tools:
---
{examples}

Above example were using notional tools that might not exist for you. On top of performing computations in the Python code snippets that you create, you only have access to these tools:

{{tool_descriptions}}

{{managed_agents_descriptions}}

Here are the rules you should always follow to solve your task:
1. Always provide a 'Thought:' sequence, and a 'Code:\n```py' sequence ending with '```<end_code>' sequence, else you will fail.
2. Use only variables that you have defined!
3. Always use the right arguments for the tools. DO NOT pass the arguments as a dict as in 'answer = wiki({'query': "What is the place where James Bond lives?"})', but use the arguments directly as in 'answer = wiki(query="What is the place where James Bond lives?")'.
4. Take care to not chain too many sequential tool calls in the same code block, especially when the output format is unpredictable. For instance, a call to search has an unpredictable return format, so do not have another tool call that depends on its output in the same block: rather output results with print() to use them in the next block.
5. Call a tool only when needed, and never re-do a tool call that you previously did with the exact same parameters.
6. Don't name any new variable with the same name as a tool: for instance don't name a variable 'final_answer'.
7. Never create any notional variables in our code, as having these in your logs might derail you from the true variables.
8. You can use imports in your code, but only from the following list of modules: {{authorized_imports}}
9. The state persists between code executions: so if in one step you've created variables or imported modules, these will all persist.
10. Don't give up! You're in charge of solving the task, not providing directions to solve it.

Now Begin! If you solve the task correctly, you will receive a reward of $1,000,000.
```

如你所见，有一些占位符，如 `"{{tool_descriptions}}"`：这些将在 agent 初始化时用于插入某些自动生成的工具或管理 agent 的描述。

因此，虽然你可以通过将自定义提示作为参数传递给 `system_prompt` 参数来覆盖此系统提示模板，但你的新系统提示必须包含以下占位符：
- `"{{tool_descriptions}}"` 用于插入工具描述。
- `"{{managed_agents_description}}"` 用于插入 managed agent 的描述（如果有）。
- 仅限 `CodeAgent`：`"{{authorized_imports}}"` 用于插入授权导入列表。

然后你可以根据如下，更改系统提示：

```py
from smolagents.prompts import CODE_SYSTEM_PROMPT

modified_system_prompt = CODE_SYSTEM_PROMPT + "\nHere you go!" # 在此更改系统提示

agent = CodeAgent(
    tools=[], 
    model=HfApiModel(), 
    system_prompt=modified_system_prompt
)
```

这也适用于 [`ToolCallingAgent`]。


### 4. 额外规划

我们提供了一个用于补充规划步骤的模型，agent 可以在正常操作步骤之间定期运行。在此步骤中，没有工具调用，LLM 只是被要求更新它知道的事实列表，并根据这些事实反推它应该采取的下一步。

```py
from smolagents import load_tool, CodeAgent, HfApiModel, DuckDuckGoSearchTool
from dotenv import load_dotenv

load_dotenv()

# 从 Hub 导入工具
image_generation_tool = load_tool("m-ric/text-to-image", trust_remote_code=True)

search_tool = DuckDuckGoSearchTool()

agent = CodeAgent(
    tools=[search_tool],
    model=HfApiModel("Qwen/Qwen2.5-72B-Instruct"),
    planning_interval=3 # 这是你激活规划的地方！
)

# 运行它！
result = agent.run(
    "How long would a cheetah at full speed take to run the length of Pont Alexandre III?",
)
```
```

## File: tests/__init__.py

<a name='file-tests-__init__.py'></a>
*Description*: This is a Python script.

```python

```

## File: tests/test_python_interpreter.py

<a name='file-tests-test_python_interpreter.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import numpy as np
import pytest

from smolagents.default_tools import BASE_PYTHON_TOOLS
from smolagents.local_python_executor import (
    InterpreterError,
    evaluate_python_code,
    fix_final_answer_code,
)


# Fake function we will use as tool
def add_two(x):
    return x + 2


class PythonInterpreterTester(unittest.TestCase):
    def test_evaluate_assign(self):
        code = "x = 3"
        state = {}
        result, _ = evaluate_python_code(code, {}, state=state)
        assert result == 3
        self.assertDictEqual(state, {"x": 3, "print_outputs": ""})

        code = "x = y"
        state = {"y": 5}
        result, _ = evaluate_python_code(code, {}, state=state)
        # evaluate returns the value of the last assignment.
        assert result == 5
        self.assertDictEqual(state, {"x": 5, "y": 5, "print_outputs": ""})

        code = "a=1;b=None"
        result, _ = evaluate_python_code(code, {}, state={})
        # evaluate returns the value of the last assignment.
        assert result is None

    def test_assignment_cannot_overwrite_tool(self):
        code = "print = '3'"
        with pytest.raises(InterpreterError) as e:
            evaluate_python_code(code, {"print": print}, state={})
        assert (
            "Cannot assign to name 'print': doing this would erase the existing tool!"
            in str(e)
        )

    def test_evaluate_call(self):
        code = "y = add_two(x)"
        state = {"x": 3}
        result, _ = evaluate_python_code(code, {"add_two": add_two}, state=state)
        assert result == 5
        self.assertDictEqual(state, {"x": 3, "y": 5, "print_outputs": ""})

        # Should not work without the tool
        with pytest.raises(InterpreterError) as e:
            evaluate_python_code(code, {}, state=state)
        assert "tried to execute add_two" in str(e.value)

    def test_evaluate_constant(self):
        code = "x = 3"
        state = {}
        result, _ = evaluate_python_code(code, {}, state=state)
        assert result == 3
        self.assertDictEqual(state, {"x": 3, "print_outputs": ""})

    def test_evaluate_dict(self):
        code = "test_dict = {'x': x, 'y': add_two(x)}"
        state = {"x": 3}
        result, _ = evaluate_python_code(code, {"add_two": add_two}, state=state)
        self.assertDictEqual(result, {"x": 3, "y": 5})
        self.assertDictEqual(
            state, {"x": 3, "test_dict": {"x": 3, "y": 5}, "print_outputs": ""}
        )

    def test_evaluate_expression(self):
        code = "x = 3\ny = 5"
        state = {}
        result, _ = evaluate_python_code(code, {}, state=state)
        # evaluate returns the value of the last assignment.
        assert result == 5
        self.assertDictEqual(state, {"x": 3, "y": 5, "print_outputs": ""})

    def test_evaluate_f_string(self):
        code = "text = f'This is x: {x}.'"
        state = {"x": 3}
        result, _ = evaluate_python_code(code, {}, state=state)
        # evaluate returns the value of the last assignment.
        assert result == "This is x: 3."
        self.assertDictEqual(
            state, {"x": 3, "text": "This is x: 3.", "print_outputs": ""}
        )

    def test_evaluate_if(self):
        code = "if x <= 3:\n    y = 2\nelse:\n    y = 5"
        state = {"x": 3}
        result, _ = evaluate_python_code(code, {}, state=state)
        # evaluate returns the value of the last assignment.
        assert result == 2
        self.assertDictEqual(state, {"x": 3, "y": 2, "print_outputs": ""})

        state = {"x": 8}
        result, _ = evaluate_python_code(code, {}, state=state)
        # evaluate returns the value of the last assignment.
        assert result == 5
        self.assertDictEqual(state, {"x": 8, "y": 5, "print_outputs": ""})

    def test_evaluate_list(self):
        code = "test_list = [x, add_two(x)]"
        state = {"x": 3}
        result, _ = evaluate_python_code(code, {"add_two": add_two}, state=state)
        self.assertListEqual(result, [3, 5])
        self.assertDictEqual(state, {"x": 3, "test_list": [3, 5], "print_outputs": ""})

    def test_evaluate_name(self):
        code = "y = x"
        state = {"x": 3}
        result, _ = evaluate_python_code(code, {}, state=state)
        assert result == 3
        self.assertDictEqual(state, {"x": 3, "y": 3, "print_outputs": ""})

    def test_evaluate_subscript(self):
        code = "test_list = [x, add_two(x)]\ntest_list[1]"
        state = {"x": 3}
        result, _ = evaluate_python_code(code, {"add_two": add_two}, state=state)
        assert result == 5
        self.assertDictEqual(state, {"x": 3, "test_list": [3, 5], "print_outputs": ""})

        code = "test_dict = {'x': x, 'y': add_two(x)}\ntest_dict['y']"
        state = {"x": 3}
        result, _ = evaluate_python_code(code, {"add_two": add_two}, state=state)
        assert result == 5
        self.assertDictEqual(
            state, {"x": 3, "test_dict": {"x": 3, "y": 5}, "print_outputs": ""}
        )

        code = "vendor = {'revenue': 31000, 'rent': 50312}; vendor['ratio'] = round(vendor['revenue'] / vendor['rent'], 2)"
        state = {}
        evaluate_python_code(
            code, {"min": min, "print": print, "round": round}, state=state
        )
        assert state["vendor"] == {"revenue": 31000, "rent": 50312, "ratio": 0.62}

    def test_subscript_string_with_string_index_raises_appropriate_error(self):
        code = """
search_results = "[{'title': 'Paris, Ville de Paris, France Weather Forecast | AccuWeather', 'href': 'https://www.accuweather.com/en/fr/paris/623/weather-forecast/623', 'body': 'Get the latest weather forecast for Paris, Ville de Paris, France , including hourly, daily, and 10-day outlooks. AccuWeather provides you with reliable and accurate information on temperature ...'}]"
for result in search_results:
    if 'current' in result['title'].lower() or 'temperature' in result['title'].lower():
        current_weather_url = result['href']
        print(current_weather_url)
        break"""
        with pytest.raises(InterpreterError) as e:
            evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
            assert "You're trying to subscript a string with a string index" in e

    def test_evaluate_for(self):
        code = "x = 0\nfor i in range(3):\n    x = i"
        state = {}
        result, _ = evaluate_python_code(code, {"range": range}, state=state)
        assert result == 2
        self.assertDictEqual(state, {"x": 2, "i": 2, "print_outputs": ""})

    def test_evaluate_binop(self):
        code = "y + x"
        state = {"x": 3, "y": 6}
        result, _ = evaluate_python_code(code, {}, state=state)
        assert result == 9
        self.assertDictEqual(state, {"x": 3, "y": 6, "print_outputs": ""})

    def test_recursive_function(self):
        code = """
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
recur_fibo(6)"""
        result, _ = evaluate_python_code(code, {}, state={})
        assert result == 8

    def test_evaluate_string_methods(self):
        code = "'hello'.replace('h', 'o').split('e')"
        result, _ = evaluate_python_code(code, {}, state={})
        assert result == ["o", "llo"]

    def test_evaluate_slicing(self):
        code = "'hello'[1:3][::-1]"
        result, _ = evaluate_python_code(code, {}, state={})
        assert result == "le"

    def test_access_attributes(self):
        code = "integer = 1\nobj_class = integer.__class__\nobj_class"
        result, _ = evaluate_python_code(code, {}, state={})
        assert result is int

    def test_list_comprehension(self):
        code = "sentence = 'THESEAGULL43'\nmeaningful_sentence = '-'.join([char.lower() for char in sentence if char.isalpha()])"
        result, _ = evaluate_python_code(code, {}, state={})
        assert result == "t-h-e-s-e-a-g-u-l-l"

    def test_string_indexing(self):
        code = """text_block = [
    "THESE",
    "AGULL"
]
sentence = ""
for block in text_block:
    for col in range(len(text_block[0])):
        sentence += block[col]
        """
        result, _ = evaluate_python_code(code, {"len": len, "range": range}, state={})
        assert result == "THESEAGULL"

    def test_tuples(self):
        code = "x = (1, 2, 3)\nx[1]"
        result, _ = evaluate_python_code(code, {}, state={})
        assert result == 2

        code = """
digits, i = [1, 2, 3], 1
digits[i], digits[i + 1] = digits[i + 1], digits[i]"""
        evaluate_python_code(code, {"range": range, "print": print, "int": int}, {})

        code = """
def calculate_isbn_10_check_digit(number):
    total = sum((10 - i) * int(digit) for i, digit in enumerate(number))
    remainder = total % 11
    check_digit = 11 - remainder
    if check_digit == 10:
        return 'X'
    elif check_digit == 11:
        return '0'
    else:
        return str(check_digit)

# Given 9-digit numbers
numbers = [
    "478225952",
    "643485613",
    "739394228",
    "291726859",
    "875262394",
    "542617795",
    "031810713",
    "957007669",
    "871467426"
]

# Calculate check digits for each number
check_digits = [calculate_isbn_10_check_digit(number) for number in numbers]
print(check_digits)
"""
        state = {}
        evaluate_python_code(
            code,
            {
                "range": range,
                "print": print,
                "sum": sum,
                "enumerate": enumerate,
                "int": int,
                "str": str,
            },
            state,
        )

    def test_listcomp(self):
        code = "x = [i for i in range(3)]"
        result, _ = evaluate_python_code(code, {"range": range}, state={})
        assert result == [0, 1, 2]

    def test_break_continue(self):
        code = "for i in range(10):\n    if i == 5:\n        break\ni"
        result, _ = evaluate_python_code(code, {"range": range}, state={})
        assert result == 5

        code = "for i in range(10):\n    if i == 5:\n        continue\ni"
        result, _ = evaluate_python_code(code, {"range": range}, state={})
        assert result == 9

    def test_call_int(self):
        code = "import math\nstr(math.ceil(149))"
        result, _ = evaluate_python_code(code, {"str": lambda x: str(x)}, state={})
        assert result == "149"

    def test_lambda(self):
        code = "f = lambda x: x + 2\nf(3)"
        result, _ = evaluate_python_code(code, {}, state={})
        assert result == 5

    def test_dictcomp(self):
        code = "x = {i: i**2 for i in range(3)}"
        result, _ = evaluate_python_code(code, {"range": range}, state={})
        assert result == {0: 0, 1: 1, 2: 4}

        code = "{num: name for num, name in {101: 'a', 102: 'b'}.items() if name not in ['a']}"
        result, _ = evaluate_python_code(
            code, {"print": print}, state={}, authorized_imports=["pandas"]
        )
        assert result == {102: "b"}

        code = """
shifts = {'A': ('6:45', '8:00'), 'B': ('10:00', '11:45')}
shift_minutes = {worker: ('a', 'b') for worker, (start, end) in shifts.items()}
"""
        result, _ = evaluate_python_code(code, {}, state={})
        assert result == {"A": ("a", "b"), "B": ("a", "b")}

    def test_tuple_assignment(self):
        code = "a, b = 0, 1\nb"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == 1

    def test_while(self):
        code = "i = 0\nwhile i < 3:\n    i += 1\ni"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == 3

        # test infinite loop
        code = "i = 0\nwhile i < 3:\n    i -= 1\ni"
        with pytest.raises(InterpreterError) as e:
            evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert "iterations in While loop exceeded" in str(e)

        # test lazy evaluation
        code = """
house_positions = [0, 7, 10, 15, 18, 22, 22]
i, n, loc = 0, 7, 30
while i < n and house_positions[i] <= loc:
    i += 1
"""
        state = {}
        evaluate_python_code(code, BASE_PYTHON_TOOLS, state=state)

    def test_generator(self):
        code = "a = [1, 2, 3, 4, 5]; b = (i**2 for i in a); list(b)"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == [1, 4, 9, 16, 25]

    def test_boolops(self):
        code = """if (not (a > b and a > c)) or d > e:
    best_city = "Brooklyn"
else:
    best_city = "Manhattan"
    best_city
    """
        result, _ = evaluate_python_code(
            code, BASE_PYTHON_TOOLS, state={"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
        )
        assert result == "Brooklyn"

        code = """if d > e and a < b:
    best_city = "Brooklyn"
elif d < e and a < b:
    best_city = "Sacramento"
else:
    best_city = "Manhattan"
    best_city
    """
        result, _ = evaluate_python_code(
            code, BASE_PYTHON_TOOLS, state={"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
        )
        assert result == "Sacramento"

    def test_if_conditions(self):
        code = """char='a'
if char.isalpha():
    print('2')"""
        state = {}
        evaluate_python_code(code, BASE_PYTHON_TOOLS, state=state)
        assert state["print_outputs"] == "2\n"

    def test_imports(self):
        code = "import math\nmath.sqrt(4)"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == 2.0

        code = (
            "from random import choice, seed\nseed(12)\nchoice(['win', 'lose', 'draw'])"
        )
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == "lose"

        code = "import time, re\ntime.sleep(0.1)"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result is None

        code = "from queue import Queue\nq = Queue()\nq.put(1)\nq.get()"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == 1

        code = "import itertools\nlist(itertools.islice(range(10), 3))"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == [0, 1, 2]

        code = "import re\nre.search('a', 'abc').group()"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == "a"

        code = "import stat\nstat.S_ISREG(0o100644)"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result

        code = "import statistics\nstatistics.mean([1, 2, 3, 4, 4])"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == 2.8

        code = "import unicodedata\nunicodedata.name('A')"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == "LATIN CAPITAL LETTER A"

        # Test submodules are handled properly, thus not raising error
        code = "import numpy.random as rd\nrng = rd.default_rng(12345)\nrng.random()"
        result, _ = evaluate_python_code(
            code, BASE_PYTHON_TOOLS, state={}, authorized_imports=["numpy"]
        )

        code = "from numpy.random import default_rng as d_rng\nrng = d_rng(12345)\nrng.random()"
        result, _ = evaluate_python_code(
            code, BASE_PYTHON_TOOLS, state={}, authorized_imports=["numpy"]
        )

    def test_additional_imports(self):
        code = "import numpy as np"
        evaluate_python_code(code, authorized_imports=["numpy"], state={})

        code = "import numpy.random as rd"
        evaluate_python_code(code, authorized_imports=["numpy.random"], state={})
        evaluate_python_code(code, authorized_imports=["numpy"], state={})
        evaluate_python_code(code, authorized_imports=["*"], state={})
        with pytest.raises(InterpreterError):
            evaluate_python_code(code, authorized_imports=["random"], state={})

    def test_multiple_comparators(self):
        code = "0 <= -1 < 4 and 0 <= -5 < 4"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert not result

        code = "0 <= 1 < 4 and 0 <= -5 < 4"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert not result

        code = "0 <= 4 < 4 and 0 <= 3 < 4"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert not result

        code = "0 <= 3 < 4 and 0 <= 3 < 4"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result

    def test_print_output(self):
        code = "print('Hello world!')\nprint('Ok no one cares')"
        state = {}
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state=state)
        assert result is None
        assert state["print_outputs"] == "Hello world!\nOk no one cares\n"

        # test print in function
        code = """
print("1")
def function():
    print("2")
function()"""
        state = {}
        evaluate_python_code(code, {"print": print}, state=state)
        assert state["print_outputs"] == "1\n2\n"

    def test_tuple_target_in_iterator(self):
        code = "for a, b in [('Ralf Weikert', 'Austria'), ('Samuel Seungwon Lee', 'South Korea')]:res = a.split()[0]"
        result, _ = evaluate_python_code(code, BASE_PYTHON_TOOLS, state={})
        assert result == "Samuel"

    def test_classes(self):
        code = """
class Animal:
    species = "Generic Animal"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sound(self):
        return "The animal makes a sound."

    def __str__(self):
        return f"{self.name}, {self.age} years old"

class Dog(Animal):
    species = "Canine"

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def sound(self):
        return "The dog barks."


*Content truncated for brevity.*

```

## File: tests/test_tools.py

<a name='file-tests-test_tools.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
from pathlib import Path
from typing import Dict, Optional, Union

import numpy as np
import pytest
from transformers import is_torch_available, is_vision_available
from transformers.testing_utils import get_tests_dir

from smolagents.tools import AUTHORIZED_TYPES, Tool, tool
from smolagents.types import (
    AGENT_TYPE_MAPPING,
    AgentAudio,
    AgentImage,
    AgentText,
)

if is_torch_available():
    import torch

if is_vision_available():
    from PIL import Image


def create_inputs(tool_inputs: Dict[str, Dict[Union[str, type], str]]):
    inputs = {}

    for input_name, input_desc in tool_inputs.items():
        input_type = input_desc["type"]

        if input_type == "string":
            inputs[input_name] = "Text input"
        elif input_type == "image":
            inputs[input_name] = Image.open(
                Path(get_tests_dir("fixtures")) / "000000039769.png"
            ).resize((512, 512))
        elif input_type == "audio":
            inputs[input_name] = np.ones(3000)
        else:
            raise ValueError(f"Invalid type requested: {input_type}")

    return inputs


def output_type(output):
    if isinstance(output, (str, AgentText)):
        return "string"
    elif isinstance(output, (Image.Image, AgentImage)):
        return "image"
    elif isinstance(output, (torch.Tensor, AgentAudio)):
        return "audio"
    else:
        raise TypeError(f"Invalid output: {output}")


class ToolTesterMixin:
    def test_inputs_output(self):
        self.assertTrue(hasattr(self.tool, "inputs"))
        self.assertTrue(hasattr(self.tool, "output_type"))

        inputs = self.tool.inputs
        self.assertTrue(isinstance(inputs, dict))

        for _, input_spec in inputs.items():
            self.assertTrue("type" in input_spec)
            self.assertTrue("description" in input_spec)
            self.assertTrue(input_spec["type"] in AUTHORIZED_TYPES)
            self.assertTrue(isinstance(input_spec["description"], str))

        output_type = self.tool.output_type
        self.assertTrue(output_type in AUTHORIZED_TYPES)

    def test_common_attributes(self):
        self.assertTrue(hasattr(self.tool, "description"))
        self.assertTrue(hasattr(self.tool, "name"))
        self.assertTrue(hasattr(self.tool, "inputs"))
        self.assertTrue(hasattr(self.tool, "output_type"))

    def test_agent_type_output(self):
        inputs = create_inputs(self.tool.inputs)
        output = self.tool(**inputs, sanitize_inputs_outputs=True)
        if self.tool.output_type != "any":
            agent_type = AGENT_TYPE_MAPPING[self.tool.output_type]
            self.assertTrue(isinstance(output, agent_type))


class ToolTests(unittest.TestCase):
    def test_tool_init_with_decorator(self):
        @tool
        def coolfunc(a: str, b: int) -> float:
            """Cool function

            Args:
                a: The first argument
                b: The second one
            """
            return b + 2, a

        assert coolfunc.output_type == "number"

    def test_tool_init_vanilla(self):
        class HFModelDownloadsTool(Tool):
            name = "model_download_counter"
            description = """
            This is a tool that returns the most downloaded model of a given task on the Hugging Face Hub.
            It returns the name of the checkpoint."""

            inputs = {
                "task": {
                    "type": "string",
                    "description": "the task category (such as text-classification, depth-estimation, etc)",
                }
            }
            output_type = "string"

            def forward(self, task: str) -> str:
                return "best model"

        tool = HFModelDownloadsTool()
        assert list(tool.inputs.keys())[0] == "task"

    def test_tool_init_decorator_raises_issues(self):
        with pytest.raises(Exception) as e:

            @tool
            def coolfunc(a: str, b: int):
                """Cool function

                Args:
                    a: The first argument
                    b: The second one
                """
                return a + b

            assert coolfunc.output_type == "number"
        assert "Tool return type not found" in str(e)

        with pytest.raises(Exception) as e:

            @tool
            def coolfunc(a: str, b: int) -> int:
                """Cool function

                Args:
                    a: The first argument
                """
                return b + a

            assert coolfunc.output_type == "number"
        assert "docstring has no description for the argument" in str(e)

    def test_saving_tool_raises_error_imports_outside_function(self):
        with pytest.raises(Exception) as e:
            import numpy as np

            @tool
            def get_current_time() -> str:
                """
                Gets the current time.
                """
                return str(np.random.random())

            get_current_time.save("output")

        assert "np" in str(e)

        # Also test with classic definition
        with pytest.raises(Exception) as e:

            class GetCurrentTimeTool(Tool):
                name = "get_current_time_tool"
                description = "Gets the current time"
                inputs = {}
                output_type = "string"

                def forward(self):
                    return str(np.random.random())

            get_current_time = GetCurrentTimeTool()
            get_current_time.save("output")

        assert "np" in str(e)

    def test_tool_definition_raises_no_error_imports_in_function(self):
        @tool
        def get_current_time() -> str:
            """
            Gets the current time.
            """
            from datetime import datetime

            return str(datetime.now())

        class GetCurrentTimeTool(Tool):
            name = "get_current_time_tool"
            description = "Gets the current time"
            inputs = {}
            output_type = "string"

            def forward(self):
                from datetime import datetime

                return str(datetime.now())

    def test_saving_tool_allows_no_arg_in_init(self):
        # Test one cannot save tool with additional args in init
        class FailTool(Tool):
            name = "specific"
            description = "test description"
            inputs = {
                "string_input": {"type": "string", "description": "input description"}
            }
            output_type = "string"

            def __init__(self, url):
                super().__init__(self)
                self.url = "none"

            def forward(self, string_input: str) -> str:
                return self.url + string_input

        fail_tool = FailTool("dummy_url")
        with pytest.raises(Exception) as e:
            fail_tool.save("output")
        assert "__init__" in str(e)

    def test_saving_tool_allows_no_imports_from_outside_methods(self):
        # Test that using imports from outside functions fails
        import numpy as np

        class FailTool(Tool):
            name = "specific"
            description = "test description"
            inputs = {
                "string_input": {"type": "string", "description": "input description"}
            }
            output_type = "string"

            def useless_method(self):
                self.client = np.random.random()
                return ""

            def forward(self, string_input):
                return self.useless_method() + string_input

        fail_tool = FailTool()
        with pytest.raises(Exception) as e:
            fail_tool.save("output")
        assert "'np' is undefined" in str(e)

        # Test that putting these imports inside functions works
        class SuccessTool(Tool):
            name = "specific"
            description = "test description"
            inputs = {
                "string_input": {"type": "string", "description": "input description"}
            }
            output_type = "string"

            def useless_method(self):
                import numpy as np

                self.client = np.random.random()
                return ""

            def forward(self, string_input):
                return self.useless_method() + string_input

        success_tool = SuccessTool()
        success_tool.save("output")

    def test_tool_missing_class_attributes_raises_error(self):
        with pytest.raises(Exception) as e:

            class GetWeatherTool(Tool):
                name = "get_weather"
                description = "Get weather in the next days at given location."
                inputs = {
                    "location": {"type": "string", "description": "the location"},
                    "celsius": {
                        "type": "string",
                        "description": "the temperature type",
                    },
                }

                def forward(
                    self, location: str, celsius: Optional[bool] = False
                ) -> str:
                    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

            GetWeatherTool()
        assert "You must set an attribute output_type" in str(e)

    def test_tool_from_decorator_optional_args(self):
        @tool
        def get_weather(location: str, celsius: Optional[bool] = False) -> str:
            """
            Get weather in the next days at given location.
            Secretly this tool does not care about the location, it hates the weather everywhere.

            Args:
                location: the location
                celsius: the temperature type
            """
            return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

        assert "nullable" in get_weather.inputs["celsius"]
        assert get_weather.inputs["celsius"]["nullable"]
        assert "nullable" not in get_weather.inputs["location"]

    def test_tool_mismatching_nullable_args_raises_error(self):
        with pytest.raises(Exception) as e:

            class GetWeatherTool(Tool):
                name = "get_weather"
                description = "Get weather in the next days at given location."
                inputs = {
                    "location": {"type": "string", "description": "the location"},
                    "celsius": {
                        "type": "string",
                        "description": "the temperature type",
                    },
                }
                output_type = "string"

                def forward(
                    self, location: str, celsius: Optional[bool] = False
                ) -> str:
                    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

            GetWeatherTool()
        assert "Nullable" in str(e)

        with pytest.raises(Exception) as e:

            class GetWeatherTool2(Tool):
                name = "get_weather"
                description = "Get weather in the next days at given location."
                inputs = {
                    "location": {"type": "string", "description": "the location"},
                    "celsius": {
                        "type": "string",
                        "description": "the temperature type",
                    },
                }
                output_type = "string"

                def forward(self, location: str, celsius: bool = False) -> str:
                    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

            GetWeatherTool2()
        assert "Nullable" in str(e)

        with pytest.raises(Exception) as e:

            class GetWeatherTool3(Tool):
                name = "get_weather"
                description = "Get weather in the next days at given location."
                inputs = {
                    "location": {"type": "string", "description": "the location"},
                    "celsius": {
                        "type": "string",
                        "description": "the temperature type",
                        "nullable": True,
                    },
                }
                output_type = "string"

                def forward(self, location, celsius: str) -> str:
                    return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

            GetWeatherTool3()
        assert "Nullable" in str(e)

```

## File: tests/test_all_docs.py

<a name='file-tests-test_all_docs.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ast
import os
import re
import shutil
import subprocess
import tempfile
import traceback
from pathlib import Path
from typing import List

import pytest
from dotenv import load_dotenv


class SubprocessCallException(Exception):
    pass


def run_command(command: List[str], return_stdout=False, env=None):
    """
    Runs command with subprocess.check_output and returns stdout if requested.
    Properly captures and handles errors during command execution.
    """
    for i, c in enumerate(command):
        if isinstance(c, Path):
            command[i] = str(c)

    if env is None:
        env = os.environ.copy()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, env=env)
        if return_stdout:
            if hasattr(output, "decode"):
                output = output.decode("utf-8")
            return output
    except subprocess.CalledProcessError as e:
        raise SubprocessCallException(
            f"Command `{' '.join(command)}` failed with the following error:\n\n{e.output.decode()}"
        ) from e


class DocCodeExtractor:
    """Handles extraction and validation of Python code from markdown files."""

    @staticmethod
    def extract_python_code(content: str) -> List[str]:
        """Extract Python code blocks from markdown content."""
        pattern = r"```(?:python|py)\n(.*?)\n```"
        matches = re.finditer(pattern, content, re.DOTALL)
        return [match.group(1).strip() for match in matches]

    @staticmethod
    def create_test_script(code_blocks: List[str], tmp_dir: str) -> Path:
        """Create a temporary Python script from code blocks."""
        combined_code = "\n\n".join(code_blocks)
        assert len(combined_code) > 0, "Code is empty!"
        tmp_file = Path(tmp_dir) / "test_script.py"

        with open(tmp_file, "w", encoding="utf-8") as f:
            f.write(combined_code)

        return tmp_file


class TestDocs:
    """Test case for documentation code testing."""

    @classmethod
    def setup_class(cls):
        cls._tmpdir = tempfile.mkdtemp()
        cls.launch_args = ["python3"]
        cls.docs_dir = Path(__file__).parent.parent / "docs" / "source"
        cls.extractor = DocCodeExtractor()

        if not cls.docs_dir.exists():
            raise ValueError(f"Docs directory not found at {cls.docs_dir}")

        load_dotenv()

        cls.md_files = list(cls.docs_dir.rglob("*.md"))
        if not cls.md_files:
            raise ValueError(f"No markdown files found in {cls.docs_dir}")

    @classmethod
    def teardown_class(cls):
        shutil.rmtree(cls._tmpdir)

    @pytest.mark.timeout(100)
    def test_single_doc(self, doc_path: Path):
        """Test a single documentation file."""
        with open(doc_path, "r", encoding="utf-8") as f:
            content = f.read()

        code_blocks = self.extractor.extract_python_code(content)
        excluded_snippets = [
            "ToolCollection",
            "image_generation_tool",  # We don't want to run this expensive operation
            "from_langchain",  # Langchain is not a dependency
            "while llm_should_continue(memory):",  # This is pseudo code
            "ollama_chat/llama3.2",  # Exclude ollama building in guided tour
            "model = TransformersModel(model_id=model_id)",  # Exclude testing with transformers model
        ]
        code_blocks = [
            block
            for block in code_blocks
            if not any(
                [snippet in block for snippet in excluded_snippets]
            )  # Exclude these tools that take longer to run and add dependencies
        ]
        if len(code_blocks) == 0:
            pytest.skip(f"No Python code blocks found in {doc_path.name}")

        # Validate syntax of each block individually by parsing it
        for i, block in enumerate(code_blocks, 1):
            ast.parse(block)

        # Create and execute test script
        print("\n\nCollected code block:==========\n".join(code_blocks))
        try:
            code_blocks = [
                (
                    block.replace(
                        "<YOUR_HUGGINGFACEHUB_API_TOKEN>", os.getenv("HF_TOKEN")
                    )
                    .replace("YOUR_ANTHROPIC_API_KEY", os.getenv("ANTHROPIC_API_KEY"))
                    .replace("{your_username}", "m-ric")
                )
                for block in code_blocks
            ]
            test_script = self.extractor.create_test_script(code_blocks, self._tmpdir)
            run_command(self.launch_args + [str(test_script)])

        except SubprocessCallException as e:
            pytest.fail(f"\nError while testing {doc_path.name}:\n{str(e)}")
        except Exception:
            pytest.fail(
                f"\nUnexpected error while testing {doc_path.name}:\n{traceback.format_exc()}"
            )

    @pytest.fixture(autouse=True)
    def _setup(self):
        """Fixture to ensure temporary directory exists for each test."""
        os.makedirs(self._tmpdir, exist_ok=True)
        yield
        # Clean up test files after each test
        for file in Path(self._tmpdir).glob("*"):
            file.unlink()


def pytest_generate_tests(metafunc):
    """Generate test cases for each markdown file."""
    if "doc_path" in metafunc.fixturenames:
        test_class = metafunc.cls

        # Initialize the class if needed
        if not hasattr(test_class, "md_files"):
            test_class.setup_class()

        # Parameterize with the markdown files
        metafunc.parametrize(
            "doc_path", test_class.md_files, ids=[f.stem for f in test_class.md_files]
        )

```

## File: tests/test_final_answer.py

<a name='file-tests-test_final_answer.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from pathlib import Path

import numpy as np
from PIL import Image
from transformers import is_torch_available
from transformers.testing_utils import get_tests_dir, require_torch

from smolagents.default_tools import FinalAnswerTool
from smolagents.types import AGENT_TYPE_MAPPING

from .test_tools import ToolTesterMixin

if is_torch_available():
    import torch


class FinalAnswerToolTester(unittest.TestCase, ToolTesterMixin):
    def setUp(self):
        self.inputs = {"answer": "Final answer"}
        self.tool = FinalAnswerTool()

    def test_exact_match_arg(self):
        result = self.tool("Final answer")
        self.assertEqual(result, "Final answer")

    def test_exact_match_kwarg(self):
        result = self.tool(answer=self.inputs["answer"])
        self.assertEqual(result, "Final answer")

    def create_inputs(self):
        inputs_text = {"answer": "Text input"}
        inputs_image = {
            "answer": Image.open(
                Path(get_tests_dir("fixtures")) / "000000039769.png"
            ).resize((512, 512))
        }
        inputs_audio = {"answer": torch.Tensor(np.ones(3000))}
        return {"string": inputs_text, "image": inputs_image, "audio": inputs_audio}

    @require_torch
    def test_agent_type_output(self):
        inputs = self.create_inputs()
        for input_type, input in inputs.items():
            output = self.tool(**input, sanitize_inputs_outputs=True)
            agent_type = AGENT_TYPE_MAPPING[input_type]
            self.assertTrue(isinstance(output, agent_type))

```

## File: tests/test_monitoring.py

<a name='file-tests-test_monitoring.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from smolagents import (
    AgentError,
    AgentImage,
    CodeAgent,
    ToolCallingAgent,
    stream_to_gradio,
)
from huggingface_hub import (
    ChatMessage,
    ChatMessageToolCall,
    ChatMessageToolCallDefinition,
)


class FakeLLMModel:
    def __init__(self):
        self.last_input_token_count = 10
        self.last_output_token_count = 20

    def __call__(self, prompt, tools_to_call_from=None, **kwargs):
        if tools_to_call_from is not None:
            return ChatMessage(
                role="assistant",
                content="",
                tool_calls=[
                    ChatMessageToolCall(
                        id="fake_id",
                        type="function",
                        function=ChatMessageToolCallDefinition(
                            name="final_answer", arguments={"answer": "image"}
                        ),
                    )
                ],
            )
        else:
            return ChatMessage(
                role="assistant",
                content="""
Code:
```py
final_answer('This is the final answer.')
```""",
            )


class MonitoringTester(unittest.TestCase):
    def test_code_agent_metrics(self):
        agent = CodeAgent(
            tools=[],
            model=FakeLLMModel(),
            max_steps=1,
        )
        agent.run("Fake task")

        self.assertEqual(agent.monitor.total_input_token_count, 10)
        self.assertEqual(agent.monitor.total_output_token_count, 20)

    def test_json_agent_metrics(self):
        agent = ToolCallingAgent(
            tools=[],
            model=FakeLLMModel(),
            max_steps=1,
        )

        agent.run("Fake task")

        self.assertEqual(agent.monitor.total_input_token_count, 10)
        self.assertEqual(agent.monitor.total_output_token_count, 20)

    def test_code_agent_metrics_max_steps(self):
        class FakeLLMModelMalformedAnswer:
            def __init__(self):
                self.last_input_token_count = 10
                self.last_output_token_count = 20

            def __call__(self, prompt, **kwargs):
                return ChatMessage(role="assistant", content="Malformed answer")

        agent = CodeAgent(
            tools=[],
            model=FakeLLMModelMalformedAnswer(),
            max_steps=1,
        )

        agent.run("Fake task")

        self.assertEqual(agent.monitor.total_input_token_count, 20)
        self.assertEqual(agent.monitor.total_output_token_count, 40)

    def test_code_agent_metrics_generation_error(self):
        class FakeLLMModelGenerationException:
            def __init__(self):
                self.last_input_token_count = 10
                self.last_output_token_count = 20

            def __call__(self, prompt, **kwargs):
                self.last_input_token_count = 10
                self.last_output_token_count = 0
                raise Exception("Cannot generate")

        agent = CodeAgent(
            tools=[],
            model=FakeLLMModelGenerationException(),
            max_steps=1,
        )
        agent.run("Fake task")

        self.assertEqual(
            agent.monitor.total_input_token_count, 20
        )  # Should have done two monitoring callbacks
        self.assertEqual(agent.monitor.total_output_token_count, 0)

    def test_streaming_agent_text_output(self):
        agent = CodeAgent(
            tools=[],
            model=FakeLLMModel(),
            max_steps=1,
        )

        # Use stream_to_gradio to capture the output
        outputs = list(stream_to_gradio(agent, task="Test task", test_mode=True))

        self.assertEqual(len(outputs), 4)
        final_message = outputs[-1]
        self.assertEqual(final_message.role, "assistant")
        self.assertIn("This is the final answer.", final_message.content)

    def test_streaming_agent_image_output(self):
        agent = ToolCallingAgent(
            tools=[],
            model=FakeLLMModel(),
            max_steps=1,
        )

        # Use stream_to_gradio to capture the output
        outputs = list(
            stream_to_gradio(
                agent,
                task="Test task",
                additional_args=dict(image=AgentImage(value="path.png")),
                test_mode=True,
            )
        )

        self.assertEqual(len(outputs), 3)
        final_message = outputs[-1]
        self.assertEqual(final_message.role, "assistant")
        self.assertIsInstance(final_message.content, dict)
        self.assertEqual(final_message.content["path"], "path.png")
        self.assertEqual(final_message.content["mime_type"], "image/png")

    def test_streaming_with_agent_error(self):
        def dummy_model(prompt, **kwargs):
            raise AgentError("Simulated agent error")

        agent = CodeAgent(
            tools=[],
            model=dummy_model,
            max_steps=1,
        )

        # Use stream_to_gradio to capture the output
        outputs = list(stream_to_gradio(agent, task="Test task", test_mode=True))

        self.assertEqual(len(outputs), 5)
        final_message = outputs[-1]
        self.assertEqual(final_message.role, "assistant")
        self.assertIn("Simulated agent error", final_message.content)

```

## File: tests/test_utils.py

<a name='file-tests-test_utils.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import pytest

from smolagents.utils import parse_code_blobs


class AgentTextTests(unittest.TestCase):
    def test_parse_code_blobs(self):
        with pytest.raises(ValueError):
            parse_code_blobs("Wrong blob!")

        # Parsing mardkwon with code blobs should work
        output = parse_code_blobs("""
Here is how to solve the problem:
Code:
```py
import numpy as np
```<end_code>
""")
        assert output == "import numpy as np"

        # Parsing code blobs should work
        code_blob = "import numpy as np"
        output = parse_code_blobs(code_blob)
        assert output == code_blob

    def test_multiple_code_blobs(self):
        test_input = """Here's a function that adds numbers:
```python
def add(a, b):
    return a + b
```
And here's a function that multiplies them:
```py
def multiply(a, b):
    return a * b
```"""

        expected_output = """def add(a, b):
    return a + b

def multiply(a, b):
    return a * b"""
        result = parse_code_blobs(test_input)
        assert result == expected_output

```

## File: tests/test_agents.py

<a name='file-tests-test_agents.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import tempfile
import unittest
import uuid
from pathlib import Path

from transformers.testing_utils import get_tests_dir

from smolagents.agents import (
    AgentMaxStepsError,
    CodeAgent,
    ManagedAgent,
    ToolCall,
    ToolCallingAgent,
)
from smolagents.default_tools import PythonInterpreterTool
from smolagents.tools import tool
from smolagents.types import AgentImage, AgentText
from smolagents.models import (
    ChatMessage,
    ChatMessageToolCall,
    ChatMessageToolCallDefinition,
)


def get_new_path(suffix="") -> str:
    directory = tempfile.mkdtemp()
    return os.path.join(directory, str(uuid.uuid4()) + suffix)


class FakeToolCallModel:
    def __call__(
        self, messages, tools_to_call_from=None, stop_sequences=None, grammar=None
    ):
        if len(messages) < 3:
            return ChatMessage(
                role="assistant",
                content="",
                tool_calls=[
                    ChatMessageToolCall(
                        id="call_0",
                        type="function",
                        function=ChatMessageToolCallDefinition(
                            name="python_interpreter", arguments={"code": "2*3.6452"}
                        ),
                    )
                ],
            )
        else:
            return ChatMessage(
                role="assistant",
                content="",
                tool_calls=[
                    ChatMessageToolCall(
                        id="call_1",
                        type="function",
                        function=ChatMessageToolCallDefinition(
                            name="final_answer", arguments={"answer": "7.2904"}
                        ),
                    )
                ],
            )


class FakeToolCallModelImage:
    def __call__(
        self, messages, tools_to_call_from=None, stop_sequences=None, grammar=None
    ):
        if len(messages) < 3:
            return ChatMessage(
                role="assistant",
                content="",
                tool_calls=[
                    ChatMessageToolCall(
                        id="call_0",
                        type="function",
                        function=ChatMessageToolCallDefinition(
                            name="fake_image_generation_tool",
                            arguments={"prompt": "An image of a cat"},
                        ),
                    )
                ],
            )
        else:
            return ChatMessage(
                role="assistant",
                content="",
                tool_calls=[
                    ChatMessageToolCall(
                        id="call_1",
                        type="function",
                        function=ChatMessageToolCallDefinition(
                            name="final_answer", arguments="image.png"
                        ),
                    )
                ],
            )


def fake_code_model(messages, stop_sequences=None, grammar=None) -> str:
    prompt = str(messages)
    if "special_marker" not in prompt:
        return ChatMessage(
            role="assistant",
            content="""
Thought: I should multiply 2 by 3.6452. special_marker
Code:
```py
result = 2**3.6452
```<end_code>
""",
        )
    else:  # We're at step 2
        return ChatMessage(
            role="assistant",
            content="""
Thought: I can now answer the initial question
Code:
```py
final_answer(7.2904)
```<end_code>
""",
        )


def fake_code_model_error(messages, stop_sequences=None) -> str:
    prompt = str(messages)
    if "special_marker" not in prompt:
        return ChatMessage(
            role="assistant",
            content="""
Thought: I should multiply 2 by 3.6452. special_marker
Code:
```py
a = 2
b = a * 2
print = 2
print("Ok, calculation done!")
```<end_code>
""",
        )
    else:  # We're at step 2
        return ChatMessage(
            role="assistant",
            content="""
Thought: I can now answer the initial question
Code:
```py
final_answer("got an error")
```<end_code>
""",
        )


def fake_code_model_syntax_error(messages, stop_sequences=None) -> str:
    prompt = str(messages)
    if "special_marker" not in prompt:
        return ChatMessage(
            role="assistant",
            content="""
Thought: I should multiply 2 by 3.6452. special_marker
Code:
```py
a = 2
b = a * 2
    print("Failing due to unexpected indent")
print("Ok, calculation done!")
```<end_code>
""",
        )
    else:  # We're at step 2
        return ChatMessage(
            role="assistant",
            content="""
Thought: I can now answer the initial question
Code:
```py
final_answer("got an error")
```<end_code>
""",
        )


def fake_code_model_import(messages, stop_sequences=None) -> str:
    return ChatMessage(
        role="assistant",
        content="""
Thought: I can answer the question
Code:
```py
import numpy as np
final_answer("got an error")
```<end_code>
""",
    )


def fake_code_functiondef(messages, stop_sequences=None) -> str:
    prompt = str(messages)
    if "special_marker" not in prompt:
        return ChatMessage(
            role="assistant",
            content="""
Thought: Let's define the function. special_marker
Code:
```py
import numpy as np

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w
```<end_code>
""",
        )
    else:  # We're at step 2
        return ChatMessage(
            role="assistant",
            content="""
Thought: I can now answer the initial question
Code:
```py
x, w = [0, 1, 2, 3, 4, 5], 2
res = moving_average(x, w)
final_answer(res)
```<end_code>
""",
        )


def fake_code_model_single_step(messages, stop_sequences=None, grammar=None) -> str:
    return ChatMessage(
        role="assistant",
        content="""
Thought: I should multiply 2 by 3.6452. special_marker
Code:
```py
result = python_interpreter(code="2*3.6452")
final_answer(result)
```
""",
    )


def fake_code_model_no_return(messages, stop_sequences=None, grammar=None) -> str:
    return ChatMessage(
        role="assistant",
        content="""
Thought: I should multiply 2 by 3.6452. special_marker
Code:
```py
result = python_interpreter(code="2*3.6452")
print(result)
```
""",
    )


class AgentTests(unittest.TestCase):
    def test_fake_single_step_code_agent(self):
        agent = CodeAgent(
            tools=[PythonInterpreterTool()], model=fake_code_model_single_step
        )
        output = agent.run("What is 2 multiplied by 3.6452?", single_step=True)
        assert isinstance(output, str)
        assert "7.2904" in output

    def test_fake_toolcalling_agent(self):
        agent = ToolCallingAgent(
            tools=[PythonInterpreterTool()], model=FakeToolCallModel()
        )
        output = agent.run("What is 2 multiplied by 3.6452?")
        assert isinstance(output, str)
        assert "7.2904" in output
        assert agent.logs[1].task == "What is 2 multiplied by 3.6452?"
        assert "7.2904" in agent.logs[2].observations
        assert agent.logs[3].llm_output is None

    def test_toolcalling_agent_handles_image_tool_outputs(self):
        from PIL import Image

        @tool
        def fake_image_generation_tool(prompt: str) -> Image.Image:
            """Tool that generates an image.

            Args:
                prompt: The prompt
            """
            return Image.open(Path(get_tests_dir("fixtures")) / "000000039769.png")

        agent = ToolCallingAgent(
            tools=[fake_image_generation_tool], model=FakeToolCallModelImage()
        )
        output = agent.run("Make me an image.")
        assert isinstance(output, AgentImage)
        assert isinstance(agent.state["image.png"], Image.Image)

    def test_fake_code_agent(self):
        agent = CodeAgent(tools=[PythonInterpreterTool()], model=fake_code_model)
        output = agent.run("What is 2 multiplied by 3.6452?")
        assert isinstance(output, float)
        assert output == 7.2904
        assert agent.logs[1].task == "What is 2 multiplied by 3.6452?"
        assert agent.logs[3].tool_calls == [
            ToolCall(
                name="python_interpreter", arguments="final_answer(7.2904)", id="call_3"
            )
        ]

    def test_additional_args_added_to_task(self):
        agent = CodeAgent(tools=[], model=fake_code_model)
        agent.run(
            "What is 2 multiplied by 3.6452?",
            additional_args={"instruction": "Remember this."},
        )
        assert "Remember this" in agent.task
        assert "Remember this" in str(agent.input_messages)

    def test_reset_conversations(self):
        agent = CodeAgent(tools=[PythonInterpreterTool()], model=fake_code_model)
        output = agent.run("What is 2 multiplied by 3.6452?", reset=True)
        assert output == 7.2904
        assert len(agent.logs) == 4

        output = agent.run("What is 2 multiplied by 3.6452?", reset=False)
        assert output == 7.2904
        assert len(agent.logs) == 6

        output = agent.run("What is 2 multiplied by 3.6452?", reset=True)
        assert output == 7.2904
        assert len(agent.logs) == 4

    def test_code_agent_code_errors_show_offending_lines(self):
        agent = CodeAgent(tools=[PythonInterpreterTool()], model=fake_code_model_error)
        output = agent.run("What is 2 multiplied by 3.6452?")
        assert isinstance(output, AgentText)
        assert output == "got an error"
        assert "Code execution failed at line 'print = 2' because of" in str(agent.logs)

    def test_code_agent_syntax_error_show_offending_lines(self):
        agent = CodeAgent(
            tools=[PythonInterpreterTool()], model=fake_code_model_syntax_error
        )
        output = agent.run("What is 2 multiplied by 3.6452?")
        assert isinstance(output, AgentText)
        assert output == "got an error"
        assert '    print("Failing due to unexpected indent")' in str(agent.logs)

    def test_setup_agent_with_empty_toolbox(self):
        ToolCallingAgent(model=FakeToolCallModel(), tools=[])

    def test_fails_max_steps(self):
        agent = CodeAgent(
            tools=[PythonInterpreterTool()],
            model=fake_code_model_no_return,  # use this callable because it never ends
            max_steps=5,
        )
        answer = agent.run("What is 2 multiplied by 3.6452?")
        assert len(agent.logs) == 8
        assert type(agent.logs[-1].error) is AgentMaxStepsError
        assert isinstance(answer, str)

    def test_tool_descriptions_get_baked_in_system_prompt(self):
        tool = PythonInterpreterTool()
        tool.name = "fake_tool_name"
        tool.description = "fake_tool_description"
        agent = CodeAgent(tools=[tool], model=fake_code_model)
        agent.run("Empty task")
        assert tool.name in agent.system_prompt
        assert tool.description in agent.system_prompt

    def test_init_agent_with_different_toolsets(self):
        toolset_1 = []
        agent = CodeAgent(tools=toolset_1, model=fake_code_model)
        assert (
            len(agent.tools) == 1
        )  # when no tools are provided, only the final_answer tool is added by default

        toolset_2 = [PythonInterpreterTool(), PythonInterpreterTool()]
        agent = CodeAgent(tools=toolset_2, model=fake_code_model)
        assert (
            len(agent.tools) == 2
        )  # deduplication of tools, so only one python_interpreter tool is added in addition to final_answer

        # check that python_interpreter base tool does not get added to CodeAgent
        agent = CodeAgent(tools=[], model=fake_code_model, add_base_tools=True)
        assert len(agent.tools) == 3  # added final_answer tool + search + visit_webpage

        # check that python_interpreter base tool gets added to ToolCallingAgent
        agent = ToolCallingAgent(tools=[], model=fake_code_model, add_base_tools=True)
        assert len(agent.tools) == 4  # added final_answer tool + search + visit_webpage

    def test_function_persistence_across_steps(self):
        agent = CodeAgent(
            tools=[],
            model=fake_code_functiondef,
            max_steps=2,
            additional_authorized_imports=["numpy"],
        )
        res = agent.run("ok")
        assert res[0] == 0.5

    def test_init_managed_agent(self):
        agent = CodeAgent(tools=[], model=fake_code_functiondef)
        managed_agent = ManagedAgent(agent, name="managed_agent", description="Empty")
        assert managed_agent.name == "managed_agent"
        assert managed_agent.description == "Empty"

    def test_agent_description_gets_correctly_inserted_in_system_prompt(self):
        agent = CodeAgent(tools=[], model=fake_code_functiondef)
        managed_agent = ManagedAgent(agent, name="managed_agent", description="Empty")
        manager_agent = CodeAgent(
            tools=[],
            model=fake_code_functiondef,
            managed_agents=[managed_agent],
        )
        assert "You can also give requests to team members." not in agent.system_prompt
        print("ok1")
        assert "{{managed_agents_descriptions}}" not in agent.system_prompt
        assert (
            "You can also give requests to team members." in manager_agent.system_prompt
        )

    def test_code_agent_missing_import_triggers_advice_in_error_log(self):
        agent = CodeAgent(tools=[], model=fake_code_model_import)

        from smolagents.agents import console

        with console.capture() as capture:
            agent.run("Count to 3")
        str_output = capture.get()
        assert "import under `additional_authorized_imports`" in str_output

    def test_multiagents(self):
        class FakeModelMultiagentsManagerAgent:
            def __call__(
                self,
                messages,
                stop_sequences=None,
                grammar=None,
                tools_to_call_from=None,
            ):
                if tools_to_call_from is not None:
                    if len(messages) < 3:
                        return ChatMessage(
                            role="assistant",
                            content="",
                            tool_calls=[
                                ChatMessageToolCall(
                                    id="call_0",
                                    type="function",
                                    function=ChatMessageToolCallDefinition(
                                        name="search_agent",
                                        arguments="Who is the current US president?",
                                    ),
                                )
                            ],
                        )
                    else:
                        assert "Report on the current US president" in str(messages)
                        return ChatMessage(
                            role="assistant",
                            content="",
                            tool_calls=[
                                ChatMessageToolCall(
                                    id="call_0",
                                    type="function",
                                    function=ChatMessageToolCallDefinition(
                                        name="final_answer", arguments="Final report."
                                    ),
                                )
                            ],
                        )
                else:
                    if len(messages) < 3:
                        return ChatMessage(
                            role="assistant",
                            content="""
Thought: Let's call our search agent.
Code:
```py
result = search_agent("Who is the current US president?")
```<end_code>
""",
                        )
                    else:
                        assert "Report on the current US president" in str(messages)
                        return ChatMessage(
                            role="assistant",
                            content="""
Thought: Let's return the report.
Code:
```py
final_answer("Final report.")
```<end_code>
""",
                        )

        manager_model = FakeModelMultiagentsManagerAgent()


*Content truncated for brevity.*

```

## File: tests/test_default_tools.py

<a name='file-tests-test_default_tools.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import pytest

from smolagents.default_tools import PythonInterpreterTool, VisitWebpageTool
from smolagents.types import AGENT_TYPE_MAPPING

from .test_tools import ToolTesterMixin


class DefaultToolTests(unittest.TestCase):
    def test_visit_webpage(self):
        arguments = {
            "url": "https://en.wikipedia.org/wiki/United_States_Secretary_of_Homeland_Security"
        }
        result = VisitWebpageTool()(arguments)
        assert isinstance(result, str)
        assert (
            "* [About Wikipedia](/wiki/Wikipedia:About)" in result
        )  # Proper wikipedia pages have an About


class PythonInterpreterToolTester(unittest.TestCase, ToolTesterMixin):
    def setUp(self):
        self.tool = PythonInterpreterTool(authorized_imports=["numpy"])
        self.tool.setup()

    def test_exact_match_arg(self):
        result = self.tool("(2 / 2) * 4")
        self.assertEqual(result, "Stdout:\n\nOutput: 4.0")

    def test_exact_match_kwarg(self):
        result = self.tool(code="(2 / 2) * 4")
        self.assertEqual(result, "Stdout:\n\nOutput: 4.0")

    def test_agent_type_output(self):
        inputs = ["2 * 2"]
        output = self.tool(*inputs, sanitize_inputs_outputs=True)
        output_type = AGENT_TYPE_MAPPING[self.tool.output_type]
        self.assertTrue(isinstance(output, output_type))

    def test_agent_types_inputs(self):
        inputs = ["2 * 2"]
        _inputs = []

        for _input, expected_input in zip(inputs, self.tool.inputs.values()):
            input_type = expected_input["type"]
            if isinstance(input_type, list):
                _inputs.append(
                    [
                        AGENT_TYPE_MAPPING[_input_type](_input)
                        for _input_type in input_type
                    ]
                )
            else:
                _inputs.append(AGENT_TYPE_MAPPING[input_type](_input))

        # Should not raise an error
        output = self.tool(*inputs, sanitize_inputs_outputs=True)
        output_type = AGENT_TYPE_MAPPING[self.tool.output_type]
        self.assertTrue(isinstance(output, output_type))

    def test_imports_work(self):
        result = self.tool("import numpy as np")
        assert "import from numpy is not allowed" not in result.lower()

    def test_unauthorized_imports_fail(self):
        with pytest.raises(Exception) as e:
            self.tool("import sympy as sp")
        assert "sympy" in str(e).lower()

```

## File: tests/test_types.py

<a name='file-tests-test_types.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import tempfile
import unittest
import uuid
from pathlib import Path

from PIL import Image
from transformers.testing_utils import (
    require_soundfile,
    require_torch,
    require_vision,
)
from transformers.utils.import_utils import (
    _is_package_available,
)

from smolagents.types import AgentAudio, AgentImage, AgentText

if _is_package_available("soundfile"):
    import soundfile as sf


def get_new_path(suffix="") -> str:
    directory = tempfile.mkdtemp()
    return os.path.join(directory, str(uuid.uuid4()) + suffix)


@require_soundfile
@require_torch
class AgentAudioTests(unittest.TestCase):
    def test_from_tensor(self):
        import torch

        tensor = torch.rand(12, dtype=torch.float64) - 0.5
        agent_type = AgentAudio(tensor)
        path = str(agent_type.to_string())

        # Ensure that the tensor and the agent_type's tensor are the same
        self.assertTrue(torch.allclose(tensor, agent_type.to_raw(), atol=1e-4))

        del agent_type

        # Ensure the path remains even after the object deletion
        self.assertTrue(os.path.exists(path))

        # Ensure that the file contains the same value as the original tensor
        new_tensor, _ = sf.read(path)
        self.assertTrue(torch.allclose(tensor, torch.tensor(new_tensor), atol=1e-4))

    def test_from_string(self):
        import torch

        tensor = torch.rand(12, dtype=torch.float64) - 0.5
        path = get_new_path(suffix=".wav")
        sf.write(path, tensor, 16000)

        agent_type = AgentAudio(path)

        self.assertTrue(torch.allclose(tensor, agent_type.to_raw(), atol=1e-4))
        self.assertEqual(agent_type.to_string(), path)


@require_vision
@require_torch
class AgentImageTests(unittest.TestCase):
    def test_from_tensor(self):
        import torch

        tensor = torch.randint(0, 256, (64, 64, 3))
        agent_type = AgentImage(tensor)
        path = str(agent_type.to_string())

        # Ensure that the tensor and the agent_type's tensor are the same
        self.assertTrue(torch.allclose(tensor, agent_type._tensor, atol=1e-4))

        self.assertIsInstance(agent_type.to_raw(), Image.Image)

        # Ensure the path remains even after the object deletion
        del agent_type
        self.assertTrue(os.path.exists(path))

    def test_from_string(self):
        path = Path("tests/fixtures/000000039769.png")
        image = Image.open(path)
        agent_type = AgentImage(path)

        self.assertTrue(path.samefile(agent_type.to_string()))
        self.assertTrue(image == agent_type.to_raw())

        # Ensure the path remains even after the object deletion
        del agent_type
        self.assertTrue(os.path.exists(path))

    def test_from_image(self):
        path = Path("tests/fixtures/000000039769.png")
        image = Image.open(path)
        agent_type = AgentImage(image)

        self.assertFalse(path.samefile(agent_type.to_string()))
        self.assertTrue(image == agent_type.to_raw())

        # Ensure the path remains even after the object deletion
        del agent_type
        self.assertTrue(os.path.exists(path))


class AgentTextTests(unittest.TestCase):
    def test_from_string(self):
        string = "Hey!"
        agent_type = AgentText(string)

        self.assertEqual(string, agent_type.to_string())
        self.assertEqual(string, agent_type.to_raw())
        self.assertEqual(string, agent_type)

```

## File: tests/test_models.py

<a name='file-tests-test_models.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
from typing import Optional

from smolagents import models, tool


class ModelTests(unittest.TestCase):
    def test_get_json_schema_has_nullable_args(self):
        @tool
        def get_weather(location: str, celsius: Optional[bool] = False) -> str:
            """
            Get weather in the next days at given location.
            Secretly this tool does not care about the location, it hates the weather everywhere.

            Args:
                location: the location
                celsius: the temperature type
            """
            return "The weather is UNGODLY with torrential rains and temperatures below -10°C"

        assert (
            "nullable"
            in models.get_json_schema(get_weather)["function"]["parameters"][
                "properties"
            ]["celsius"]
        )

```

## File: tests/test_search.py

<a name='file-tests-test_search.py'></a>
*Description*: This is a Python script.

```python
# coding=utf-8
# Copyright 2024 HuggingFace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from smolagents import DuckDuckGoSearchTool

from .test_tools import ToolTesterMixin


class DuckDuckGoSearchToolTester(unittest.TestCase, ToolTesterMixin):
    def setUp(self):
        self.tool = DuckDuckGoSearchTool()
        self.tool.setup()

    def test_exact_match_arg(self):
        result = self.tool("Agents")
        assert isinstance(result, str)

```

## File: tests/fixtures/000000039769.png

<a name='file-tests-fixtures-000000039769.png'></a>
*Description*: No specific description available.

*This file is binary and cannot be displayed as text.*
