---
id: PROC-O2C-IC-001
title: Intercompany Order-to-Cash (Advanced Intercompany Sales - 5D2)
scenario_type: business_process
domain: order-to-cash
modules:
  - SD
  - MM
  - FI
  - CO
sap_products:
  - S4HANA
  - ECC
releases:
  - S4HANA_2023
  - S4HANA_2025
  - ECC_6_EHP8
deployment:
  - on-premise
  - private-cloud
difficulty: advanced
status: draft
business_capabilities:
  - intercompany-sales
  - valuated-stock-in-transit
dependencies:
  - ENT-MFG-REF-001
  - MD-GOV-MAT-001
related_scenarios: []
sources: []
last_verified: null
reviewed_by: null
---

# Intercompany Order-to-Cash (`PROC-O2C-IC-001`)

> **Verification Status:** `draft` — Illustrative cross-functional vertical slice using [Apex Industrial Systems](../../../01-ENTERPRISE-STRUCTURE/examples/manufacturing-enterprise.md) (`IN01` selling to external customer; `DE01` Plant `DE10` manufacturing and shipping).

## 1. Business Context
An Indian customer places an order with **Apex India (`IN01`, Sales Org `IN10`)**, which fulfills the order directly from **Apex Germany's Munich Plant (`DE10`, Company Code `DE01`)**.

## 2. Prerequisites & Linked Knowledge
- Enterprise Structure: [ENT-MFG-REF-001](../../../01-ENTERPRISE-STRUCTURE/examples/manufacturing-enterprise.md)
- Master Data: [MD-GOV-MAT-001](../../../02-MASTER-DATA/master-data-governance/master-data-dependency-matrix.md)

## 3. Conceptual Process Flow
See [`process-flow.mmd`](process-flow.mmd) for the Mermaid diagram:

```mermaid
flowchart TD
    A[External Customer PO to IN01] --> B[Sales Order OR in IN01 / Plant DE10]
    B --> C[Auto Intercompany PO in IN01 & SO in DE01]
    C --> D[Plant DE10 Delivery & GI to Delivering VSiT - Mvt 687]
    D --> E[Incoterm Handover to Selling VSiT - Mvt 683]
    E --> F[Intercompany Billing IV2 in DE01 & Auto MIRO in IN01]
    E --> G[Final Transfer to Customer - Mvt 601/685]
    G --> H[Customer Invoice F2 in IN01 -> ACDOCA]
```

## 4. Key S/4HANA (`5D2`) vs. ECC Classic Intercompany Differences
- **Classic ECC:** Relied on Sales Order (`OR`) -> Delivery (`LF`, Mvt `601`) -> Intercompany Billing (`IV`) with no purchasing document in the selling company code and no Valuated Stock in Transit (`VSiT`).
- **S/4HANA Advanced Intercompany (`5D2`):** Orchestrates a full value chain via Fiori **Monitor Value Chains (`F4854`)**, using **Movement Type `687`** (Delivering VSiT) and **Movement Type `683`** (Title transfer to Selling VSiT) for IFRS-15 revenue cutoff compliance.

## 5. Scenario Modules
- [`process-flow.mmd`](process-flow.mmd) — Standalone Mermaid diagram source.
- [`configuration.md`](configuration.md) — Illustrative SPRO configuration overview.
- [`accounting-impact.md`](accounting-impact.md) — Conceptual Dr/Cr journal entry flow across `DE01` and `IN01`.
