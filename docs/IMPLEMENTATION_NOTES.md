# Implementation Notes
## Business Data Automation Toolkit

### 1. System Architecture

The project follows a modular architecture. Each Python module performs a specific responsibility.

- reader.py: Reads CSV and JSON input files.
- validator.py: Checks required fields, data formats, and duplicate property IDs.
- cleaner.py: Separates valid and invalid records.
- reporter.py: Generates cleaned data, exception reports, and summary reports.
- main.py: Coordinates the complete processing workflow.

### 2. Processing Workflow

1. Read the input file.
2. Identify its format (CSV or JSON).
3. Load property records.
4. Validate required fields and values.
5. Identify duplicate property IDs.
6. Separate valid and invalid records.
7. Convert valid numeric values into numeric types.
8. Save cleaned records.
9. Generate an exception report.
10. Generate a processing summary.
11. Record application activities in the log file.

### 3. Validation Rules

- Required fields must contain values.
- Price must be numeric and cannot be negative.
- Property size must be numeric and greater than zero.
- Status must be Available or Sold.
- Duplicate property IDs are flagged.

### 4. Technical Decisions

**Modular design:** Separate modules make the application easier to understand, test, and maintain.

**Python standard library:** CSV, JSON, pathlib, logging, and os are used for core functionality without additional runtime dependencies.

**Pytest:** Automated tests verify individual modules and the complete CSV and JSON workflows.

**Environment variables:** Input and output paths can be configured without changing source code.

### 5. Data Integrity

Invalid records are not silently deleted. They are preserved in an exception report with their validation errors.

Duplicate property IDs are flagged so that a human can review them.

The system does not automatically invent or replace missing property information.

### 6. Error Handling and Logging

The application handles common file and input errors and records processing information in a log file.

Unexpected errors are also logged for troubleshooting.

### 7. Current Limitations

- Validation rules are designed for the defined property dataset.
- Duplicate detection is based on property IDs.
- Output reports are CSV and JSON files.
- The application does not automatically correct invalid business values.

### 8. Future Improvements

- Add more configurable validation rules.
- Support additional business datasets.
- Introduce a graphical user interface.
- Add processing statistics and advanced reports.
