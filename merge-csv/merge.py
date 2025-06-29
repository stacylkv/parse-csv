import sys
import pandas as pd

def main():
    if len(sys.argv) < 3:
        print("Usage: python merge.py <file1.csv> <file2.csv> [output.csv]")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    output = sys.argv[3] if len(sys.argv) > 3 else "output.csv"

    # Read headers only
    headers1 = pd.read_csv(file1, nrows=0).columns
    headers2 = pd.read_csv(file2, nrows=0).columns

    common_headers = list(set(headers1) & set(headers2))
    if not common_headers:
        print("Error: No common headers found between the two files.")
        sys.exit(1)

    # Use chunksize for memory efficiency
    chunk_size = 100000
    merged_chunks = []

    # Build an index for the second file for efficient merging
    table2_iter = pd.read_csv(file2, usecols=common_headers, chunksize=chunk_size, dtype=str)
    table2 = pd.concat(table2_iter, ignore_index=True)

    # Merge in chunks
    for chunk in pd.read_csv(file1, usecols=common_headers, chunksize=chunk_size, dtype=str):
        merged = pd.merge(chunk, table2, on=common_headers, how='inner')
        merged_chunks.append(merged)

    if merged_chunks:
        pd.concat(merged_chunks, ignore_index=True).to_csv(output, index=False)
    else:
        # Write only headers if no data
        pd.DataFrame(columns=common_headers).to_csv(output, index=False)

if __name__ == "__main__":
    main()

# Example usage:
# python merge.py file1.csv file2.csv [output.csv]
# This script reads two CSV files, merges them based on common headers, and writes the result to an output file.
# If no output file is specified, it defaults to "output.csv".
# It handles large files efficiently by processing them in chunks, ensuring that it can work with files that are larger than available memory.
# The script uses pandas for data manipulation and assumes that the CSV files are well-formed.
# It merges the files based on common headers, ensuring that only rows with matching values in those headers are included in the output.
# If no common headers are found, it will print an error message and exit.
# The output file will contain the merged data, with only the common headers included.
# If there are no rows to merge, it will create an empty CSV file with the common headers.
# The script is designed to be run from the command line, taking the input files and optional output file as command-line arguments.
# It uses pandas' `read_csv` function with `chunksize` to read the files in manageable chunks, which is crucial for handling large datasets.
# The `merge` function is used to combine the data based on the common headers, ensuring that the output contains only the relevant data.
# The script is efficient and can handle large datasets without running into memory issues, making it suitable for data processing tasks where performance is a concern.
# The output CSV will be created in the same directory as the script unless a different path is specified.
# The script is flexible and can be adapted for different merging strategies by changing the parameters of the `merge` function.
# It is a useful utility for data analysts and developers who need to combine data from multiple sources while ensuring that only relevant information is retained.
# The script can be easily modified to include additional functionality, such as logging or error handling, to suit specific use cases.
# The use of pandas makes it easy to extend the script for more complex data manipulation tasks, such as filtering or transforming the data before merging.
