import json
import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from validate_metadata import extract_frontmatter, validate_doc


class TestMetadataValidation(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads((ROOT / "schemas" / "scenario.schema.json").read_text(encoding="utf-8"))

    def test_sample_documents_pass_validation(self):
        samples = [
            ROOT / "01-ENTERPRISE-STRUCTURE/examples/manufacturing-enterprise.md",
            ROOT / "02-MASTER-DATA/master-data-governance/master-data-dependency-matrix.md",
            ROOT / "03-BUSINESS-PROCESSES/order-to-cash/intercompany-sales/README.md",
        ]
        for sample in samples:
            self.assertTrue(sample.exists(), f"Missing sample: {sample}")
            meta = extract_frontmatter(sample)
            self.assertIsNotNone(meta)
            errors = validate_doc(sample, self.schema)
            self.assertEqual(errors, [], f"Validation errors in {sample}: {errors}")


if __name__ == "__main__":
    unittest.main()
