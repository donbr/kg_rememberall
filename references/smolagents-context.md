# Combined Context for LLM

Source Directory: ../data/raw/smolagents
Generated On: 2025-01-14 14:59:11

## Table of Contents

- [Combined Context for LLM](#combined-context-for-llm)
  - [Table of Contents](#table-of-contents)
  - [File: e2b.Dockerfile](#file-e2bdockerfile)
  - [File: pyproject.toml](#file-pyprojecttoml)
  - [File: README.md](#file-readmemd)
  - [Code agents?](#code-agents)
  - [How smol is it really?](#how-smol-is-it-really)
  - [How strong are open models for agentic workflows?](#how-strong-are-open-models-for-agentic-workflows)
  - [Citing smolagents](#citing-smolagents)
  - [File: LICENSE](#file-license)
  - [File: package-lock.json](#file-package-lockjson)
  - [File: CONTRIBUTING.md](#file-contributingmd)
  - [File: CODE\_OF\_CONDUCT.md](#file-code_of_conductmd)
  - [File: e2b.toml](#file-e2btoml)
  - [File: Dockerfile](#file-dockerfile)
  - [File: package.json](#file-packagejson)
  - [File: .pre-commit-config.yaml](#file-pre-commit-configyaml)
  - [File: examples/tool\_calling\_agent\_ollama.py](#file-examplestool_calling_agent_ollamapy)
  - [File: examples/benchmark.py](#file-examplesbenchmarkpy)
  - [File: examples/e2b\_example.py](#file-examplese2b_examplepy)
  - [File: examples/gradio\_upload.py](#file-examplesgradio_uploadpy)
  - [File: examples/text\_to\_sql.py](#file-examplestext_to_sqlpy)
  - [File: examples/rag.py](#file-examplesragpy)
  - [File: examples/tool\_calling\_agent\_from\_any\_llm.py](#file-examplestool_calling_agent_from_any_llmpy)
  - [File: docs/source/en/guided\_tour.md](#file-docssourceenguided_tourmd)
      - [CodeAgent and ToolCallingAgent](#codeagent-and-toolcallingagent)
    - [Inspecting an agent run](#inspecting-an-agent-run)
  - [Tools](#tools)
    - [Default toolbox](#default-toolbox)
    - [Create a new tool](#create-a-new-tool)
  - [Multi-agents](#multi-agents)
  - [Talk with your agent and visualize its thoughts in a cool Gradio interface](#talk-with-your-agent-and-visualize-its-thoughts-in-a-cool-gradio-interface)
  - [Next steps](#next-steps)
  - [File: docs/source/en/index.md](#file-docssourceenindexmd)
  - [File: docs/source/en/reference/tools.md](#file-docssourceenreferencetoolsmd)
  - [File: docs/source/en/reference/agents.md](#file-docssourceenreferenceagentsmd)
    - [TransformersModel](#transformersmodel)
    - [HfApiModel](#hfapimodel)
    - [LiteLLMModel](#litellmmodel)
  - [File: docs/source/en/conceptual\_guides/intro\_agents.md](#file-docssourceenconceptual_guidesintro_agentsmd)
  - [✅ When to use agents / ⛔ when to avoid them](#when-to-use-agents--when-to-avoid-them)
  - [Why `smolagents`?](#why-smolagents)
  - [Code agents](#code-agents-1)
    - [Build our agent](#build-our-agent)
    - [Level 2: Table joins](#level-2-table-joins)
  - [🔍 Create a web search tool](#-create-a-web-search-tool)
  - [Build our multi-agent system 🤖🤝🤖](#build-our-multi-agent-system-)
    - [Share your tool to the Hub](#share-your-tool-to-the-hub)
    - [Import a Space as a tool](#import-a-space-as-a-tool)
    - [Use LangChain tools](#use-langchain-tools)
    - [Manage your agent's toolbox](#manage-your-agents-toolbox)
    - [Use a collection of tools](#use-a-collection-of-tools)
    - [Give more arguments to the agent](#give-more-arguments-to-the-agent)
  - [How to debug your agent](#how-to-debug-your-agent)
    - [1. Use a stronger LLM](#1-use-a-stronger-llm)
    - [2. Provide more guidance / more information](#2-provide-more-guidance--more-information)
    - [3. Change the system prompt (generally not advised)](#3-change-the-system-prompt-generally-not-advised)
    - [4. Extra planning](#4-extra-planning)

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
