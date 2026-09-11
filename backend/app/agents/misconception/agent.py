from pydantic import BaseModel


class MisconceptionResult(BaseModel):
    has_misconception: bool
    misconception: str
    explanation: str


def detect_misconception(
    analysis: dict,
) -> MisconceptionResult:

    main_issue = analysis.get("main_issue", "").strip()

    if not main_issue or main_issue.lower() in {
        "none",
        "no issue",
        "no bug",
    }:
        return MisconceptionResult(
            has_misconception=False,
            misconception="",
            explanation="No clear misconception detected.",
        )

    return MisconceptionResult(
        has_misconception=True,
        misconception=main_issue,
        explanation=(
            "The student's main issue may indicate a gap "
            "in understanding the underlying DSA concept."
        ),
    )