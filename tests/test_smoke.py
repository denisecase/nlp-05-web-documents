"""Offline smoke tests for the web-document EVTL stages."""

import logging
from types import SimpleNamespace

import pandas as pd
import pytest
import requests

from nlp.stage01_extract import run_extract
from nlp.stage02_validate import run_validate
from nlp.stage03_transform import run_transform
from nlp.stage04_load import run_load

HTML = """<html><head><link rel="canonical" href="https://arxiv.org/abs/1234.56789"></head>
<body>
<h1 class="title">Title: Example Paper</h1>
<div class="authors"><a>Ada</a><a>Grace</a></div>
<blockquote class="abstract">Abstract: Language models analyze text.</blockquote>
<div class="subheader">Subjects: Computation and Language</div>
<div class="dateline">Submitted on 1 January 2026</div>
</body></html>
"""


def test_html_stages_extract_document_metadata(monkeypatch, tmp_path):
    """Exercise extraction, page validation, transformation, and CSV loading."""

    def fake_get(url, *, headers, timeout):
        assert url == "https://example.test/paper"
        assert "User-Agent" in headers
        assert timeout == 30
        return SimpleNamespace(text=HTML, raise_for_status=lambda: None)

    monkeypatch.setattr(requests, "get", fake_get)
    log = logging.getLogger(__name__)
    raw_path = tmp_path / "raw.html"
    csv_path = tmp_path / "processed.csv"

    html = run_extract(
        "https://example.test/paper", {"User-Agent": "pytest"}, raw_path, log
    )
    df = run_transform(run_validate(html, log), log)
    run_load(df, csv_path, log)

    assert raw_path.read_text(encoding="utf-8") == HTML
    assert csv_path.stat().st_size > 0
    saved = pd.read_csv(csv_path, dtype={"arxiv_id": str})
    assert saved.loc[0, "title"] == "Example Paper"
    assert saved.loc[0, "authors"] == "Ada, Grace"
    assert saved.loc[0, "arxiv_id"] == "1234.56789"
    assert saved.loc[0, "author_count"] == 2
    assert saved.loc[0, "abstract_word_count"] == 4


def test_html_validation_requires_an_abstract():
    """Reject a page that does not contain the required abstract element."""
    missing_abstract = HTML.replace('class="abstract"', 'class="missing"')
    with pytest.raises(ValueError, match="abstract"):
        run_validate(missing_abstract, logging.getLogger(__name__))
