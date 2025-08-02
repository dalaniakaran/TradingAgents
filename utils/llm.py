import requests

def query_ollama(prompt, model="llama3", system="You are a helpful analyst."):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "system": system,
        "temperature": 0.7,
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        print(f"Error: {e}")
        return ""
