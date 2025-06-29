# Get Slug

A simple Python script to extract slugs from URLs in a CSV file.

## Usage

```bash
python get-slug.py input.csv output.csv
```

- **input.csv**: CSV file with URLs in the first column.
- **output.csv**: Output file containing the extracted slugs.

## How it works

- Reads the input CSV file.
- Extracts the slug (the last part after the last slash) from each URL in the first column.
- Writes each slug to the output CSV file, each enclosed in single quotes and followed by a comma (`'slug',`), one per line.
- Overwrites the output file if it already exists.

## Notes

- Assumes the input file is a simple CSV with one URL per line in the first column.
- Does **not** handle advanced CSV dialects or quoting rules.
- If the input file contains headers, they will be processed as well.
- Does **not** validate URLs; simply extracts the last segment after the last slash.
- If a URL ends with a slash, the slug will be an empty string.
