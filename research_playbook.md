# MAG7 Deep Research Playbook

This document instructs deep-research agents and models how to search the web and append structured information to `mag7_spending_reorganized.json`.

The goal is to expand and refine the dataset of **R&D and investment events** across the MAG7:

- Apple
- Microsoft
- Alphabet (Google)
- Amazon
- NVIDIA
- Tesla
- Meta

The working dataset is a JSON file with the structure documented in `schema.md`.

---

## 1. Core principles

1. **Prioritize factual, attributable spend**  
   Target events that are:
   - Explicitly quantified in a credible source, **or**
   - Clearly real but unquantified (then store `investment_amount_billions_usd = null`).

2. **Respect the schema and avoid double counting**  
   - Each record must belong to exactly **one domain** (see Section 2).  
   - If an event logically fits several domains (e.g. Redwood = batteries + recycling), choose the **most specific** or **most central** domain and note the overlap in `notes` or `tags`.  
   - Do **not** add company-level R&D totals multiple times; if you add such roll-ups in future, mark them explicitly as roll-ups in new fields (see Section 6).

3. **Source hierarchy (for links)**  
   Prefer, when available:
   1. Company filings (10-K/20-F, annual reports, sustainability/impact reports)
   2. Official company press releases / blogs
   3. High-quality newswire / financial press (Reuters, FT, WSJ, Bloomberg, etc.)
   4. Reputable secondary analysis if necessary (avoid pure speculation).

4. **Timeframe**  
   - Primary focus: **2015–2025** (capturing the last decade of transformative tech investment).  
   - Earlier foundational events (2010-2014) may be included if:
     - They represent major platform investments still active today (e.g., AWS infrastructure, early quantum labs)
     - They establish baseline for decade-over-decade growth analysis
     - They are referenced in current strategic narratives
   - Always set the `year` to the **main public announcement year** or **deal year**, not necessarily the start of internal R&D.
   - For multi-year programs announced in one year, use `timeframe` to capture duration.

5. **Speculation and estimates**  
   If the only available numbers are rough press estimates (e.g., “≈$20B over a decade”), it is usually better to:
   - Store `investment_amount_billions_usd = null`  
   - Describe the magnitude qualitatively in `notes`  
   - Make clear in `source_figure` that the number is a third-party estimate.

---

## 2. Domains and what belongs where

The JSON is organized by **company**, then by **domain key**. Each domain belongs conceptually to a pillar, but only the domain key is stored in the JSON.

### 2.1 Core AI & Compute

- `ai_foundation_models`  
  Foundation / frontier / generative AI models, large AI stakes and partnerships, and major internal AI model efforts.  
  Examples:
  - Investments in OpenAI, Anthropic, etc.
  - Internal LLM stacks, multimodal models, “frontier model” programs.

- `ai_efficiency_methods`  
  Techniques and infrastructure to make AI training and inference more efficient.  
  Examples:
  - LoRA, REALM, RAG, distillation, quantization, parameter-efficient fine-tuning.
  - RAG-heavy architectures and platforms.

- `semiconductor_ai_hardware`  
  Hardware specifically designed for AI workloads.  
  Examples:
  - NVIDIA GPUs (H100, Blackwell), Google TPUs, Amazon Trainium/Inferentia, Tesla Dojo, Apple Neural Engine.

- `cloud_data_centers_ai_infra`  
  Data centers and cloud regions primarily for AI compute and hosting.  
  Examples:
  - Hyperscale data center capex.
  - Sovereign AI supercomputers.
  - GPU clusters provisioned by cloud providers.

### 2.2 Quantum & Advanced Physics

- `quantum_computing`  
  Quantum processors, quantum labs/campuses, and major quantum-computing programs.

- `superconducting_devices_squids`  
  Superconducting qubits and circuits, SQUID-style devices, Josephson junction work.

### 2.3 Automation & Robotics

- `robotics_autonomy`  
  Humanoids, warehouse robots, home robots, embodied AI, “General-purpose robots”.

- `autonomous_mobility`  
  Self-driving stacks, robotaxis, full self-driving programs, dedicated AV units.

- `industrial_automation_supply_chain`  
  Warehouse and fulfillment automation, industrial robots for logistics and supply chain.

### 2.4 Energy, Climate & Materials

- `batteries_and_storage`  
  Batteries and non-trivial storage systems (lithium-ion, solid-state, 4680, molten-salt, long-duration storage, etc.).

- `renewable_energy_generation`  
  Wind, solar, geothermal, and bioenergy projects, plus related PPAs and investments.

- `circularity_reuse_recycling`  
  Recycling and circular economy efforts, including e-waste and battery recycling, circular centers, and related funds.

### 2.5 Health, Bio & Wellbeing

- `digital_health_devices`  
  Wearables, digital health services, telehealth acquisitions, large-scale health studies using devices.

- `bio_ai_and_drug_discovery`  
  AI for biology and drug discovery, such as protein-folding models, dedicated health supercomputers, Verily-scale projects.

- `wellness_vr_and_behavioral`  
  VR fitness and wellness, behavior and mental-health programs rooted in XR.

### 2.6 Connectivity & Digital Economy

- `satellite_and_subsea_infrastructure`  
  Satellite constellations, Kuiper/Starlink-style projects, subsea cable networks, backbone communications infrastructure.

- `digital_inclusion_and_economy`  
  Digital inclusion and regional digital-economy investments (e.g., Jio stake, country-level digitization funds).

### 2.7 Trust, Governance & Society

- `security_cryptography`  
  Cryptography, encryption, post-quantum crypto, confidential computing, zero trust.

- `responsible_ai_safety_governance`  
  AI safety and governance programs, labs and partnerships.  
  (Currently sparse; future work should populate this.)

- `diversity_equity_inclusion`  
  DEI-related investments and structural moves (including explicit rollback/removal).

### 2.8 Experiential / Sci-Fi Products

- `xr_metaverse_and_spatial_computing`  
  XR, AR/VR, spatial computing, metaverse platforms (Vision Pro, Quest, Project Starline/Beam, etc.).

- `sci_fi_consumer_devices`  
  Futuristic consumer hardware like home robots, BCI-style devices, and other "sci-fi" products.

### 2.9 Manufacturing & Supply Chain Innovation

- `advanced_manufacturing_materials`  
  Next-generation manufacturing techniques, advanced materials R&D, additive manufacturing, and process innovation.

- `supply_chain_digitization`  
  Digital twins, supply chain visibility platforms, blockchain for provenance, IoT-enabled logistics.

### 2.10 Edge Computing & 5G/6G

- `edge_computing_infrastructure`  
  Edge data centers, CDN expansions, edge AI compute nodes, distributed computing infrastructure.

- `5g_6g_network_infrastructure`  
  5G/6G network equipment, private 5G networks, Open RAN, spectrum acquisitions, next-gen wireless R&D.

### 2.11 Content, Media & Gaming

- `content_production_studios`  
  Game studios, film/TV production companies, content creation tools, original content investments.

- `gaming_platforms_engines`  
  Game engines, cloud gaming infrastructure, metaverse gaming platforms, esports investments.

- `media_streaming_infrastructure`  
  Video/music streaming platforms, podcast networks, content delivery infrastructure.

### 2.12 Financial Services & Fintech

- `payments_financial_services`  
  Digital payment platforms, BNPL services, banking partnerships, financial infrastructure.

- `blockchain_web3`  
  Blockchain infrastructure, cryptocurrency initiatives, NFT platforms, Web3 investments.

### 2.13 Education & Workforce Development

- `education_technology_platforms`  
  Educational software, online learning platforms, coding bootcamps, digital literacy programs.

- `workforce_training_reskilling`  
  Workforce development programs, apprenticeships, certification programs, skills training.

### 2.14 Real Estate & Physical Infrastructure

- `corporate_real_estate_campuses`  
  Campus expansions, headquarters construction, office space investments, real estate acquisitions.

- `retail_physical_infrastructure`  
  Retail store buildouts, experiential retail spaces, fulfillment centers, distribution networks.

### 2.15 Acquisitions & Strategic Investments

- `major_acquisitions`  
  Significant M&A activity (>$500M) that doesn't fit cleanly into other domains.

- `venture_capital_funds`  
  Corporate VC arms, innovation funds, strategic investment vehicles.

### 2.16 Legal, Regulatory & Compliance

- `regulatory_compliance_investments`  
  Compliance infrastructure, privacy engineering, content moderation systems, regulatory response.

- `litigation_settlements_fines`  
  Legal settlements, antitrust fines, regulatory penalties.

---

## 3. Record structure and update rules

Each record in a domain array should have:

```jsonc
{
  "investment_amount_billions_usd": 4.0, // or null
  "year": 2023,
  "initiatives": [
    "Short label 1",
    "Short label 2"
  ],
  "notes": "Plain-language context and caveats.",
  "source_figure": "Key numerical statement, paraphrased.",
  "links": [
    "https://primary-source-1",
    "https://secondary-source-2"
  ],
  "orig_domain": "robotics",
  "spend_type": "capex",
  "timeframe": {"start": 2023, "end": 2025},
  "amount_basis": "multi_year_commitment",
  "certainty": "company_guidance",
  "is_rollup": false
}
```

### 3.1 When appending a new record

1. Identify `Company` and `Domain`.  
   - Company must be one of Apple, Microsoft, Alphabet, Amazon, NVIDIA, Tesla, Meta.  
   - Domain must be one of the keys listed in Section 2.

2. Check for duplicates:  
   - A candidate event is a likely duplicate if:
     - The **first link** matches an existing record for that company, or
     - The `source_figure` and `initiatives` are clearly identical in meaning.
   - If you detect a duplicate:
     - **Merge** details into the existing record (add new link to `links`, expand `initiatives` if truly new).
     - Do **not** create a separate record.

3. Set fields:
   - `investment_amount_billions_usd`  
     - Numeric **billions of USD** if a reasonably precise, non-speculative figure is available.  
     - Otherwise `null`.
   - `year`  
     - Year of main announcement or deal.
   - `initiatives`  
     - 1–3 short phrases; avoid full sentences.
   - `notes`  
     - Brief but explicit explanation, including whether it’s part of a larger multi-year plan.
   - `source_figure`  
     - The most important sentence/figure to quote in your analysis layer.
   - `links`  
     - Primary source first, then supporting sources.
   - `orig_domain`  
     - Set to the **most similar old domain label** from the previous schema if applicable (e.g. `"robotics"`, `"lithium_ion_battery_technology"`).  
     - If not applicable (purely new record), set `orig_domain` to the new domain name (e.g. `"ai_foundation_models"`).
   - `spend_type` *(optional but recommended when clear)*  
     - One of: `r_and_d`, `capex`, `equity`, `fund`, `ppa`, `pledge`, `opex`, `other`.  
     - Helps separate equity stakes/pledges from capex or internal R&D.
   - `timeframe` *(optional)*  
     - Object with `start` and `end` years for multi-year commitments; use `null` for open-ended; omit for single-year events.
   - `amount_basis` *(optional)*  
     - One of: `single_year_spend`, `multi_year_commitment`, `project_cost`, `valuation_or_stake`, `pledge`, `undisclosed`.  
     - Clarifies whether the headline number is a pledge/valuation vs actual spend.
   - `certainty` *(optional)*  
     - One of: `audited_filing`, `company_guidance`, `press_report`, `third_party_estimate`.  
     - Signals evidence strength.
   - `is_rollup` *(optional)*  
     - Boolean, default `false`. Set `true` for aggregates like annual R&D totals or multi-year program roll-ups to avoid double counting.

### 3.2 When updating an existing record

Update instead of appending if:

- A more precise amount becomes available (e.g., from a later filing).  
- The original record used a vague or speculative number and a better one exists.  
- New context materially changes interpretation (e.g., cancellation, massive scale-up or reduction).

Rules:

- Overwrite `investment_amount_billions_usd` only if the new value is from a **more authoritative source** (filing > press release > media > blog > rumor).  
- Always preserve old sources in `links` when they are still correct and non-misleading.  
- Expand `notes` rather than deleting prior caveats.

---

## 4. Search strategy per domain

This section provides term families and query templates for the most important domains. Models should instantiate `{company}`, `{year}`, `{partner}`, `{chip_name}`, etc., and adapt/extend as needed.

### 4.1 `ai_foundation_models`

**Core terms:**

- `"large language model"`, `"foundation model"`, `"generative AI"`, `"LLM"`, `"multimodal model"`, `"frontier model"`

**Spend terms:**

- `"R&D spending"`, `"investment"`, `"multi-year commitment"`,
- `"compute cluster"`, `"GPU cluster"`, `"supercomputer"`

**Query templates:**

- `{company} investment in foundation models`
- `{company} large language model supercomputer cost`
- `{company} {partner_model_or_company} funding round amount`
- `{company} frontier AI training compute cluster`

### 4.2 `ai_efficiency_methods`

**Core terms:**

- `"Low-Rank Adaptation"`, `"LoRA"`, `"parameter-efficient fine-tuning"`,
- `"retrieval-augmented generation"`, `"RAG"`, `"REALM"`, `"knowledge-intensive NLP"`,
- `"distillation"`, `"quantization"`

**Query templates:**

- `{company} LoRA low-rank adaptation research`
- `{company} retrieval-augmented generation RAG paper`
- `{company} REALM retrieval language model`
- `{company} parameter efficient fine tuning {year}`

### 4.3 `semiconductor_ai_hardware`

**Core terms:**

- `"GPU"`, `"AI accelerator"`, `"custom chip"`, `"ASIC"`, `"Neural Engine"`,
- `"Dojo"`, `"TPU"`, `"Trainium"`, `"Inferentia"`, `"H100"`, `"Blackwell"`

**Spend terms:**

- `"development cost"`, `"R&D expenses"`, `"tape-out"`, `"fab investment"`, `"foundry deal"`, `"capex"`

**Query templates:**

- `{company} custom AI chip development cost`
- `{company} {chip_name} R&D spending`
- `{company} deal with TSMC or Samsung for 3nm`
- `{company} data center GPU capex {year}`

### 4.4 `cloud_data_centers_ai_infra`

**Core terms:**

- `"data center"`, `"cloud region"`, `"availability zone"`,
- `"AI supercomputer"`, `"GPU supercomputer"`, `"sovereign AI"`, `"hyperscale"`.

**Query templates:**

- `{company} data center investment {country_or_region}`
- `{company} sovereign AI supercomputer spend`
- `{company} annual capex on data centers`
- `{company} announces {amount} investment in cloud region`

### 4.5 `batteries_and_storage`

**Core terms:**

- `"lithium-ion battery"`, `"solid-state battery"`, `"4680 cell"`,
- `"grid-scale storage"`, `"molten salt storage"`, `"long duration storage"`

**Query templates:**

- `{company} battery factory investment {location}`
- `{company} invests in {battery_startup}`
- `{company} long duration energy storage project cost`
- `{company} 4680 production investment`

### 4.6 `renewable_energy_generation`

**Core terms:**

- `"solar project"`, `"wind project"`, `"renewable energy"`, `"PPA"`, `"power purchase agreement"`, `"geothermal"`, `"bioenergy"`

**Query templates:**

- `{company} renewable energy PPA MW`
- `{company} green bond spend on solar and wind`
- `{company} invests in wind farm OR solar project`
- `{company} data center renewable energy contract {year}`

### 4.7 `circularity_reuse_recycling`

**Core terms:**

- `"circular economy"`, `"recycling"`, `"circular center"`, `"e-waste"`,
- `"battery recycling"`, `"materials recovery"`

**Query templates:**

- `{company} circular center server reuse`
- `{company} closed loop partners investment`
- `{company} battery recycling plant cost`
- `{company} recycling infrastructure fund`

### 4.8 `robotics_autonomy` / `autonomous_mobility` / `industrial_automation_supply_chain`

**Core terms (robotics_autonomy):**

- `"humanoid robot"`, `"warehouse robot"`, `"home robot"`, `"embodied AI"`

**Core terms (autonomous_mobility):**

- `"autonomous vehicle"`, `"self-driving"`, `"robotaxi"`, `"full self-driving"`

**Core terms (industrial_automation_supply_chain):**

- `"fulfillment center automation"`, `"warehouse automation"`, `"supply chain robotics"`

**Query templates:**

- `{company} humanoid robot project investment`
- `{company} self driving investment or annual loss`
- `{company} invests in warehouse robotics startup`
- `{company} industrial innovation fund {amount}`

### 4.9 `satellite_and_subsea_infrastructure`

**Core terms:**

- `"LEO satellite"`, `"satellite constellation"`, `"Kuiper"`,
- `"subsea cable"`, `"undersea cable"`, `"fiber backbone"`

**Query templates:**

- `{company} satellite broadband investment`
- `{company} subsea cable project cost`
- `{company} invests in international cable system`

### 4.10 `digital_inclusion_and_economy`

**Core terms:**

- `"digitization fund"`, `"digital economy"`, `"SMB enablement"`,
- `"e-commerce enablement"`, `"small business program"`

**Query templates:**

- `{company} digitization fund {country}`
- `{company} invests {amount} in local digital economy`
- `{company} stake in {regional_platform}`

### 4.11 `security_cryptography` and `responsible_ai_safety_governance`

**Core terms (security_cryptography):**

- `"end-to-end encryption"`, `"post-quantum cryptography"`, `"PQC"`,
- `"zero trust"`, `"confidential computing"`, `"trusted execution"`

**Core terms (responsible_ai_safety_governance):**

- `"AI safety"`, `"responsible AI"`, `"AI governance"`,
- `"red teaming"`, `"alignment"`, `"AI principles"`

**Query templates:**

- `{company} commits {amount} to cybersecurity`
- `{company} post-quantum cryptography rollout`
- `{company} responsible AI program funding`
- `{company} AI safety research partnership`

### 4.12 `xr_metaverse_and_spatial_computing` / `sci_fi_consumer_devices`

**Core terms (XR/metaverse):**

- `"virtual reality headset"`, `"mixed reality"`, `"AR/VR"`,
- `"spatial computing"`, `"metaverse platform"`

**Core terms (sci_fi_consumer_devices):**

- `"home robot"`, `"social robot"`, `"ambient computing device"`,
- `"brain-computer interface"`, `"BCI"`

**Query templates:**

- `{company} XR or VR division operating loss`
- `{company} spatial computing investment`
- `{company} home robot {device_name} development`
- `{company} brain computer interface research`

### 4.13 `advanced_manufacturing_materials` / `supply_chain_digitization`

**Core terms (advanced_manufacturing):**

- `"additive manufacturing"`, `"3D printing"`, `"advanced materials"`,
- `"carbon fiber"`, `"manufacturing automation"`, `"smart factory"`

**Core terms (supply_chain_digitization):**

- `"digital twin"`, `"supply chain visibility"`, `"blockchain provenance"`,
- `"IoT logistics"`, `"predictive supply chain"`

**Query templates:**

- `{company} advanced manufacturing facility investment`
- `{company} 3D printing factory cost`
- `{company} digital twin supply chain investment`
- `{company} blockchain supply chain pilot`

### 4.14 `edge_computing_infrastructure` / `5g_6g_network_infrastructure`

**Core terms (edge computing):**

- `"edge data center"`, `"CDN expansion"`, `"edge AI"`,
- `"distributed computing"`, `"edge node"`

**Core terms (5G/6G):**

- `"5G network"`, `"private 5G"`, `"Open RAN"`,
- `"spectrum acquisition"`, `"6G research"`, `"mmWave"`

**Query templates:**

- `{company} edge computing infrastructure investment`
- `{company} CDN expansion capex`
- `{company} private 5G network deployment cost`
- `{company} spectrum auction bid amount`

### 4.15 `content_production_studios` / `gaming_platforms_engines` / `media_streaming_infrastructure`

**Core terms (content production):**

- `"game studio acquisition"`, `"film production"`, `"original content"`,
- `"content creation tools"`, `"animation studio"`

**Core terms (gaming platforms):**

- `"game engine"`, `"cloud gaming"`, `"esports"`,
- `"gaming platform"`, `"game streaming"`

**Core terms (media streaming):**

- `"video streaming"`, `"music streaming"`, `"podcast network"`,
- `"content delivery network"`, `"streaming infrastructure"`

**Query templates:**

- `{company} acquires {studio_name} for {amount}`
- `{company} original content budget {year}`
- `{company} cloud gaming infrastructure investment`
- `{company} streaming platform capex`

### 4.16 `payments_financial_services` / `blockchain_web3`

**Core terms (payments/fintech):**

- `"digital payments"`, `"Apple Pay"`, `"Google Pay"`,
- `"buy now pay later"`, `"BNPL"`, `"financial services"`, `"banking partnership"`

**Core terms (blockchain/Web3):**

- `"blockchain infrastructure"`, `"cryptocurrency"`, `"NFT platform"`,
- `"Web3"`, `"decentralized"`, `"smart contracts"`

**Query templates:**

- `{company} payment processing infrastructure investment`
- `{company} fintech partnership deal value`
- `{company} blockchain project investment`
- `{company} Web3 initiative funding`

### 4.17 `education_technology_platforms` / `workforce_training_reskilling`

**Core terms (education technology):**

- `"online learning"`, `"educational software"`, `"coding bootcamp"`,
- `"digital literacy"`, `"edtech platform"`

**Core terms (workforce training):**

- `"workforce development"`, `"apprenticeship program"`, `"reskilling"`,
- `"certification program"`, `"skills training"`, `"talent development"`

**Query templates:**

- `{company} education platform investment`
- `{company} workforce training program budget`
- `{company} apprenticeship program {amount} commitment`
- `{company} digital skills initiative funding`

### 4.18 `corporate_real_estate_campuses` / `retail_physical_infrastructure`

**Core terms (corporate real estate):**

- `"headquarters construction"`, `"campus expansion"`, `"office space"`,
- `"real estate acquisition"`, `"corporate campus"`

**Core terms (retail infrastructure):**

- `"retail store"`, `"Apple Store"`, `"Amazon Go"`,
- `"fulfillment center"`, `"distribution center"`, `"warehouse facility"`

**Query templates:**

- `{company} new headquarters cost {location}`
- `{company} campus expansion {amount} investment`
- `{company} retail store expansion plan budget`
- `{company} fulfillment center construction {location} cost`

### 4.19 `major_acquisitions` / `venture_capital_funds`

**Core terms (acquisitions):**

- `"acquisition"`, `"acquires"`, `"merger"`, `"M&A"`,
- `"deal value"`, `"purchase price"`, `"takeover"`

**Core terms (VC funds):**

- `"venture capital"`, `"innovation fund"`, `"strategic investment"`,
- `"corporate VC"`, `"investment arm"`, `"fund commitment"`

**Query templates:**

- `{company} acquires {target} for {amount} billion`
- `{company} M&A spending {year}`
- `{company} launches {amount} innovation fund`
- `{company} venture capital portfolio investments`

### 4.20 `regulatory_compliance_investments` / `litigation_settlements_fines`

**Core terms (compliance):**

- `"compliance infrastructure"`, `"privacy engineering"`, `"content moderation"`,
- `"regulatory response"`, `"data protection"`, `"GDPR compliance"`

**Core terms (litigation/fines):**

- `"antitrust fine"`, `"settlement"`, `"penalty"`,
- `"legal settlement"`, `"regulatory fine"`, `"lawsuit settlement"`

**Query templates:**

- `{company} compliance system investment`
- `{company} content moderation spending`
- `{company} antitrust fine {amount}`
- `{company} settles lawsuit for {amount}`

---

## 5. Handling remaining empty sets

If, after a focused search using the templates and domain definitions above, there is **no credible evidence** of a meaningful spend or R&D effort in a given `(company, domain)`:

- **Do not fabricate or infer** a record.  
- Treat the empty set as a real signal (this company is not visibly active in this domain, or activity is too small / too secret to show up in reputable public sources).  
- Optionally add a short **research log** outside the JSON noting which queries were attempted and why no entry was added.

---

## 6. Future extensions (optional fields)

The schema now supports optional fields to improve aggregation quality:

- `spend_type` (e.g., internal R&D vs capex vs equity vs PPA vs pledge)
- `timeframe` (start/end years for multi-year commitments)
- `amount_basis` (single-year spend vs multi-year commitment vs project cost vs valuation/stake)
- `certainty` (audited filing vs company guidance vs press report vs third-party estimate)
- `is_rollup` (flag company-level roll-ups such as annual R&D)

Guidance:
- Set these **when evidence is clear**; otherwise leave them out (they default to omitted/false).  
- Use `is_rollup = true` on aggregates (e.g., annual R&D totals) to avoid double counting against project-level entries.  
- Use `amount_basis` and `spend_type` to distinguish pledges/valuations/equity from concrete capex or R&D.  
- Avoid back-filling old records unless the source unambiguously supports the added metadata.

---

## 7. Enhanced search strategies for comprehensive coverage

### 7.1 Multi-source triangulation

For high-value spending events (>$1B), validate across multiple sources:

1. **Primary source**: Company press release, SEC filing, or investor presentation
2. **Financial press**: Reuters, Bloomberg, WSJ, FT reporting
3. **Industry analysis**: Gartner, IDC, or sector-specific research firms
4. **Academic/technical**: Research papers, patent filings, technical blogs

**Example workflow:**
```
1. Find initial claim: "Microsoft invests $10B in OpenAI"
2. Verify in SEC filings or official Microsoft newsroom
3. Cross-check with Reuters/Bloomberg for deal structure
4. Note any discrepancies in amount_basis (equity vs credits vs cash)
```

### 7.2 Temporal search patterns

To capture decade-long spending trends, use year-specific searches:

**Annual sweep pattern:**
- `{company} {domain_keyword} investment 2015`
- `{company} {domain_keyword} investment 2016`
- ...continuing through 2025

**Multi-year commitment tracking:**
- `{company} five-year plan {domain}`
- `{company} 2020-2025 commitment {domain}`
- `{company} decade investment {domain}`

**Quarterly earnings calls:**
- `{company} Q1 2024 earnings capex guidance`
- `{company} fiscal year {year} R&D breakdown`

### 7.3 SEC filing mining

Key sections to search in 10-K/10-Q filings:

- **Item 1 (Business)**: Strategic initiatives, major programs
- **Item 1A (Risk Factors)**: Large ongoing commitments mentioned as risks
- **Item 7 (MD&A)**: Capital expenditure plans, R&D trends
- **Item 8 (Financial Statements)**: Cash flow statements (capex line items)
- **Exhibits**: Material contracts, partnership agreements

**Query templates for SEC EDGAR:**
- `{company} 10-K site:sec.gov filetype:htm {keyword}`
- `{company} 8-K acquisition site:sec.gov`

### 7.4 Patent and academic publication tracking

Use patent filings and research publications as signals of R&D investment:

**Patent databases:**
- Google Patents: `assignee:{company} {technology_domain}`
- USPTO: Track filing dates and inventor counts for R&D intensity

**Academic publications:**
- Google Scholar: `author:"{company_research_lab}" {domain}`
- ArXiv: Company-affiliated papers in AI, quantum, etc.

**Inference rules:**
- 50+ patents/year in domain → likely >$100M R&D
- Major conference papers (NeurIPS, CVPR) → active research program
- Note: Store as qualitative evidence unless spending explicitly disclosed

### 7.5 Supply chain and partner announcements

Track spending through supplier and partner announcements:

**Supplier announcements:**
- `TSMC announces {company} 3nm wafer order`
- `{battery_supplier} secures {amount} contract with {company}`

**Partnership press releases:**
- Joint ventures often disclose total program value
- Cloud partnerships may reveal infrastructure commitments
- Manufacturing partnerships often cite facility investment

### 7.6 Geographic and regulatory filings

Non-US regulatory filings can reveal spending not disclosed in US filings:

**Key jurisdictions:**
- **EU**: Competition filings, state aid notifications
- **China**: MOFCOM filings for foreign investments
- **India**: FDI disclosures, regulatory approvals
- **UK**: Companies House filings for subsidiaries

**Query templates:**
- `{company} investment {country} regulatory approval {amount}`
- `{company} {country} ministry announcement {domain}`

### 7.7 Industry conference and analyst day mining

Companies often disclose spending plans at industry events:

**Key events to monitor:**
- Company-specific: Apple WWDC, Microsoft Build, Google I/O, AWS re:Invent, NVIDIA GTC, Tesla AI Day, Meta Connect
- Industry: CES, MWC, Computex, SC (supercomputing), Hot Chips

**Search patterns:**
- `{company} {event_name} {year} {domain} investment announcement`
- `{company} analyst day {year} capex guidance`

### 7.8 Sustainability and ESG report mining

Annual sustainability reports often detail spending in:
- Renewable energy (PPAs, project investments)
- Circular economy (recycling infrastructure)
- DEI programs (budget commitments)
- Supply chain (ethical sourcing investments)

**Query templates:**
- `{company} environmental progress report {year} renewable energy`
- `{company} sustainability report {year} investment`
- `{company} ESG disclosure {domain} spending`

### 7.9 Competitive intelligence and market research

Use industry analyst reports for spending estimates:

**Reputable sources:**
- Gartner, IDC, Forrester (IT spending)
- IHS Markit, Omdia (semiconductor, telecom)
- Wood Mackenzie (energy)
- CB Insights (venture/M&A)

**Usage guidelines:**
- Mark as `certainty: "third_party_estimate"`
- Note methodology in `notes` field
- Prefer company-confirmed figures when available

### 7.10 Negative space analysis

Identify conspicuous absences to guide targeted research:

**Coverage gaps to investigate:**
1. **Missing years**: If 2020-2024 data exists but 2015-2019 is sparse
2. **Domain imbalances**: If one company has 20 records and another has 2 in same domain
3. **Asymmetric disclosure**: If competitors disclose but target company doesn't

**Strategies for filling gaps:**
- Search for program cancellations or wind-downs
- Look for rebranding (old program names)
- Check archived press releases (Wayback Machine)
- Review analyst Q&A transcripts for indirect mentions

---

## 8. Historical context and decade-specific search patterns

### 8.1 MAG7 spending evolution (2015-2025)

Understanding how spending priorities shifted helps target research:

**2015-2017: Cloud infrastructure buildout era**
- Focus: Data center capex, cloud region expansion
- Key events: AWS dominance, Azure/GCP scaling, mobile-first transitions
- Search emphasis: `{company} data center investment 2015-2017`

**2018-2019: AI awakening and platform consolidation**
- Focus: ML infrastructure, TPU/GPU clusters, AI acquisitions
- Key events: BERT, GPT-2, AlphaGo, early transformer models
- Search emphasis: `{company} AI research investment 2018-2019`, `{company} acquires AI startup`

**2020-2021: Pandemic acceleration and supply chain**
- Focus: Remote work infrastructure, supply chain resilience, health tech
- Key events: Work-from-home surge, chip shortage, telehealth boom
- Search emphasis: `{company} pandemic response investment 2020`, `{company} supply chain 2021`

**2022-2023: Generative AI gold rush**
- Focus: Foundation models, GPU procurement, AI safety
- Key events: ChatGPT launch, LLM race, AI regulation discussions
- Search emphasis: `{company} generative AI investment 2022-2023`, `{company} GPU order`

**2024-2025: AI infrastructure and energy**
- Focus: Massive data center expansion, energy solutions, sovereign AI
- Key events: $100B+ AI capex plans, nuclear/renewable for data centers
- Search emphasis: `{company} 2024 capex guidance`, `{company} energy infrastructure 2025`

### 8.2 Company-specific inflection points

Track major strategic pivots that signal spending shifts:

**Apple**
- 2015: Apple Watch launch → health tech investment
- 2020: Apple Silicon transition → semiconductor R&D surge
- 2023: Vision Pro → spatial computing investment

**Microsoft**
- 2014: Satya Nadella CEO → cloud-first transformation
- 2019: OpenAI partnership → AI infrastructure ramp
- 2023: Copilot launch → enterprise AI integration

**Alphabet**
- 2015: Alphabet restructuring → Other Bets funding
- 2019: Quantum supremacy → quantum computing acceleration
- 2023: Bard/Gemini → competitive AI response

**Amazon**
- 2017: Whole Foods acquisition → physical retail
- 2020: Project Kuiper approval → satellite broadband
- 2022: Climate Pledge → renewable energy acceleration

**NVIDIA**
- 2016: DGX systems launch → AI hardware focus
- 2020: Arm acquisition attempt → platform expansion
- 2023: H100 demand surge → capacity expansion

**Tesla**
- 2016: SolarCity merger → energy storage integration
- 2019: Autonomy Day → FSD investment ramp
- 2023: Dojo announcement → custom AI hardware

**Meta**
- 2014: Oculus acquisition → VR investment begins
- 2021: Meta rebrand → metaverse commitment
- 2023: "Year of Efficiency" → Reality Labs scrutiny

### 8.3 Decade-specific search modifiers

Adjust search strategies based on era:

**2015-2017 searches:**
- Add terms: `"cloud migration"`, `"mobile-first"`, `"IoT"`
- Check: Early press releases (less indexed), archived investor decks

**2018-2020 searches:**
- Add terms: `"machine learning"`, `"deep learning"`, `"neural network"`
- Check: Research papers, GitHub repos, conference presentations

**2021-2023 searches:**
- Add terms: `"generative AI"`, `"large language model"`, `"foundation model"`
- Check: Earnings calls, analyst days, regulatory filings

**2024-2025 searches:**
- Add terms: `"AI infrastructure"`, `"sovereign AI"`, `"energy efficiency"`
- Check: Recent press releases, sustainability reports, capex guidance

## 9. Quality control and validation

### 8.1 Red flags for unreliable data

Be skeptical of:
- Round numbers without source attribution ($10B, $5B) in blog posts
- "Up to" language without minimum commitment
- Conflicting figures across sources (investigate discrepancy)
- Stale data republished without date context
- Aggregations mixing different spend types (R&D + capex + equity)

### 8.2 Validation checklist

Before adding a record >$1B:
- [ ] Primary source identified and linked
- [ ] Year of announcement/commitment confirmed
- [ ] Spend type classified (R&D/capex/equity/etc.)
- [ ] Timeframe clarified (single-year vs multi-year)
- [ ] Currency confirmed as USD (convert if needed)
- [ ] No obvious duplicate in existing records

### 9.3 Continuous improvement

Periodically review and upgrade:
- **Quarterly**: Add latest earnings call disclosures
- **Annually**: Refresh with 10-K filings and annual reports
- **Event-driven**: Update when major M&A or programs announced
- **Retroactive**: Upgrade `null` amounts when better data emerges

---

## 10. Quick reference: Priority research targets

### 10.1 Highest-value domains (by expected total spend 2015-2025)

**Tier 1: $100B+ total across MAG7**
1. `cloud_data_centers_ai_infra` - Hyperscale data center buildout
2. `ai_foundation_models` - LLM development and partnerships
3. `semiconductor_ai_hardware` - Custom chip development
4. `major_acquisitions` - M&A activity
5. `corporate_real_estate_campuses` - Campus expansions and HQs

**Tier 2: $10B-$100B total**
6. `renewable_energy_generation` - Clean energy commitments
7. `autonomous_mobility` - Self-driving programs (Waymo, FSD, Cruise)
8. `satellite_and_subsea_infrastructure` - Kuiper, 2Africa, etc.
9. `xr_metaverse_and_spatial_computing` - Reality Labs, Vision Pro
10. `content_production_studios` - Gaming and media acquisitions

**Tier 3: $1B-$10B total**
11. `robotics_autonomy` - Humanoid and warehouse robots
12. `batteries_and_storage` - EV and grid storage
13. `digital_health_devices` - Wearables and health services
14. `security_cryptography` - Cybersecurity programs
15. `quantum_computing` - Quantum labs and hardware

### 10.2 Most under-documented domains (research gaps)

Based on current dataset analysis, prioritize:

1. **`5g_6g_network_infrastructure`** - Limited data across all companies
2. **`supply_chain_digitization`** - Mostly qualitative, need quantification
3. **`workforce_training_reskilling`** - Large programs but sparse dollar figures
4. **`regulatory_compliance_investments`** - Significant but rarely disclosed
5. **`edge_computing_infrastructure`** - Conflated with cloud, needs separation
6. **`blockchain_web3`** - Mixed with other domains, needs clarity
7. **`bio_ai_and_drug_discovery`** - Alphabet/NVIDIA strong, others weak
8. **`litigation_settlements_fines`** - Incomplete historical record

### 10.3 Company-specific research priorities

**Apple:** Fill gaps in
- Semiconductor R&D spend (Apple Silicon program costs)
- Health device R&D (Watch, glucose monitoring)
- Services infrastructure (iCloud, Apple TV+)

**Microsoft:** Fill gaps in
- Gaming content spend (post-Activision integration)
- Quantum computing lab investments
- Edge computing (Azure Edge Zones)

**Alphabet:** Fill gaps in
- Waymo cumulative spend (update beyond $30B estimate)
- YouTube infrastructure and content
- Subsea cable investments (Equiano, Grace Hopper, etc.)

**Amazon:** Fill gaps in
- Fulfillment center automation (robotics beyond Industrial Innovation Fund)
- Kuiper ground infrastructure (beyond satellite constellation)
- Healthcare (One Medical integration, pharmacy)

**NVIDIA:** Fill gaps in
- Fab partnerships and capacity reservations
- Automotive platform investments (DRIVE)
- Omniverse infrastructure

**Tesla:** Fill gaps in
- Gigafactory capex breakdowns (beyond Mexico announcement)
- Optimus development costs
- Energy business infrastructure (Megapack factories)

**Meta:** Fill gaps in
- Subsea cable consortium investments (2Africa, others)
- AI chip development (MTIA program costs)
- Content moderation infrastructure

### 10.4 Essential sources by information type

**For capex/R&D totals:**
- 10-K filings (Item 7, MD&A section)
- Earnings call transcripts (CFO prepared remarks)
- Investor presentations (capital allocation slides)

**For specific projects:**
- Company newsrooms (press releases)
- SEC 8-K filings (material events)
- State/local government press releases (incentive deals)

**For acquisitions:**
- SEC filings (8-K, proxy statements)
- Antitrust filings (FTC, DOJ, EU Commission)
- Target company press releases

**For partnerships:**
- Joint press releases
- Partner earnings calls
- Industry trade publications

**For real estate:**
- Local permit databases
- Commercial real estate news
- Economic development authority announcements

**For energy/sustainability:**
- Annual sustainability reports
- CDP disclosures
- PPA announcements from utilities

---

## Appendix: Useful search operators and sites

### Google search operators
```
site:sec.gov {company} 10-K
site:{company_domain}/newsroom {keyword} investment
intitle:"press release" {company} {keyword} {year}
filetype:pdf {company} sustainability report
```

### Key domains to search
```
sec.gov - SEC filings
{company}.com/newsroom - Official press releases
{company}.com/investor - Investor relations
reuters.com, bloomberg.com, wsj.com, ft.com - Financial press
techcrunch.com, theverge.com, arstechnica.com - Tech news
```

### Specialized databases
- **Patents**: patents.google.com, uspto.gov
- **Academic**: scholar.google.com, arxiv.org
- **M&A**: pitchbook.com, crunchbase.com
- **Real estate**: costar.com, bisnow.com
- **Energy**: eia.gov, iea.org
