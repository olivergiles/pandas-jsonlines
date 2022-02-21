# Pandas JSONLINES

- Description: A short script to read jsonlines files into pandas dataframe.
- Why: jsonlines is a great format for scraping especially when using the 
scrapy framework.

# Installation

```bash
pip install pandas-jsonlines
```

# Usage

```
from pandas_jsonlines.read_jsonlines import read_jsonlines
df = read_jsonlines("file.jsonlines")
```
