#isAww
import pandas as pd

def json_to_csv(json_file, csv_file):
    """
    Convert a JSON (.json) file to CSV (.csv)
    :param json_file: Path to the input JSON file
    :param csv_file: Path where the output CSV file will be saved
    """
    try:
        # Read JSON file
        df = pd.read_json(json_file)
        
        # Convert and save to CSV
        df.to_csv(csv_file, index=False)
        
        print(f"✅ Successfully converted '{json_file}' to '{csv_file}'")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage:
# json_to_csv("data.json", "data.csv")
