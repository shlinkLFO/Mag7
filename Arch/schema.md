# MAG7 R&D / Investment Dataset Schema

This schema describes `mag7_spending_reorganized.json`, which reorganizes the original MAG7 spending data into a cleaner domain taxonomy.

## 1. Top-level structure

The JSON file is a single object mapping **company name** to a nested object of **domains**:

```json
{
  "Apple": {
    "ai_foundation_models": [ /* records */ ],
    "batteries_and_storage": [ /* records */ ],
    "...": []
  },
  "Microsoft": {
    "...": []
  },
  "Alphabet": {
    "...": []
  },
  "Amazon": {
    "...": []
  },
  "NVIDIA": {
    "...": []
  },
  "Tesla": {
    "...": []
  },
  "Meta": {
    "...": []
  }
}
```

- Top-level keys: `"Apple"`, `"Microsoft"`, `"Alphabet"`, `"Amazon"`, `"NVIDIA"`, `"Tesla"`, `"Meta"`.
- Second-level keys: **domains** (see Section 2).
- Each domain maps to an **array of records**, each record describing one identifiable R&D or investment event.

## 2. Pillars and domains

Domains are grouped conceptually into pillars, but the JSON only stores the **domain key**. Pillar information is for your analysis layer.

**Current dataset contains 30 active domains across 8 pillars.**

### 2.1 Core AI & Compute

- `ai_foundation_models`  
  Foundation / frontier / generative AI models and major AI investments (e.g. OpenAI, Anthropic, Scale AI, internal LLM stacks).

- `ai_efficiency_methods`  
  Transfer learning, LoRA, RAG/REALM, parameter-efficient fine-tuning, etc.

- `semiconductor_ai_hardware`  
  GPUs and accelerators (H100/Blackwell, TPUs, Dojo, Trainium, Neural Engine, etc.).

- `cloud_data_centers_ai_infra`  
  AI/ML data-center capex, sovereign AI supercomputers, large GPU clusters, cloud regions.

### 2.2 Quantum & Advanced Physics

- `quantum_computing`  
  Quantum processors, labs, campuses, and quantum services.

- `superconducting_devices_squids`  
  Superconducting qubits, Josephson-junction / SQUID-style devices (often overlaps conceptually with quantum_computing).

### 2.3 Automation & Robotics

- `robotics_autonomy`  
  Humanoids, warehouse robots, home robots, embodied AI.

- `autonomous_mobility`  
  Self-driving / robotaxis, AV units, FSD-type stacks.

- `industrial_automation_supply_chain`  
  Fulfillment and warehouse automation, supply-chain robotics and related investments.

### 2.4 Energy, Climate & Materials

- `batteries_and_storage`  
  Lithium-ion, solid-state, 4680, molten salt, and other long-duration storage projects and investments.

- `renewable_energy_generation`  
  Wind, solar, geothermal, bioenergy projects, PPA-backed capacity, etc.

- `circularity_reuse_recycling`  
  Circular centers, recycling infrastructure (including battery recycling), e-waste, and related funds.

### 2.5 Health, Bio & Wellbeing

- `digital_health_devices`  
  Wearables, digital health services, telehealth/primary care acquisitions, large-scale health studies using devices.

- `bio_ai_and_drug_discovery`  
  AI-driven bio / drug discovery and structural biology (e.g. protein-folding models, Verily, Cambridge-1 health compute).

- `wellness_vr_and_behavioral`  
  VR fitness and wellness, behavior-modification via VR/AR.

### 2.6 Connectivity & Digital Economy

- `satellite_and_subsea_infrastructure`  
  LEO constellations and subsea cable systems (Project Kuiper, 2Africa, etc.).

- `digital_inclusion_and_economy`  
  Digitization funds, digital inclusion programs, large strategic stakes in key regional digital platforms (e.g. Jio).

### 2.7 Trust, Governance & Society

- `security_cryptography`  
  Encryption, post-quantum crypto, zero-trust and security-by-design programs.

- `responsible_ai_safety_governance`  
  AI safety, red-teaming, AI governance, and principles.

- `diversity_equity_inclusion`  
  DEI-related investments and structural changes (including rollback/removal of DEI language where relevant).

### 2.8 Experiential / Sci-Fi Products

- `xr_metaverse_and_spatial_computing`  
  XR / AR / VR, metaverse platforms, spatial computing (Vision Pro, Quest, Project Starline).

- `sci_fi_consumer_devices`  
  Futuristic consumer devices such as home robots, BCI-style devices, etc.

### 2.9 Edge Computing, Network & Supply Chain

- `edge_computing_infrastructure`  
  Edge data centers, CDN expansions, edge AI compute nodes, and distributed computing infrastructure.

- `5g_6g_network_infrastructure`  
  Investments in 5G/6G network equipment, private 5G networks, Open RAN, spectrum acquisitions, and next-gen wireless R&D.

- `supply_chain_digitization`  
  Digital twins, supply chain visibility platforms, blockchain for provenance, and IoT-enabled logistics beyond pure robotics.

### 2.10 Content, Media & Gaming

- `content_production_studios`  
  Acquisitions of game studios, film/TV production companies, content creation tools, and original content investments.

- `gaming_platforms_engines`  
  Game engines, cloud gaming infrastructure, metaverse gaming platforms, and esports investments.

### 2.11 Workforce Development

- `workforce_training_reskilling`  
  Internal and external workforce development programs, apprenticeships, certification programs, and skills training initiatives.

### 2.12 Legal, Regulatory & Compliance

- `regulatory_compliance_investments`  
  Major investments in compliance infrastructure, privacy engineering, content moderation systems, and regulatory response programs.

- `litigation_settlements_fines`  
  Significant legal settlements, antitrust fines, and regulatory penalties (for completeness in spend tracking).

## 3. Record-level structure

Each **record** in a domain array has the fields:

```json
{
  "investment_amount_billions_usd": 4.0,
  "year": 2023,
  "initiatives": ["Short bullet label 1", "Short bullet label 2"],
  "notes": "Plain-language context and caveats.",
  "source_figure": "Quote or paraphrase of the key numerical claim.",
  "links": ["https://primary-source-1", "https://secondary-source-2"],
  "spend_type": "capex",
  "timeframe": {"start": 2023, "end": 2025},
  "amount_basis": "multi_year_commitment",
  "certainty": "company_guidance",
  "is_rollup": false
}
```

Field definitions:

- `investment_amount_billions_usd`  
  - Numeric amount in **billions of USD** (e.g. `4.0` means \$4B).  
  - `null` if no credible, non-speculative number is available.

- `year`  
  - Integer year associated with the event (e.g. 2023).  
  - `null` if year is ambiguous or multi-period.

- `initiatives`  
  - Short labels summarizing what the spending covers (max few phrases).

- `notes`  
  - Free-text explanation, assumptions, caveats, and context.

- `source_figure`  
  - The sentence/summary of the key figure as used in your analysis (e.g. a paraphrased headline line).

- `links`  
  - Array of URL strings, ideally starting with primary sources (company filings, official newsrooms) before media coverage.

- `orig_domain`  
  - The original domain label from the previous schema (string or array of strings).  
  - Useful for tracing how records were remapped; **do not** use for new grouping going forward.

- `spend_type` *(optional, recommended)*  
  - One of: `r_and_d`, `capex`, `equity`, `fund`, `ppa`, `opex`, `other`, `M&A`, `Venture`, `CapEx`.  
  - Indicates the nature of the spend to reduce mixing incomparable flows.
  - Note: Use lowercase variants for consistency (e.g., `capex` not `CapEx`).

- `timeframe` *(optional)*  
  - Object with `start` and `end` years for multi-year commitments.  
  - Use `null` for open-ended; omit entirely for single-year events.

- `amount_basis` *(optional)*  
  - One of: `single_year_spend`, `multi_year_commitment`, `project_cost`, `valuation_or_stake`, `undisclosed`, `acquisition_cost`, `actual`, `company_guidance`, `cumulative`, `cumulative_estimate`, `program_budget`, `program_total`, `round_total`, `single_event_cost`, `up to`.  
  - Clarifies whether the headline number is a yearly spend, multi-year pledge, project cost, or equity valuation.

- `certainty` *(optional)*  
  - One of: `audited_filing`, `company_guidance`, `press_report`, `third_party_estimate`, `approx`, `certain`, `regulatory_filing`.  
  - Signals evidence strength.

- `is_rollup` *(optional, boolean)*  
  - `true` when the record is an aggregate (e.g., annual company R&D) rather than a discrete project/deal.  
  - Defaults to `false` if omitted.


## 4. Usage tips

- Treat `investment_amount_billions_usd = null` as **"qualitative evidence only"**.  
- Use `year` to build time series but be cautious with multi-year commitments where only a single headline year is present.  
- When in doubt, rely on `links` and `notes` in your Mathematica/Wolfram code to perform manual or semi-automated validation.

## 5. Domain coverage expectations by company

This matrix indicates which domains are **expected** to have substantial activity for each MAG7 company. Use this to guide research prioritization.

**30 active domains** are tracked in the current dataset.

| Domain | AAPL | MSFT | GOOGL | AMZN | NVDA | TSLA | META |
|--------|------|------|-------|------|------|------|------|
| **Core AI & Compute** |
| ai_foundation_models | ● | ●● | ●● | ●● | ●● | ● | ●● |
| ai_efficiency_methods | ● | ●● | ●● | ●● | ●● | ● | ●● |
| semiconductor_ai_hardware | ●● | ○ | ●● | ● | ●●● | ●● | ● |
| cloud_data_centers_ai_infra | ● | ●●● | ●●● | ●●● | ● | ○ | ●● |
| **Quantum & Advanced Physics** |
| quantum_computing | ○ | ●● | ●●● | ● | ●● | ○ | ○ |
| superconducting_devices_squids | ○ | ● | ●● | ○ | ● | ○ | ○ |
| **Automation & Robotics** |
| robotics_autonomy | ● | ● | ●● | ●● | ●● | ●●● | ● |
| autonomous_mobility | ●● | ● | ●●● | ●● | ● | ●●● | ○ |
| industrial_automation_supply_chain | ○ | ○ | ○ | ●●● | ● | ●● | ○ |
| **Energy, Climate & Materials** |
| batteries_and_storage | ● | ○ | ● | ● | ● | ●●● | ○ |
| renewable_energy_generation | ●● | ●● | ●● | ●●● | ● | ●●● | ●● |
| circularity_reuse_recycling | ●● | ● | ● | ● | ● | ●● | ● |
| **Health, Bio & Wellbeing** |
| digital_health_devices | ●●● | ● | ● | ●● | ○ | ○ | ○ |
| bio_ai_and_drug_discovery | ○ | ● | ●● | ○ | ●● | ○ | ○ |
| wellness_vr_and_behavioral | ○ | ● | ○ | ○ | ○ | ○ | ●● |
| **Connectivity & Digital Economy** |
| satellite_and_subsea_infrastructure | ●● | ● | ●● | ●●● | ○ | ○ | ●● |
| digital_inclusion_and_economy | ●● | ●● | ●●● | ●● | ○ | ○ | ●● |
| **Trust, Governance & Society** |
| security_cryptography | ●●● | ●●● | ●● | ●● | ●● | ● | ●● |
| responsible_ai_safety_governance | ● | ●● | ●● | ● | ● | ○ | ● |
| diversity_equity_inclusion | ●● | ●● | ●● | ●● | ● | ○ | ●● |
| **Experiential / Sci-Fi Products** |
| xr_metaverse_and_spatial_computing | ●●● | ●● | ●● | ○ | ○ | ○ | ●●● |
| sci_fi_consumer_devices | ●● | ● | ● | ●● | ○ | ● | ●● |
| **Edge, Network & Supply Chain** |
| edge_computing_infrastructure | ● | ●● | ●● | ●●● | ● | ○ | ●● |
| 5g_6g_network_infrastructure | ●● | ● | ●● | ● | ● | ○ | ○ |
| supply_chain_digitization | ● | ● | ● | ●●● | ○ | ● | ○ |
| **Content, Media & Gaming** |
| content_production_studios | ●● | ●●● | ● | ●● | ○ | ○ | ●● |
| gaming_platforms_engines | ●● | ●●● | ● | ●● | ●● | ○ | ●● |
| **Workforce Development** |
| workforce_training_reskilling | ●● | ●●● | ●● | ●●● | ● | ○ | ●● |
| **Legal & Regulatory** |
| regulatory_compliance_investments | ●● | ●● | ●●● | ●● | ● | ● | ●●● |
| litigation_settlements_fines | ●● | ●● | ●●● | ●● | ○ | ● | ●●● |

**Legend:**
- ●●● = Core strategic domain; expect multiple large investments (>$1B cumulative)
- ●● = Significant activity; expect several investments ($100M-$1B+ range)
- ● = Moderate activity; expect some investments or R&D programs
- ○ = Limited/no expected activity; search but don't prioritize

**Usage:**
- Prioritize research on ●●● and ●● domains for each company
- For ○ domains, perform cursory search but don't invest extensive time
- Empty cells indicate uncertainty; conduct exploratory research
