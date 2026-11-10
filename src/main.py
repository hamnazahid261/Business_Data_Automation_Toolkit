
import logging
import os
from pathlib import Path

from src.reader import read_csv, read_json
from src.cleaner import clean_records
from src.reporter import (
    save_clean_data,
    save_exception_report,
    save_summary
)


def setup_logging():
    """Configure application logging."""

    log_path = Path(
        os.getenv("LOG_FILE", "logs/processing.log")
    )
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        filename=log_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8",
        force=True
    )


def main():
    """Run the complete data processing workflow."""

    setup_logging()

    input_file = Path(
        os.getenv("INPUT_FILE", "data/input/properties.csv")
    )

    output_dir = Path(
        os.getenv("OUTPUT_DIR", "data/output")
    )

    report_dir = Path(
        os.getenv("REPORT_DIR", "reports")
    )

    try:
        logging.info("Processing started")

        # Step 1: Read CSV or JSON
        if input_file.suffix.lower() == ".csv":
            records = read_csv(input_file)

        elif input_file.suffix.lower() == ".json":
            records = read_json(input_file)

        else:
            raise ValueError("Only CSV and JSON files are supported.")

        print("Total records loaded:", len(records))
        logging.info("Loaded %s records", len(records))

        # Step 2: Validate and clean records
        valid_records, invalid_records = clean_records(records)

        # Step 3: Generate reports
        save_clean_data(
            valid_records,
            output_dir / "cleaned_data.csv"
        )

        save_exception_report(
            invalid_records,
            report_dir / "exception_report.csv"
        )

        save_summary(
            len(records),
            len(valid_records),
            len(invalid_records),
            report_dir / "summary.json"
        )

        # Step 4: Display results
        print("\nProcessing completed!")
        print("---------------------")
        print("Total records:", len(records))
        print("Valid records:", len(valid_records))
        print("Invalid records:", len(invalid_records))

        logging.info("Processing completed successfully")

    except (FileNotFoundError, ValueError, OSError) as error:
        logging.exception("Processing failed")
        print("ERROR:", error)

    except Exception:
        logging.exception("Unexpected error occurred")
        print("An unexpected error occurred. Check the log file.")


if __name__ == "__main__":
    main()
