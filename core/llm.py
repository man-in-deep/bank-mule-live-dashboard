import os
import requests

API_URL = os.getenv("LLM_API_URL")
API_KEY = os.getenv("LLM_API_KEY")

def explain_mule(account, mule_info):
    if not API_URL or not API_KEY:
        return "LLM not configured."

    prompt = f"""
You are a senior bank AML compliance officer.

Account: {account}
Mule Score: {mule_info['mule_score']}
Triggered Scenarios: {', '.join(mule_info['scenarios'])}

Explain clearly:
1. Why this account is suspected as a mule
2. What risk it poses to the bank
3. Recommended compliance action
"""

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    r = requests.post(API_URL, headers=headers, json=payload, timeout=30)

    if r.status_code != 200:
        return "LLM request failed."

    return r.json()["choices"][0]["message"]["content"]