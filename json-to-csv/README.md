# JSON to CSV Converter

This script converts a JSON file to a CSV file, flattening nested structures for easier analysis.

## Usage

```bash
python parse_json.py input.json output.csv
```

## Features

- Converts JSON files to CSV format.
- Flattens nested JSON structures.
- Supports input JSON as a list of dictionaries or a single dictionary.
- If the input is a dictionary with a single key, uses its value as the list to convert.
- Handles command-line arguments for input and output file paths using `argparse`.
- Overwrites the output CSV file if it already exists.
- Prints error messages for invalid input or unsupported formats.

## Requirements

- Python 3.x

## Notes

- Ensure your input JSON file is valid and contains the data you want to convert.
- The script will raise a `ValueError` for unsupported JSON formats.

