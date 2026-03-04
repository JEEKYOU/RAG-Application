import ollama
from retriever import retrieve
from config import LLM_MODEL, SYSTEM_PROMPT

def answer(query):
    context_chunks = retrieve(query)
    context = "\n\n".join(context_chunks)

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"""
Context:
{context}

Question:
{query}
"""
            }
        ]
    )

    return response["message"]["content"]

if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or type 'exit'): ")
        if q.lower() == "exit":
            break

        print("\nAnswer:\n")
        print(answer(q))
