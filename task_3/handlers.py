from pathlib import Path
from constants import log_types
from helpers import check_if_line_is_valid, filter_logs_by_level

# Parses a single log line into a dictionary containing the date, time, log type, and message.
# Includes exception handling to verify that all required log components are present.
def parse_log_line(line: str) -> dict:
    try:
        date, time, log_type, *message_array = line.split(" ")
        dict_log = {
            "date": date,
            "time": time,
            "type": log_type,
            "message": " ".join(message_array).strip()
        }
        return dict_log

    except ValueError:
        print("Log line is not valid")

# Loads and parses log entries from a specified file path.  
# Validates each line before parsing and returns a list of log dictionaries.  
def load_logs(file_path: str) -> list:
    try:
        absolute_path_to_file = Path(file_path).resolve()
        with open(absolute_path_to_file, 'r', encoding='utf-8') as file:
            logs = [parse_log_line(line) for line in file if check_if_line_is_valid(line)]
            return logs

    except FileNotFoundError:
        print("Please, check if logs.txt file exists and run the script from task_3 folder")  

# Counts the number of log entries for each log level.  
# @returns a dictionary with counts per level.
def count_logs_by_level(logs: list) -> dict:
    logs_count = {}
    for log_type in log_types:
        filtered_logs_list = filter_logs_by_level(logs, log_type)
        logs_count[log_type] = len(filtered_logs_list)

    return logs_count

# Displays a formatted table showing the count of log entries for each log level.
def display_log_counts(counts: dict):
    log_counts_message = f"""
Рівень логування | Кількість
-----------------|----------
"""
    for log_type, count in counts.items():
        log_counts_message += f"{log_type:<17}| {count}\n"

    print(log_counts_message)

# Displays detailed log entries for a specific log level.
def display_logs_per_type(logs: list, log_type: str):
    filtered_logs_list = filter_logs_by_level(logs, log_type)
    filtered_logs_message = f"Деталі логів для рівня {log_type}:\n"

    for log in filtered_logs_list:
        filtered_logs_message += f"{log['date']} {log['time']} - {log['message']}\n"

    print(filtered_logs_message)