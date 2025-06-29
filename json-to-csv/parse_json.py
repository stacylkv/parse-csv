# !venv/bin/python3.13
import json
import csv
import argparse

def flatten_json(y, prefix=''):
    out = {}
    if isinstance(y, dict):
        for k, v in y.items():
            out.update(flatten_json(v, f"{prefix}{k}." if prefix else k + "."))
    elif isinstance(y, list):
        for i, v in enumerate(y):
            out.update(flatten_json(v, f"{prefix}{i}."))
    else:
        out[prefix[:-1]] = y
    return out

def collect_headers_and_rows(json_list):
    headers = set()
    rows = []
    for item in json_list:
        flat = flatten_json(item)
        headers.update(flat.keys())
        rows.append(flat)
    return sorted(headers), rows

def main():
    parser = argparse.ArgumentParser(description="Convert JSON to CSV with flattening.")
    parser.add_argument("input_path", help="Path to input JSON file")
    parser.add_argument("output_path", help="Path to output CSV file")
    args = parser.parse_args()

    with open(args.input_path, 'r') as json_file:
        data = json.load(json_file)
        
        # If the root is a dict with a single key, use its value as the list
        if isinstance(data, dict) and len(data) == 1 and isinstance(next(iter(data.values())), list):
            data = next(iter(data.values()))
        elif isinstance(data, dict):
            data = [data]
        elif not isinstance(data, list):
            raise ValueError("Unsupported JSON structure.")

    headers, rows = collect_headers_and_rows(data)

    with open(args.output_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

if __name__ == "__main__":
    main()
