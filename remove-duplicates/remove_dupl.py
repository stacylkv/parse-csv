import sys

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    seen = set()
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            line_clean = line.rstrip('\n')
            if line_clean in seen:
                continue
            seen.add(line_clean)
            out_file.write(line)

if __name__ == "__main__":
    main()
