"""src/nlp/stage03_transform.py.

(EDIT YOUR VERSION OF THIS FILE)

Source: validated BeautifulSoup object
Sink: Pandas DataFrame

NOTE: We use Pandas here to contrast with Polars (from Module 4).
You may use Polars or another library if you prefer:
the pipeline pattern is identical; only the DataFrame API differs.

Pandas vs. Polars:
- Pandas is widely used and has a larger ecosystem.
- Polars is faster, more memory efficient, handles larger datasets,
  and is better suited for production pipelines and complex
  transformations.

Purpose

  Transform validated BeautifulSoup object into a structured format.

Analytical Questions

- Which fields are needed from the HTML data?
- How can records be normalized into tabular form?
- What derived fields would support analysis?

How to find the fields you want to extract from the web page:

  1. Open the web page in your browser.
  2. Right-click anywhere on the page and select "View Page Source".
  3. Use Ctrl+F to search for text you can see on the page,
     e.g. the paper title or "Abstract:".
  4. Find the HTML tag and class that wraps it, e.g.:
       <h1 class="title mathjax"><span class="descriptor">Title:</span>
  5. Use soup.find("h1", class_="title") to locate the associated tag.
  6. Use .get_text(strip=True) to extract the visible text from inside the tag.
  7. If the tag contains a descriptor prefix like "Title:" or "Authors:",
     use .replace("Title:", "").strip() to remove it.
  8. If the tag is not found, soup.find() returns None which is not a string.
     To avoid errors, use a conditional expression to return "unknown" as a safe fallback:
       value = tag.get_text(strip=True) if tag else "unknown"

Apply this process for each field you want to extract for analysis.
The same approach works for any web page.

Example: For the arXiv page at https://arxiv.org/abs/2602.20021,
we can extract the following fields using BeautifulSoup:

- title from <h1 class="title"> (string)
- authors from <div class="authors"> (string)
- abstract from <blockquote class="abstract"> (string)
- primary subject from <div class="subheader"> (string)
- submission date from <div class="dateline"> (string)
- arXiv ID from canonical link in the <head> section (string)

we can calculate derived fields like:
- abstract word count (integer)
- author count (integer)

IMPORTANT: Getting information from a web page is not as simple as it looks.
Web pages are designed for human consumption, not for data extraction.
The HTML structure can be complex and inconsistent, and may require careful inspection and handling to extract the desired information.
The title and abstract are wrapped in tags with descriptor text ("Title:", "Abstract:") that must be removed to get clean values.
The authors are listed as multiple <a> tags inside a <div>, so we must extract each author separately and join them with commas to avoid double-comma issues.
The arXiv ID is not directly visible on the page but can be extracted from the canonical link in the HTML head.
This stage requires careful inspection of the HTML structure and thoughtful handling of edge cases to ensure we extract clean, structured data for analysis.

Use all your resources, creativity, and problem-solving skills to navigate the complexities of web data extraction and transformation.

Notes:
Following our process, do NOT edit this  file directly,
keep it as a working example.

In your custom project, copy this .py file and
append with _yourname.py instead.

Then edit your copied Python file to:
- extract the fields needed for your analysis,
- normalize records into a consistent structure,
- create any derived fields required.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging

from bs4 import BeautifulSoup, Tag
import pandas as pd

# ============================================================
# Section 2. Define Run Transform Function
# ============================================================


def run_transform(
    soup: BeautifulSoup,
    LOG: logging.Logger,
) -> pd.DataFrame:
    """Transform HTML into a structured DataFrame.

    Args:
        soup (BeautifulSoup): Validated BeautifulSoup object.
        LOG (logging.Logger): The logger instance.

    Returns:
        pd.DataFrame: The transformed dataset.
    """
    LOG.info("========================")
    LOG.info("STAGE 03: TRANSFORM starting...")
    LOG.info("========================")

    LOG.info("Extracting metadata from HTML")
    LOG.info(
        "We must manually inspect the HTML structure to identify the fields we want to extract."
    )
    LOG.info(
        "For this arXiv page, we can extract:"
        "\n- Title from <h1 class='title'>"
        "\n- Authors from <div class='authors'>"
        "\n- Abstract from <blockquote class='abstract'>"
        "\n- Primary subject from <div class='subheader'>"
        "\n- Submission date from <div class='dateline'>"
        "\n- ArXiv ID from canonical link"
    )
    LOG.info("Replace any missing content with `unknown` to ensure all are strings.")

    LOG.info("========================")
    LOG.info("STAGE 03a: Extract bibliographic fields (title, authors, abstract)")
    LOG.info("========================")

    # By reading the web page source, we see title tag is located in <h1>
    title_tag: Tag | None = soup.find("h1", class_="title")

    # Authors tag from <div class="authors">
    authors_tag: Tag | None = soup.find("div", class_="authors")

    # Abstract tag from <blockquote class="abstract">
    abstract_tag: Tag | None = soup.find("blockquote", class_="abstract")

    # Extract title text from the tag, or use "unknown" if tag not found.
    # The arXiv page includes "Title:" as a descriptor inside the tag: strip it.
    # .get_text(strip=True) removes extra whitespace and newlines.
    # .replace("Title:", "") removes the descriptor prefix.
    # .strip() removes any remaining leading/trailing whitespace.
    title: str = (
        title_tag.get_text(strip=True).replace("Title:", "").strip()
        if title_tag
        else "unknown"
    )

    # The authors <div> contains one <a> tag per author, like this:
    #   <div class="authors">
    #     <a href="...">Natalie Shapira</a>,
    #     <a href="...">Chris Wendler</a>,
    #     ...
    #   </div>
    #
    # If we use .get_text() on the whole <div>, we get the commas too,
    # which causes double-comma problems in our output.
    #
    # Instead, we find all <a> tags inside the authors <div>.
    # .find_all("a") returns a list of Tag objects, one per author.
    # If the authors_tag is None (not found), we use an empty list.
    author_tags_list: list[Tag] = authors_tag.find_all("a") if authors_tag else []

    # Now we extract the text from each author Tag in the list.
    # We use a list comprehension as a concise way to transform one list into another.
    # It loops over each tag in the list and calls .get_text().
    # This gives us a plain list of author name strings:
    #   ["Natalie Shapira", "Chris Wendler", "Avery Yen", ...]
    #
    # ", ".join(...) then joins that list into a single "comma space"-separated string:
    #   "Natalie Shapira, Chris Wendler, Avery Yen, ..."
    #
    # If author_tags_list is empty (no authors found), use "unknown".
    authors: str = (
        ", ".join([tag.get_text(strip=True) for tag in author_tags_list])
        .replace("Authors:", "")
        .strip()
        if authors_tag
        else "unknown"
    )

    # Extract abstract text, or "unknown" if tag not found.
    # .replace("Abstract:", "") removes the descriptor prefix.
    abstract: str = (
        abstract_tag.get_text(strip=True).replace("Abstract:", "").strip()
        if abstract_tag
        else "unknown"
    )

    # Log the extracted values for debugging
    # Log only the first 100 characters of the abstract
    LOG.info(f"Extracted title: {title}")
    LOG.info(f"Extracted authors: {authors}")
    LOG.info(f"Extracted abstract: {abstract[:100]}...")

    LOG.info("========================")
    LOG.info("STAGE 03b: Extract metadata field subjects from subheader")
    LOG.info("========================")

    # Primary subject from <div class="subheader">
    subheader: Tag | None = soup.find("div", class_="subheader")

    # Subjects may be in the format "Subjects: cs.AI (primary); cs.LG; stat.ML"
    # We can extract the primary subject and also keep the full list if needed.
    subjects: str = subheader.get_text(strip=True) if subheader else "unknown"
    LOG.info(f"Extracted subjects: {subjects}")

    LOG.info("========================")
    LOG.info("STAGE 03c: Extract metadata field date from dateline")
    LOG.info("========================")

    # Submission date from <div class="dateline">
    dateline: Tag | None = soup.find("div", class_="dateline")
    date_submitted_str: str = dateline.get_text(strip=True) if dateline else "unknown"
    LOG.info(f"Extracted submitted: {date_submitted_str}")

    LOG.info("========================")
    LOG.info("STAGE 03d: Extract metadata field arxiv_id from canonical link")
    LOG.info("========================")

    # The canonical link looks like this in the HTML <head>:
    #   <link rel="canonical" href="https://arxiv.org/abs/2602.20021"/>
    #
    # canonical["href"] accesses the HTML `href` attribute value.
    # BeautifulSoup returns it as an AttributeValueList, not a plain string.
    # Cast it to str() first to use string methods like .split().
    #
    # .split("/abs/") splits the URL on the text "/abs/" in the URL, returning a list:
    #   ["https://arxiv.org", "2602.20021"]
    #
    # Lists in Python are zero-indexed, so
    # [0] gets the first element of the list,
    # [1] gets the second element of the list,
    # [-1] gets the last element of the list.
    #
    # To get the arXiv ID, we can use either:
    #   [1] to get the second element, or
    #   [-1] to get the last element
    #
    # Example:
    #   "https://arxiv.org/abs/2602.20021".split("/abs/")
    #   returns a list with two items: ["https://arxiv.org", "2602.20021"]
    #   the last (or second) item is the arxiv id: "2602.20021"
    canonical: Tag | None = soup.find("link", rel="canonical")

    if canonical is None:
        LOG.warning("Canonical link not found, setting arXiv ID to 'unknown'")
        arxiv_id: str = "unknown"
    else:
        href: str = str(canonical["href"])
        arxiv_id: str = href.split("/abs/")[-1]
    LOG.info(f"Extracted arxiv_id: {arxiv_id}")

    LOG.info("========================")
    LOG.info("STAGE 03e: Calculate derived fields")
    LOG.info("========================")

    # Calculate derived field: abstract word count
    abstract_word_count: int = len(abstract.split()) if abstract != "unknown" else 0
    LOG.info(f"Calculated abstract word count: {abstract_word_count}")

    # Calculate derived field: author count
    author_count: int = (
        len([a.strip() for a in authors.split(",")]) if authors != "unknown" else 0
    )
    LOG.info(f"Calculated author count: {author_count}")

    LOG.info("========================")
    LOG.info("STAGE 03f: Build record and create DataFrame")
    LOG.info("========================")

    record = {
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": authors,
        "subjects": subjects,
        "submitted": date_submitted_str,
        "abstract": abstract,
        "abstract_word_count": abstract_word_count,
        "author_count": author_count,
    }

    df = pd.DataFrame([record])
    LOG.info(f"Created DataFrame with {len(df)} row and {len(df.columns)} columns")
    LOG.info(f"Columns: {list(df.columns)}")

    LOG.info("DataFrame Details")
    LOG.info(f"  Title: {title}")
    LOG.info(f"  Author count: {record['author_count']}")
    LOG.info(f"  Abstract word count: {record['abstract_word_count']}")
    LOG.info(f"  DataFrame preview:\n{df.head()}")

    LOG.info("Sink: Pandas DataFrame created")
    LOG.info("Transformation complete.")

    # Return the transformed DataFrame for use in the Load stage.
    return df
