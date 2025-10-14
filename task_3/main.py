import sys
from constants import log_types
from handlers import load_logs, count_logs_by_level, display_log_counts, display_logs_per_type

# Loads a log file from command-line arguments, counts log levels, 
# and optionally displays logs of a specified type.
def main():
    try: 
        _, *system_arguments = sys.argv
        if not system_arguments:
            raise ValueError("No file path provided.")

        logs_list = load_logs(system_arguments[0])
        if not logs_list:
            raise ValueError("No valid log entries found in the file.")
        
        counted_logs = count_logs_by_level(logs_list)
        display_log_counts(counted_logs)

        if len(system_arguments) > 1:
            cmd = system_arguments[1].upper()
            if not cmd in log_types:
                raise ValueError(f"Log type '{cmd}' is not recognized. Valid types are: {', '.join(log_types)}") 
            
            display_logs_per_type(logs_list, cmd)
            
    except ValueError as e:
        print(e)
        return

if __name__ == "__main__":
    main()
