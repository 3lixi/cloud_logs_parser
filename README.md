# Cloud Logs Parser

A Python project that safely parses log files, handles invalid lines, and exports clean results to JSON.

## Features
- Parse single log lines into `(timestamp, level, service, message)` tuples.
- Process lists of log lines and skip invalid ones.
- Read log files line-by-line and show first valid entries.
- Count total, valid, and invalid lines.
- Export parsed logs to `parsed_logs.json`.

## Usage
1. Run Task 1 tests:  
```bash
python task1_parse_single.py
Parse a list of lines:

python task2_parse_list.py
Parse a log file:

python task3_parse_file.py
Count invalid lines:

python task4_report_invalids.py
Export parsed logs to JSON:

python task5_export_parsed_json.py
Output
parsed_logs.json contains all valid log lines in JSON format.
