# Merge CSV Utility

This utility script merges two CSV files based on their common headers, efficiently handling large files by processing them in chunks.

## Usage

```bash
python merge.py file1.csv file2.csv [output.csv]
```

- `file1.csv` and `file2.csv`: Input CSV files to be merged.
- `output.csv` (optional): Name of the output file. Defaults to `output.csv` if not specified.

## Features

- **Efficient Processing:** Handles large files by reading them in chunks using pandas, making it suitable for datasets larger than available memory.
- **Header-Based Merge:** Merges files based on common headers. Only rows with matching values in those headers are included in the output.
- **Automatic Output:** If no output file is specified, the result is saved as `output.csv` in the script's directory.
- **Graceful Handling:** If no common headers are found, the script prints an error and exits. If there are no rows to merge, it creates an empty CSV with the common headers.
- **Extensible:** Easily adaptable for different merging strategies or additional features such as logging or advanced error handling.

## Requirements

- Python 3.x
- [pandas](https://pandas.pydata.org/)

## Example

```bash
python merge.py data1.csv data2.csv merged.csv
```

## Notes

- Assumes input CSV files are well-formed.
- The script can be extended for more complex data manipulation, such as filtering or transforming data before merging.

## License

MIT License
