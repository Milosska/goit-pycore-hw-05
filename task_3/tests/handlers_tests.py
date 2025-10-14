from handlers import parse_log_line, load_logs, count_logs_by_level

# Tests for parse_log_line function
assert parse_log_line("2025-10-14 10:00 INFO System started") == {
    "date": "2025-10-14",
    "time": "10:00",
    "type": "INFO",
    "message": "System started"
}
assert parse_log_line("2025-10-14 10:10") is None  # missing log type and message

# Tests for load_logs function
assert load_logs("non_existent_file.txt") is None  # file does not exist
assert load_logs("../README.md") == [] # file does not have valid log entries

# Tests for count_logs_by_level function
sample_logs = [
    {"date": "2025-10-14", "time": "10:00", "type": "INFO", "message": "System started"},
    {"date": "2025-10-14", "time": "10:05", "type": "ERROR", "message": "Failed to load config"},
    {"date": "2025-10-14", "time": "10:10", "type": "WARNING", "message": "Low disk space"},
]

assert count_logs_by_level(sample_logs) == { "INFO": 1, "ERROR": 1, "WARNING": 1, "DEBUG": 0 }