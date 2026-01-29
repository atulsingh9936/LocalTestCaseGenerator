import ollama
import json

def test_ollama_connection():
    print("Testing Ollama Connection...")
    try:
        # List models to see what we have
        models = ollama.list()
        print(f"Raw models data structure: {type(models)}")
        # Inspecting the list of models
        model_list = getattr(models, 'models', models)
        if hasattr(model_list, '__iter__'):
            model_names = []
            for m in model_list:
                # Handle both dict and object types
                if hasattr(m, 'model'):
                    name = m.model
                elif isinstance(m, dict) and 'name' in m:
                    name = m['name']
                elif isinstance(m, dict) and 'model' in m:
                    name = m['model']
                else:
                    name = str(m)
                model_names.append(name)
        else:
            model_names = []
            
        print("Available Models:")
        for name in model_names:
            print(f" - {name}")
        
        target_model = "llama3.2:1b"
        if target_model not in model_names:
             # Fallback to check if name without tag exists or pick first
             if "llama3.2:latest" in model_names:
                 target_model = "llama3.2:latest"
             elif model_names:
                 target_model = model_names[0]
                 print(f"Target model not found, falling back to: {target_model}")
             else:
                 print("No models found!")
                 return

        print(f"Ping model '{target_model}'...")
        response = ollama.chat(model=target_model, messages=[
            {'role': 'user', 'content': 'Say hello and confirm you are ready.'}
        ])
        
        if response and 'message' in response:
            print(f"Success! Model response: {response['message']['content']}")
        else:
            print("Failed! Received invalid response format.")
            
    except Exception as e:
        print(f"Error connecting to Ollama: {str(e)}")

if __name__ == "__main__":
    test_ollama_connection()
