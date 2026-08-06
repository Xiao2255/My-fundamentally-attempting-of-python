from datetime import datetime

def log_operation(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f'{start_time.strftime("%Y-%m-%d %H:%M:%S")}执行了以下操作')
        result = func(*args, **kwargs)
        return result
    return wrapper

