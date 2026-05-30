from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Interaction:
    date: str   # ISO format: "2026-05-30"
    type: str   # "Email" | "Call" | "LinkedIn" | "Demo" | "Meeting" | "Contract" | "Internal" | "Webinar"
    summary: str


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
    interaction_history: List[Interaction]


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
        interaction_history=[
            Interaction("2026-05-28", "LinkedIn", "Liked our post on Industry 4.0 ROI case studies — no direct message."),
            Interaction("2026-05-09", "Email", "Third outreach email sent (product-focused). Opened but no reply."),
            Interaction("2026-05-02", "Email", "Second outreach email sent. Opened but no reply."),
            Interaction("2026-04-25", "Email", "Initial cold outreach sent referencing ERP modernization trends. Opened but no reply."),
            Interaction("2026-04-18", "Internal", "Added to pipeline as strong ICP fit. Identified via LinkedIn job post about digital transformation lead hire."),
        ],
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
        interaction_history=[
            Interaction("2026-05-23", "Webinar", "Attended workflow automation webinar. Stayed for full Q&A but did not complete post-event survey."),
            Interaction("2026-05-23", "Internal", "Added to pipeline as warm webinar lead. VP-level role at insurance group is strong ICP fit."),
            Interaction("2026-05-16", "Email", "Webinar invitation sent via marketing sequence."),
        ],
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
        interaction_history=[
            Interaction("2026-05-19", "Email", "Follow-up email with product one-pager sent after LinkedIn reply. Not opened after 11 days."),
            Interaction("2026-05-16", "LinkedIn", "Tom replied to cold outreach: 'interesting — send me more info.'"),
            Interaction("2026-05-10", "LinkedIn", "Cold outreach message sent, focused on engineering velocity and LMS integration pain points."),
        ],
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
        interaction_history=[
            Interaction("2026-05-28", "Email", "Priya replied within 2 hours requesting a 30-minute discovery call next Tuesday. Flagged she's evaluating 3 vendors."),
            Interaction("2026-05-28", "Email", "Intro email sent following LinkedIn connection."),
            Interaction("2026-05-25", "LinkedIn", "Connected after Priya engaged with our automated reporting content."),
            Interaction("2026-05-20", "Internal", "Identified as warm inbound lead via LinkedIn. Added to pipeline."),
        ],
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
        interaction_history=[
            Interaction("2026-05-26", "Call", "45-minute discovery call. Strong engagement; asked about attribution modeling and GA4 migration hooks. Wants Head of Ad Ops involved before next step."),
            Interaction("2026-05-22", "Email", "Pre-call agenda sent along with a campaign attribution benchmark report."),
            Interaction("2026-05-18", "Email", "Follow-up proposing a discovery call to discuss fragmented reporting challenges."),
            Interaction("2026-05-15", "LinkedIn", "Cold outreach message focused on ad ops efficiency and cross-platform attribution pain."),
        ],
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
        interaction_history=[
            Interaction("2026-05-21", "Demo", "Product demo attended. Nadia took notes throughout. Specific questions on 21 CFR Part 11 compliance and e-signature workflows."),
            Interaction("2026-05-14", "Email", "Demo invite sent with compliance-focused agenda and FDA documentation case study."),
            Interaction("2026-05-07", "Call", "30-minute intro call. Confirmed regulatory compliance is top priority. FDA submission delayed 8 weeks cited unprompted."),
            Interaction("2026-04-30", "Email", "Initial outreach highlighting audit-ready data lineage and FDA documentation capabilities."),
            Interaction("2026-04-22", "LinkedIn", "Connected after Nadia posted about challenges in regulatory submission prep."),
        ],
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
        interaction_history=[
            Interaction("2026-05-25", "Internal", "Email tracking: Sarah forwarded proposal to CTO internally."),
            Interaction("2026-05-23", "Demo", "Product demo. Detailed questions on API rate limits, multi-region deployment, and CI/CD integration. High technical engagement."),
            Interaction("2026-05-16", "Email", "Proposal sent following qualification call."),
            Interaction("2026-05-09", "Call", "60-minute qualification call. Q2 budget confirmed approved. 12-engineer team is core end-user group."),
            Interaction("2026-05-02", "Email", "Initial outreach referencing infrastructure scaling challenges common in Series B SaaS companies."),
            Interaction("2026-04-20", "LinkedIn", "Cold message sent. Sarah connected and mentioned she'd been looking at solutions for onboarding bottlenecks."),
        ],
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
        interaction_history=[
            Interaction("2026-05-27", "Email", "Derek replied to proposal with 3 clarifying questions on data connectors and white-labeling for portfolio dashboards. Proposal opened 4x over 2 days."),
            Interaction("2026-05-24", "Email", "Proposal sent following executive walkthrough."),
            Interaction("2026-05-20", "Meeting", "Executive walkthrough with Derek and two portfolio operations leads. Strong engagement on KPI consolidation use case."),
            Interaction("2026-05-13", "Call", "Discovery call. KPI reporting consolidation and investment committee deck automation identified as top priorities."),
            Interaction("2026-05-06", "Email", "Intro email sent via referral from a portfolio company CEO."),
        ],
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
        interaction_history=[
            Interaction("2026-05-22", "Email", "Proposal submitted covering Epic interoperability, CMS quality reporting automation, and clinician documentation reduction."),
            Interaction("2026-05-19", "Call", "Pre-proposal scoping call. Confirmed priorities and implementation timeline requirements."),
            Interaction("2026-05-12", "Demo", "Technical demo focused on Epic EHR interoperability. Fatima asked specifically about the failure modes of the competing tool's integration."),
            Interaction("2026-05-05", "Call", "45-minute discovery call. Clinician documentation burden (3 hrs/shift) flagged as most acute pain. Revealed failed 3-month pilot with competitor."),
            Interaction("2026-04-28", "Email", "Intro email following a conference introduction via a mutual contact."),
        ],
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
        interaction_history=[
            Interaction("2026-05-18", "Email", "Legal team sent redlines: pushback on data residency clause and BAA terms. Marcus forwarded to legal and has been unresponsive since."),
            Interaction("2026-05-06", "Call", "Contract review call. Marcus confident deal would close by end of Q1; flagged legal as final hurdle."),
            Interaction("2026-04-29", "Email", "MSA draft sent for legal review."),
            Interaction("2026-04-22", "Meeting", "Executive alignment meeting with Marcus and their CISO. HIPAA compliance architecture walkthrough completed."),
            Interaction("2026-04-15", "Call", "Negotiation call. Agreed on commercial terms and SLA structure. Moved to legal review."),
            Interaction("2026-03-20", "Demo", "Technical deep-dive on HIPAA compliance controls and EHR integration architecture. Marcus's engineering lead attended."),
        ],
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
        interaction_history=[
            Interaction("2026-05-24", "Email", "Counter-proposal received: 15% discount, net-60 payment terms, and dedicated implementation manager added to scope."),
            Interaction("2026-05-17", "Call", "Pricing discussion. Initial proposal presented with standard implementation package. Lin indicated she'd consult her CFO."),
            Interaction("2026-05-10", "Meeting", "On-site business case review with Lin and CFO. ROI model walkthrough; billing dispute automation resonated strongly."),
            Interaction("2026-05-03", "Demo", "Operational workflow demo focused on port dwell time reduction and automated freight invoicing."),
            Interaction("2026-04-26", "Call", "Discovery call. Billing disputes and outdated customer visibility portal flagged as highest urgency — triggering customer churn."),
        ],
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
        interaction_history=[
            Interaction("2026-05-29", "Email", "Legal redlines received: minor changes to liability cap and IP ownership clauses."),
            Interaction("2026-05-28", "Call", "Verbal agreement reached on scope and pricing. Carlos confirmed team is ready to move forward."),
            Interaction("2026-05-21", "Email", "Revised proposal sent addressing resource utilization tracking across 3 offices."),
            Interaction("2026-05-14", "Meeting", "Proposal walkthrough with Carlos and two senior practice leads. Strong alignment on project profitability use case."),
            Interaction("2026-05-07", "Call", "30-minute discovery call. Real-time project profitability visibility flagged as urgent — missing cost overruns until invoicing."),
            Interaction("2026-04-30", "LinkedIn", "Inbound: Carlos reached out after seeing a professional services firm case study we published."),
        ],
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
        interaction_history=[
            Interaction("2026-05-12", "Email", "Missed scheduled call. Follow-up sent to reschedule. No response."),
            Interaction("2026-05-05", "Call", "Scheduled call — Olivia was a no-show. Voicemail left offering flexible reschedule options."),
            Interaction("2026-04-28", "Email", "Intro email sent to Olivia as new CDO. Previous champion (former CDO) had departed. Proposal re-submitted with executive summary."),
            Interaction("2026-04-14", "Internal", "Learned from CloudFirst contact that executive sponsor changed — new CDO Olivia Torres hired. Deal paused pending re-engagement."),
            Interaction("2026-04-07", "Meeting", "Proposal presentation with original CDO sponsor. Strong positive signal; verbal commitment to move forward after legal review."),
            Interaction("2026-03-24", "Call", "Discovery call. Inventory forecasting accuracy (below 70%) flagged as top priority. Budget and timeline confirmed."),
        ],
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
        interaction_history=[
            Interaction("2026-05-05", "Email", "Security questionnaire sent at Greg's request. No response since — gone dark."),
            Interaction("2026-05-01", "Call", "Follow-up call on proposal. Greg confirmed he'd review the security questionnaire that week. Last verbal contact."),
            Interaction("2026-04-24", "Email", "Proposal and security questionnaire sent."),
            Interaction("2026-04-17", "Demo", "Product demo for Greg and two senior attorneys. Strong engagement on matter management and client portal replacement."),
            Interaction("2026-04-10", "Call", "Discovery call. Matter management system EoL in 90 days confirmed as urgent driver. Greg noted COO controls budget."),
            Interaction("2026-04-03", "Email", "Initial outreach about matter management modernization and attorney productivity."),
        ],
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
        interaction_history=[
            Interaction("2026-04-30", "Internal", "Onboarding kickoff completed. CSM assigned. Implementation on track for week 3 milestones."),
            Interaction("2026-04-01", "Contract", "Contract signed ($98K). SOW executed."),
            Interaction("2026-03-25", "Email", "Final commercial terms agreed. MSA countersigned."),
            Interaction("2026-03-18", "Call", "Procurement and legal review call. Minor redlines on liability cap resolved."),
            Interaction("2026-03-11", "Meeting", "Executive sponsor presentation. Board sign-off received. David mentioned fleet management add-on interest for Q3."),
            Interaction("2026-02-25", "Demo", "Technical POC review. David confirmed 95% feature coverage for tracking and dispatch use cases."),
            Interaction("2026-02-11", "Call", "Discovery call. Real-time tracking gaps causing customer escalations flagged as top priority."),
        ],
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
        interaction_history=[
            Interaction("2026-05-16", "Internal", "Week 2 onboarding. 3 resistant regional managers flagged. Yemi requested change management session before full rollout."),
            Interaction("2026-05-09", "Internal", "Onboarding kickoff completed. 200-rep field team rollout plan confirmed. Strong start."),
            Interaction("2026-04-25", "Contract", "Contract signed ($320K — largest deal this quarter). Multi-year agreement executed."),
            Interaction("2026-04-18", "Call", "Final negotiation call. Multi-year pricing structure agreed."),
            Interaction("2026-04-11", "Meeting", "Stakeholder alignment session with Yemi, CFO, and 3 regional VPs. All signed off on rollout plan."),
            Interaction("2026-03-28", "Demo", "Live CRM adoption analytics demo. Forecasting accuracy improvement case study resonated with Yemi and CFO."),
            Interaction("2026-03-14", "Call", "Discovery call. CRM adoption at 55%, forecasting off 18% YTD causing downstream supply chain issues."),
        ],
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
        interaction_history=[
            Interaction("2026-04-19", "Internal", "Implementation completed. Go-live confirmed. No support tickets raised."),
            Interaction("2026-04-05", "Internal", "Final UAT passed. Field inspector training sessions completed across 3 sites."),
            Interaction("2026-03-22", "Internal", "Implementation phase 2: regulatory compliance reporting module deployed."),
            Interaction("2026-03-08", "Internal", "Implementation kickoff. Asset data migration from spreadsheets started."),
            Interaction("2026-02-22", "Contract", "Contract signed ($145K). Implementation timeline agreed: 6 weeks."),
            Interaction("2026-02-08", "Call", "Final commercial review call. Agreed on implementation timeline and success metrics."),
        ],
    ),

    # ── Closed Lost ──────────────────────────────────────────────────────────
    Client(
        id="c018",
        name="Brandon Kirk",
        company="Orion Retail Group",
        industry="Retail / E-commerce",
        role="Director of IT",
        email="bkirk@orionretail.com",
        deal_stage="Closed Lost",
        deal_value=88000,
        last_contact_days=62,
        pain_points=[
            "Inventory sync lag between warehouses and e-commerce storefront",
            "Manual order reconciliation consuming 3 FTEs",
            "No unified reporting across 12 retail locations",
        ],
        recent_activity=(
            "Informed us they selected a competitor (RetailEdge) 62 days ago. "
            "Decision was primarily driven by RetailEdge's existing Shopify integration."
        ),
        notes=(
            "Lost on integration depth, not on price or relationship. We lacked a "
            "native Shopify connector at the time of evaluation. Worth re-engaging "
            "once our Shopify integration ships in Q3."
        ),
        interaction_history=[
            Interaction("2026-03-29", "Email", "Brandon confirmed selection of RetailEdge. Shopify integration cited as primary deciding factor."),
            Interaction("2026-03-15", "Call", "Final evaluation check-in. No commitment; 'still reviewing with the team.'"),
            Interaction("2026-03-01", "Email", "Proposal sent with Shopify integration roadmap outlined (Q3 delivery)."),
            Interaction("2026-02-15", "Demo", "Inventory sync capabilities demo. Shopify connector gap surfaced — noted as potential blocker."),
            Interaction("2026-02-01", "Call", "Discovery call. 12 retail locations with e-commerce storefront; inventory sync lag is highest urgency pain."),
        ],
    ),
    Client(
        id="c019",
        name="Helen Marsh",
        company="Crestwood Legal Partners",
        industry="Legal Services",
        role="COO",
        email="hmarsh@crestwoodlegal.com",
        deal_stage="Closed Lost",
        deal_value=52000,
        last_contact_days=90,
        pain_points=[
            "Billing disputes from manual time-entry errors",
            "Matter lifecycle visibility gaps for partners",
            "Client portal outdated and causing support overhead",
        ],
        recent_activity=(
            "Deal stalled for 3 months and was formally closed out. Helen's firm "
            "decided to delay all new software purchases until next fiscal year."
        ),
        notes=(
            "Lost to budget freeze, not to a competitor. Helen was personally "
            "enthusiastic about the product. Put her on a re-engagement sequence "
            "starting next January when their new fiscal year opens."
        ),
        interaction_history=[
            Interaction("2026-03-01", "Email", "Helen confirmed all new software purchases delayed until next fiscal year. Deal formally closed out."),
            Interaction("2026-02-15", "Call", "Follow-up call. Helen still positive on the product but flagged internal budget constraints. No timeline given."),
            Interaction("2026-02-01", "Email", "Revised proposal sent with phased implementation option to reduce upfront cost."),
            Interaction("2026-01-18", "Demo", "Full product walkthrough. Helen very engaged; billing dispute resolution module resonated strongly."),
            Interaction("2026-01-04", "Call", "Discovery call. Manual time-entry billing disputes causing partner frustration flagged as top pain."),
        ],
    ),
    Client(
        id="c020",
        name="Victor Osei",
        company="Madera Construction Group",
        industry="Construction",
        role="VP of Operations",
        email="vosei@maderaconstruction.com",
        deal_stage="Closed Lost",
        deal_value=115000,
        last_contact_days=45,
        pain_points=[
            "Project cost overruns invisible until month-end reporting",
            "Subcontractor coordination managed via group texts and emails",
            "Safety compliance documentation gaps creating liability exposure",
        ],
        recent_activity=(
            "Went with an industry-specific construction ERP (BuildPro) that had "
            "pre-built subcontractor management modules we could not match."
        ),
        notes=(
            "Lost on vertical depth — BuildPro had construction-specific workflows "
            "out of the box. Victor liked us but couldn't justify the customisation "
            "cost. Good reference contact for the construction vertical in future."
        ),
        interaction_history=[
            Interaction("2026-04-15", "Email", "Victor confirmed selection of BuildPro ERP. Pre-built subcontractor management cited as key differentiator."),
            Interaction("2026-04-01", "Call", "Final evaluation call. Victor noted BuildPro's construction-specific workflows as decisive advantage over customisation cost."),
            Interaction("2026-03-18", "Meeting", "On-site demo and executive walkthrough. Strong rapport but subcontractor coordination gap acknowledged."),
            Interaction("2026-03-04", "Email", "Proposal sent with customisation scope for construction-specific workflows."),
            Interaction("2026-02-18", "Call", "Discovery call. Subcontractor coordination (group texts) and safety compliance documentation gaps flagged as top needs."),
        ],
    ),
]


def get_all_clients() -> List[Client]:
    return CLIENTS


def get_client_by_id(client_id: str) -> Optional[Client]:
    return next((c for c in CLIENTS if c.id == client_id), None)
