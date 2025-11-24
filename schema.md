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
  (Note: the current dataset does not yet include records tagged here.)

- `diversity_equity_inclusion`  
  DEI-related investments and structural changes (including rollback/removal of DEI language where relevant).

### 2.8 Experiential / Sci-Fi Products

- `xr_metaverse_and_spatial_computing`  
  XR / AR / VR, metaverse platforms, spatial computing (Vision Pro, Quest, Project Starline).

- `sci_fi_consumer_devices`  
  Futuristic consumer devices such as home robots, BCI-style devices, etc.

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
  "orig_domain": "transfer_learning_rag_lora",
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
  - One of `r_and_d`, `capex`, `equity`, `fund`, `ppa`, `pledge`, `opex`, or `other`.  
  - Indicates the nature of the spend to reduce mixing incomparable flows.

- `timeframe` *(optional)*  
  - Object with `start` and `end` years for multi-year commitments.  
  - Use `null` for open-ended; omit entirely for single-year events.

- `amount_basis` *(optional)*  
  - One of `single_year_spend`, `multi_year_commitment`, `project_cost`, `valuation_or_stake`, `pledge`, `undisclosed`.  
  - Clarifies whether the headline number is a yearly spend, multi-year pledge, project cost, or equity valuation.

- `certainty` *(optional)*  
  - One of `audited_filing`, `company_guidance`, `press_report`, `third_party_estimate`.  
  - Signals evidence strength.

- `is_rollup` *(optional, boolean)*  
  - `true` when the record is an aggregate (e.g., annual company R&D) rather than a discrete project/deal.  
  - Defaults to `false` if omitted.


## 4. Usage tips

- Treat `investment_amount_billions_usd = null` as **“qualitative evidence only”**.  
- Use `year` to build time series but be cautious with multi-year commitments where only a single headline year is present.  
- When in doubt, rely on `links` and `notes` in your Mathematica/Wolfram code to perform manual or semi-automated validation.
