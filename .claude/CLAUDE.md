# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project: Sales AI Assistant

Hackathon practice repo. Currently contains a B2B sales AI application that generates personalized outreach and follow-up recommendations for salespeople using the Anthropic Claude API.

### Stack

- **Language**: Python 3.10+
- **Frontend**: Streamlit
- **AI**: Anthropic Claude API (`claude-opus-4-8`) with prompt caching and streaming
- **Data**: Synthetic in-memory dataset — no database

### Commands

```bash
pip install -r requirements.txt
ANTHROPIC_API_KEY=<key> streamlit run app.py
```

### Architecture

```
app.py                   # Entry point — calls render_app()
frontend/dashboard.py    # Full UI: sidebar, client detail panel, recommendation section
backend/data.py          # Client dataclass + 6 synthetic B2B clients
core/recommendations.py  # Claude API: system prompt, context formatter, streaming generator
```

**Data flow:** `backend/data.py` → `core/recommendations.py` (streams Claude response chunks) → `frontend/dashboard.py` (`st.write_stream()` renders in real time). Session state caches `selected_client_id` and `recommendation` to avoid redundant API calls. System prompt uses `cache_control: ephemeral` for prompt caching.

---

## Coding Guidelines

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.
