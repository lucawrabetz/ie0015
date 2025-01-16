import csv


def add_id_to_csv(input_file, output_file):
    """Adds an auto-incrementing ID column to a CSV file and handles carriage returns and quoting.

    Args:
        input_file: Path to the input CSV file.
        output_file: Path to the output CSV file.
    """

    try:
        with open(input_file, "r", newline="", encoding="utf-8") as infile, open(
            output_file, "w", newline="", encoding="utf-8"
        ) as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(
                outfile, quoting=csv.QUOTE_NONNUMERIC
            )  # Quote all non-numeric fields

            # Write the header row with the new 'id' column
            header = next(reader)
            header.insert(0, "id")
            writer.writerow(header)

            # Write the data rows with auto-incrementing IDs and carriage return removal
            for i, row in enumerate(reader, 1):
                row.insert(0, i)
                row[2:] = [field.replace("\r", "") for field in row[2:]]
                writer.writerow(row)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage (same as before):
input_csv_file = "reviews.csv"
output_csv_file = "reviews_with_id.csv"

add_id_to_csv(input_csv_file, output_csv_file)
print(f"CSV file with 'id' column created: {output_csv_file}")
