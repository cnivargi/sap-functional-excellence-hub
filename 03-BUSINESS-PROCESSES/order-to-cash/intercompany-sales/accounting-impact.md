# Conceptual Accounting Impact (`PROC-O2C-IC-001`)

| Event | Company Code | Movement / Doc | Debit | Credit |
| :--- | :--- | :--- | :--- | :--- |
| **1. Goods Issue from Plant `DE10`** | `DE01` | Mvt `687` | Delivering VSiT Inventory | Unrestricted Plant Inventory |
| **2. Affiliate Title Transfer** | `DE01` | Mvt `683` | Intercompany COGS | Delivering VSiT Inventory |
| **3. Affiliate Title Transfer** | `IN01` | Mvt `683` | Selling VSiT Inventory | Intercompany GR/IR Clearing |
| **4. Intercompany Invoice (`IV2`)** | `DE01` | Billing `IV2` | Intercompany Receivable (`IN01`) | Intercompany Revenue |
| **5. Customer Handover & Billing** | `IN01` | `F2` / `685` | Customer AR / External COGS | External Revenue / Selling VSiT |
