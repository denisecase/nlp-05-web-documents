# Glossary

This module focuses on acquiring,
parsing, and extracting information
from semi-structured web documents.

## Quick Lookup

### HTML and Document Structure

- **HTML** - markup language for structuring web documents.
- **HTML Element** - a component of an HTML document.
- **HTML Tag** - markup identifying an HTML element.
- **HTML Attribute** - additional information associated with an element.
- **CSS Class** - a label used to identify or style HTML elements.
- **DOM** - a tree-based representation of a document.
- **HTML Parser** - software that interprets HTML structure.
- **Semi-Structured Data** - data with organizational structure but no fixed tabular schema.

### Web Acquisition and Extraction

- **Web Scraping** - extracting information from web pages.
- **Page Source** - the HTML source of a web page.
- **Element Selection** - locating elements in a document.
- **Text Extraction** - retrieving text from document content.
- **Metadata** - information describing a document.
- **Canonical URL** - the preferred URL for a web resource.
- **Structural Validation** - checking for expected document elements.
- **Fallback Value** - a substitute used when information is unavailable.

### BeautifulSoup Terms and Methods

- **BeautifulSoup** - a Python library for parsing HTML and XML.
- **Tag** - a BeautifulSoup object representing an HTML element.
- **find()** - returns the first matching element.
- **find_all()** - returns all matching elements.
- **get_text()** - extracts text from an element.
- **AttributeValueList** - a BeautifulSoup list type for multi-valued attributes.

### Python Methods and Constructs

- **str.join()** - combines strings using a separator.
- **str.split()** - separates a string into substrings.
- **str.replace()** - replaces matching text within a string.
- **List Indexing** - accesses list elements by position.
- **List Comprehension** - creates lists using expressions and iteration.

## HTML and Document Structure

### HTML (HyperText Markup Language)

**HTML** is the standard markup language
used to structure content in web pages.

HTML defines elements such as headings,
paragraphs, links, tables, and sections.

See [HTML Documentation](https://developer.mozilla.org/en-US/docs/Web/HTML).

### HTML Element

An **HTML element** is a component
of an HTML document.

Elements may contain text,
attributes, and nested elements.

An element is typically represented
by a start tag, content, and an end tag,
although some elements are void elements.

### HTML Tag

An **HTML tag** is markup
used to identify an element
and its boundaries.

Tags use angle brackets
and may contain attributes.

Examples include:

- `<h1>` - a top-level heading.
- `<p>` - a paragraph.
- `<a>` - a hyperlink.
- `<div>` - a generic container.
- `<span>` - an inline container.

### HTML Attribute

An **HTML attribute** provides
additional information about an element.

Attributes may identify an element,
specify a link destination,
or describe presentation and behavior.

For example:

```html
<a href="https://example.org">Example</a>
```

The `href` attribute identifies
the destination of the hyperlink.

### CSS Class

A **CSS class** is a value associated
with an element's `class` attribute.

Classes are commonly used for styling
and may also help identify elements
during information extraction.

Class names can change when websites are updated,
so they are not necessarily stable identifiers.

### DOM (Document Object Model)

The **DOM** is a tree-based representation
of a document that allows software
to inspect and manipulate its structure.

HTML parsing libraries also produce
tree-like representations of documents.

A parsed HTML tree is related to,
but not necessarily identical to,
the DOM constructed by a web browser.

See [Document Object Model](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model).

### HTML Parser

An **HTML parser** interprets HTML markup
and produces a structured representation
of the document.

Parsed documents can be searched
and traversed to locate elements,
attributes, and text.

### Semi-Structured Data

**Semi-structured data** contains
organizational information without necessarily
following a fixed tabular schema.

HTML and XML documents are common examples.

The structure can support information extraction,
but may vary between documents and sources.

## Web Acquisition and Extraction

### Web Scraping

**Web scraping** is the automated process
of retrieving and extracting information
from web pages.

Scraping commonly involves
fetching a document, parsing its structure,
and selecting relevant information.

Responsible scraping respects
applicable access restrictions,
server resources, and data-use requirements.

### Page Source

**Page source** is the HTML source
of a web page.

In a browser, right-click and select
"View Page Source" to inspect the HTML
and identify elements for extraction.

Browser shortcuts commonly include:

- `Ctrl+U` on Windows.
- `Cmd+Option+U` on macOS in supported browsers.

The original HTML source may differ
from the rendered document when JavaScript
modifies the page after loading.

### Requests

**Requests** is a Python library
used to make HTTP requests
and retrieve web content.

The `requests.get()` function
sends an HTTP GET request
and returns a response object.

For example:

```python
import requests

response = requests.get(
    "https://example.org",
    timeout=30,
)
```

The response object provides access
to the status code, headers,
and returned content.

### Element Selection

**Element selection** identifies document elements
using their names, attributes,
positions, or structural relationships.

Selection rules determine which portions
of a document are extracted.

### Text Extraction

**Text extraction** retrieves textual content
from a document or selected elements.

Extraction may require distinguishing
meaningful content from navigation,
formatting, scripts, and other page components.

### Metadata

**Metadata** is information
that describes a document or resource.

Metadata may identify authorship,
publication information, subject matter,
or other document properties.

### Canonical URL

A **canonical URL** identifies
a preferred address for a web resource.

Web pages may declare a canonical URL
to indicate which address should be treated
as the preferred representation.

A canonical URL is metadata supplied
by the source and should not automatically
be treated as independently verified.

### Canonical Link

A **canonical link** is an HTML `<link>`
element that declares the preferred URL
for a web resource.

It commonly appears in the document's
`<head>` section.

Example:

```html
<link rel="canonical" href="https://example.org/article">
```

The `href` attribute contains the URL.

Canonical URLs may also contain identifiers
that can be extracted for structured analysis.

### Structural Validation

**Structural validation** checks whether
a document contains the elements
and attributes expected by an extraction process.

Validation helps identify changes
in document structure
before downstream processing.

### Descriptor Prefix

A **descriptor prefix** is text
included inside an HTML element
that labels its content for human readers.

Examples include:

- `Title:`
- `Authors:`
- `Abstract:`

Descriptor prefixes may need to be removed
when extracting clean data values.

Python string methods such as `str.replace()`
can be used for this purpose.

### Fallback Value

A **fallback value** is a substitute
used when expected information
is unavailable or cannot be extracted.

Fallback values may support
consistent data representations.

Examples include:

- `"unknown"` for unavailable text.
- `0` for an unavailable numeric count, when appropriate.
- `None` for a missing or undefined value.

However, fallback values should not conceal
missing required information
or validation failures.

## BeautifulSoup Terms and Methods

### BeautifulSoup

**BeautifulSoup** is a Python library
for parsing HTML and XML documents.

BeautifulSoup creates a traversable object
from raw document content.

The resulting structure supports
searching for tags, attributes,
and text content.

Example:

```python
from bs4 import BeautifulSoup

html = "<html><body><h1>Example</h1></body></html>"

soup = BeautifulSoup(html, "html.parser")
```

### Tag

A **Tag** is a BeautifulSoup object
representing a single HTML element.

Tag objects support operations such as:

- Accessing attributes.
- Extracting text.
- Searching for nested elements.
- Traversing document structure.

Methods include `.get_text()`
and `.find_all()`.

A `find()` operation may return
a `Tag` object or `None`.

### find()

The **find()** method searches
a parsed document or element
for the first matching descendant.

Search criteria may include
a tag name and optional attributes.

It returns the first matching element,
or `None` if no match is found.

Example:

```python
heading = soup.find("h1", class_="title")
```

The result can then be inspected
or used for text extraction.

### find_all()

The **find_all()** method searches
a parsed document or element
for all matching descendants.

It returns a collection of matching elements.

If no elements match,
the collection is empty.

Example:

```python
links = soup.find_all("a")
```

This retrieves all matching
anchor elements in the searched portion
of the document.

### get_text()

The **get_text()** method retrieves
text content from a BeautifulSoup
document or element.

It combines text from the element
and its descendants.

For example:

```python
text = heading.get_text(strip=True)
```

Common arguments include:

- `strip=True` - removes leading and trailing whitespace from text fragments.
- `separator=", "` - inserts a separator between extracted text fragments.

Example:

```python
text = element.get_text(
    separator=", ",
    strip=True,
)
```

The method extracts text nodes.
It does not determine whether
the text is visually displayed
in a browser.

### AttributeValueList

**AttributeValueList** is a BeautifulSoup
list type used for HTML attributes
that support multiple values.

For example, an HTML element may contain
multiple CSS classes:

```html
<div class="article featured">Content</div>
```

Accessing the class attribute may return:

```python
tag["class"]
# ["article", "featured"]
```

Not every HTML attribute returns
an AttributeValueList.

For example, a typical `href` attribute
returns a string:

```python
link["href"]
# "https://example.org"
```

Attribute values should be handled
according to their expected types.

## Python Methods and Constructs

### String Methods

#### str.join()

The **str.join()** method combines
an iterable of strings into one string.

The string used to call the method
becomes the separator.

Example:

```python
names = ["Alice", "Bob", "Carol"]

result = ", ".join(names)

# "Alice, Bob, Carol"
```

This is useful when combining
multiple extracted text values
into a single structured field.

#### str.split()

The **str.split()** method separates
a string into a list of substrings.

A separator may be specified.

Example:

```python
url = "https://example.org/articles/123"

parts = url.split("/")

# ["https:", "", "example.org", "articles", "123"]
```

Without an explicit separator,
`split()` separates text using whitespace.

Example:

```python
text = "Natural language processing"

tokens = text.split()

# ["Natural", "language", "processing"]
```

#### str.replace()

The **str.replace()** method creates
a new string by replacing occurrences
of selected text.

Example:

```python
raw_title = "Title: Example Article"

title = raw_title.replace("Title:", "").strip()

# "Example Article"
```

This method is useful for removing
known descriptor prefixes
from extracted text.

Because strings are immutable,
`replace()` returns a new string
rather than modifying the original.

### List Operations

#### List Indexing

**List indexing** accesses
individual elements of a list
using their positions.

Python lists are zero-indexed:

- `[0]` accesses the first element.
- `[1]` accesses the second element.
- `[-1]` accesses the last element.

Example:

```python
values = ["first", "second", "third"]

first = values[0]
last = values[-1]
```

Negative indices count backward
from the end of the list.

#### List Comprehension

A **list comprehension** creates
a new list by evaluating an expression
for each item in an iterable.

Example:

```python
words = ["Python", "NLP", "Data"]

lowercase_words = [word.lower() for word in words]

# ["python", "nlp", "data"]
```

List comprehensions are useful
for transforming collections
of extracted elements or values.

For example:

```python
names = [tag.get_text(strip=True) for tag in author_tags]
```

This creates a list of text values
from a collection of BeautifulSoup
Tag objects.

## Tabular Data Tools

### Pandas

**Pandas** is a Python library
for manipulating and analyzing
structured, tabular data.

Pandas provides DataFrames
for organizing records into
rows and columns.

A DataFrame can be created
from a list of dictionaries:

```python
import pandas as pd

records = [
    {"title": "Article A", "word_count": 120},
    {"title": "Article B", "word_count": 95},
]

df = pd.DataFrame(records)
```

Each dictionary represents a record,
and its keys identify fields.

Pandas supports operations such as:

- Selecting and filtering records.
- Transforming data values.
- Calculating derived fields.
- Summarizing data.
- Reading and writing files.

---

[◄ Back to 🏠 Home](index.md)
