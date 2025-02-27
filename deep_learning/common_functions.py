



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


def check_package_import(package_name) -> bool:
    import sys
    return package_name in sys.modules


def setMyProcTitle(title):
    if check_package_import("setproctitle"):
        # 设置进程名
        # 使用 # noinspection 来禁用单行警告
        # noinspection PyUnresolvedReferences
        from setproctitle import setproctitle
        setproctitle(title)
    else:
        print(f"There is no setproctitle, setproctitle {title} failed.")