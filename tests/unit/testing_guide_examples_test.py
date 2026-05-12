from __future__ import annotations

from pathlib import Path

import pytest


pytestmark = pytest.mark.unit


def test_testing_guide_examples_reference_real_repo_files():
    repo_root = Path(__file__).resolve().parents[2]
    docs = repo_root / "docs/sdk_developers/testing.md"
    contents = docs.read_text(encoding="utf-8")

    assert "account_create_transaction_test.py" in contents
    assert "tests/integration/transfer_transaction_e2e_test.py" in contents
    assert (repo_root / "tests/unit/account_create_transaction_test.py").is_file()
    assert (repo_root / "tests/integration/transfer_transaction_e2e_test.py").is_file()
