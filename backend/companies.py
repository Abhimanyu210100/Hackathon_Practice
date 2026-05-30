from dataclasses import dataclass
from typing import List, Optional


@dataclass
class POC:
    name: str
    title: str
    linkedin: str
    phone: str
    email: str


@dataclass
class Company:
    id: str
    name: str
    industry: str
    description: str
    areas_of_interest: List[str]
    size: str          # "1–50", "51–200", "201–1000", "1000+"
    headquarters: str
    poc: POC


COMPANIES: List[Company] = [

    # ── SaaS ──────────────────────────────────────────────────────────────────
    Company(
        id="co001",
        name="NexaTech Solutions",
        industry="SaaS",
        description=(
            "Cloud-native developer tooling platform serving mid-market engineering "
            "teams. Products include CI/CD orchestration, infrastructure-as-code "
            "templates, and an internal developer portal. 300+ customers across North "
            "America and Europe."
        ),
        areas_of_interest=[
            "Infrastructure cost optimisation",
            "Developer experience & onboarding",
            "Observability & incident response",
            "Platform engineering automation",
        ],
        size="201–1000",
        headquarters="Austin, TX",
        poc=POC(
            name="Sarah Chen",
            title="VP of Engineering",
            linkedin="linkedin.com/in/sarah-chen-vpe",
            phone="+1 (512) 304-8821",
            email="schen@nexatech.com",
        ),
    ),
    Company(
        id="co002",
        name="Orbitly",
        industry="SaaS",
        description=(
            "Product analytics and experimentation platform for B2C mobile apps. "
            "Helps growth and product teams run A/B tests, track retention funnels, "
            "and build behavioural cohorts without engineering support. Series B, "
            "60 employees."
        ),
        areas_of_interest=[
            "No-code analytics tooling",
            "Mobile attribution & funnel analysis",
            "Growth experimentation infrastructure",
            "Data warehouse integrations",
        ],
        size="51–200",
        headquarters="San Francisco, CA",
        poc=POC(
            name="Jessica Tran",
            title="Head of Data & Analytics",
            linkedin="linkedin.com/in/jessica-tran-analytics",
            phone="+1 (415) 882-5503",
            email="jtran@orbitly.io",
        ),
    ),

    # ── Healthcare ────────────────────────────────────────────────────────────
    Company(
        id="co003",
        name="Apex Health Systems",
        industry="Healthcare",
        description=(
            "Multi-site regional health network operating 8 hospitals and 40+ "
            "outpatient clinics across the Pacific Northwest. Employs 6,200 clinical "
            "and administrative staff. Active Epic EHR deployment since 2019."
        ),
        areas_of_interest=[
            "Clinical documentation automation",
            "HIPAA-compliant data infrastructure",
            "EHR interoperability & HL7/FHIR integration",
            "Staff workflow optimisation",
        ],
        size="1000+",
        headquarters="Seattle, WA",
        poc=POC(
            name="Marcus Williams",
            title="CTO",
            linkedin="linkedin.com/in/marcus-williams-healthtech",
            phone="+1 (206) 741-9930",
            email="mwilliams@apexhealth.com",
        ),
    ),
    Company(
        id="co004",
        name="Meridian Healthcare Network",
        industry="Healthcare",
        description=(
            "Physician-led independent practice association (IPA) managing value-based "
            "care contracts for 1,100 affiliated physicians across 3 states. Focused on "
            "reducing total cost of care for Medicare Advantage populations."
        ),
        areas_of_interest=[
            "Quality reporting & CMS programme compliance",
            "Population health management",
            "Care gap identification & outreach",
            "Clinician documentation burden reduction",
        ],
        size="201–1000",
        headquarters="Phoenix, AZ",
        poc=POC(
            name="Fatima Al-Rashid",
            title="VP of Clinical Informatics",
            linkedin="linkedin.com/in/fatima-alrashid-clinicalinfo",
            phone="+1 (602) 558-1247",
            email="falrashid@meridianhcn.com",
        ),
    ),

    # ── Financial Services ────────────────────────────────────────────────────
    Company(
        id="co005",
        name="GlobalEdge Finance",
        industry="Financial Services",
        description=(
            "Mid-market commercial lender specialising in asset-based lending and "
            "equipment finance for manufacturing and logistics companies. $2.4B loan "
            "portfolio, 180 employees. SOC 2 Type II certified."
        ),
        areas_of_interest=[
            "Automated financial reporting & close process",
            "Cross-departmental data consolidation",
            "Regulatory audit trail & compliance tooling",
            "Portfolio risk dashboards",
        ],
        size="51–200",
        headquarters="Chicago, IL",
        poc=POC(
            name="Priya Sharma",
            title="Director of Operations",
            linkedin="linkedin.com/in/priya-sharma-finops",
            phone="+1 (312) 490-7754",
            email="psharma@globaledge.com",
        ),
    ),
    Company(
        id="co006",
        name="Fortis Capital Partners",
        industry="Private Equity",
        description=(
            "Lower-middle-market private equity firm with $1.8B AUM across 3 active "
            "funds. Portfolio of 22 operating companies in business services, healthcare "
            "IT, and industrial distribution. 35-person team."
        ),
        areas_of_interest=[
            "Portfolio company KPI consolidation",
            "Operational benchmarking across holdings",
            "Automated LP reporting",
            "Deal pipeline & CRM for origination",
        ],
        size="1–50",
        headquarters="New York, NY",
        poc=POC(
            name="Derek Huang",
            title="Managing Director, Portfolio Operations",
            linkedin="linkedin.com/in/derek-huang-pe",
            phone="+1 (212) 603-4419",
            email="dhuang@fortiscapital.com",
        ),
    ),

    # ── Insurance ─────────────────────────────────────────────────────────────
    Company(
        id="co007",
        name="Vantage Insurance Group",
        industry="Insurance",
        description=(
            "Regional P&C insurer writing commercial lines across the Midwest. "
            "Processes 14,000+ claims per year with a 140-person claims and operations "
            "team. Core system is Guidewire ClaimCenter, implemented 2021."
        ),
        areas_of_interest=[
            "Claims workflow automation & STP",
            "Adjuster workload visibility & routing",
            "Fraud detection & subrogation analytics",
            "Policy data integration & enrichment",
        ],
        size="51–200",
        headquarters="Columbus, OH",
        poc=POC(
            name="Aisha Patel",
            title="VP of Operations",
            linkedin="linkedin.com/in/aisha-patel-insurance-ops",
            phone="+1 (614) 337-8820",
            email="apatel@vantageig.com",
        ),
    ),

    # ── Manufacturing ─────────────────────────────────────────────────────────
    Company(
        id="co008",
        name="BrightPath Manufacturing",
        industry="Manufacturing",
        description=(
            "Tier-2 automotive components manufacturer with 3 plants in the US Midwest. "
            "800 employees, $310M annual revenue. Mid-way through a 3-year digital "
            "transformation programme to replace a 15-year-old SAP R/3 deployment."
        ),
        areas_of_interest=[
            "ERP modernisation & migration",
            "Real-time supply chain visibility",
            "Predictive maintenance & IIoT",
            "Shop-floor data collection & OEE tracking",
        ],
        size="201–1000",
        headquarters="Detroit, MI",
        poc=POC(
            name="James Okonkwo",
            title="Head of Digital Transformation",
            linkedin="linkedin.com/in/james-okonkwo-mfg",
            phone="+1 (313) 882-5567",
            email="jokonkwo@brightpath.com",
        ),
    ),
    Company(
        id="co009",
        name="Madera Construction Group",
        industry="Construction",
        description=(
            "General contractor specialising in commercial and industrial construction "
            "across Texas and the Gulf Coast. $480M revenue, 650 employees, 40+ active "
            "projects at any given time. Self-performing concrete and steel erection."
        ),
        areas_of_interest=[
            "Project cost tracking & EVM",
            "Subcontractor coordination & compliance",
            "Safety documentation & incident reporting",
            "Daily reporting & owner communication portals",
        ],
        size="201–1000",
        headquarters="Houston, TX",
        poc=POC(
            name="Victor Osei",
            title="VP of Operations",
            linkedin="linkedin.com/in/victor-osei-construction",
            phone="+1 (713) 556-2290",
            email="vosei@maderaconstruction.com",
        ),
    ),

    # ── Retail / E-commerce ───────────────────────────────────────────────────
    Company(
        id="co010",
        name="CloudFirst Retail",
        industry="Retail / E-commerce",
        description=(
            "Direct-to-consumer apparel brand with 18 owned stores and a Shopify-based "
            "e-commerce operation generating $95M in annual GMV. Strong loyalty "
            "programme with 1.2M active members. Recently hired a new CDO to lead "
            "omnichannel transformation."
        ),
        areas_of_interest=[
            "Inventory demand forecasting",
            "Omnichannel customer experience",
            "Merchandising analytics & markdowns",
            "Loyalty programme personalisation",
        ],
        size="201–1000",
        headquarters="Los Angeles, CA",
        poc=POC(
            name="Olivia Torres",
            title="Chief Digital Officer",
            linkedin="linkedin.com/in/olivia-torres-retail",
            phone="+1 (310) 774-6638",
            email="otorres@cloudfirst.com",
        ),
    ),
    Company(
        id="co011",
        name="Orion Retail Group",
        industry="Retail / E-commerce",
        description=(
            "Multi-brand home goods retailer operating 12 brick-and-mortar locations "
            "and a growing Shopify storefront. $78M revenue, 310 employees. Currently "
            "migrating from a legacy Magento 1 platform."
        ),
        areas_of_interest=[
            "E-commerce platform integration & migration",
            "Inventory sync across warehouse & storefront",
            "Order management & fulfilment automation",
            "Unified reporting across locations",
        ],
        size="201–1000",
        headquarters="Atlanta, GA",
        poc=POC(
            name="Brandon Kirk",
            title="Director of IT",
            linkedin="linkedin.com/in/brandon-kirk-retail-it",
            phone="+1 (404) 821-3347",
            email="bkirk@orionretail.com",
        ),
    ),

    # ── Logistics ─────────────────────────────────────────────────────────────
    Company(
        id="co012",
        name="Kinetic Logistics",
        industry="Logistics & Supply Chain",
        description=(
            "Asset-based trucking and last-mile delivery company operating a fleet of "
            "380 trucks across the Southeast. $145M revenue, 900 employees including "
            "420 drivers. TMS is McLeod, integrated with a legacy in-house dispatch tool."
        ),
        areas_of_interest=[
            "Real-time fleet tracking & visibility",
            "Driver communication & compliance (ELD)",
            "Route optimisation & fuel efficiency",
            "Customer self-service shipment portals",
        ],
        size="201–1000",
        headquarters="Nashville, TN",
        poc=POC(
            name="David Park",
            title="VP of Technology",
            linkedin="linkedin.com/in/david-park-logistics-tech",
            phone="+1 (615) 443-9901",
            email="dpark@kineticlogistics.com",
        ),
    ),
    Company(
        id="co013",
        name="Pacific Freight Solutions",
        industry="Logistics & Supply Chain",
        description=(
            "Non-vessel operating common carrier (NVOCC) specialising in trans-Pacific "
            "ocean freight. Manages 4,200 TEUs per month, 280 employees. Heavy reliance "
            "on manual email-based booking and invoicing workflows."
        ),
        areas_of_interest=[
            "Ocean freight rate management & booking automation",
            "Customer visibility portal & tracking",
            "Digital freight invoicing & billing dispute reduction",
            "Carrier API integrations",
        ],
        size="51–200",
        headquarters="Long Beach, CA",
        poc=POC(
            name="Lin Wei",
            title="COO",
            linkedin="linkedin.com/in/lin-wei-freight",
            phone="+1 (562) 990-4422",
            email="lwei@pacificfreight.com",
        ),
    ),

    # ── Media & Advertising ───────────────────────────────────────────────────
    Company(
        id="co014",
        name="Clearview Media",
        industry="Media & Advertising",
        description=(
            "Independent performance marketing agency managing $220M in annual media "
            "spend for 35 enterprise clients across retail, travel, and financial "
            "services. Team of 190, with a 40-person ad operations function."
        ),
        areas_of_interest=[
            "Cross-channel campaign reporting & attribution",
            "Ad ops automation & reconciliation",
            "First-party data strategy & clean rooms",
            "GA4 migration & measurement modernisation",
        ],
        size="51–200",
        headquarters="New York, NY",
        poc=POC(
            name="Rafael Mendez",
            title="SVP of Technology",
            linkedin="linkedin.com/in/rafael-mendez-adtech",
            phone="+1 (212) 877-5541",
            email="rmendez@clearviewmedia.com",
        ),
    ),

    # ── Biotechnology ─────────────────────────────────────────────────────────
    Company(
        id="co015",
        name="PureGrow Biotech",
        industry="Biotechnology",
        description=(
            "Clinical-stage biotech developing next-generation antibody therapies for "
            "autoimmune diseases. 3 assets in Phase II trials, 210 employees. FDA "
            "submission for lead compound expected within 18 months."
        ),
        areas_of_interest=[
            "21 CFR Part 11 compliant data management",
            "Electronic Trial Master File (eTMF)",
            "Regulatory submission preparation & eCTD",
            "Lab data integration & audit trail",
        ],
        size="51–200",
        headquarters="Boston, MA",
        poc=POC(
            name="Nadia Kowalski",
            title="Director of R&D Operations",
            linkedin="linkedin.com/in/nadia-kowalski-biotech",
            phone="+1 (617) 392-8874",
            email="nkowalski@puregrow.com",
        ),
    ),

    # ── Education Technology ──────────────────────────────────────────────────
    Company(
        id="co016",
        name="Summit EdTech",
        industry="Education Technology",
        description=(
            "EdTech platform serving K-12 school districts with adaptive learning "
            "software and professional development tools. 60 employees, 400 district "
            "customers representing 1.2M students. Series A, growing 40% YoY."
        ),
        areas_of_interest=[
            "Student engagement & learning outcome analytics",
            "LMS, CRM, and support tool integration",
            "Engineering velocity & feature release cadence",
            "District administrator reporting dashboards",
        ],
        size="51–200",
        headquarters="Denver, CO",
        poc=POC(
            name="Tom Brennan",
            title="Chief Product Officer",
            linkedin="linkedin.com/in/tom-brennan-edtech",
            phone="+1 (303) 541-7723",
            email="tbrennan@summitedtech.com",
        ),
    ),

    # ── Legal Services ────────────────────────────────────────────────────────
    Company(
        id="co017",
        name="Axiom Legal Group",
        industry="Legal Services",
        description=(
            "Mid-size litigation and corporate law firm with 120 attorneys across "
            "4 offices. Current matter management system (Aderant) reaches end-of-life "
            "in 90 days. Under review for a full practice management platform replacement."
        ),
        areas_of_interest=[
            "Matter lifecycle management",
            "Time capture & billing automation",
            "Client portal & secure document exchange",
            "Conflict-of-interest checking",
        ],
        size="51–200",
        headquarters="Washington, D.C.",
        poc=POC(
            name="Greg Novak",
            title="Director of IT",
            linkedin="linkedin.com/in/greg-novak-legalops",
            phone="+1 (202) 664-8830",
            email="gnovak@axiomlegal.com",
        ),
    ),
    Company(
        id="co018",
        name="Crestwood Legal Partners",
        industry="Legal Services",
        description=(
            "Boutique corporate and M&A firm with 55 attorneys. Strong reputation in "
            "private equity transaction work. Billing disputes and manual time-entry "
            "errors have been a persistent operational pain point for 3 years."
        ),
        areas_of_interest=[
            "Automated time capture & billing accuracy",
            "Matter profitability visibility",
            "Client self-service portal",
            "Knowledge management & precedent search",
        ],
        size="51–200",
        headquarters="Boston, MA",
        poc=POC(
            name="Helen Marsh",
            title="COO",
            linkedin="linkedin.com/in/helen-marsh-legalops",
            phone="+1 (617) 780-5512",
            email="hmarsh@crestwoodlegal.com",
        ),
    ),

    # ── Pharmaceuticals ───────────────────────────────────────────────────────
    Company(
        id="co019",
        name="Helix Pharmaceuticals",
        industry="Pharmaceuticals",
        description=(
            "Specialty pharma company with a commercial-stage portfolio of 6 branded "
            "products and a field sales force of 200 reps. $1.1B revenue. CRM is "
            "Veeva, integrated with SAP for order management. Forecasting accuracy "
            "has been a recurring issue with their S&OP process."
        ),
        areas_of_interest=[
            "Field sales territory planning & optimisation",
            "CRM adoption & data quality",
            "Commercial forecasting & S&OP analytics",
            "Speaker programme & HCP engagement tracking",
        ],
        size="1000+",
        headquarters="New Jersey, NJ",
        poc=POC(
            name="Yemi Adeyemi",
            title="Head of Commercial Operations",
            linkedin="linkedin.com/in/yemi-adeyemi-pharma",
            phone="+1 (908) 334-7761",
            email="yadeyemi@helixpharma.com",
        ),
    ),

    # ── Energy ────────────────────────────────────────────────────────────────
    Company(
        id="co020",
        name="Luminar Energy",
        industry="Energy & Utilities",
        description=(
            "Independent power producer operating 14 utility-scale solar and wind "
            "assets across the Southwest. 320 employees, 4.2 GW of installed capacity. "
            "Asset management and O&M teams currently rely on spreadsheets and "
            "email-based field inspection workflows."
        ),
        areas_of_interest=[
            "Asset performance management & CMMS",
            "Field inspection mobile workflows",
            "Regulatory compliance reporting automation",
            "Generation forecasting & curtailment analysis",
        ],
        size="201–1000",
        headquarters="Scottsdale, AZ",
        poc=POC(
            name="Simone Dubois",
            title="VP of Asset Management",
            linkedin="linkedin.com/in/simone-dubois-energy",
            phone="+1 (480) 661-3398",
            email="sdubois@luminarenergy.com",
        ),
    ),

    # ── Professional Services ─────────────────────────────────────────────────
    Company(
        id="co021",
        name="Stellarworks Architecture",
        industry="Professional Services",
        description=(
            "Architecture and interior design firm with 3 studios in New York, Miami, "
            "and Chicago. 95 staff, $38M revenue. Active portfolio of 60+ commercial "
            "and mixed-use projects. Project accounting handled in Deltek Vision."
        ),
        areas_of_interest=[
            "Project profitability & EVM",
            "Resource utilisation & capacity planning",
            "Client reporting & milestone tracking",
            "Studio collaboration & document management",
        ],
        size="51–200",
        headquarters="New York, NY",
        poc=POC(
            name="Carlos Vega",
            title="Managing Partner",
            linkedin="linkedin.com/in/carlos-vega-architecture",
            phone="+1 (212) 540-8834",
            email="cvega@stellarworks.com",
        ),
    ),
]


def get_all_companies() -> List[Company]:
    return COMPANIES


def get_company_by_id(company_id: str) -> Optional[Company]:
    return next((c for c in COMPANIES if c.id == company_id), None)


def get_company_by_name(name: str) -> Optional[Company]:
    return next((c for c in COMPANIES if c.name.lower() == name.lower()), None)
