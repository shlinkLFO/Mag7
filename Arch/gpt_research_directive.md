# MAG7 Spending Research Directive for GPT

## Mission
Expand the MAG7 spending dataset (`mag7_spending.json`) by finding missing investment records across 40+ domains for Apple, Microsoft, Alphabet, Amazon, NVIDIA, Tesla, and Meta from 2015-2025.

---

## Current Dataset Status (as of Nov 2024)

### Coverage Summary
- **Total Records**: 150 entries
- **Total Documented Spending**: $1,423.52B
- **Average Documentation Rate**: 71.1%
- **Records Missing Amounts**: 43 (28.9%)
- **Active Domains**: 30 (out of 30 tracked)

### Company Spending Overview
| Company | Records | Documented ($B) | Doc Rate |
|---------|---------|-----------------|----------|
| Apple | 22 | 609.10 | 63.6% |
| Amazon | 28 | 268.44 | 85.7% |
| Meta | 22 | 220.28 | 63.6% |
| Microsoft | 22 | 154.75 | 86.4% |
| Alphabet | 23 | 117.42 | 65.2% |
| Tesla | 16 | 30.63 | 62.5% |
| NVIDIA | 17 | 22.90 | 70.6% |

### Top Priority Domains (High Activity, Low Documentation)
1. **security_cryptography** - 8 records, 37.5% doc rate, $35.40B
2. **circularity_reuse_recycling** - 9 records, 44.4% doc rate, ~$1B
3. **batteries_and_storage** - 10 records, 50.0% doc rate, $19.56B
4. **ai_efficiency_methods** - 10 records, 50.0% doc rate, $8.80B
5. **quantum_computing** - 6 records, 50.0% doc rate, $1.80B

### Critically Under-Documented Domains (Single-Company or Low Coverage)
- **superconducting_devices_squids** - 1 record, 0% doc rate (Alphabet only)
- **edge_computing_infrastructure** - 1 record, 100% doc rate (Amazon only)
- **supply_chain_digitization** - 1 record, 100% doc rate (Apple only)
- **wellness_vr_and_behavioral** - 1 record, 100% doc rate (Meta only)
- **gaming_platforms_engines** - 1 record, 100% doc rate (Microsoft only)
- **regulatory_compliance_investments** - 1 record, 100% doc rate (Meta only)
- **litigation_settlements_fines** - 2 records, 100% doc rate (Meta only)
- **5g_6g_network_infrastructure** - 2 records, 100% doc rate (Apple, Microsoft)

---

## Research Targets by Company

### Apple (22 records, 63.6% doc rate)
**Missing Domains (11 total):**
- `bio_ai_and_drug_discovery`
- `edge_computing_infrastructure`
- `gaming_platforms_engines`
- `litigation_settlements_fines`
- `quantum_computing`
- `regulatory_compliance_investments`
- `superconducting_devices_squids`
- `wellness_vr_and_behavioral`
- Plus 3 others

**Weak/Null Amount Domains:**
- `ai_foundation_models` - 1 record, null amount
- `batteries_and_storage` - 1 record, null amount
- `circularity_reuse_recycling` - 1 record, null amount
- `digital_health_devices` - 1 record, null amount
- `security_cryptography` - 1 record, null amount

### Microsoft (22 records, 86.4% doc rate)
**Missing Domains (12 total):**
- `bio_ai_and_drug_discovery`
- `content_production_studios`
- `edge_computing_infrastructure`
- `litigation_settlements_fines`
- `regulatory_compliance_investments`
- `satellite_and_subsea_infrastructure`
- `sci_fi_consumer_devices`
- `superconducting_devices_squids`
- `wellness_vr_and_behavioral`
- `xr_metaverse_and_spatial_computing`
- Plus 2 others

**Weak/Null Amount Domains:**
- `ai_efficiency_methods` - 1 record, null amount
- `batteries_and_storage` - 1 record, null amount
- `digital_inclusion_and_economy` - 1 record, null amount (needs update)

### Alphabet (23 records, 65.2% doc rate)
**Missing Domains (15 total):**
- `5g_6g_network_infrastructure`
- `cloud_data_centers_ai_infra`
- `content_production_studios`
- `edge_computing_infrastructure`
- `gaming_platforms_engines`
- `litigation_settlements_fines`
- `regulatory_compliance_investments`
- `sci_fi_consumer_devices`
- `semiconductor_ai_hardware`
- `supply_chain_digitization`
- `wellness_vr_and_behavioral`
- `workforce_training_reskilling`
- Plus 3 others

**Weak/Null Amount Domains:**
- `ai_efficiency_methods` - 2 records, 1 null amount
- `batteries_and_storage` - 1 record, null amount
- `circularity_reuse_recycling` - 1 record, null amount
- `quantum_computing` - 2 records, 2 null amounts
- `security_cryptography` - 3 records, 1 null amount
- `superconducting_devices_squids` - 1 record, null amount
- `xr_metaverse_and_spatial_computing` - 1 record, null amount

### Amazon (28 records, 85.7% doc rate)
**Missing Domains (11 total):**
- `5g_6g_network_infrastructure`
- `bio_ai_and_drug_discovery`
- `digital_inclusion_and_economy`
- `gaming_platforms_engines`
- `litigation_settlements_fines`
- `regulatory_compliance_investments`
- `superconducting_devices_squids`
- `supply_chain_digitization`
- `wellness_vr_and_behavioral`
- `workforce_training_reskilling` (needs update)
- `xr_metaverse_and_spatial_computing`

**Weak/Null Amount Domains:**
- `renewable_energy_generation` - 2 records, 1 null amount
- `robotics_autonomy` - 2 records, 1 null amount (needs update)
- `security_cryptography` - 1 record, null amount
- `sci_fi_consumer_devices` - 1 record, null amount

### NVIDIA (17 records, 70.6% doc rate)
**Missing Domains (18 total):**
- `5g_6g_network_infrastructure`
- `batteries_and_storage`
- `content_production_studios`
- `digital_health_devices`
- `digital_inclusion_and_economy`
- `diversity_equity_inclusion`
- `edge_computing_infrastructure`
- `gaming_platforms_engines`
- `litigation_settlements_fines`
- `regulatory_compliance_investments`
- `responsible_ai_safety_governance`
- `satellite_and_subsea_infrastructure`
- `sci_fi_consumer_devices`
- `supply_chain_digitization`
- `superconducting_devices_squids`
- `wellness_vr_and_behavioral`
- `workforce_training_reskilling`
- `xr_metaverse_and_spatial_computing`

**Weak/Null Amount Domains:**
- `ai_efficiency_methods` - 2 records, 1 null amount
- `cloud_data_centers_ai_infra` - 2 records, 1 null amount
- `renewable_energy_generation` - 1 record, null amount
- `robotics_autonomy` - 2 records, 1 null amount
- `security_cryptography` - 1 record, null amount

### Tesla (16 records, 62.5% doc rate)
**Missing Domains (22 total):**
- `5g_6g_network_infrastructure`
- `ai_foundation_models`
- `bio_ai_and_drug_discovery`
- `circularity_reuse_recycling` (1 record, null amount)
- `content_production_studios`
- `digital_health_devices`
- `digital_inclusion_and_economy`
- `diversity_equity_inclusion` (1 record, null amount)
- `edge_computing_infrastructure`
- `gaming_platforms_engines`
- `litigation_settlements_fines`
- `quantum_computing`
- `regulatory_compliance_investments`
- `responsible_ai_safety_governance`
- `satellite_and_subsea_infrastructure`
- `sci_fi_consumer_devices`
- `security_cryptography`
- `supply_chain_digitization`
- `superconducting_devices_squids`
- `wellness_vr_and_behavioral`
- `workforce_training_reskilling`
- `xr_metaverse_and_spatial_computing`

**Weak/Null Amount Domains:**
- `batteries_and_storage` - 6 records, 2 null amounts
- `renewable_energy_generation` - 2 records, 1 null amount
- `robotics_autonomy` - 1 record, null amount

### Meta (22 records, 63.6% doc rate)
**Missing Domains (13 total):**
- `5g_6g_network_infrastructure`
- `autonomous_mobility`
- `batteries_and_storage`
- `bio_ai_and_drug_discovery`
- `content_production_studios`
- `digital_health_devices`
- `edge_computing_infrastructure`
- `gaming_platforms_engines`
- `quantum_computing`
- `supply_chain_digitization`
- `superconducting_devices_squids`
- `workforce_training_reskilling`
- Plus 1 other

**Weak/Null Amount Domains:**
- `ai_efficiency_methods` - 1 record, null amount
- `circularity_reuse_recycling` - 2 records, 2 null amounts
- `renewable_energy_generation` - 1 record, null amount
- `responsible_ai_safety_governance` - 2 records, 1 null amount
- `robotics_autonomy` - 1 record, null amount
- `security_cryptography` - 1 record, null amount
- `semiconductor_ai_hardware` - 1 record, null amount
- `xr_metaverse_and_spatial_computing` - 2 records, 1 null amount

---

## JSON Schema Reference

### Required Fields
```json
{
  "investment_amount_billions_usd": 4.0,  // or null
  "year": 2023,                           // or null
  "initiatives": ["Label 1", "Label 2"],
  "notes": "Context and caveats",
  "source_figure": "Key quote/paraphrase",
  "links": ["primary-source", "secondary"],
  "spend_type": "capex",                  // r_and_d, capex, equity, fund, ppa, pledge, opex, other
  "timeframe": {"start": 2023, "end": 2025},  // optional
  "amount_basis": "multi_year_commitment",     // optional
  "certainty": "company_guidance",             // optional
  "is_rollup": false
}
```

### Spend Type Definitions
- **r_and_d**: Internal research and development
- **capex**: Capital expenditures (buildings, equipment, infrastructure)
- **equity**: Acquisitions, stakes, investments in other companies
- **fund**: Venture capital funds, innovation funds
- **ppa**: Power purchase agreements (renewable energy)
- **opex**: Operating expenses (ongoing costs)
- **M&A**: Mergers and acquisitions (use `equity` for consistency)
- **Venture**: Venture investments (use `equity` for consistency)
- **CapEx**: Capital expenditures (use lowercase `capex` for consistency)
- **other**: Doesn't fit above categories

**Note**: Prefer lowercase variants (`capex`, `equity`) for consistency.

---

## Search Strategy

### Priority 1: Expand Single-Company Domains
Focus on domains with only 1-2 companies but expected broader activity:

**Edge Computing Infrastructure** (1 company: Amazon)
- Target: Microsoft, Alphabet, Meta, Apple
- `{company} edge data center investment`
- `{company} CDN expansion capex`
- `{company} edge AI infrastructure`

**Supply Chain Digitization** (1 company: Apple)
- Target: Amazon, Tesla, Microsoft
- `{company} digital twin supply chain investment`
- `{company} blockchain supply chain pilot`
- `{company} IoT logistics investment`

**Wellness VR and Behavioral** (1 company: Meta)
- Target: Apple, Alphabet
- `{company} VR fitness investment`
- `{company} wellness app development`
- `{company} behavioral health technology`

**Gaming Platforms/Engines** (1 company: Microsoft)
- Target: Meta, Apple, Amazon, Alphabet
- `{company} game engine development`
- `{company} cloud gaming infrastructure`
- `{company} gaming platform investment`

**Regulatory Compliance Investments** (1 company: Meta)
- Target: Alphabet, Amazon, Apple, Microsoft
- `{company} compliance infrastructure investment`
- `{company} content moderation spending`
- `{company} privacy engineering budget`

**5G/6G Network Infrastructure** (2 companies: Apple, Microsoft)
- Target: Alphabet, Amazon, NVIDIA
- `{company} 5G network investment`
- `{company} private 5G deployment cost`
- `{company} spectrum auction bid`

### Priority 2: Update High-Activity Domains with Null Amounts
Target records that exist but lack dollar figures (43 null amounts total):

**Security Cryptography** (5 null amounts, 37.5% doc rate)
- Apple: PQ3 protocol development → R&D estimate
- Amazon: AWS Clean Rooms → infrastructure cost
- Alphabet: ID Quantique acquisition → deal value
- Meta: WhatsApp encryption → engineering budget
- NVIDIA: cuPQC development → R&D allocation

**Circularity/Reuse/Recycling** (5 null amounts, 44.4% doc rate)
- Apple: Daisy/Dave robots → development cost
- Alphabet: Zero-waste data centers → infrastructure investment
- Meta: Data center waste diversion (2 records) → program costs
- Tesla: Battery recycling → facility investment

**Batteries and Storage** (5 null amounts, 50.0% doc rate)
- Apple: CATL/BYD talks → any disclosed amounts
- Microsoft: Group14 participation → specific check
- Alphabet: Project Malta → X lab funding
- Tesla: 4680 production (2 records) → capex breakdown

**AI Efficiency Methods** (5 null amounts, 50.0% doc rate)
- Apple: RAG research → R&D allocation
- Microsoft: LoRA development → research budget
- Alphabet: REALM → AI research funding
- Meta: RAG/DPR → FAIR budget allocation
- NVIDIA: NeMo framework → platform R&D

**Quantum Computing** (3 null amounts, 50.0% doc rate)
- Alphabet: Quantum AI campus → "several billion" estimate
- Alphabet: Willow chip → development cost
- Amazon: Braket service → platform investment

### Priority 3: Company-Specific High-Value Targets

**Apple:**
- Apple Silicon R&D costs (2020-2025)
- Apple Pay infrastructure investment
- iCloud data center capex (post-2023)
- Apple Store expansion (2020-2025)

**Microsoft:**
- Activision Blizzard integration costs ($68.7B acquisition + integration)
- Azure Edge Zones investment
- LinkedIn Learning content budget
- GitHub Copilot infrastructure

**Alphabet:**
- YouTube content/infrastructure spend (annual)
- Waymo updated cumulative (beyond $30B)
- Subsea cables: Equiano, Grace Hopper, Firmina (individual costs)
- Google Fiber expansion

**Amazon:**
- AWS edge locations capex
- Fulfillment center robotics (beyond $1B estimate)
- One Medical integration costs
- Amazon Pharmacy infrastructure

**NVIDIA:**
- TSMC capacity reservations
- NVIDIA DRIVE automotive platform
- Omniverse cloud infrastructure
- Own data center capex

**Tesla:**
- Gigafactory Texas/Berlin expansion (detailed)
- Optimus development budget
- Megapack factory network (beyond Shanghai)
- Dojo Phase 2+ expansion

**Meta:**
- 2Africa subsea cable (Meta's share)
- MTIA chip development costs
- Content moderation infrastructure
- Instagram/WhatsApp infrastructure

---

## Source Hierarchy

### Tier 1: Company Filings (Highest Priority)
- 10-K/10-Q annual/quarterly reports
- 8-K material event filings
- Proxy statements
- Investor presentations
- Earnings call transcripts

### Tier 2: Official Company Sources
- Press releases (company newsrooms)
- Corporate blogs
- Sustainability/ESG reports
- Annual impact reports

### Tier 3: Financial Press
- Reuters, Bloomberg, WSJ, Financial Times
- Industry analysts (Gartner, IDC, Omdia)
- Regulatory filings (FTC, DOJ, EU Commission)

### Tier 4: Secondary Sources
- TechCrunch, The Verge, Ars Technica
- Industry trade publications
- Academic papers (for R&D context)
- Patent databases (for R&D signals)

---

## Search Query Templates

### For Missing Domains
```
{company} {domain_keyword} investment {year}
{company} {domain_keyword} spending {year}
{company} announces {amount} {domain_keyword}
{company} commits {amount} to {domain_keyword}
site:sec.gov {company} 10-K {domain_keyword}
site:{company}.com/newsroom {domain_keyword} investment
```

### For Updating Null Amounts
```
{company} {specific_initiative} cost
{company} {specific_initiative} budget
{company} {specific_initiative} capex
{company} {specific_initiative} investment amount
```

### For Time Series Updates
```
{company} {domain} 2024 spending
{company} {domain} 2025 guidance
{company} fiscal year {year} capex breakdown
{company} Q{1-4} {year} earnings {domain}
```

---

## Quality Control Checklist

Before adding a record, verify:
- [ ] Amount is in billions USD (convert if needed)
- [ ] Year is announcement/commitment year (not project completion)
- [ ] No duplicate exists (check company + domain + year + initiatives)
- [ ] Source is credible (prefer Tier 1-2)
- [ ] Spend type is classified
- [ ] Notes explain any caveats or estimates
- [ ] Links include primary source first

For amounts >$1B, additionally verify:
- [ ] Primary source identified
- [ ] Timeframe clarified (single-year vs multi-year)
- [ ] Amount basis specified (spend vs commitment vs valuation)
- [ ] Certainty level indicated

---

## Red Flags to Avoid

- Round numbers without attribution ($10B, $5B in blogs)
- "Up to" language without minimum commitment
- Conflicting figures across sources (investigate discrepancy)
- Stale data republished without date context
- Aggregations mixing spend types (R&D + capex + equity)
- Third-party estimates without methodology

---

## Output Format

When proposing new records, provide:

1. **Company**: [Name]
2. **Domain**: [domain_key]
3. **Amount**: [number or null]
4. **Year**: [year or null]
5. **Initiatives**: [list]
6. **Notes**: [context]
7. **Source Figure**: [quote]
8. **Links**: [URLs]
9. **Spend Type**: [type]
10. **Certainty**: [level]
11. **Justification**: Why this record should be added

---

## Success Metrics

Target outcomes for next research phase:
- Reduce null amounts from 28.9% to <20% (43 → <30 records)
- Add at least 3 companies to each single-company domain
- Achieve 50+ new records across all companies (150 → 200+)
- Increase average documentation rate from 71.1% to >80%
- Fill all single-company domain gaps (8 domains currently at 1-2 companies)
- Update all "unspecified" spend_type entries (currently 9 records)

---

## Domain Reference (30 Active Domains)

### Core AI & Compute (4)
ai_foundation_models, ai_efficiency_methods, semiconductor_ai_hardware, cloud_data_centers_ai_infra

### Quantum & Advanced Physics (2)
quantum_computing, superconducting_devices_squids

### Automation & Robotics (3)
robotics_autonomy, autonomous_mobility, industrial_automation_supply_chain

### Energy, Climate & Materials (3)
batteries_and_storage, renewable_energy_generation, circularity_reuse_recycling

### Health, Bio & Wellbeing (3)
digital_health_devices, bio_ai_and_drug_discovery, wellness_vr_and_behavioral

### Connectivity & Digital Economy (2)
satellite_and_subsea_infrastructure, digital_inclusion_and_economy

### Trust, Governance & Society (3)
security_cryptography, responsible_ai_safety_governance, diversity_equity_inclusion

### Experiential / Sci-Fi Products (2)
xr_metaverse_and_spatial_computing, sci_fi_consumer_devices

### Edge Computing, Network & Supply Chain (3)
edge_computing_infrastructure, 5g_6g_network_infrastructure, supply_chain_digitization

### Content, Media & Gaming (2)
content_production_studios, gaming_platforms_engines

### Workforce Development (1)
workforce_training_reskilling

### Legal, Regulatory & Compliance (2)
regulatory_compliance_investments, litigation_settlements_fines

---

## Timeline Focus: 2015-2025

### Era-Specific Search Patterns

**2015-2017: Cloud Infrastructure Buildout**
- Data center capex, cloud region expansion
- Search: `{company} data center investment 2015-2017`

**2018-2019: AI Awakening**
- ML infrastructure, TPU/GPU clusters, AI acquisitions
- Search: `{company} AI research investment 2018-2019`

**2020-2021: Pandemic Acceleration**
- Remote work infrastructure, supply chain resilience
- Search: `{company} pandemic response investment 2020`

**2022-2023: Generative AI Gold Rush**
- Foundation models, GPU procurement, AI safety
- Search: `{company} generative AI investment 2022-2023`

**2024-2025: AI Infrastructure & Energy**
- Massive data center expansion, energy solutions
- Search: `{company} 2024 capex guidance`, `{company} energy infrastructure 2025`

---

## Begin Research

Start with Priority 1 domains (zero records) for companies with ●●● or ●● expected activity. Use SEC filings and company newsrooms as primary sources. Document all findings with proper citations and certainty levels.

