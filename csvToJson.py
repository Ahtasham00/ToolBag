#isAww
import pandas as pd

def csv_to_json(csv_file, json_file):
    """
    Convert a CSV (.csv) file to JSON (.json)
    :param csv_file: Path to the input CSV file
    :param json_file: Path where the output JSON file will be saved
    """
    try:
        # Read CSV file
        df = pd.read_csv(csv_file)
        
        # Convert to JSON and save
        df.to_json(json_file, orient="records", indent=4)
        
        print(f"✅ Successfully converted '{csv_file}' to '{json_file}'")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage:
# csv_to_json("data.csv", "data.json")
