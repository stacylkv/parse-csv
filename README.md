# Python Data Processing and SEO Scripts

Welcome to the **Python Data Processing and SEO Scripts** repository. This project contains a collection of utility scripts for common data manipulation and SEO analysis tasks. Each script is designed for efficiency and serves a specific purpose, from parsing file formats to analyzing web crawl data.

## Project Scripts

This repository includes the following scripts. Refer to their individual `README.md` files for detailed usage and functionality:

- **[Screaming Frog Broken Link Finder](get-broken-links/README.md)**: Analyzes large CSV exports from the Screaming Frog SEO Spider to identify and report broken links (4xx and 5xx status codes).
- **[Merge CSV Utility](merge-csv/README.md)**: This utility script merges two CSV files based on their common headers, efficiently handling large files by processing them in chunks.
- **[JSON to CSV Converter](json-to-csv/README.md)**: Converts complex, nested JSON files into a flattened CSV format.
- **[Get Difference](get-difference/README.md)**: A simple Python script to find the difference between two text files (such as CSVs) line by line.
- **[Get Slug](get-slug/README.md)**: A simple Python script to extract slugs from URLs in a CSV file.
- **[Remove Duplicates Utility](remove-duplicates/README.md)**: A simple Python script to remove duplicate lines from a text file.

## Setup and Usage

To use these scripts, you need Python 3 installed. It is recommended to use a Python virtual environment to manage dependencies.

### 1. Create a Virtual Environment

Navigate to the root directory of this project and run:

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

- On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```
- On Windows:
    ```cmd
    .\venv\Scripts\activate
    ```

Your terminal prompt will change to show the virtual environment is active.

### 3. Install Dependencies

Create a `requirements.txt` file in the project root and add required packages (e.g., `pandas`):

```
pandas
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Running the Scripts

With the environment set up, run any script from the project root. See each script's `README.md` for command-line arguments and examples.

To deactivate the virtual environment:

```bash
deactivate
```

---

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.