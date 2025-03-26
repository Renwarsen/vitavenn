import datetime

def log_error(message: str, origin: str = "unknown"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ({origin}) {message}\n"
    
    with open("error.log", "a") as log_file:
        log_file.write(log_entry)
    
    print(log_entry.strip())
