
# Business Data Automation Toolkit

## 1. Project Overview

The Business Data Automation Toolkit is a Python-based application designed to automate the process of reading, validating, cleaning, and reporting business data.

It processes property records from CSV and JSON files, identifies invalid or duplicate records, saves valid records separately, and generates exception and summary reports.

## 2. Project Objectives

- Automate business data processing.
- Validate required fields and data formats.
- Identify missing and invalid values.
- Detect duplicate property IDs.
- Separate valid and invalid records.
- Generate processing reports.
- Maintain application logs.

## 3. Features

- CSV and JSON input support.
- Required field validation.
- Price and property size validation.
- Property status validation.
- Duplicate record detection.
- Automatic data cleaning.
- Exception report generation.
- JSON summary report.
- Logging and exception handling.
- Environment-based configuration.
- Automated testing using pytest.

## 4. Technologies Used

- Python
- CSV and JSON modules
- pathlib
- logging
- os (environment variables)
- pytest (automated testing)

## Business_Data_Automation_Toolkit/

|
|-- data/
|   |-- input/
|   |   |-- properties.csv
|   |   |-- properties.json
|   |
|   |-- output/
|
|-- logs/
|-- reports/
|
|-- src/
|   |-- __init__.py
|   |-- main.py
|   |-- reader.py
|   |-- validator.py
|   |-- cleaner.py
|   |-- reporter.py
|
|-- tests/
|   |-- __init__.py
|   |-- test_main.py
|   |-- test_reader.py
|   |-- test_validator.py
|   |-- test_cleaner.py
|   |-- test_reporter.py
|
|-- .venv/
|-- .gitignore
|-- requirements.txt
|-- README.md

## 6. Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 7. Running the Application

Run the application from the project root directory:

```bash
python -m src.main
```

By default, the application reads:

`data/input/properties.csv`

## 8. Configuration

The application supports environment variables:

| Variable | Default |
|---|---|
| INPUT_FILE | data/input/properties.csv |
| OUTPUT_DIR | data/output |
| REPORT_DIR | reports |
| LOG_FILE | logs/processing.log |

Example in PowerShell:

```powershell
$env:INPUT_FILE="data/input/properties.json"
$env:OUTPUT_DIR="custom_output"
$env:REPORT_DIR="custom_reports"
$env:LOG_FILE="logs/processing.log"

python -m src.main
```

## 9. Generated Outputs

The application generates:

- `cleaned_data.csv` — validated property records.
- `exception_report.csv` — invalid records with their errors.
- `summary.json` — total, valid, and invalid record counts.
- `processing.log` — application processing logs.

## 10. Running Automated Tests

Run all tests using:

```bash
python -m pytest -v
```

The project currently contains 20 automated tests, including an integration test for the complete CSV workflow.

## 11. Data Validation Rules

- Required fields must not be empty.
- Property prices must be numeric and non-negative.
- Property sizes must be numeric and greater than zero.
- Property status must be Available or Sold.
- Duplicate property IDs are flagged as invalid.

Invalid records are preserved in the exception report for review instead of being silently discarded.

## 12. Limitations and Future Improvements

- Currently uses a property-record sample dataset.
- Validation rules are designed around the defined property data structure.
- Reports are generated in CSV and JSON formats.
- Future improvements may include additional input formats, configurable validation rules, and a graphical user interface.

## 13. Responsible Data Handling

The toolkit uses sample property data for demonstration. Invalid records are retained in exception reports to support human review and data integrity.
