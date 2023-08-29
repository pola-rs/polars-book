"""Run all Python code snippets."""
import matplotlib
import pytest
import runpy
from pathlib import Path

# Do not show plots
matplotlib.use("Agg")

python_snippets_dir = Path(__file__).parent.parent / "docs" / "src" / "python"
snippets = list(python_snippets_dir.rglob("*.py"))


@pytest.mark.parametrize("snippet", snippets)
def test_run_python_snippets(snippet):
    runpy.run_path(snippet)
