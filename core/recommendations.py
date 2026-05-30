from typing import Generator

import anthropic

from backend.data import Client

SYSTEM_PROMPT = """You are an expert B2B sales strategist and communication coach. \
Your role is to help salespeople craft highly personalized outreach and follow-up strategies \
for their prospects and clients.

For each client, deliver a structured recommendation with these four sections:

**Situation Assessment** (2-3 sentences)
Summarize where this deal stands and the key dynamic the salesperson needs to navigate.

**Recommended Action**
One clear, specific next step with a brief rationale grounded in the client's situation.

**Message Draft**
A ready-to-send email or LinkedIn message (label which channel). Keep it concise, \
personal, and value-focused — not a feature pitch.

**Talking Points** (2-3 bullets)
Key themes to weave into the conversation, tied directly to the client's stated pain points \
and context.

Guidelines:
- Be specific to this client's industry, role, and deal stage — never generic
- Match tone to the relationship stage (warmer for existing contacts, more formal for cold)
- Focus on their business outcomes, not your product features
- For at-risk deals, prioritize re-engagement over pitching
- For closed-won, focus on expansion and relationship deepening"""


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


def stream_recommendation(client: Client) -> Generator[str, None, None]:
    """Stream a personalized recommendation for the given client."""
    anthropic_client = anthropic.Anthropic()

    with anthropic_client.messages.stream(
        model="claude-opus-4-8",
        max_tokens=1024,
        system=[
            {
                "type": "text",
                "text": SYSTEM_PROMPT,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[
            {
                "role": "user",
                "content": format_client_context(client),
            }
        ],
    ) as stream:
        for text in stream.text_stream:
            yield text
