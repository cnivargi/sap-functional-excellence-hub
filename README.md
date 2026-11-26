# SAP Functional Excellence Hub

> **The Open Knowledge Engineering Platform for SAP Functional Consultants**  
> *S/4HANA First · ECC Comparisons · Cross-Functional · AI-Ready*

## Mission
Make complex SAP functional knowledge accessible, interconnected, verifiable, reusable, and continuously maintainable—from business requirements to enterprise implementation, operations, and intelligent automation.

## Core Principles
1. **Knowledge Engineering, Not a Document Dump:** Every scenario uses standardized YAML frontmatter validated against JSON Schemas (`schemas/`).
2. **Process-First Navigation:** Organized around end-to-end business processes (`03-BUSINESS-PROCESSES/`) rather than isolated module silos.
3. **Human-Reviewed Accuracy:** Automation and AI assist with discovery, validation, and drafting; **functional approval is strictly human-reviewed**.
4. **Release & Deployment Honesty:** Every guide distinguishes *Standard SAP behaviour*, *Recommended practice*, *Illustrative configuration*, and *Verified sandbox behaviour*.

## Repository Architecture (Domains D01–D10)
| Folder | Domain | Coverage |
| :--- | :--- | :--- |
| [`00-START-HERE/`](00-START-HERE/README.md) | Onboarding | Learning paths, glossary, consulting standards |
| [`01-ENTERPRISE-STRUCTURE/`](01-ENTERPRISE-STRUCTURE/README.md) | D01: Enterprise Structure | Org units, assignments, enterprise design principles |
| [`02-MASTER-DATA/`](02-MASTER-DATA/README.md) | D02: Master Data | BP (CVI), Material, Finance, Pricing, Governance & Migration |
| [`03-BUSINESS-PROCESSES/`](03-BUSINESS-PROCESSES/README.md) | D03: Business Processes | O2C, P2P, P2M, R2R, EWM, Service, Projects, Subscriptions |
| [`04-GOODS-AND-INVOICE-MOVEMENTS/`](04-GOODS-AND-INVOICE-MOVEMENTS/README.md) | D04: Goods & Invoices | Inventory movements, GR/GI, Invoice Verification, OBYC/VKOA |
| [`05-CROSS-FUNCTIONAL-INTEGRATION/`](05-CROSS-FUNCTIONAL-INTEGRATION/README.md) | D05: Cross-Functional | SD-FI, MM-FI, SD-MM, SD-EWM, SD-GTS, SD-BRIM, PS-FI |
| [`06-SAP-INTEGRATION/`](06-SAP-INTEGRATION/README.md) | D06: Technical Integration | IDoc/ALE, RFC/BAPI, OData APIs, Integration Suite, Event Mesh |
| [`07-REPORTING-AND-OUTPUTS/`](07-REPORTING-AND-OUTPUTS/README.md) | D07: Reporting & Outputs | Fiori Analytics, CDS Views, SAC, BRF+ (OPD), Adobe Forms |
| [`08-SAP-BTP-AND-AI/`](08-SAP-BTP-AND-AI/README.md) | D08: BTP, AI & Joule | BTP Fundamentals, Joule Assistants/Agents, AI Core, Use Cases |
| [`09-IMPLEMENTATION-TOOLKIT/`](09-IMPLEMENTATION-TOOLKIT/README.md) | D09: Implementation Toolkit | SAP Activate, Fit-to-Standard, FSD, Testing, Cutover, Hypercare |
| [`10-TROUBLESHOOTING/`](10-TROUBLESHOOTING/README.md) | D10: Troubleshooting | Symptom-to-root-cause playbooks & error catalogue |
| [`11-REFERENCE-LIBRARY/`](11-REFERENCE-LIBRARY/README.md) | Reference Library | T-Codes, Fiori Apps, Tables, Movement Types, Acronyms |
| [`12-SANDBOX-PROJECTS/`](12-SANDBOX-PROJECTS/README.md) | Sandbox Projects | End-to-end simulated enterprise implementations |
| [`13-RELEASE-INTELLIGENCE/`](13-RELEASE-INTELLIGENCE/README.md) | Release Intelligence | Release registry, S/4HANA deltas, verification backlog |

## Quick Validation (Offline)
```bash
python tools/validate_metadata.py
python tools/validate_links.py
python tools/validate_references.py
python -m unittest discover -s tests -v
```

See [CONTRIBUTING.md](CONTRIBUTING.md) and [ROADMAP.md](ROADMAP.md) to get involved.
