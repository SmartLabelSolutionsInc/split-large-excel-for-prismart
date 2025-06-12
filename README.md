# Excel Splitter for Hanshow PriSmart Import

This Python utility splits a large Excel file into multiple smaller files, each containing a **customizable number of rows** (excluding the header). It is designed to address a limitation in the **Hanshow PriSmart** electronic shelf label (ESL) system, which only allows importing **up to 1000 rows per file**.

By using this tool, users can efficiently break down large datasets into import-ready files that conform to PriSmart’s constraints.

---

## ✅ Features

- Splits any Excel file (`.xlsx`) into smaller files with a user-defined number of data rows per file
- Preserves the original **header row** in every output file
- Automatically **treats all values as strings** to prevent unintended type conversions (e.g., leading zeros)
- Generates sequential output files like `output_1.xlsx`, `output_2.xlsx`, etc.
- Automatically creates an output folder for clean organization

---

## 📦 Requirements

- Python 3.6+
- Required packages:
  - `pandas`
  - `openpyxl`

Install dependencies using pip:

```bash
pip install pandas openpyxl

```

## 🚀 Usage

1. Place your Excel file in the project directory (e.g., `your_file.xlsx`)
2. Open `split_excel.py` and configure the following two lines:

```python
input_file = 'your_file.xlsx'  # Name of your Excel file
rows_per_file = 950            # Number of data rows per output file (change as needed)
```

3. Run the script:

```python
python split_excel.py
```

4. Output files will be saved in the `output_files/` directory.

## ⚙️ Configuration

You can freely change the number of rows per output file by editing:

```python
rows_per_file = 950
```

For example:

- Use `950` to stay safely below the 1000-row limit in PriSmart
- Use `1000` if you're confident your data will import correctly
- Use any number appropriate for your case

## 📌 Motivation

Hanshow’s **PriSmart ESL platform** limits bulk import files to **no more than 1000 rows**. This tool helps automate the splitting of large product lists into smaller, system-compatible chunks for efficient import.

## 📂 Output Example

For an input file with 10,000 rows and `rows_per_file = 950`, you will get:

```sql
output_files/
├── output_1.xlsx  (rows 1–950)
├── output_2.xlsx  (rows 951–1900)
├── ...

```

## 📝 Notes

- The script assumes a clean Excel format without merged cells.
- All columns are loaded as strings to avoid Excel type conversion issues (e.g., `00123` becoming `123`).
- If you're using a `.csv` file instead of `.xlsx`, replace:

pd.read_excel(...)

```python
pd.read_excel(...)
```

with

```python
pd.read_csv(...)
```

