import json

def log_finding(finding_type, data, impact="medium"):
    report_entry = {
        "type": finding_type,
        "impact": impact,
        "data": data
    }
    with open("fuzz_report.json", "a") as report_file:
        json.dump(report_entry, report_file, indent=4)
        report_file.write(",\n")
