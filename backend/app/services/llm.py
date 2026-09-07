from ollama import chat

MODEL = "qwen3:1.7b-q4_K_M"

SYSTEM = """
You are AURA, an enterprise IT service desk assistant.
Rules:
1. Never invent ticket, asset, metric, policy, or knowledge-base facts.
2. For knowledge answers, use supplied evidence and cite the source filenames.
3. Tools are authoritative for live system state.
4. Never execute high-impact actions without an explicit human approval record.
5. If uncertain, ask a focused question or escalate to a human.
6. Keep answers concise and operationally useful.
"""

def ask(messages: list[dict]):
    """Send a conversation history to Ollama with the AURA system prompt."""
    response = chat(
        model=MODEL,
        messages=[{"role": "system", "content": SYSTEM}] + messages,
        options={"temperature": 0.1, "num_ctx": 4096},
    )
    return response.message
