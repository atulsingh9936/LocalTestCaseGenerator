# Task Plan

## Phase 1: Blueprint & Discovery - COMPLETED
- [x] Initialize Project Memory (Protocol 0)
- [x] Gather Requirements & Discovery Answers
- [x] Define Data Schema in `gemini.md`
- [x] Create Approved Blueprint

### Approved Blueprint
- **Core Engine**: Python (FastAPI) for the backend bridge.
- **LLM Integration**: `ollama` (Python library) to a local Ollama instance running `llama3.2`.
- **UI Architecture**: Single-page Chat interface served by FastAPI, using Vanilla JS and CSS for a premium "Glassmorphism" look.
- **Prompt Strategy**: Internal Python-based system template for structured test cases.

## Phase 2: Architecture & Foundation - COMPLETED
- [x] Set up Python environment and install dependencies (`fastapi`, `uvicorn`, `ollama`).
- [x] Verified Ollama connectivity with handshake script.
- [ ] Create basic FastAPI server structure.
- [ ] Implement Ollama interaction utility using the Python library.

## Phase 3: Architect - IN PROGRESS
- [x] Create Technical SOP (`architecture/llm_testcase_gen_sop.md`).
- [ ] Define Navigation logic (FastAPI Router).
- [ ] Build Layer 3 Tools (Ollama wrapper).

## Phase 4: Implementation
- [ ] Build the Glassmorphism Chat frontend (HTML/CSS).
- [ ] Create API endpoint for chat processing.
- [ ] Integrate the stored Prompt Template.

## Phase 4: Verification & Polish
- [ ] Add smooth transitions and loading states.
- [ ] Final visual polish on the UI.
