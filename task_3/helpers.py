from constants import log_types

# Checks if a log line is valid and contains a recognized log type.
# If the file has lines with invalid info, those lines will be skipped.
def check_if_line_is_valid(line: str) -> bool:
    return line.strip() and any(log_type in line for log_type in log_types)

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['type'] == level, logs))