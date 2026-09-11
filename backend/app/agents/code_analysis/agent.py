from app.ai.hf_client import client


MODEL ="Qwen/Qwen3-Next-80B-A3B-Instruct"


async def analyze_code(
    problem: str,
    code: str,
    language: str,
) -> str:

    prompt = f"""
You are an expert DSA coding tutor.

Analyze this student's solution.

Problem:
{problem}

Language:
{language}

Student Code:
{code}

Give:
1. Correctness
2. Time complexity
3. Space complexity
4. Main issue or bug
5. DSA concept involved
6. One short hint

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

    return response.choices[0].message.content