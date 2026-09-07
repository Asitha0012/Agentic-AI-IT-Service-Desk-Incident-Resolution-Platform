import ollama
from backend.app.rag.search import search_kb

def ask_aura(user_question: str) -> str:
    # 1. Retrieve the relevant knowledge base chunks
    context_chunks = search_kb(user_question)
    
    # Combine the text from the chunks into a single string
    context_text = "\n\n".join([chunk["text"] for chunk in context_chunks])
    
    # 2. Build the strict prompt with guardrails
    system_prompt = f"""You are AURA, an AI IT Service Desk Agent. 
    Answer the user's question using ONLY the provided context. 
    If the context does not contain the answer, politely state that you do not have that information.
    
    Context:
    {context_text}
    """
    
    # 3. Ask the LLM to reason and respond
    response = ollama.chat(
        model="qwen3:1.7b-q4_K_M",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_question}
        ]
    )
    
    return response['message']['content']