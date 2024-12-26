


# 查看当前 pip packages 位置
import sysconfig

#  /root/miniconda3/envs/auto_homework/lib/python3.8/site-packages
# e.g. pip3 --target=/root/miniconda3/envs/auto_homework/lib/python3.8/site-packages install <some module>
print("where install python packages.")
print(sysconfig.get_paths()["purelib"])


# 设置进程名
from setproctitle import setproctitle
setproctitle("yxb_testing")



# 检查 GPU 可用性
import torch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")



# 计算时差
def format_time_diff(start_timestamp, end_timestamp):
    # 计算时间差（单位：秒）
    time_diff = end_timestamp - start_timestamp

    # 计算小时、分钟、秒和毫秒
    hours = int(time_diff // 3600)  # 小时
    minutes = int((time_diff % 3600) // 60)  # 分钟
    seconds = int(time_diff % 60)  # 秒
    milliseconds = int((time_diff - int(time_diff)) * 1000)  # 毫秒

    # 返回格式化的时间差
    return hours, minutes, seconds, milliseconds



