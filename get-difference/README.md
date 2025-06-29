# Get Difference

A simple Python script to find the difference between two text files (such as CSVs) line by line.

## Usage

```bash
python get_difference.py input_file_1.csv input_file_2.csv output_file.csv
```

- Reads `input_file_1.csv` and `input_file_2.csv`.
- Writes lines that are in `input_file_1.csv` but **not** in `input_file_2.csv` to `output_file.csv`.
- The output file will be **overwritten** if it already exists.
- Input files should be text files with one entry per line and in the same format.

## Notes

- Ensure both input files contain the same type of data.
- This script does not handle complex CSV parsing (e.g., quoted fields with commas).
