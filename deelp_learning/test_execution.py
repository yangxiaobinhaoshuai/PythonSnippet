import time
from turtledemo.penrose import start


print("Test execution.")

start_timestamp = time.time()
time.sleep(0.060)
end_timestamp = time.time()


from deelp_learning.common_function import format_time_diff
# 调用函数
hours, minutes, seconds, milliseconds = format_time_diff(start_timestamp, end_timestamp)

# 打印结果
print(f"时间差: {hours}小时 {minutes}分钟 {seconds}秒 {milliseconds}毫秒")

