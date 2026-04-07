from llm.bedrock_llm import call_bedrock
from agent.tools import pdf_search
from agent.memory import add_to_memory, get_memory


def agent_decision(query):
    prompt = f"""
You are an AI agent.

Decide whether to use a tool.

Available tools:
1. PDF_SEARCH

Rules:
- If question is about document → say: TOOL: PDF_SEARCH
- Otherwise → say: DIRECT

Question: {query}
"""

    return call_bedrock(prompt)


def generate_answer(query, context):
    memory = get_memory()

    prompt = f"""
You are a helpful AI assistant.

Conversation history:
{memory}

Context:
{context}

Question:
{query}

Answer clearly:
"""

    return call_bedrock(prompt)


def ask_agent(query):
    try:
        decision = agent_decision(query)

        if "PDF_SEARCH" in decision:
            context = pdf_search(query)
        else:
            context = ""

        answer = generate_answer(query, context)

        add_to_memory(query, answer)

        return answer

    except Exception as e:
        return f"Agent error: {str(e)}"