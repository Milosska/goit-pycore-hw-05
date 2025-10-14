from helpers import check_if_line_is_valid, filter_logs_by_level

# Tests for check_if_line_is_valid function
assert check_if_line_is_valid("INFO System started") == True
assert check_if_line_is_valid("2024-01-22 09:00:45 ERROR Database connection failed.") == True
assert check_if_line_is_valid("2024-01-22 09:00:45 Database connection failed") == False

# Tests for filter_logs_by_level function
sample_logs = [
    {"date": "2025-10-14", "time": "10:00", "type": "INFO", "message": "System started"},
    {"date": "2025-10-14", "time": "10:05", "type": "ERROR", "message": "Failed to load config"},
    {"date": "2025-10-14", "time": "10:10", "type": "WARNING", "message": "Low disk space"},
]

assert filter_logs_by_level(sample_logs, "INFO") == [
    {"date": "2025-10-14", "time": "10:00", "type": "INFO", "message": "System started"}
]
assert filter_logs_by_level(sample_logs, "ERROR") == [
    {"date": "2025-10-14", "time": "10:05", "type": "ERROR", "message": "Failed to load config"}
]
assert filter_logs_by_level(sample_logs, "WARNING") == [
    {"date": "2025-10-14", "time": "10:10", "type": "WARNING", "message": "Low disk space"}
]
assert filter_logs_by_level(sample_logs, "DEBUG") == []