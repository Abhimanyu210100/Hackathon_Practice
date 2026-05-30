from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Correspondence:
    id: str
    client_id: str
    type: str          # "email_thread" | "phone_call" | "linkedin_message" | "meeting_notes"
    date: str          # ISO 8601 date of the most recent message/event
    subject: Optional[str]
    body: str          # full content: email thread, call transcript, or notes


CORRESPONDENCE: List[Correspondence] = [

    # ── c001: James Okonkwo | BrightPath Manufacturing | Prospecting ──────────

    Correspondence(
        id="cr001",
        client_id="c001",
        type="email_thread",
        date="2026-04-19",
        subject="Modernising supply chain visibility at BrightPath",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: James Okonkwo <jokonkwo@brightpath.com>
Date: 2026-04-19

Hi James,

I came across BrightPath's profile while researching automotive Tier-2 suppliers going through digital transformation — impressive work on the plant expansion in Toledo.

We work with manufacturers in exactly your position: mid-ERP-migration, trying to get real-time visibility into the supply chain without waiting for the SAP cutover. Happy to share a couple of case studies if useful.

Would a 20-minute call this week or next make sense?

Best,
Alex Rivera | Account Executive, Acme Solutions

---
[No reply received. Email opened per tracking.]""",
    ),

    Correspondence(
        id="cr002",
        client_id="c001",
        type="email_thread",
        date="2026-04-28",
        subject="Re: Modernising supply chain visibility at BrightPath",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: James Okonkwo <jokonkwo@brightpath.com>
Date: 2026-04-28

Hi James,

Following up on my note from last week. I know your plate is full mid-transformation.

One thing I'm seeing a lot in automotive manufacturing right now: teams blocked on legacy ERP data latency while trying to run lean production schedules. We helped a Tier-1 supplier cut unplanned downtime 30% by layering real-time IIoT data over their existing SAP environment — no rip-and-replace required.

Worth a quick conversation?

Alex

---
[No reply received. Email opened per tracking.]""",
    ),

    Correspondence(
        id="cr003",
        client_id="c001",
        type="email_thread",
        date="2026-05-09",
        subject="Industry 4.0 at BrightPath — a different angle",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: James Okonkwo <jokonkwo@brightpath.com>
Date: 2026-05-09

James,

I saw you engaged with a post on Industry 4.0 predictive maintenance case studies — that's exactly the territory I wanted to talk about.

Most vendors pitching you right now are probably leading with the full platform sale. We've had more success with manufacturers like BrightPath starting with a focused use case: real-time OEE dashboards fed by IIoT sensors, running in parallel with your existing ERP. Proves value in 60 days without touching the migration timeline.

If that sounds different from what you've been hearing, I'd genuinely value 15 minutes to compare notes.

Alex Rivera | Acme Solutions

---
[No reply received. Email opened per tracking.]""",
    ),

    # ── c002: Aisha Patel | Vantage Insurance Group | Prospecting ─────────────

    Correspondence(
        id="cr004",
        client_id="c002",
        type="meeting_notes",
        date="2026-05-22",
        subject="Webinar attendance — Workflow Automation for Insurance Operations",
        body="""Event: Acme Solutions Webinar — Workflow Automation for Insurance Operations
Date: 2026-05-22, 1:00 PM EST
Registrant: Aisha Patel, VP of Operations, Vantage Insurance Group

Attendance notes:
- Joined at 1:02 PM, stayed through full Q&A (ended 2:15 PM). Did not submit post-event survey.
- Asked in chat: "How does your solution handle Guidewire ClaimCenter integrations for automated routing?" — answered live by product team.
- No follow-up contact initiated by attendee post-event.

Webinar content covered:
- Straight-through processing (STP) for low-complexity claims.
- Adjuster workload routing dashboard demo.
- Case study: Regional P&C insurer reduced average claims cycle from 16 days to 9 days.
- Fraud detection signal integration overview.""",
    ),

    Correspondence(
        id="cr005",
        client_id="c002",
        type="email_thread",
        date="2026-05-23",
        subject="Following up from yesterday's webinar — Vantage Insurance",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Aisha Patel <apatel@vantageig.com>
Date: 2026-05-23

Hi Aisha,

Thanks for joining our workflow automation webinar yesterday — great to see such strong engagement from Vantage.

I noticed you asked about Guidewire ClaimCenter integrations during the Q&A. That's a live connector we support out of the box — the most common entry point for claims teams on Guidewire who want to automate straight-through processing without a platform migration.

At Vantage's scale — 14,000+ claims per year — there's likely a meaningful cycle-time improvement available without major infrastructure change. The case study we showed (16 days → 9 days) was a similarly sized regional P&C carrier on ClaimCenter.

Would you be open to a 30-minute discovery call this week? I can share the ClaimCenter integration spec and a relevant case study ahead of time.

Best,
Alex Rivera | Acme Solutions

---
[No reply received as of 2026-05-30.]""",
    ),

    # ── c003: Tom Brennan | Summit EdTech | Prospecting ──────────────────────

    Correspondence(
        id="cr006",
        client_id="c003",
        type="linkedin_message",
        date="2026-05-16",
        subject="LinkedIn cold outreach and response",
        body="""Platform: LinkedIn
Date: 2026-05-16

Alex Rivera → Tom Brennan:
Tom — saw Summit EdTech's growth trajectory (40% YoY is impressive for K-12 SaaS). Quick question: is your team spending meaningful engineering time on data integrations between your LMS, CRM, and support tooling? That's often the hidden tax slowing down product orgs at your stage. Happy to share what we've built for similar EdTech platforms if there's overlap.

Tom Brennan → Alex Rivera:
Interesting — send me more info.

Alex Rivera → Tom Brennan:
Great — will send over an email with a couple of relevant examples. What's the best address?

Tom Brennan → Alex Rivera:
tbrennan@summitedtech.com""",
    ),

    Correspondence(
        id="cr007",
        client_id="c003",
        type="email_thread",
        date="2026-05-19",
        subject="Summit EdTech — integration layer + engineering velocity",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Tom Brennan <tbrennan@summitedtech.com>
Date: 2026-05-19

Hi Tom,

As promised — a couple of things that might be relevant to Summit EdTech.

The pattern I see most often in EdTech platforms at your growth stage: LMS data lives in one silo, CRM in another, support tickets in a third. The product team can't get a unified view of student engagement without engineering doing custom ETL every time someone needs a new report. That backlog pressure kills feature release cadence.

We built a lightweight integration layer specifically for this stack. For a 60-person EdTech company we worked with, it eliminated roughly 30% of unplanned engineering work in the first quarter — hours that went back into product.

Two things attached:
1. EdTech integration architecture overview (2 pages)
2. Case study: how one EdTech customer reduced LMS-CRM sync latency from 24 hours to real-time

Happy to walk through either on a call. No pressure.

Alex

---
[Sent 2026-05-19. No open or reply recorded as of 2026-05-30.]""",
    ),

    # ── c004: Priya Sharma | GlobalEdge Finance | Qualification ──────────────

    Correspondence(
        id="cr008",
        client_id="c004",
        type="linkedin_message",
        date="2026-05-24",
        subject="LinkedIn — warm inbound connection",
        body="""Platform: LinkedIn
Date: 2026-05-24

Alex Rivera → Priya Sharma:
Priya — your profile came up while I was researching Directors of Operations at commercial lenders. We've been working with mid-market finance teams on automating monthly close reporting — the manual consolidation work is usually the first thing they flag. Would it make sense to connect?

Priya Sharma → Alex Rivera:
Yes, this is relevant. I'll send you a note at your work email — easier to share context there.""",
    ),

    Correspondence(
        id="cr009",
        client_id="c004",
        type="email_thread",
        date="2026-05-28",
        subject="Re: Automating financial reporting at GlobalEdge",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Priya Sharma <psharma@globaledge.com>
Date: 2026-05-26

Hi Priya,

Thanks for connecting on LinkedIn. Our platform is built for operations teams in financial services drowning in manual reporting. Most common scenario: data siloed across departments, a monthly close that takes 40+ hours because nothing talks to each other, and audit trails that are a patchwork of spreadsheet versions.

For GlobalEdge — given your SOC 2 Type II posture and asset-based lending model, I'd guess regulatory reporting and cross-portfolio data consolidation are the acute pressure points. Happy to be wrong on the call.

You mentioned evaluating 3 vendors — what should I know about your process going in?

Alex

---

From: Priya Sharma <psharma@globaledge.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-28, 9:47 AM

Alex,

Appreciate the direct framing. The monthly reporting process is a genuine crisis right now — we missed a board reporting deadline two weeks ago because two departments were working off different data cuts. That cannot happen again.

Yes, three vendors. I'm the main evaluator; our CFO signs off on anything over $50k. Six-week timeline ideally.

Can we do 30 minutes next Tuesday at 10 AM CT? I need to understand your data connector story — we have five internal systems that don't talk to each other.

Priya Sharma | Director of Operations, GlobalEdge Finance

---

From: Alex Rivera <alex@acme-solutions.com>
To: Priya Sharma <psharma@globaledge.com>
Date: 2026-05-28, 11:15 AM

Tuesday 10 AM CT works perfectly. Sending a calendar invite now. If you can share the short list of systems ahead of time, I'll make sure we cover every connector on the call.

Alex""",
    ),

    # ── c005: Rafael Mendez | Clearview Media | Qualification ─────────────────

    Correspondence(
        id="cr010",
        client_id="c005",
        type="email_thread",
        date="2026-05-20",
        subject="Campaign reporting consolidation — Clearview Media",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Rafael Mendez <rmendez@clearviewmedia.com>
Date: 2026-05-16

Hi Rafael,

I work with performance marketing agencies managing $100M+ in media spend. The pattern I see repeatedly: reporting fragmented across 6-8 platforms, attribution inconsistencies nobody fully trusts, and ad ops teams spending more time reconciling numbers than optimising campaigns.

Clearview's scale — $220M in managed spend — puts you squarely in the territory where that reconciliation tax becomes a serious margin problem.

Would you be open to 20 minutes?

Alex Rivera | Acme Solutions

---

From: Rafael Mendez <rmendez@clearviewmedia.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-20

Alex — yeah, this is timely. We're mid-GA4 migration and the attribution story is a mess right now. Set up a call.""",
    ),

    Correspondence(
        id="cr011",
        client_id="c005",
        type="phone_call",
        date="2026-05-26",
        subject="Discovery call — 45 minutes",
        body="""[Phone call — 2026-05-26, 2:00 PM EST, ~45 min]
Participants: Alex Rivera (AE, Acme Solutions), Rafael Mendez (SVP Technology, Clearview Media)

Alex: You mentioned the GA4 migration in your email — where does that stand?

Rafael: We were fully on Universal Analytics, built our entire attribution model around it. The GA4 cutover broke our cross-channel view. We're running six different platform reports — Google, Meta, DV360, The Trade Desk, LinkedIn, a couple of publisher direct buys — and nothing reconciles cleanly. My ad ops team of 40 people is spending about 60% of their week just pulling and normalising data. That's not sustainable.

Alex: What does the current reporting workflow look like end to end?

Rafael: Each platform lead pulls their own report weekly, exports to Excel, sends to a central analyst who tries to reconcile across platforms. We have an attribution model in our BI tool but it was built on UA data structures and hasn't been rebuilt for GA4. So right now we're flying blind on true ROAS across channels.

Alex: Are clients questioning the numbers?

Rafael: Constantly. We had a client last month threaten to pull $8M in spend because our ROAS numbers didn't match what they were seeing in Meta. Had to do a manual audit — found a view-through vs click-through attribution window mismatch — but we burned a week to find it. That should be automated.

Alex: Let me show you how we handle that. [Screen share, 20-minute demo]

Rafael: The cross-channel normalisation layer is interesting. How does the GA4 connector work specifically?

Alex: Direct API integration — we pull raw event data, not aggregated GA4 reports, so we can rebuild the attribution model from source. You control attribution windows per channel.

Rafael: That's the right approach. Before we go further, I want to loop in my Head of Ad Ops — Diane Cho. She'd actually live with this day to day. Can we set up a follow-on call with her included?

Alex: Absolutely. I'll wait for your intro.

Rafael: I'll email her today and copy you.

[Call ended 2:47 PM]""",
    ),

    Correspondence(
        id="cr012",
        client_id="c005",
        type="email_thread",
        date="2026-05-26",
        subject="Follow-up: discovery call summary + Diane intro",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Rafael Mendez <rmendez@clearviewmedia.com>
Date: 2026-05-26

Rafael,

Summary from today:

Current state at Clearview:
- 6-platform reporting stack, no unified attribution layer
- Ad ops team spending ~60% of time on manual reconciliation
- GA4 migration broke existing attribution model; no clean cross-channel ROAS
- Recent $8M client escalation traced to attribution window mismatch

What we'd address:
- Unified reporting layer connecting all 6 platforms via API (GA4 raw event data)
- Attribution model rebuilt on normalised events with configurable windows per channel
- Automated reconciliation dashboard replacing the weekly Excel workflow

Next step: Call with you and Diane Cho. Waiting on your intro email.

Alex

---

From: Rafael Mendez <rmendez@clearviewmedia.com>
To: Alex Rivera <alex@acme-solutions.com>, Diane Cho <dcho@clearviewmedia.com>
Date: 2026-05-26

Diane — meet Alex from Acme Solutions. Good call today on consolidating our platform reporting. Their GA4 integration approach is worth a look given where we are with the migration. Can you connect with Alex for a follow-up?

Rafael""",
    ),

    # ── c006: Nadia Kowalski | PureGrow Biotech | Qualification ──────────────

    Correspondence(
        id="cr013",
        client_id="c006",
        type="email_thread",
        date="2026-05-13",
        subject="Regulatory data management for PureGrow's Phase II assets",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Nadia Kowalski <nkowalski@puregrow.com>
Date: 2026-05-10

Nadia,

I've been following PureGrow's pipeline — three Phase II assets with an FDA submission expected within 18 months is an ambitious timeline. The data management challenge at that stage is usually the biggest operational constraint.

The pattern I see in clinical-stage biotechs: trial data scattered across Excel, SharePoint, and lab notebooks, no unified audit trail, and regulatory submission prep taking 2-3x longer than it should because the documentation isn't audit-ready.

We built a platform specifically for 21 CFR Part 11 compliance and eCTD submission prep. Happy to show you a 30-minute demo if any of this sounds familiar.

Alex Rivera | Acme Solutions

---

From: Nadia Kowalski <nkowalski@puregrow.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-13

Alex,

This is directly relevant. Our last FDA submission review was delayed 8 weeks because documentation wasn't audit-ready — we cannot repeat that for the lead compound submission.

Send me a demo invite. I want to bring our Head of Regulatory Affairs as well.

Nadia Kowalski | Director, R&D Operations, PureGrow Biotech""",
    ),

    Correspondence(
        id="cr014",
        client_id="c006",
        type="meeting_notes",
        date="2026-05-21",
        subject="Product demo — PureGrow Biotech",
        body="""Event: Product Demo
Date: 2026-05-21, 10:00 AM EST, ~60 min (Zoom)
Attendees:
  - Nadia Kowalski (Director, R&D Operations) — took notes throughout
  - Dr. Anne Fischer (Head of Regulatory Affairs) — listened, one question at end
  - Alex Rivera (AE, Acme Solutions)
  - Jordan Kim (Solutions Engineer, Acme Solutions)

Demo flow: data ingestion from lab instruments/SharePoint/ELN → audit trail → 21 CFR Part 11 e-signature workflow → eCTD Module 2/3 automated compilation.

Key questions from Nadia:
- "How granular is the audit trail — can you show field-level change history for a specific lab result?" (Answered yes, demonstrated live.)
- "What does the validation package look like for Part 11? Do you have IQ/OQ/PQ documentation?" (Jordan: yes, offered to share post-demo.)
- "Implementation timeline for a company our size?" (Jordan: 10-14 weeks with dedicated CSM.)
- "Can e-signature routing accommodate multi-site sign-off? We have labs in Boston and San Diego." (Confirmed yes, role-based routing supports multi-site.)

From Dr. Fischer (end of call):
- "Have any of your clients been through a successful FDA PAI using your platform?" (Alex: yes, can share reference — needs customer approval first.)

Nadia's close: "This covers the core of what we need. I'll need to bring our CFO in before we move forward on budget. I'll be back in touch."

Post-demo actions:
- Alex: Send IQ/OQ/PQ validation package, Part 11 compliance guide, reference contact request.
- Nadia: Internal discussion with CFO on budget (timeline unknown).""",
    ),

    # ── c007: Sarah Chen | NexaTech Solutions | Proposal ─────────────────────

    Correspondence(
        id="cr015",
        client_id="c007",
        type="phone_call",
        date="2026-05-13",
        subject="Discovery call — NexaTech Solutions",
        body="""[Phone call — 2026-05-13, 11:00 AM PST, ~35 min]
Participants: Alex Rivera (AE, Acme Solutions), Sarah Chen (VP Engineering, NexaTech Solutions)

Alex: You came in from the infrastructure cost landing page — what's driving that search right now?

Sarah: We're scaling fast and our infra spend is scaling faster. Cloud costs growing 4x while revenue grows 2.3x. The main driver is inefficient CI/CD — failed builds still consuming compute, no auto-scaling on test environments, and 12 engineers each spinning up their own environments and forgetting to tear them down.

Alex: What does your CI/CD stack look like today?

Sarah: GitHub Actions for CI, Terraform for IaC, but fairly manual. Three senior engineers who know how it all works. Onboarding a new engineer takes about 3 weeks right now. We had two pipeline failures last sprint that blocked our release for 4 days.

Alex: Four-day delay — what's the downstream impact?

Sarah: We ship weekly. A 4-day delay means the whole release slips. We had to push back a feature a key customer was expecting. That damages relationships.

Alex: Budget context?

Sarah: Approved for Q2. My CTO knows we need to fix this — it's been on the roadmap two quarters. I have authority up to a threshold; anything bigger needs his sign-off.

Alex: I'll send our infra cost optimisation playbook and a case study — 40% CI cost reduction in 90 days. Can we do a demo next week?

Sarah: Yes. Tuesday or Wednesday.

[Call ended 11:36 AM]""",
    ),

    Correspondence(
        id="cr016",
        client_id="c007",
        type="meeting_notes",
        date="2026-05-20",
        subject="Product demo — NexaTech Solutions",
        body="""Event: Product Demo
Date: 2026-05-20, 2:00 PM PST, ~50 min (Zoom)
Attendees:
  - Sarah Chen (VP Engineering, NexaTech) — highly engaged, technical questions throughout
  - Alex Rivera (AE, Acme Solutions)
  - Jordan Kim (SE, Acme Solutions)

Highlights:
- CI/CD cost visibility dashboard: Sarah asked to see cost attribution by engineer and by pipeline — impressed by per-run breakdown.
- Auto-scaling test environments: "This is exactly what we need — right now environments stay warm indefinitely."
- Developer portal / IDP: Showed onboarding checklist and self-service environment provisioning.

Technical questions from Sarah:
- "What are your API rate limits for the GitHub integration?" (Jordan: 10k requests/hour, configurable per plan.)
- "Does the IDP support multi-region deployment? We're planning EU expansion." (Jordan: yes, confirmed with architecture diagram.)
- "Terraform integration — do you wrap it or call it directly?" (Jordan: direct Terraform calls with state file management, no proprietary wrapper.)

Close: Sarah wants to forward the proposal to her CTO before moving forward. "He'll want to see the architecture spec and pricing." Requested a one-page executive summary.

Post-demo actions:
- Alex: Send proposal, architecture spec, executive summary, pricing.
- Sarah: Forward to CTO (Ryan Liu) for review.""",
    ),

    Correspondence(
        id="cr017",
        client_id="c007",
        type="email_thread",
        date="2026-05-25",
        subject="Proposal: Acme Solutions — NexaTech Engineering Platform",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Sarah Chen <schen@nexatech.com>
Date: 2026-05-25

Sarah,

Proposal attached — includes executive summary (1 page), technical architecture + integration spec, 12-month pricing, and two VP Engineering reference contacts.

Scoped to three use cases: CI/CD cost optimisation, auto-scaling test environments, developer onboarding via IDP. Multi-region configuration left for Phase 2 to keep initial scope manageable.

Happy to set up a call with you and your CTO to walk through questions. Just send a time.

Alex

---

From: Sarah Chen <schen@nexatech.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-25

Alex — received. I've forwarded to my CTO (Ryan Liu). He'll review this weekend. Expect to hear back early next week.

Sarah""",
    ),

    # ── c008: Derek Huang | Fortis Capital Partners | Proposal ───────────────

    Correspondence(
        id="cr018",
        client_id="c008",
        type="email_thread",
        date="2026-05-16",
        subject="Portfolio operations platform — Fortis Capital Partners",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Derek Huang <dhuang@fortiscapital.com>
Date: 2026-05-14

Derek,

Lower-middle-market PE firms in your AUM range tend to hit a specific wall: reporting 20+ portfolio companies on different systems, IC decks built manually each quarter, no standardised operational benchmarks to compare holdings.

We built a portfolio operations layer that consolidates KPIs across holdings, automates LP reporting, and gives your deal team a live view of operational health — without requiring portfolio companies to change their own systems.

Worth 30 minutes?

Alex Rivera | Acme Solutions

---

From: Derek Huang <dhuang@fortiscapital.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-16

Alex — yes. This is exactly the problem we're trying to solve for Q3. Send me a calendar link.

Derek""",
    ),

    Correspondence(
        id="cr019",
        client_id="c008",
        type="phone_call",
        date="2026-05-20",
        subject="Discovery + demo call — Fortis Capital Partners",
        body="""[Phone call — 2026-05-20, 9:30 AM EST, ~60 min]
Participants: Alex Rivera (AE, Acme Solutions), Derek Huang (MD Portfolio Operations, Fortis Capital Partners)

Derek: We have 22 portfolio companies. Each CFO sends financials monthly in whatever format they feel like — Excel, PDF, QuickBooks exports. My team spends two weeks every month normalising data before we can do any analysis. Then we build the IC deck manually. That's a 35-person PE firm doing enormous amounts of clerical work.

Alex: How much variance is there in how companies report? Financial KPIs only, or operational metrics too?

Derek: Both — that's the problem. We've started pushing companies to report operational metrics: revenue per employee, gross margin by product line, working capital efficiency. But everyone interprets the definitions differently. No standardisation.

Alex: Do portfolio companies need to change anything on their end?

Derek: Ideally no. Some of these are 50-person businesses. I'm not asking them to implement new ERP just so we can get clean data.

Alex: That's exactly our design assumption. [Proceeds to demo]

Derek: The normalisation engine is interesting. How do you handle completely different chart of accounts structures?

Alex: We map to a master COA on our side. Takes 2-4 hours per company to set up; after that it's automated. We've done it for QuickBooks, Sage, NetSuite, and SAP.

Derek: What about white-labelling? I'd want portfolio company dashboards to show Fortis branding, not Acme.

Alex: I'll confirm current status and timeline with our product team and come back to you on that.

Derek: That's important. Also tell me about the LP reporting module — what formats does it support?

[... continued on LP reporting, data connectors, pricing model ...]

Derek: Send me the proposal.

[Call ended 10:32 AM]""",
    ),

    Correspondence(
        id="cr020",
        client_id="c008",
        type="email_thread",
        date="2026-05-27",
        subject="Re: Proposal — Fortis Capital Portfolio Operations Platform",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Derek Huang <dhuang@fortiscapital.com>
Date: 2026-05-22

Derek,

Proposal attached — scoped for 22 portfolio companies, LP reporting automation, and operational benchmarking dashboard.

On white-labelling: confirmed with product team — custom branding on portfolio company dashboards is available on the Enterprise tier. Full white-label (custom domain) is on the H2 roadmap. I've flagged this explicitly in the proposal so there are no surprises.

Alex

---

From: Derek Huang <dhuang@fortiscapital.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-27

Alex,

Three questions before we can move forward:

1. Data source connectors: The proposal lists QuickBooks, NetSuite, and Sage. We have two portfolio companies on Dynamics 365 Business Central — is that supported or does it require a custom integration?

2. White-labelling: You mention "custom branding" on Enterprise. Does that include the portfolio company-facing dashboard or only the LP reporting interface? Need to be precise.

3. Pricing: Is the per-portfolio-company fee fixed or does it scale with users per company? Some holdings have 5 finance users, others have 1.

These are blocking items. Happy to get on a call to resolve.

Derek Huang | MD Portfolio Operations, Fortis Capital Partners""",
    ),

    # ── c009: Fatima Al-Rashid | Meridian Healthcare Network | Proposal ───────

    Correspondence(
        id="cr021",
        client_id="c009",
        type="phone_call",
        date="2026-05-08",
        subject="Discovery call — Meridian Healthcare Network",
        body="""[Phone call — 2026-05-08, 3:00 PM EST, ~40 min]
Participants: Alex Rivera (AE, Acme Solutions), Fatima Al-Rashid (VP Clinical Informatics, Meridian Healthcare Network)

Fatima: I'll be direct — we ran a 3-month pilot with a competitor last year. It failed on Epic interoperability. Before we go further, I need to know your HL7/FHIR integration story is solid.

Alex: Can you tell me specifically where the competitor failed? FHIR resource mapping, bulk data export, or real-time event streaming?

Fatima: Bulk data export. They claimed full FHIR R4 support but the Clinical Data Repository export was incomplete — missing resource types our quality reporting team depends on.

Alex: Noted. We do bulk FHIR export across all R4 resource types and I can show you our CDR export mapping for Epic. We have 8 live deployments on Epic 2023 or later. Let me send you a technical spec and an intro to our integration team before the demo.

Fatima: Yes. That's the right order.

Alex: What are the primary use cases beyond interoperability?

Fatima: Three things. Clinician documentation burden — our physicians average 3 hours per shift on documentation. Quality reporting for our CMS value-based care programme — we have 4 FTEs dedicated to reporting, which is unsustainable. And care gap identification — we need to surface gaps to PCPs proactively, not 6 months after the fact.

Alex: Strong fit across all three. Let me propose a structured demo scoped to those use cases — week of May 18?

Fatima: Yes. My informatics team lead will join.

[Call ended 3:42 PM]""",
    ),

    Correspondence(
        id="cr022",
        client_id="c009",
        type="meeting_notes",
        date="2026-05-15",
        subject="Technical demo — Meridian Healthcare Network",
        body="""Event: Technical Demo — Epic Integration & Clinical Informatics
Date: 2026-05-15, 2:00 PM EST, ~75 min (Zoom)
Attendees:
  - Fatima Al-Rashid (VP Clinical Informatics)
  - Dr. Ravi Mehta (Informatics Team Lead)
  - Alex Rivera (AE, Acme Solutions)
  - Jordan Kim (SE, Acme Solutions)
  - Priya Anand (Integration Architect, Acme Solutions)

Outcomes by section:

1. Epic FHIR Integration:
   - Priya walked through full FHIR R4 bulk export mapping including CDR resources (Observation, DiagnosticReport, Condition, Procedure).
   - Dr. Mehta tested against Meridian's specific CDR schema — confirmed all required resource types covered.
   - Fatima: "This is what was missing with the other vendor. Good."

2. Clinician documentation (AI-assisted notes):
   - Fatima asked how HIPAA BAA is structured — confirmed BA agreement included in contract.
   - Dr. Mehta raised concern about physician workflow change management and adoption risk.

3. CMS quality reporting:
   - Demo of automated HEDIS measure calculation and direct CMS reporting export.
   - Fatima: "If this eliminates two of the four reporting FTEs, it pays for itself."

4. Care gap identification:
   - Live demo of care gap dashboard fed by FHIR patient data — strong positive reaction.

Post-demo: Proposal sent 2026-05-22.""",
    ),

    Correspondence(
        id="cr023",
        client_id="c009",
        type="email_thread",
        date="2026-05-22",
        subject="Proposal: Acme Solutions — Meridian Healthcare Clinical Informatics",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Fatima Al-Rashid <falrashid@meridianhcn.com>
Date: 2026-05-22

Fatima,

Proposal attached — scoped to Epic FHIR integration + downstream analytics, AI-assisted clinical documentation, and automated CMS quality reporting. BAA included as Exhibit B. Sub-processor list attached separately per your request from the demo.

I know you're at a conference this week — happy to schedule a call for when you're back.

Alex

---
[No reply received. Call to Fatima's office 2026-05-28: assistant confirmed Fatima is at AMIA conference through Friday, returns 2026-06-01.]""",
    ),

    # ── c010: Marcus Williams | Apex Health Systems | Negotiation ─────────────

    Correspondence(
        id="cr024",
        client_id="c010",
        type="email_thread",
        date="2026-04-15",
        subject="Re: Contract v2 — Apex Health Systems / Acme Solutions",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Marcus Williams <mwilliams@apexhealth.com>
Date: 2026-04-10

Marcus,

Attaching updated contract draft. Key changes from v1:
- Section 7.3: Data residency updated to US-only with West Coast data centre commitment
- Exhibit A: BAA terms updated per your legal team's HIPAA requirements
- Section 9.1: Liability cap adjusted to 2x annual contract value

Let me know if legal needs anything else before signature.

Alex

---

From: Marcus Williams <mwilliams@apexhealth.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-04-15

Alex, forwarding to our legal team now. They'll come back to you directly on remaining redlines. I'm supportive of moving forward.

Marcus

---
[No further communication from legal or Marcus until 2026-05-18 check-in call — see below.]""",
    ),

    Correspondence(
        id="cr025",
        client_id="c010",
        type="phone_call",
        date="2026-05-18",
        subject="Check-in call — contract status",
        body="""[Phone call — 2026-05-18, 10:00 AM PST, ~15 min]
Participants: Alex Rivera (AE, Acme Solutions), Marcus Williams (CTO, Apex Health Systems)

Alex: Wanted to check in on where legal stands. It's been a few weeks since the last redline exchange.

Marcus: It's out of my hands. Legal has a full queue — we're also going through HITRUST recertification which is eating bandwidth. I've nudged them twice. No timeline to give you.

Alex: Is there anything specific they're still hung up on? The data residency clause and BAA were the two issues we addressed in the April draft.

Marcus: Data residency is resolved. They have a new question about your sub-processor chain — specifically around the AI/ML vendor for the clinical documentation module. They want disclosure of any sub-processors that touch PHI.

Alex: I can have our full sub-processor list to your legal team by end of day. Would that help move things?

Marcus: Yes. I'll send you the legal contact.

Alex: I also want to flag — we have a competitor in evaluation at a couple of your peer health systems. I don't want to pressure, but I want to make sure we don't lose momentum. Is there anything I can do to help accelerate the review?

Marcus: I'll escalate again internally this week. Sub-processor list will help.

[Call ended 10:16 AM]

Post-call: Alex sent sub-processor list to Apex legal 2026-05-18. No response received as of 2026-05-30.""",
    ),

    # ── c011: Lin Wei | Pacific Freight Solutions | Negotiation ──────────────

    Correspondence(
        id="cr026",
        client_id="c011",
        type="email_thread",
        date="2026-05-10",
        subject="Re: Proposal — Pacific Freight Solutions",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Lin Wei <lwei@pacificfreight.com>
Date: 2026-05-06

Lin,

Formal proposal attached — scoped for ocean freight booking automation, customer visibility portal, and digital invoicing/dispute reduction. Pricing: $190,000 annual, includes implementation and first-year support.

Happy to discuss on a call this week.

Alex

---

From: Lin Wei <lwei@pacificfreight.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-10

Alex,

The functionality is what we need. Three commercial items before we move forward:

1. Pricing: We need to be at $161,500 (15% reduction). Our budget committee approved this project at a $162k ceiling.
2. Payment terms: Our standard is net-60. Your proposal says net-30 — that doesn't work operationally.
3. Implementation: I need a dedicated implementation manager from contract signing. Not shared. Dedicated.

These are not opening positions.

Lin Wei | COO, Pacific Freight Solutions""",
    ),

    Correspondence(
        id="cr027",
        client_id="c011",
        type="phone_call",
        date="2026-05-24",
        subject="Negotiation call — pricing and implementation terms",
        body="""[Phone call — 2026-05-24, 11:00 AM PST, ~30 min]
Participants: Alex Rivera (AE, Acme Solutions), Lin Wei (COO, Pacific Freight Solutions)

Alex: I've gone back to my leadership team on your three points.

On pricing — we can get to $167,000. That's a 12% reduction. Getting to 15% would require cutting implementation scope, and I don't think that serves either of us.

Lin: I said 15%. $167k is not $161.5k. What's the gap?

Alex: $5,500. If we phase the carrier API integrations — top 5 carriers in month one, remaining carriers in month three — I can get to $162k and keep the full platform licence.

Lin: Acceptable on pricing if the remaining carrier integrations are guaranteed in the contract, not best-efforts.

Alex: Agreed — it goes in the SOW.

On net-60 — our standard is net-30 but I can go to net-45.

Lin: Net-45 is workable.

On the dedicated implementation manager — I need your honest answer.

Alex: I need to confirm with our Professional Services team. We've done dedicated IMs for strategic accounts. Can I come back to you by end of week?

Lin: End of week is fine. If it's no, we'll need to find another oversight structure — I'm not running this project with a shared resource.

[Call ended 11:32 AM]""",
    ),

    # ── c012: Carlos Vega | Stellarworks Architecture | Negotiation ───────────

    Correspondence(
        id="cr028",
        client_id="c012",
        type="phone_call",
        date="2026-05-20",
        subject="Verbal agreement call — Stellarworks Architecture",
        body="""[Phone call — 2026-05-20, 2:00 PM EST, ~25 min]
Participants: Alex Rivera (AE, Acme Solutions), Carlos Vega (Managing Partner, Stellarworks Architecture)

Carlos: Alex, I've discussed with my partners. We're ready to move forward. Scope and price work — $48,000 for year one, project profitability and resource utilisation modules, plus the Deltek Vision integration.

Alex: Great to hear. I'll get the contract to your legal team this week. Specific contact, or does it go through you?

Carlos: Our external counsel handles contract review. I'll give you their contact. They're usually quick for a deal this size.

Alex: Any commercial terms I should expect — IP, liability, payment?

Carlos: We always push back on liability caps and IP ownership of any custom configurations. Nothing unusual.

Alex: Understood. I'll send the contract directly to counsel and copy you.

Carlos: And honestly, I've already told the office managers we're moving forward. Just need the paper signed.

[Call ended 2:26 PM]""",
    ),

    Correspondence(
        id="cr029",
        client_id="c012",
        type="email_thread",
        date="2026-05-28",
        subject="Re: Contract redlines — Stellarworks / Acme Solutions",
        body="""From: Michael Torres <counsel@stellarworkslaw.com> [external counsel]
To: Alex Rivera <alex@acme-solutions.com>
CC: Carlos Vega <cvega@stellarworks.com>
Date: 2026-05-28

Alex,

Stellarworks redlines to the MSA attached. Changes are tracked. Summary of material changes:

1. Section 11.2 (Liability Cap): Stellarworks proposes 2x annual contract value rather than 1x as drafted.
2. Section 13.4 (IP Ownership): Stellarworks requests ownership of any custom configuration templates, report formats, or workflows built specifically for Stellarworks during implementation.
3. Section 8.1 (Payment Terms): Net-45 instead of net-30.

These are the only substantive changes.

Michael Torres, Esq. | External Counsel, Stellarworks Architecture

---

From: Carlos Vega <cvega@stellarworks.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-28

Alex — exactly what I flagged on our call. None of this should be a blocker. Let me know what you need from me to close this quickly.

Carlos""",
    ),

    # ── c013: Olivia Torres | CloudFirst Retail | At Risk ─────────────────────

    Correspondence(
        id="cr030",
        client_id="c013",
        type="email_thread",
        date="2026-04-20",
        subject="CloudFirst Retail — evaluation check-in",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Olivia Torres <otorres@cloudfirst.com>
Date: 2026-04-20

Hi Olivia,

Following up on our last conversation — we'd scoped a demo for inventory forecasting and omnichannel experience. Wanted to check if this week or next works for you.

Alex

---
[No reply received.]""",
    ),

    Correspondence(
        id="cr031",
        client_id="c013",
        type="email_thread",
        date="2026-05-04",
        subject="Re: CloudFirst — still on your radar?",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Olivia Torres <otorres@cloudfirst.com>
Date: 2026-05-04

Olivia,

I know things can get busy. I also noticed there was a recent CDO change at CloudFirst — wanted to make sure we're still connected to the right person for this evaluation.

If you're still the right contact, I'd love to reconnect. If not, happy to be pointed in the right direction.

Alex

---
[No reply received.]""",
    ),

    Correspondence(
        id="cr032",
        client_id="c013",
        type="meeting_notes",
        date="2026-05-12",
        subject="Internal note — CloudFirst contact intelligence",
        body="""Date: 2026-05-12
Source: Conversation with Jordan Kim (SE) who has a contact inside CloudFirst.

Intelligence:
- Previous CDO (Daniel Ramos) was the original champion for this evaluation. Left the company ~6 weeks ago.
- Olivia Torres joined as new CDO ~4 weeks ago, hired externally from a competitor retailer.
- Per contact: "Olivia is doing a full audit of active vendor evaluations. Some will be deprioritised."
- Inventory forecasting and omnichannel remain strategic priorities but the new CDO wants to put her own stamp on vendor decisions.
- Olivia has not been seen engaging with any vendor from the previous CDO's pipeline.

Background from earlier evaluation (with prior CDO):
- Pain points discussed: inventory forecasting accuracy below 70%, fragmented customer experience across web/app/store, merchandising decisions lagging 2 weeks behind market signals.
- Two product demos completed; both received positively.

Risk: Two scheduled calls missed without rescheduling (2026-04-28, 2026-05-06).
Assessment: High churn risk. Need to re-establish executive-level relationship with Olivia directly.""",
    ),

    # ── c014: Greg Novak | Axiom Legal Group | At Risk ────────────────────────

    Correspondence(
        id="cr033",
        client_id="c014",
        type="email_thread",
        date="2026-04-22",
        subject="Axiom Legal Group — security questionnaire",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: Greg Novak <gnovak@axiomlegal.com>
Date: 2026-04-15

Greg,

Sending the security questionnaire as requested — standard InfoSec assessment for legal sector deployments. Should take your IT team about 45 minutes. Also attaching our SOC 2 Type II report (2025), penetration test summary, and data retention policy.

Let me know once your team has had a chance to review — happy to get on a call for any questions.

Alex

---

From: Greg Novak <gnovak@axiomlegal.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-04-22

Alex, received. Will get this to my security team. Should have it back within 2 weeks.

Greg

---
[Security questionnaire not returned. No response to follow-up emails on 2026-05-05 and 2026-05-12.]""",
    ),

    Correspondence(
        id="cr034",
        client_id="c014",
        type="meeting_notes",
        date="2026-05-05",
        subject="Internal note — Axiom Legal budget intelligence",
        body="""Date: 2026-05-05
Source: Follow-up call attempt — reached Greg's IT coordinator instead.

Information from coordinator (informal):
- Greg is in the office but "very busy with other things."
- Coordinator mentioned "some discussion about spending this quarter" — declined to elaborate.
- Via indirect network contact: a budget freeze was announced by the CFO covering discretionary technology spend for Q2.
- The Aderant EoL (90 days from original conversation) may not have been escalated to the CFO as an operational risk requiring urgent spend.

Context from earlier engagement:
- Greg had been actively engaged: attended two demos, completed a requirements mapping session, discussed implementation timeline.
- Pain points discussed: Aderant matter management system hitting end-of-life in 90 days, attorneys spending 45 min/day on admin tasks instead of billable work, client portal complaints up 30% this quarter.
- Greg is IT Director, not the economic buyer — COO controls discretionary spend.

Assessment: Budget freeze is a procurement hold, not a product rejection. Path forward likely requires COO engagement, framing Aderant EoL as an operational continuity risk rather than a discretionary purchase.""",
    ),

    # ── c015: David Park | Kinetic Logistics | Closed Won ─────────────────────

    Correspondence(
        id="cr035",
        client_id="c015",
        type="email_thread",
        date="2026-04-30",
        subject="Contract signed — Kinetic Logistics onboarding kickoff",
        body="""From: Alex Rivera <alex@acme-solutions.com>
To: David Park <dpark@kineticlogistics.com>
Date: 2026-04-30

David,

Excited to get started. Your CSM is Ria Nair (rnair@acme-solutions.com) — she'll reach out today to schedule the kickoff call. Implementation target is 8 weeks; week-3 milestones are fleet tracking integration and driver app rollout.

Separately: you mentioned interest in the fleet management add-on — predictive maintenance, fuel efficiency analytics. Worth revisiting once you're stable on the core platform, probably Q3. I'll reconnect then.

Alex

---

From: David Park <dpark@kineticlogistics.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-04-30

Alex, thanks. Ria can reach me directly. And yes — remind me about the fleet management module in Q3.

David""",
    ),

    # ── c016: Yemi Adeyemi | Helix Pharmaceuticals | Closed Won ──────────────

    Correspondence(
        id="cr036",
        client_id="c016",
        type="email_thread",
        date="2026-05-16",
        subject="Re: Helix Pharma — week 2 onboarding status",
        body="""From: Ria Nair <rnair@acme-solutions.com>
To: Yemi Adeyemi <yadeyemi@helixpharma.com>
CC: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-16

Yemi,

Week 2 status:

Completed:
- Veeva CRM integration live, pulling field activity data.
- Territory planning module configured for 3 pilot regions (Southeast, Midwest, Northeast).
- Initial data quality pass complete — flagged 4,200 stale HCP records for your team to review.

In progress:
- SAP order management connector (targeting end of week 3).
- Forecasting model training on 18 months of historical data.

Open item — change management:
You mentioned 3 regional managers are resistant to the new workflow. We recommend a dedicated change management session before full rollout — we have a structured programme for this. Suggest scheduling for week 4, before we go live across the full field team.

Can we get 60 minutes with you and the 3 regional managers in week 4?

Ria Nair | Customer Success Manager, Acme Solutions

---

From: Yemi Adeyemi <yadeyemi@helixpharma.com>
To: Ria Nair <rnair@acme-solutions.com>
CC: Alex Rivera <alex@acme-solutions.com>
Date: 2026-05-16

Ria, good progress. Let's schedule change management for week 4 — I'll get the three regional managers (Dan Cho, Miami; Patricia Osei, Chicago; Kevin Liu, Dallas) on the call. They need to hear directly from your team why this workflow change is worth it. They're protective of their territory numbers.

One more thing: our EU commercial team has been asking about expanding to Germany and UK in H2. Can you flag this to Alex?

Yemi

---

From: Alex Rivera <alex@acme-solutions.com>
To: Yemi Adeyemi <yadeyemi@helixpharma.com>
CC: Ria Nair <rnair@acme-solutions.com>
Date: 2026-05-16

Yemi — great to see onboarding tracking well. The EU expansion is exactly the conversation I want to have with you in Q3. I'll come prepared with a Phase 2 scoping framework. For now, let's make sure the US rollout is solid.

Alex""",
    ),

    # ── c017: Simone Dubois | Luminar Energy | Closed Won ─────────────────────

    Correspondence(
        id="cr037",
        client_id="c017",
        type="email_thread",
        date="2026-04-15",
        subject="Luminar Energy — implementation complete, 30-day check-in",
        body="""From: Ria Nair <rnair@acme-solutions.com>
To: Simone Dubois <sdubois@luminarenergy.com>
CC: Alex Rivera <alex@acme-solutions.com>
Date: 2026-04-15

Simone,

Implementation milestone: all 14 asset sites are now live. Field inspection mobile app deployed to 45 field technicians. Asset maintenance schedule automated and running.

What's live:
- Asset performance management module across 14 solar/wind sites
- Field inspection mobile workflow with offline sync
- NERC regulatory compliance reporting automated

We'd normally schedule a 30-day check-in at this point. Can we get 30 minutes to review adoption metrics and make sure the team is getting value?

Ria Nair | CSM, Acme Solutions

---
[No reply received as of 2026-05-30.]""",
    ),

    # ── c018: Brandon Kirk | Orion Retail Group | Closed Lost ────────────────

    Correspondence(
        id="cr038",
        client_id="c018",
        type="email_thread",
        date="2026-03-29",
        subject="Re: Orion Retail — evaluation decision",
        body="""From: Brandon Kirk <bkirk@orionretail.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-03-29

Alex,

After an extensive evaluation, we've decided to go with RetailEdge. This was a difficult decision — your team and product are strong. The primary factor was their native Shopify integration. Our e-commerce business runs entirely on Shopify and their connector — inventory sync, order routing, fulfilment automation — was purpose-built for our stack in a way that yours isn't currently.

We appreciated the process. If your Shopify integration story changes, we'd be open to revisiting.

Brandon Kirk | Director of IT, Orion Retail Group

---

From: Alex Rivera <alex@acme-solutions.com>
To: Brandon Kirk <bkirk@orionretail.com>
Date: 2026-03-29

Brandon,

Thank you for the honest feedback. Integration depth for Shopify was the gap — that's fair.

For what it's worth, a native Shopify connector is on our Q3 roadmap. When it ships, I'd like to reconnect. I'll hold off on reaching out until there's something concrete to share.

Good luck with the RetailEdge rollout.

Alex""",
    ),

    # ── c019: Helen Marsh | Crestwood Legal Partners | Closed Lost ───────────

    Correspondence(
        id="cr039",
        client_id="c019",
        type="email_thread",
        date="2026-03-01",
        subject="Re: Crestwood Legal — evaluation status",
        body="""From: Helen Marsh <hmarsh@crestwoodlegal.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-03-01

Alex,

I owe you an update. Our firm's management committee made a decision last week to freeze all new software purchases until the start of our next fiscal year (October 2026). This isn't a reflection of Acme's solution — I was personally advocating for moving forward and still believe it's the right tool for us.

The billing dispute and manual time-entry problems aren't going away. We'll be living with them for another 6+ months, which is frustrating. But the decision is final.

I'd like to stay in touch and revisit this in September/October when our new budget cycle opens. Would you be willing to reconnect then?

Helen Marsh | COO, Crestwood Legal Partners

---

From: Alex Rivera <alex@acme-solutions.com>
To: Helen Marsh <hmarsh@crestwoodlegal.com>
Date: 2026-03-01

Helen,

Thank you for the transparency — genuinely appreciated. I know how frustrating it is to identify the right solution and then hit a budget hold.

I'll reach out the week of September 8, 2026 — unless you'd prefer different timing. And I'll keep you posted on any significant product developments in the meantime.

Alex""",
    ),

    # ── c020: Victor Osei | Madera Construction Group | Closed Lost ──────────

    Correspondence(
        id="cr040",
        client_id="c020",
        type="email_thread",
        date="2026-04-15",
        subject="Re: Madera Construction — evaluation decision",
        body="""From: Victor Osei <vosei@maderaconstruction.com>
To: Alex Rivera <alex@acme-solutions.com>
Date: 2026-04-15

Alex,

We've made our decision — going with BuildPro. This was genuinely tough. Your platform is more sophisticated in several areas. But BuildPro had pre-built modules for subcontractor management and safety compliance documentation specific to commercial construction workflows. Building those on Acme's platform would have required significant customisation we couldn't budget for or wait on.

Not about price or relationship. Your team was excellent throughout. Purely a vertical depth issue.

Victor Osei | VP of Operations, Madera Construction Group

---

From: Alex Rivera <alex@acme-solutions.com>
To: Victor Osei <vosei@maderaconstruction.com>
Date: 2026-04-15

Victor,

I appreciate the honest debrief. Subcontractor management and safety docs for construction — that's a real gap on our end, and I understand the decision. I'll share this with our product team.

If things change with BuildPro or your needs expand into areas where we're stronger, I'd welcome the chance to reconnect.

Alex""",
    ),
]


def get_correspondence_for_client(client_id: str) -> List[Correspondence]:
    return sorted(
        [c for c in CORRESPONDENCE if c.client_id == client_id],
        key=lambda c: c.date,
    )
