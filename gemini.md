# Project Constitution (gemini.md)

## 1. Data Schemas

### Input (User Message)
```json
{
  "userInput": "string",
  "config": {
    "model": "llama3.2",
    "template": "v1"
  }
}
```

### Output (Ollama JSON Response)
```json
{
  "test_cases": [
    {
      "id": "string",
      "title": "string",
      "preconditions": "string",
      "steps": ["string"],
      "expectedResult": "string",
      "priority": "High|Medium|Low"
    }
  ]
}
```

## 2. Behavioral Rules
- **Protocol**: Follow B.L.A.S.T. strictly.
- **Reliability**: Prioritize reliability over speed. All LLM calls must use fixed system templates.
- **Parsing**: All LLM outputs must be validated against the JSON schema before delivery.
- **Tools**: No scripts in `tools/` until SOP is approved.

## 3. Architectural Invariants
- **Model**: Local Ollama instance (`llama3.2:1b`).
- **Framework**: FastAPI (Backend) + Vanilla HTML/CSS/JS (Frontend).
- **Architecture**: A.N.T. (Application, Network, Tooling).
- **Prompt Template**:
  ```text
  You are a professional QA automation engineer. Convert the user input into a rigorous set of test cases.
  Output the result in JSON format ONLY using the structure defined in the provided schema.
  User Input: {userInput}
  ```
