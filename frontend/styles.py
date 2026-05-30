STAGE_META = {
    "Prospecting":   {"icon": "○", "bg": "#DBEAFE", "text": "#1D4ED8"},
    "Qualification": {"icon": "◐", "bg": "#EDE9FE", "text": "#6D28D9"},
    "Proposal":      {"icon": "◑", "bg": "#FEF3C7", "text": "#B45309"},
    "Negotiation":   {"icon": "◕", "bg": "#FFEDD5", "text": "#C2410C"},
    "Closed Won":    {"icon": "●", "bg": "#D1FAE5", "text": "#065F46"},
    "At Risk":       {"icon": "!", "bg": "#FEE2E2", "text": "#B91C1C"},
}

STAGE_ORDER = ["Prospecting", "Qualification", "Proposal", "Negotiation", "At Risk", "Closed Won"]

CSS = """
<style>
/* ── Global ── */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #FFFFFF;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background-color: #F1F5F9;
    border-right: 1px solid #E2E8F0;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #1E293B;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}

/* ── Sidebar client buttons ── */
[data-testid="stSidebar"] .stButton > button {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    color: #334155;
    font-size: 0.85rem;
    padding: 10px 12px;
    text-align: left;
    transition: all 0.15s ease;
}
[data-testid="stSidebar"] .stButton > button:hover {
    background-color: #EFF6FF;
    border-color: #93C5FD;
    color: #1D4ED8;
}
[data-testid="stSidebar"] .stButton > button[kind="primary"] {
    background-color: #EFF6FF;
    border-color: #2563EB;
    color: #1D4ED8;
    font-weight: 600;
}

/* ── Cards ── */
.card {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 12px;
}
.card-blue  { background: #F0F7FF; border-color: #BFDBFE; }
.card-grey  { background: #F8FAFC; border-color: #E2E8F0; }
.card-red   { background: #FFF5F5; border-color: #FECACA; }
.card-green { background: #F0FDF4; border-color: #BBF7D0; }

/* ── Stage badge ── */
.stage-badge {
    display: inline-block;
    border-radius: 20px;
    padding: 4px 12px;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.03em;
}

/* ── Metric tile ── */
.metric-tile {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 14px 18px;
    text-align: center;
}
.metric-tile .label {
    font-size: 0.72rem;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 4px;
}
.metric-tile .value {
    font-size: 1.15rem;
    font-weight: 700;
    color: #1E293B;
}

/* ── Section heading ── */
.section-heading {
    font-size: 0.72rem;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 8px;
}

/* ── Pain pill ── */
.pain-pill {
    display: inline-block;
    background: #F1F5F9;
    border: 1px solid #CBD5E1;
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 0.82rem;
    color: #334155;
    margin: 3px 3px 3px 0;
}

/* ── Divider ── */
hr { border: none; border-top: 1px solid #E2E8F0; margin: 20px 0; }

/* ── Buttons ── */
.stButton > button[kind="primary"] {
    background-color: #2563EB;
    border: none;
    border-radius: 8px;
    color: #FFFFFF;
    font-weight: 600;
    padding: 10px 20px;
    transition: background-color 0.15s ease;
}
.stButton > button[kind="primary"]:hover { background-color: #1D4ED8; }
.stButton > button[kind="secondary"] {
    background-color: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    color: #475569;
    font-weight: 500;
}
.stButton > button[kind="secondary"]:hover { border-color: #94A3B8; color: #1E293B; }

/* ── AI output ── */
.ai-box {
    background: #F0F7FF;
    border: 1px solid #BFDBFE;
    border-left: 4px solid #2563EB;
    border-radius: 10px;
    padding: 20px 24px;
    color: #1E293B;
    line-height: 1.65;
}

/* ── Priority row ── */
.priority-row {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    margin-bottom: 8px;
    cursor: pointer;
    transition: border-color 0.15s;
}
.priority-row:hover { border-color: #93C5FD; background: #F0F7FF; }

h1 { color: #1E293B !important; font-weight: 800 !important; }
</style>
"""


def badge(stage: str) -> str:
    m = STAGE_META.get(stage, {"icon": "·", "bg": "#F1F5F9", "text": "#64748B"})
    return (
        f'<span class="stage-badge" '
        f'style="background:{m["bg"]};color:{m["text"]}">'
        f'{m["icon"]}  {stage}</span>'
    )


def metric_tile(label: str, value: str, value_color: str = "#1E293B") -> str:
    return (
        f'<div class="metric-tile">'
        f'<div class="label">{label}</div>'
        f'<div class="value" style="color:{value_color}">{value}</div>'
        f'</div>'
    )
