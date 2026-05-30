from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Client:
    id: str
    name: str
    company: str
    industry: str
    role: str
    email: str
    deal_stage: str
    deal_value: int
    last_contact_days: int
    pain_points: List[str]
    recent_activity: str
    notes: str


CLIENTS: List[Client] = [
    # ── Prospecting ──────────────────────────────────────────────────────────
    Client(
        id="c001",
        name="James Okonkwo",
        company="BrightPath Manufacturing",
        industry="Manufacturing",
        role="Head of Digital Transformation",
        email="jokonkwo@brightpath.com",
        deal_stage="Prospecting",
        deal_value=120000,
        last_contact_days=21,
        pain_points=[
            "Legacy ERP migration blocking growth",
            "Zero real-time supply chain visibility",
            "Unplanned downtime from reactive maintenance",
        ],
        recent_activity=(
            "Opened 3 outreach emails but has not responded. Liked a LinkedIn post "
            "about Industry 4.0 case studies two days ago."
        ),
        notes=(
            "Strong ICP fit — 800-person manufacturer mid-way through a 3-year digital "
            "transformation. Went cold after initial outreach. Generic product messaging "
            "isn't landing; need a different angle."
        ),
    ),
    Client(
        id="c002",
        name="Aisha Patel",
        company="Vantage Insurance Group",
        industry="Insurance",
        role="VP of Operations",
        email="apatel@vantageig.com",
        deal_stage="Prospecting",
        deal_value=95000,
        last_contact_days=7,
        pain_points=[
            "Claims processing taking 14+ days on average",
            "High manual data entry across policy workflows",
            "Lack of real-time visibility into adjuster workloads",
        ],
        recent_activity=(
            "Attended our webinar on workflow automation last Thursday. Did not fill out "
            "the post-event survey but stayed for the full Q&A session."
        ),
        notes=(
            "Came in as a warm webinar lead. No direct outreach yet — this is the first "
            "touch. Insurance vertical is a new focus for us this quarter; good logo if "
            "we can land it."
        ),
    ),
    Client(
        id="c003",
        name="Tom Brennan",
        company="Summit EdTech",
        industry="Education Technology",
        role="Chief Product Officer",
        email="tbrennan@summitedtech.com",
        deal_stage="Prospecting",
        deal_value=42000,
        last_contact_days=14,
        pain_points=[
            "Student engagement dropping post-pandemic",
            "No unified data across LMS, CRM, and support tools",
            "Engineering bandwidth bottleneck for new feature releases",
        ],
        recent_activity=(
            "Responded to a cold LinkedIn message with 'interesting — send me more info.' "
            "Has not opened the follow-up email sent 3 days later."
        ),
        notes=(
            "Small deal but strategic — EdTech is an expansion vertical. Tom is a "
            "product person, not procurement; speak his language around user outcomes "
            "and velocity, not cost savings."
        ),
    ),

    # ── Qualification ────────────────────────────────────────────────────────
    Client(
        id="c004",
        name="Priya Sharma",
        company="GlobalEdge Finance",
        industry="Financial Services",
        role="Director of Operations",
        email="psharma@globaledge.com",
        deal_stage="Qualification",
        deal_value=55000,
        last_contact_days=2,
        pain_points=[
            "Manual monthly reporting consuming 40+ hours",
            "Data siloed across 5 departments",
            "Audit trail gaps for regulatory compliance",
        ],
        recent_activity=(
            "Replied to intro email within 2 hours. Requested a 30-minute discovery "
            "call for next Tuesday. Mentioned she's evaluating 3 vendors simultaneously."
        ),
        notes=(
            "Warm inbound lead from LinkedIn. Responsive and engaged. The manual "
            "reporting pain is acute — her team just missed a board deadline. "
            "Decision likely within 6 weeks."
        ),
    ),
    Client(
        id="c005",
        name="Rafael Mendez",
        company="Clearview Media",
        industry="Media & Advertising",
        role="SVP of Technology",
        email="rmendez@clearviewmedia.com",
        deal_stage="Qualification",
        deal_value=78000,
        last_contact_days=4,
        pain_points=[
            "Campaign reporting fragmented across 6 platforms",
            "Attribution model inconsistencies costing budget efficiency",
            "Ad ops team spending 60% of time on manual reconciliation",
        ],
        recent_activity=(
            "Had a 45-minute discovery call yesterday. Engaged and asked good questions. "
            "Wants to loop in his Head of Ad Ops before moving forward."
        ),
        notes=(
            "Technical buyer with budget authority. The Head of Ad Ops is the real "
            "end-user — getting her involved is key. Rafael flagged that they're mid-way "
            "through a GA4 migration which could be a natural integration hook."
        ),
    ),
    Client(
        id="c006",
        name="Nadia Kowalski",
        company="PureGrow Biotech",
        industry="Biotechnology",
        role="Director of R&D Operations",
        email="nkowalski@puregrow.com",
        deal_stage="Qualification",
        deal_value=130000,
        last_contact_days=9,
        pain_points=[
            "Trial data scattered across Excel, SharePoint, and lab notebooks",
            "Regulatory submission prep taking 3x longer than competitors",
            "No audit-ready data lineage for FDA documentation",
        ],
        recent_activity=(
            "Attended product demo. Took notes throughout. Asked specifically about "
            "21 CFR Part 11 compliance and e-signature workflows."
        ),
        notes=(
            "High-value deal with a 6-month sales cycle expected. Nadia is the champion "
            "but final sign-off requires the CFO. Compliance angle is the primary hook — "
            "their last FDA submission was delayed 8 weeks due to documentation issues."
        ),
    ),

    # ── Proposal ─────────────────────────────────────────────────────────────
    Client(
        id="c007",
        name="Sarah Chen",
        company="NexaTech Solutions",
        industry="SaaS",
        role="VP of Engineering",
        email="schen@nexatech.com",
        deal_stage="Proposal",
        deal_value=85000,
        last_contact_days=5,
        pain_points=[
            "Scaling infrastructure costs outpacing revenue growth",
            "Developer onboarding taking 3+ weeks",
            "CI/CD pipeline failures blocking weekly releases",
        ],
        recent_activity=(
            "Attended product demo last week. Asked detailed questions about API rate "
            "limits and multi-region deployment options. Forwarded proposal to her CTO."
        ),
        notes=(
            "Very technical buyer — prefers data-driven conversations over marketing "
            "speak. Budget approved for Q2. Her team of 12 engineers is the main "
            "end-user group. CTO involvement is new and could accelerate or stall."
        ),
    ),
    Client(
        id="c008",
        name="Derek Huang",
        company="Fortis Capital Partners",
        industry="Private Equity",
        role="Managing Director, Portfolio Operations",
        email="dhuang@fortiscapital.com",
        deal_stage="Proposal",
        deal_value=210000,
        last_contact_days=3,
        pain_points=[
            "Portfolio company KPI reporting takes 2 weeks to consolidate monthly",
            "No standardized operational benchmarks across holdings",
            "Investment committee decks built manually each quarter",
        ],
        recent_activity=(
            "Reviewed the proposal PDF — email tracking shows 4 opens over 2 days. "
            "Replied with 3 clarifying questions about data source connectors and "
            "white-labeling for portfolio company dashboards."
        ),
        notes=(
            "Derek is the economic buyer and decision-maker. Questions suggest serious "
            "evaluation. White-labeling requirement is a differentiator we can offer — "
            "confirm with product before next call. High-value, fast-moving deal."
        ),
    ),
    Client(
        id="c009",
        name="Fatima Al-Rashid",
        company="Meridian Healthcare Network",
        industry="Healthcare",
        role="VP of Clinical Informatics",
        email="falrashid@meridianhcn.com",
        deal_stage="Proposal",
        deal_value=165000,
        last_contact_days=8,
        pain_points=[
            "Clinician documentation burden averaging 3 hours per shift",
            "Interoperability gaps between Epic and downstream analytics tools",
            "Quality reporting for CMS programs requiring dedicated staff",
        ],
        recent_activity=(
            "Proposal submitted 8 days ago. No response yet. Her assistant confirmed "
            "she's been at a conference this week and returns Monday."
        ),
        notes=(
            "Strong fit — her team ran a 3-month internal pilot with a competing tool "
            "that failed on interoperability. That failure is our biggest selling point. "
            "Follow up Monday afternoon when she's back."
        ),
    ),

    # ── Negotiation ──────────────────────────────────────────────────────────
    Client(
        id="c010",
        name="Marcus Williams",
        company="Apex Health Systems",
        industry="Healthcare",
        role="CTO",
        email="mwilliams@apexhealth.com",
        deal_stage="Negotiation",
        deal_value=240000,
        last_contact_days=12,
        pain_points=[
            "HIPAA compliance overhead consuming engineering cycles",
            "EHR system integration complexity delaying product roadmap",
            "Staff adoption consistently below 40% for new tooling rollouts",
        ],
        recent_activity=(
            "Legal team pushed back on the data residency clause and BAA terms. "
            "Marcus went quiet after forwarding to legal 12 days ago."
        ),
        notes=(
            "Deal nearly closed in Q1 before legal stepped in. Marcus is a strong "
            "champion but has limited control over legal timelines. Competitor "
            "HealthBridge is also in evaluation — need to re-engage before they "
            "make a decision without us."
        ),
    ),
    Client(
        id="c011",
        name="Lin Wei",
        company="Pacific Freight Solutions",
        industry="Logistics & Supply Chain",
        role="COO",
        email="lwei@pacificfreight.com",
        deal_stage="Negotiation",
        deal_value=190000,
        last_contact_days=6,
        pain_points=[
            "Dwell time at ports averaging 4.2 days vs industry benchmark of 2.8",
            "Customer visibility portal outdated and triggering churn",
            "Billing disputes from manual freight invoicing causing cash flow issues",
        ],
        recent_activity=(
            "Counter-proposed on pricing — asked for a 15% discount and extended "
            "payment terms of net-60. Also wants a dedicated implementation manager "
            "included in the contract."
        ),
        notes=(
            "Lin has full budget authority. The discount ask is negotiable; the "
            "implementation manager request is the real sticking point — check with "
            "Professional Services on feasibility. Deal is winnable but she's also "
            "talking to FreightForce."
        ),
    ),
    Client(
        id="c012",
        name="Carlos Vega",
        company="Stellarworks Architecture",
        industry="Professional Services",
        role="Managing Partner",
        email="cvega@stellarworks.com",
        deal_stage="Negotiation",
        deal_value=48000,
        last_contact_days=2,
        pain_points=[
            "Project profitability invisible until invoicing — too late to course-correct",
            "Resource utilization tracked in spreadsheets across 3 offices",
            "Client reporting is manual and inconsistent between project managers",
        ],
        recent_activity=(
            "Verbal agreement on scope and pricing. Legal redlines came back yesterday "
            "with minor changes to liability cap and IP ownership clauses."
        ),
        notes=(
            "Smaller deal but clean — Carlos just wants reasonable contract language. "
            "Legal redlines are standard; should close within a week if we respond "
            "quickly. He's already told his team they're moving forward."
        ),
    ),

    # ── At Risk ──────────────────────────────────────────────────────────────
    Client(
        id="c013",
        name="Olivia Torres",
        company="CloudFirst Retail",
        industry="Retail / E-commerce",
        role="Chief Digital Officer",
        email="otorres@cloudfirst.com",
        deal_stage="At Risk",
        deal_value=175000,
        last_contact_days=18,
        pain_points=[
            "Inventory forecasting accuracy stuck below 70%",
            "Fragmented customer experience across web, app, and in-store",
            "Merchandising decisions lagging 2 weeks behind market signals",
        ],
        recent_activity=(
            "Missed last two scheduled calls without rescheduling. A contact at "
            "CloudFirst mentioned they may be re-evaluating priorities since their "
            "new CDO joined last month."
        ),
        notes=(
            "Deal was tracking well until the executive sponsor changed. Olivia is "
            "the new CDO who inherited this evaluation — she may not be the original "
            "champion. Need to re-establish executive alignment quickly or risk losing "
            "to inertia."
        ),
    ),
    Client(
        id="c014",
        name="Greg Novak",
        company="Axiom Legal Group",
        industry="Legal Services",
        role="Director of IT",
        email="gnovak@axiomlegal.com",
        deal_stage="At Risk",
        deal_value=62000,
        last_contact_days=25,
        pain_points=[
            "Matter management system end-of-life in 90 days",
            "Attorneys billing 45 minutes per day on admin instead of billable work",
            "Client portal complaints up 30% this quarter",
        ],
        recent_activity=(
            "Was actively engaged 5 weeks ago. Went dark after we sent the security "
            "questionnaire. IT contacts say a budget freeze was announced internally "
            "but hasn't been officially communicated to vendors."
        ),
        notes=(
            "The EoL deadline creates urgency but the budget freeze complicates things. "
            "Greg is not the economic buyer — the COO controls discretionary spend. "
            "May need to go above Greg to keep this alive."
        ),
    ),

    # ── Closed Won ───────────────────────────────────────────────────────────
    Client(
        id="c015",
        name="David Park",
        company="Kinetic Logistics",
        industry="Logistics & Supply Chain",
        role="VP of Technology",
        email="dpark@kineticlogistics.com",
        deal_stage="Closed Won",
        deal_value=98000,
        last_contact_days=30,
        pain_points=[
            "Real-time shipment tracking gaps causing customer escalations",
            "Driver communication routed through personal phones",
            "Route optimization done manually by dispatchers",
        ],
        recent_activity=(
            "Contract signed 30 days ago. Onboarding kickoff completed. CSM assigned "
            "and implementation is on track for week 3 milestones."
        ),
        notes=(
            "Excellent relationship throughout the sales process. David mentioned "
            "interest in the fleet management add-on module for Q3. Strong expansion "
            "opportunity — intro him to the Customer Success team now."
        ),
    ),
    Client(
        id="c016",
        name="Yemi Adeyemi",
        company="Helix Pharmaceuticals",
        industry="Pharmaceuticals",
        role="Head of Commercial Operations",
        email="yadeyemi@helixpharma.com",
        deal_stage="Closed Won",
        deal_value=320000,
        last_contact_days=14,
        pain_points=[
            "Sales rep territory planning relying on 6-month-old data",
            "CRM adoption below 55% across field team of 200 reps",
            "Forecasting accuracy off by 18% YTD, causing supply chain issues",
        ],
        recent_activity=(
            "Week 2 of onboarding. Kickoff went well. Yemi flagged that 3 regional "
            "managers are resistant to the new workflow — wants a change management "
            "session before full rollout."
        ),
        notes=(
            "Largest deal this quarter. Yemi is a strong internal advocate. The "
            "change management ask is a real risk — loop in the Customer Success "
            "Director proactively. Expansion potential to their EU operations in H2."
        ),
    ),
    Client(
        id="c017",
        name="Simone Dubois",
        company="Luminar Energy",
        industry="Energy & Utilities",
        role="VP of Asset Management",
        email="sdubois@luminarenergy.com",
        deal_stage="Closed Won",
        deal_value=145000,
        last_contact_days=45,
        pain_points=[
            "Asset maintenance schedules managed in aging spreadsheets",
            "Field inspection data not syncing to central systems for days",
            "Regulatory compliance reporting requiring 2 dedicated FTEs",
        ],
        recent_activity=(
            "Implementation completed 6 weeks ago. Quiet since then — no issues "
            "raised but also no check-in scheduled."
        ),
        notes=(
            "Long silence post-implementation is a yellow flag. Need to reconnect, "
            "confirm adoption health, and get a success story or case study if "
            "they're happy. Also a natural candidate for the compliance module upsell."
        ),
    ),
]


def get_all_clients() -> List[Client]:
    return CLIENTS


def get_client_by_id(client_id: str) -> Optional[Client]:
    return next((c for c in CLIENTS if c.id == client_id), None)
