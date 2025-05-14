# Building Coding Agents

General design of a coding agent:

```
   .-------.         .-----.
   | Agent | <--+--> | LLM | Architect
   `-------'    |    `-----'
    - tools     |    .-----.
    - chat logs `--> | LLM | Editor (search/replace generator)
                     `-----'
```

There are some strategies to implement the editing part of coding agents:

- Use native tools support on LLMs and expose functions like `read_file`, `edit_file`, ...
    - Pros:
        - Leverage tool handling (fine tuned LLM, input/output parsing, etc) by
          each LLM provider
        - Simplify your agent code
        - 
    - Cons:
        - Dependent on LLM provider
        - Some LLMs do not support tools yet, or are still error
          prone/experimental (eg DeepSeek)
        - It can get expensive given more cheap models like DeepSeek are not
          available, only the ones that support tools like Claude Sonnet or
          OpenAI's LLM family
- Use blocks of search/replace changes
    - Pros:
        - Work on any LLM (strategy followed by Aider, for instance)
    - Cons:
        - Not flexible, limit the operations to be only search/replace
          back-and-forth
        - Requires user to explicitly add files to context window
- Use a "hack" to inject tools into LLMs that doesn't support it
    - Pros:
        - Makes it possible to use any function/REST API/MCP as a tool
        - Possible to use cheaper models like DeepSeek
    - Cons:
        - Experimental, error prone

At same time, there are also some strategies on how to organize an agent to be
able to do efficient coding:

- Only one code writer/editor, usually with tools
- One architect LLM and one independent writer LLM: the architect understands
  the global picture (ie all source files, requirements, etc) and asks for a
  writer LLM to iterate over each file that requires changes and suggest
  search/replace blocks that "answers" the user request

We're going to implement each one in the following sections.

# Setup

Before we move along, let's setup a Python env so you can run your agents:

```bash
git clone git@github.com:automata/aicodeguide.git
cd aicodeguide/building-coding-agents
python3 -m venv .venv             # or uv venv
source .venv/bin/activate
pip install -r requirements.txt   # or uv pip install -r requirements.txt
```

# References

- [Agents](https://huyenchip.com/2025/01/07/agents.html) by Chip Huyen: it
  presents a general design for what we see as modern agents
