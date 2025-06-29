# Screaming Frog Broken Link Finder

A Python script to filter broken links (4xx/5xx status codes) from a large Screaming Frog CSV export.

## Usage

```bash
python get_broken.py input.csv output.csv
```

- **input.csv**: Path to the Screaming Frog CSV export.
- **output.csv**: Path where the filtered results will be saved.

## Features

- Reads large CSV files in chunks for efficient memory usage.
- Filters out rows with broken links (status codes 4xx/5xx).
- Outputs a CSV containing only broken links, sorted by the `Address` column.
- Handles missing or invalid input gracefully with error messages.
- Uses `pandas` for fast data processing.

## Requirements

- Python 3.x
- pandas

## Notes

- Ensure the input CSV contains the columns: `Address`, `Content Type`, `Status Code`, `Status`.
- The output file will be created or overwritten.
- Adjust the `chunksize` parameter in the script for optimal performance based on your system's memory.

