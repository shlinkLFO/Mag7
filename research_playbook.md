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
   - Primary focus: ~2015–present.  
   - Earlier foundational events may be included if directly relevant (e.g., first-generation quantum/superconducting milestones).  
   - Always set the `year` to the **main public announcement year** or **deal year**, not necessarily the start of internal R&D.

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
  Futuristic consumer hardware like home robots, BCI-style devices, and other “sci-fi” products.

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
