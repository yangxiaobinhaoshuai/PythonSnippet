import time
from turtledemo.penrose import start



# Choose gpu
import os
import time

os.environ["CUDA_VISIBLE_DEVICES"] = "5"


print("curren pid:", os.getpid())

import runpy
# os.system("python ../deep_learning/inspect_env.py --proc_title=我的GPU进程")
params= {"proc_title": "ggggg"}
runpy.run_path("inspect_env.py", run_name="__main__", init_globals=params)

time.sleep(300)