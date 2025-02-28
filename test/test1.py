import os



# Choose gpu
import os
import time

os.environ["CUDA_VISIBLE_DEVICES"] = "5"


print("curren pid:", os.getpid())

import runpy
# os.system("python ../deep_learning/inspect_env.py --proc_title=我的GPU进程")
runpy.run_path("../deep_learning/inspect_env.py")

time.sleep(300)

