from backend.app.services.llm import ask

def answer_from_context(question: str, hits: list[dict]) -> str:
    """Generate a grounded answer strictly using evidence retrieved from RAG."""
    context = "\n\n".join(
        f"SOURCE: {h['source']}\n{h['text']}" for h in hits
    )
    prompt = f"""
Question: {question}

Evidence:
{context}

Answer using only the evidence. Cite the source filename(s).
If evidence is insufficient, say so and recommend human escalation.
"""
    return ask([{"role": "user", "content": prompt}]).content
