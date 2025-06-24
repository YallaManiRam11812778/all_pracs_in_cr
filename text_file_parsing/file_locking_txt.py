import datetime
import time
from multiprocessing import Pool
import pandas as pd
start = time.time()
from functools import wraps

def ezy_fetch_d140(return_period:str) -> list[dict]:
    if not isinstance(return_period,str) or len(str(return_period))!=6:
        return "Pass valid return Period"
    """Takes return_period as parameter and returns data of D140 based on the return_period mentioned in list of dicts as the output."""
    try:
        file = f"/home/caratred/ezygst_bench/sites/rgst.com/private/files/d140/HRCHANDIGARH/{return_period}.txt"
        f = open(file, "r")
        jungliee = f.read().split("\n")

        jungliee = list(filter(None,jungliee))

        tuples = zip(jungliee)

        with Pool() as pool:
            result = pool.starmap(eval, tuples)

        end = time.time() - start
        print(f"Time taken for fetching data of D140 File on return_period : {return_period} is --- ",end)
        return result
        """new_list = list(map(lambda x : eval(x), filter(None,jungliee)))
        end = time.time() - start"""
    except Exception as e:
        return 
        
a = ezy_fetch_d140("062023")
        
# pddf = pd.DataFrame.from_records(result)