# Illustrative Configuration Overview (`PROC-O2C-IC-001`)

> **Release Dependency:** Verify exact SPRO paths against your target S/4HANA release (2023/2025) and deployment model.

1. Assign Delivering Plant `DE10` (CoCode `DE01`) as an allowed plant for Sales Organization `IN10` (CoCode `IN01`) via `OVX6`.
2. Define Internal Customer Number representing `IN01` inside `DE01` and Internal Supplier Number representing `DE01` inside `IN01`.
3. Activate Advanced Intercompany Sales Value Chain (`5D2`) and configure Incoterm-based Transfer of Control dates.
4. Configure Intercompany Billing Type `IV2` and automated EDI/SOAP inbound Supplier Invoice (`MIRO`) posting.
