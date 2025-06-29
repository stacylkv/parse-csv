# Remove Duplicates Utility

A simple Python script to remove duplicate lines from a text file.

## Usage

```bash
python remove_dupl.py input_file.csv output_file.csv
```

- **input_file.csv**: Path to the input file (one entry per line).
- **output_file.csv**: Path to the output file (will be overwritten if it exists).

## How it works

- Reads the input file.
- Removes duplicate lines.
- Writes only unique lines to the output file.

## Notes

- This script treats each line as a unique entry and does **not** handle CSV formatting or multi-column data.
- For more complex CSV files, use a CSV reader/writer to ensure proper handling.
- For advanced data processing, consider using libraries like [pandas](https://pandas.pydata.org/).

## Limitations

- Not intended for complex data transformation.
- Best suited for cleaning up simple data files or logs.
