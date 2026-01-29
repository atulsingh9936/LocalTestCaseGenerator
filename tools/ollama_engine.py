import ollama
import json

def generate_test_cases(user_input: str):
    """
    Deterministic tool to generate test cases using Ollama.
    Layer 3: Tool
    """
    model = "llama3.2:1b"
    
    system_prompt = (
        "You are a professional QA automation engineer. Convert the user input into a rigorous set of test cases.\n"
        "Output the result in JSON format ONLY. Do not include markdown blocks or any other text.\n"
        "CRITICAL: The 'steps' field must be an array of simple strings. DO NOT use objects inside the steps array.\n"
        "Structure: {\"test_cases\": [{\"title\": \"string\", \"priority\": \"High|Medium|Low\", \"steps\": [\"string\"], \"expected_result\": \"string\"}]}"
    )
    
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': user_input}
            ],
            format='json',
            options={'temperature': 0.2} # Low temperature for deterministic output
        )
        
        # Parse output
        content = response['message']['content']
        return json.loads(content)
        
    except Exception as e:
        return {"error": str(e), "raw": content if 'content' in locals() else None}

if __name__ == "__main__":
    # Quick test
    test_input = "Login button on the landing page"
    print(json.dumps(generate_test_cases(test_input), indent=2))
