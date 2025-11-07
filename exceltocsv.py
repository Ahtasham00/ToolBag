#isAww
import pandas as pd

def excel_to_csv(excel_file, csv_file):
    """
    Convert an Excel (.xlsx) file to CSV (.csv)
    :param excel_file: Path to the input Excel file
    :param csv_file: Path where the output CSV file will be saved
    """
    try:
        # Read Excel file
        df = pd.read_excel(excel_file)
        
        # Save as CSV
        df.to_csv(csv_file, index=False)
        
        print(f"✅ Successfully converted '{excel_file}' to '{csv_file}'")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage:
# excel_to_csv("data.xlsx", "data.csv")
