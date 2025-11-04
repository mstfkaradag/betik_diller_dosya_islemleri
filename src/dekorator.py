from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t0= time.perf_counter() # 0.andaki time
        result=func(*args,**kwargs)
        total_time=time.perf_counter()-t0
        print("total_time: ", total_time)
        return result
    return wrapper


def required_column(requireds: set[str]):
    def deco(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            result = func(*args, **kwargs)
            if not result:
                raise ValueError("Boş veri seti")
            
            if isinstance(result, list) and len(result) > 0:
                keys= set(result[0].keys())
                missing=requireds-keys
                if missing:
                    raise ValueError(f"Eksik kolon: {missing}")
            return result
        return wrapper
    return deco
        
                


