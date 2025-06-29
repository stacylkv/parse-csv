# !venv/bin/python3.13
import pandas as pd
import argparse
import sys
import os

def main():
    parser = argparse.ArgumentParser(description="Find broken links (4xx/5xx) in a large Screaming Frog CSV export.")
    parser.add_argument("input_file", help="Path to input CSV file")
    parser.add_argument("output_file", help="Path to output CSV file")
    args = parser.parse_args()

    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist.", file=sys.stderr)
        sys.exit(1)

    status_codes = set(range(400, 600))  # 4xx and 5xx
    chunksize = 100_000  # Adjust based on your memory
    header_written = False

    try:
        for chunk in pd.read_csv(
            args.input_file,
            usecols=['Address', 'Content Type', 'Status Code', 'Status'],
            index_col='Address',
            chunksize=chunksize
        ):
            if not {'Status Code', 'Content Type', 'Status'}.issubset(chunk.columns):
                print("Error: Input CSV does not contain required columns.", file=sys.stderr)
                sys.exit(1)
            filtered = chunk[chunk['Status Code'].isin(status_codes)]
            filtered = filtered.sort_index()
            filtered.to_csv(args.output_file, mode='a', header=not header_written, encoding='utf-8')
            header_written = True
    except pd.errors.EmptyDataError:
        print("Error: Input CSV file is empty or invalid.", file=sys.stderr)
        sys.exit(1)
    except pd.errors.ParserError as e:
        print(f"Error parsing CSV: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
