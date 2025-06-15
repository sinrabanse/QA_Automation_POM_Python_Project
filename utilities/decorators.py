from utilities.logger import Logger
from functools import wraps

def log_step(method_name=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            name = method_name or func.__name__
            Logger.add_start_step(method=name)
            try:
                result = func(*args, **kwargs)
                driver = getattr(args[0], 'driver', None)
                current_url = driver.current_url if driver else "Unknown"
                Logger.add_end_step(url=current_url, method=name)
                return result
            except Exception as e:
                Logger.add_error(method=name, error=e)
                raise
        return wrapper
    return decorator
