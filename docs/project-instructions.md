# Project Instructions

## Goal

Apply **web document acquisition and information extraction**
to retrieve HTML content, validate document structure,
and transform extracted information into structured data.

Use an Extract, Validate, Transform, Load (EVTL) pipeline.

## A. Set Up Machine

Complete [Workflow A: Set Up Machine](https://denisecase.github.io/pro-analytics-02/workflow-a-set-up-machine/)
if your machine is not ready.

## B. Explore Example Project

Follow [Workflow B: Explore Example Project](https://denisecase.github.io/pro-analytics-02/workflow-b-explore-example-project/).

Explore how the example:

- Retrieves an HTML document from arXiv.
- Preserves the original HTML content.
- Parses the document using BeautifulSoup.
- Validates required HTML elements.
- Extracts document text and metadata.
- Calculates derived fields.
- Saves the structured results as a CSV artifact.

Review how HTML tags, attributes, and selectors
are used to locate the required information.

Consider what happens when an expected element is missing.

## C. Start New Project

Follow [Workflow C: Start New Project](https://denisecase.github.io/pro-analytics-02/workflow-c-start-new-project/).

IMPORTANT: New repository name:
**nlp-05-web-documents-custom**.

VERIFY: You have completed git add-commit-push to GitHub at least twice.

## D. Apply Skills

Follow [Workflow D: Apply Skills](https://denisecase.github.io/pro-analytics-02/workflow-d-apply-skills/).

**Your problem:** Extract and analyze metadata
from an academic paper of your choice.

Select a different paper from
[arXiv](https://arxiv.org/).

Keep the original `_case.py` files as working examples.
Create and modify copies for your custom processing stages.

Update the pipeline imports as needed
so your custom implementation executes.

### Progression 1. Your Project Works Like the Example

Ensure your new custom project runs like the example.

Verify that key files have been updated to use **your GitHub account** and
the **new custom repository name**.

### Progression 2. Make a Technical Modification

Add one new derived field to the Transform stage.

For example, calculate the number of sentences
in the extracted abstract.

Verify that the new field appears
in the resulting DataFrame and CSV artifact.

Explain how the field is calculated
and what it measures.

### Progression 3. Apply to a New Problem

Apply the EVTL pipeline
to your selected arXiv paper.

- Update the source URL in your custom configuration.
- Retrieve and inspect the HTML document.
- Identify the elements containing the desired information.
- Verify that the HTML structure meets validation requirements.
- Extract the title, authors, abstract, and subject information.
- Apply appropriate cleaning to extracted values.
- Include your new derived field.
- Save the structured results as a CSV artifact.
- Verify that the extracted information is correct.

Explain how the selected HTML elements
support the extraction process.

Identify one challenge or limitation
associated with extracting information from HTML.

The goal is to understand how web documents
can be converted into structured datasets
using a reproducible pipeline.

## E. Finalize Project

Follow [Workflow E: Finalize Project](https://denisecase.github.io/pro-analytics-02/workflow-e-finalize/).

Use `docs/index.md` to report:

- Selected document and source URL.
- Information selected for extraction.
- HTML structure and validation requirements.
- Transformation and derived fields.
- Extracted results and a relevant visual.
- Interpretation and limitations.

Include a clickable link to your repository and artifacts.

## Success

- [ ] README.md project-specific links use **your GitHub account**.
- [ ] README.md project-specific links use **your custom repository name**.
- [ ] docs/index.md project-specific links use **your GitHub account**.
- [ ] docs/index.md project-specific links use **your custom repository name**.
- [ ] pyproject.toml `name` has been changed to use **your custom repository name**.
- [ ] The `src/nlp` folder reflects your authorship and custom work.
- [ ] The custom EVTL pipeline processes your selected document.
- [ ] The raw HTML and processed CSV artifacts are available.
- [ ] All necessary commands are provided and work successfully.
- [ ] Links to the Professional Python Guide (pro-analytics-02) remain unchanged.
- [ ] Commit history shows **at least** the git add-commit-push history required in the instructions.

---

[◄ Back to Home](index.md)
