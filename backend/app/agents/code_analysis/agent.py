import json

from app.ai.hf_client import client


MODEL = "Qwen/Qwen3-Next-80B-A3B-Instruct"


async def analyze_code(
    problem: str,
    code: str,
    language: str,
) -> dict:

    prompt = f"""
You are an expert DSA coding tutor.

Analyze this student's solution.

Problem:
{problem}

Language:
{language}

Student Code:
{code}

Return ONLY valid JSON in exactly this format:

{{
    "correctness": "...",
    "time_complexity": "...",
    "space_complexity": "...",
    "main_issue": "...",
    "dsa_concept": "...",
    "hint": "..."
}}

Do not provide the complete solution.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=300,
    )

    content = response.choices[0].message.content

    return json.loads(content)