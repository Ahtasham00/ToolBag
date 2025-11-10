#isAww
import pandas as pd

def csv_to_excel(csv_file, excel_file):
    """
    Convert a CSV (.csv) file to Excel (.xlsx)
    :param csv_file: Path to the input CSV file
    :param excel_file: Path where the output Excel file will be saved
    """
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)
        
        # Save as Excel file
        df.to_excel(excel_file, index=False)
        
        print(f"✅ Successfully converted '{csv_file}' to '{excel_file}'")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage:
# csv_to_excel("data.csv", "data.xlsx")
