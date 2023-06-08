# MedThread Demo

## Overview

The goal of this project is to automate the process of extracting data, correlations, key features, and conclusions from a database  of research papers. Data is parsed in the form of text as well as quantitative charts and tables.

The model draws conclusions from the text, and converts any numeric data into  data structures for further analysis via machine learning.

The textual conclusions are compared with the output of the analytical model to verify results and provide key insights, as well as citations pointing to specific areas in the source material that can be used as evidence.


## Technical Overview

The model is written in Python with the following dependencies:

```
pdf2image
pytesseract
tabula
```

## Setup and Usage

### Parsing Papers in PDF Format

- Install Dependencies using pip/conda/brew
- Place papers in single folder called Papers (or rename in code as needed)
- Create empty folder called ParsedPapers (or rename in code as needed)
- Run readPaper.py

PDF text (as .txt) and Table data (.csv) files will be saved to ParsedPapers folder as '<paper filename> (TEXT).txt' and '<paper filename> (TABLES).csv'
  
### Generating Report from Data
  
1. ChatGPT API to summarize findings (piecemeal)
2. Pandas DF to run correlation analysis




