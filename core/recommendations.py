from typing import Generator

import ollama

from backend.data import Client

SYSTEM_PROMPT = """You are an expert B2B sales strategist. Given a client profile, produce \
a recommendation in exactly three sections using these headers (include the ## prefix):

## Situation Summary
2-3 sentences. State where the deal stands, the key dynamic, and what makes this client \
urgent or important right now.

## Reasoning
3-5 bullet points (use "- " prefix). Explain WHY the recommended action is the right move: \
what signals from the client data support it, what risks it addresses, and what outcome it \
drives. Be specific — no generic sales advice.

## Outreach
First line: "Channel: Email" or "Channel: LinkedIn" or "Channel: Phone"
If Email or LinkedIn, second line: "Subject: <subject line>"
Then a blank line, then the ready-to-send message body.
For Phone, write a short call agenda with talking points instead of a message.

Rules:
- Output ONLY the three sections above. No preamble, no closing remarks.
- Be specific to this client's industry, role, stage, and pain points — never generic.
- Outreach tone: warm for existing contacts, direct for cold leads, empathetic for at-risk.
- Focus on their business outcomes, not product features."""


def format_client_context(client: Client) -> str:
    pain_points = "\n".join(f"- {p}" for p in client.pain_points)
    return f"""CLIENT PROFILE
Name: {client.name}
Role: {client.role} at {client.company}
Industry: {client.industry}
Email: {client.email}

DEAL DETAILS
Stage: {client.deal_stage}
Estimated Value: ${client.deal_value:,}
Days Since Last Contact: {client.last_contact_days}

PAIN POINTS
{pain_points}

RECENT ACTIVITY
{client.recent_activity}

SALES NOTES
{client.notes}

---
Generate a personalized recommendation for this client."""


def parse_recommendation(text: str) -> dict[str, str]:
    """Split generated text into its three named sections."""
    import re
    parts = re.split(r"\n?##\s+", text.strip())
    result: dict[str, str] = {}
    key_map = {
        "situation summary": "situation",
        "reasoning": "reasoning",
        "outreach": "outreach",
    }
    for part in parts:
        if not part.strip():
            continue
        first_line, _, body = part.partition("\n")
        key = key_map.get(first_line.strip().lower())
        if key:
            result[key] = body.strip()
    return result


def stream_recommendation(client: Client) -> Generator[str, None, None]:
    """Stream a personalized recommendation for the given client."""
    stream = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": format_client_context(client)},
        ],
        stream=True,
    )
    for chunk in stream:
        yield chunk["message"]["content"]
