import ollama
from backend.app.rag.search import search_kb
from backend.app.tools import get_asset_info

def ask_aura(user_question: str) -> str:
    # 1. RAG Context
    context_chunks = search_kb(user_question)
    context_text = "\n\n".join([chunk["text"] for chunk in context_chunks])
    
    system_prompt = f"""You are AURA, an AI IT Service Desk Agent. 
    You have access to tools to look up real-time database information.
    Use the provided context for general troubleshooting.
    
    Context:
    {context_text}
    """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_question}
    ]
    
    # 2. First Pass: Ask the LLM, giving it the tool as an option
    response = ollama.chat(
        model="qwen3:1.7b-q4_K_M",
        messages=messages,
        tools=[get_asset_info]  # Ollama magically reads your function's docstring and types!
    )
    
    # 3. The Orchestration Loop: Did the LLM decide to use a tool?
    if response['message'].get('tool_calls'):
        for tool in response['message']['tool_calls']:
            if tool['function']['name'] == 'get_asset_info':
                # Extract the asset tag the LLM identified from the user's question
                asset_tag = tool['function']['arguments'].get('asset_tag')
                
                # Run our Python function to query PostgreSQL
                tool_result = get_asset_info(asset_tag)
                
                # Add the LLM's tool request and our database result to the chat history
                messages.append(response['message'])
                messages.append({
                    "role": "tool",
                    "content": str(tool_result),
                    "name": tool['function']['name']
                })
        
        # 4. Second Pass: Let the LLM read the database result and write a final answer
        final_response = ollama.chat(
            model="qwen3:1.7b-q4_K_M",
            messages=messages
        )
        return final_response['message']['content']
    
    # 5. If no tools were needed, just return the standard text response
    return response['message']['content']