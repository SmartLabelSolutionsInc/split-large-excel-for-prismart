import pandas as pd
import math
import os

# Input file name (change this to your actual file path)
input_file = 'template.xlsx'  # Replace with your Excel file name
output_folder = 'output_files'  # Folder to save split files

# Number of data rows per output file (excluding header)
rows_per_file = 950

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the entire Excel file
df = pd.read_excel(input_file)

# Total number of data rows (excluding header)
total_rows = len(df)

# Calculate the number of output files needed
num_files = math.ceil(total_rows / rows_per_file)

print(f"Total rows: {total_rows}. Splitting into {num_files} files...")

for i in range(num_files):
    # Determine start and end row indices for the current chunk
    start_row = i * rows_per_file
    end_row = start_row + rows_per_file

    # Extract the chunk of rows
    df_chunk = df.iloc[start_row:end_row]

    # Construct output file name (e.g., output_1.xlsx, output_2.xlsx, etc.)
    output_filename = os.path.join(output_folder, f'output_{i+1}.xlsx')

    # Write the chunk to an Excel file, including the header
    df_chunk.to_excel(output_filename, index=False)

    print(f"Written: {output_filename}")

print("All files created successfully.")
