from typing import Callable, Any
from functools import wraps
import time
roles_perms = {"FOM":1,"DOF":1,"FM":0}

def check_role_perms(func:Callable) -> Callable:
    @wraps(func)
    def validate_role(*args,**kwargs) -> bool:
        if not roles_perms.get(*args, False):
            raise PermissionError
        result : Any = func(*args,**kwargs)
    return validate_role

@check_role_perms
def main(a):
    print("Executing......")
    time.sleep(2)

if __name__ == "__main__":
    main("FOM")
