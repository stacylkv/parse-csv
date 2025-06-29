# !venv/bin/python3.13
import argparse

def main(input_file_1, input_file_2, output_file):
    with open(input_file_1, 'r') as in_file_1, open(input_file_2, 'r') as in_file_2, open(output_file, 'w') as out_file:
        data_one = set(line.rstrip() for line in in_file_1)
        data_two = set(line.rstrip() for line in in_file_2)
        difference = data_one - data_two
        for element in difference:
            out_file.write(element + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find difference between two CSV files.")
    parser.add_argument('input_file_1', help='First input CSV file')
    parser.add_argument('input_file_2', help='Second input CSV file')
    parser.add_argument('output_file', help='Output CSV file for differences')
    args = parser.parse_args()
    main(args.input_file_1, args.input_file_2, args.output_file)
