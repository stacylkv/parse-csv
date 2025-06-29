import csv
import sys

def extract_slug(url):
    parts = [part for part in url.strip().split('/') if part]
    return parts[-1] if parts else ""

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <input_csv> <output_csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            url = row[0]
            slug = extract_slug(url)
            writer.writerow([f"'{slug}',"])

if __name__ == "__main__":
    main()
