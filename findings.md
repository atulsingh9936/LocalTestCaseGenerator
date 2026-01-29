# Findings & Research

## Project Context
- **Goal**: Create a local LLM Testcase generator using Ollama.
- **Protocol**: BLAST (Blueprint, Link, Architect, Stylize, Trigger).

## Research Results
- **Ollama API**: Provides a REST API for model interaction (chat, generate, embeddings).
- **Client Libraries**: Official libraries exist for Python (`ollama-python`) and JavaScript (`ollama-js`).
- **Core Functionality**: Supports generating code/text based on prompts, which can be used to produce test scripts.
- **Testing Frameworks**: Can be integrated with `pytest` (Python) or `Mocha`/`Jest` (JavaScript).

## Constraints
- Must use Ollama.
- Must follow BLAST Protocol.
- Local execution only.

## Research Results
- **Ollama API**: Supports `/api/generate` and `/api/chat` endpoints. Local server usually runs at `http://localhost:11434`.
- **Model**: `llama3.2` is the target model (3B parameters version is excellent for local speed).
- **Client Libraries**: Official `ollama` (Python) and `ollama-js` (JavaScript) libraries are available.
- **Test Case Generation**: Can be achieved by providing structural templates to the LLM to ensure consistency.

## Research Results
- **Ollama API**: Local REST server at `http://localhost:11434`.
- **Model**: `llama3.2` is the target model.
- **Library**: `ollama` (Python library) as requested.
- **UI Architecture**: Python-based web framework (FastAPI/Flask) with a custom premium HTML/CSS frontend.

## Unresolved Questions / Discovery - RESOLVED
- **North Star:** Local LLM Testcase generator using Ollama (llama3.2) with a Chat UI.
- **Integrations:** Ollama (Local API via Python library).
- **Source of Truth:** Real-time user input via Chat.
- **Delivery Payload:** Premium UI Chat interface (Glassmorphism).
- **Behavioral Rules:** User Input -> System Prompt Template -> Ollama-Python -> Response.
- **The Prompt:** [Awaiting user input - to be stored in code logic].
