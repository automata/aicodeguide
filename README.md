<div align="center">
<img src="https://i.imgur.com/ufmNDoc.png" alt="AI Code Guide">
  <p align="center">
    𝕏 <a href="https://x.com/aut0mata">Follow me on X</a> • 
    🤗 <a href="https://void.cc">My personal website</a> • 
    💻 <a href="https://github.com/automata">My GitHub</a>
  </p>
</div>
<br/>

Everything you wanted to know about using AI to code.

## Introduction

It's April, I just arrived in Munich -- I live in London but I'm here for a
work trip -- and I decided to open my laptop, pop a Club Mate and dump
everything I have been researching and implementing around AI to help on
code generation..

I really love coding, I do. I'm doing that for a living during the past 15
years as both a SWE and AI/ML Engineer. I love computers, to build them, break
them in parts, understand their fundamentals and everything around it. And
because of that I love to spend time reading about it, studying it, hacking
it...

All that is to say that I've been following hypes and trends for a long time
and the way we interact with computers and code them is
changing. And it's a profound change. It's a change on the tools we use, the
way we code and think about software products and systems.

And it's changing super fast! New LLM models are being released every week. New
tools, new editors, new "vibe coding" practices, new protocols (MCP, A2A, SLOP,
...)... and it's really hard to keep track of all that. Everything is
scattered in different places, websites, repos, etc.

That's why I decided to
write this guide. It's my humble attempt to put everything together and present
you the practices and tools around AI coding or AI code generation, all in one
place, with no fluf, in an accessible way.

But wait, is this guide for me? Let's see:

- If you're a coder/dev/SWE/MLE who already know how to code but is not using
  AI code assistants yet. Yep, this guide is for you: it introduces all most
  recent tools and practices to make the most of them to help on your daily
  jobs
- If you never coded before but you're interested in this new "vibe coding"
  thing to build your own SaaS and other software products. This guide is
  definetely for you: I'll try to do my best to remove obscurity and leave you
  only what's required to start your journey, but being super critic about what
  is really important and what's "just hype" (tm)

Let's start!

# AI coding? Vibe coding?

All those terms are pretty similar. But basically AI coding is about using AI
models (specially LLMs these days) and all the tooling around it to help you
write software. It's also called "AI for code generation" or "code gen" for
short, and there's an entire fascinating field of research and engineering,
that dates back to 1950's when we used Lisp to generate code. Now we have LLMs
as main engines to power code generation, and there's also some threads on
neurosymbolic hybrid approaches starting to show up. And AI coding is also a
practice: if you're using Cursor and tab-tab-tab your way to get completions,
you're "AI coding"; if you're full on using Cursor agent mode, you're also "AI
coding". In summary: it's any way to use an AI models to help you to generate
code. Generally you have coders in this group.

Vibe coding is AI coding cranked up :-) Here you don't care much about the code
being generated, you just give a prompt and expect the AI to code everything
for you. The term was creaetd by Karpathy in 2024 and it's getting pretty
popular. IMHO it's helping to democratize coding for everyone that never
thought about coding before!

So, in summary, no matter if you're using AI to discuss your software ideas or
to help on coding only parts of your already existing code base, or if you're
full on vibe coding, you're using AI to help you generate code. Let's call it
AI coding and move on.

## What's AI and LLM?

If you know what's all about, please move on for the next section. Otherwise,
just a few words about our main guys here.

# The Roadmap

## How I start?

If you don't know how to code and want to play with it, I recommend starting
with some web-based tool like Bolt.new, Replit or Lovable.

If you already know how to code, install Cursor, Windsurf

If you already know how to code and is a terminal maniac like me, check aider.

Install those tools, some are free to use, some will ask you for a $20-ish
monthly plan (I pay for Cursor, for instance).

📚 Resources:

## How I prompt for coding?

After you installed, played with those tools a bit, you'll notice they will
hallucinate, enter in endless cycles of trying to

📚 Resources:

## How I avoid hallucinations?

PRD. What?! They say that the best ways to solve a problem in engineering is to
create a new achronym and here it's no exception :-) J/k... PRD is short for
Project Requirements Document. Basically, it's just a bunch of docs (or only
one doc) describing the requirements and other details about your software
project.

Turns out, if you leave your loved LLM free, with not much context of what to
do, it will hallucinate pretty wild and quick. You need to tame the beast and
PRDs are a great way to do it.

What I most like about PRDs is how they are super helpful to anyone, from
people who never coded before to senior SWE.

You don't need any background to start a PRD, you just need your idea for an
app and that's it.

To write a PRD, you can follow some strategies:

Strategy 1:

Open ChatGPT and copy-and-paste the following prompt:

...

Strategy 2:

In Cursor, ...

## How I deal with errors?

One thing you must know about coding and softwares in general: they will fail.
No matter what you try to prevent that, it will happen. So let's first embrace
that and be friends with errors and bugs.

The first strategy here is to mimic what SWE do: see what the
interpreter/compiler gave to you as an error message and try to understand it. 

## I want to learn more about all this code the AI is generating

That's great! I prepared some down the rabbit hole sessions here.

# Common Questions

- How to deal with hallucinations?
    - What's a PRD?
- Start from scratch or with a boilerplate?
- Greenfield/clean state/fresh project vs existing codebase
- What's the best tool?
- What I do with bugs? Debugging?
- How to deal with the fact that LLMs are "yes machines"?
  - More specific details, use different LLMs to confirm, be critic
- Do I need to understand programming? Computer and systems fundamentals?
- Specs/stdlib?
- Should I use TDD or any other type of tests?
- How to get structured data?

# Tools

Here I keep an updated list of main tools around using AI for coding. I tested
most of them and you'll find my honest opinion during the time I tested.

## Editors / IDE

- Cursor
- Cline
- Windsurf
- OpenHands

## CLI

- Claude Code
- Aider
- Claude Engineer
- Roo

## Webapps
 
- Bolt
- Replt
- Lovable

## Misc

- Task master
- CodeGuide
- repomix
-
# Roadmap

- Intro
    - [x] What's this guide about?
    - [x] AI coding? Vibe coding?
    - [] What's a LLM?
- Tools
    - Cursor
    - Cline
    - Windsurf
    - Bolt
    - Lovable
    - Repl
    - Sweep
    - Task master
    - CodeGuide
    - repomix
- Cursor rules
- PRD and specs/stdlib
    - Break into tasks
- Star your project
    - Web?
- MCP and SLOP
    - Best servers
    - Creating your own
- Debugging
- Make it safe
- And if my code already exists?
    - repomix, llmtxt and other ways to fit your code base into LLMs
    - go per task instead of per project!
- Going deeper the code gen rabbit hole... Let's build a code assistant ourselves!
    - Show lilcoder, different versions
- Going deeper the web dev rabbit hole
    - Explain how web works, webapps, etc
- Going deeper the LLM rabbit hole
    - CoT
    - RAG and CAG
    - LangChain and LangGraph, Autogen
    - Embeddings and vector databases: LlamaIndex, MongoDB Vector DB, Pinecone, ...
    - Validating outputs of LLMs: https://github.com/confident-ai/deepeval

# Who to follow

- geoff

# Refs

- llm-course
- https://www.deeplearning.ai/short-courses/vibe-coding-101-with-replit/
- awesome lists
- https://mcpslop.com/
- https://www.oreilly.com/radar/the-end-of-programming-as-we-know-it
- https://github.com/mongodb-developer/GenAI-Showcase

# Acknowledgements

This guide was inspired by the great [llm-course](https://github.com/milanm/DevOps-Roadmap) from Maxime Labonne.

Special thanks to:

* Gabriela Thumé for everything <3
