import pandas as pd
# Import chardet (needed if we go back to read_csv and need encoding detection)
import chardet


def read_data(path):
    # Attempt to read as an Excel file first due to the .xlsx extension
    try:
        dataset = pd.read_excel(path)
        print("File read successfully as Excel.")
    except Exception as e:
        print(f"Failed to read as Excel: {e}")
        # If reading as Excel fails, assume it's a CSV and try with different encodings
        print("Attempting to read as CSV with encoding detection...")
        # Original chardet detection code
        with open(path, 'rb') as f:
            result = chardet.detect(f.read())
            detected_encoding = result['encoding']
            print(f"Chardet detected encoding: {detected_encoding}")

        # Try reading with detected encoding
        try:
            dataset = pd.read_csv(path, encoding=detected_encoding)
            print("File read successfully with detected encoding.")
        except UnicodeDecodeError:
            print(f"UnicodeDecodeError with detected encoding '{detected_encoding}'. Trying common encodings...")
            # List of common encodings to try
            common_encodings = ['latin-1', 'cp1252', 'utf-8']
            for encoding in common_encodings:
                try:
                    dataset = pd.read_csv(path, encoding=encoding)
                    print(f"File read successfully with encoding: {encoding}")
                    break # Exit the loop if successful
                except UnicodeDecodeError:
                    print(f"UnicodeDecodeError with encoding: {encoding}")
                except Exception as e:
                    print(f"Error reading with encoding {encoding}: {e}")
            else:
                print("Failed to read the file with common encodings. The file might be corrupted or have an unusual encoding.")
                
    return dataset