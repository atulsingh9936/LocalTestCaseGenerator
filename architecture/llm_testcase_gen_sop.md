# SOP: Local LLM Testcase Generator

## 1. Goal
Generate structured software test cases from informal user input using a local Ollama instance (model: llama3.2).

## 2. Inputs
- `userInput`: Informal description of a feature or bug.
- `internalTemplate`: A system-level prompt that guides the LLM to output valid JSON.

## 3. Tool Logic (Deterministic)
### 3.1 Prompt Interpolation
The tool must wrap the `userInput` into the following template:
```text
System: You are an expert QA Engineer. Generate a structured set of test cases for the following feature. 
Output ONLY valid JSON matching this schema: 
{"test_cases": [{"title": "...", "priority": "...", "steps": ["..."], "expectedResult": "..."}]}

User Input: {userInput}
```

### 3.2 Ollama API Call
- **Endpoint**: `ollama.chat` (via `ollama-python` library).
- **Model**: `llama3.2:1b` (or latest available).
- **Format**: `json` (to ensure the model respects the schema).

### 3.3 Post-Processing
- Validate that the output is valid JSON.
- If JSON parsing fails, return a "Healing" prompt to the LLM or an error to the UI.

## 4. Edge Cases
- **Empty Input**: Return an "Input cannot be empty" message.
- **Garbage Input**: Handle cases where the LLM cannot identify any features (return "No test cases could be generated").
- **LLM Timeout**: Implement a timeout for local execution to prevent UI hang.

## 5. UI Requirements (Layer 1 Aesthetics)
- **Glassmorphism**: Backdrop blur (16px), semi-transparent gradients, thin white borders.
- **Micro-animations**: Loading Spinner during generate, smooth entry for cards.
