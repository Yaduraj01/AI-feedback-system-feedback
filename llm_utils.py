import requests

# ⭐ MANUALLY PASTE YOUR API KEY HERE ⭐
API_KEY = "enter your key here"

MODEL = "mistralai/ministral-14b-2512"
URL = "https://openrouter.ai/api/v1/chat/completions"


def call_llm(prompt: str) -> str:
    """
    Calls the LLM and returns the response text.
    Works with OpenRouter free tier models.
    """

    # ⭐ FIX: Only check if empty, not if it matches anything
    if not API_KEY or API_KEY.strip() == "":
        return "API key is not set. Please update API_KEY in llm_utils.py"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
        "max_tokens": 200,
    }

    try:
        response = requests.post(URL, json=payload, headers=headers, timeout=20)
        response.raise_for_status()

        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"LLM Error: {str(e)}"
