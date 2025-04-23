# Building Coding Agents

Existing strategies to build coding agents:

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

# 
