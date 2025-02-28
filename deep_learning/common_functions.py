


def get_current_process_gpu():
    import os
    import subprocess
    pid = os.getpid()  # 获取当前进程ID

    # 获取进程和GPU UUID的关联
    try:
        result = subprocess.check_output(['nvidia-smi', '--query-compute-apps=pid,gpu_uuid', '--format=csv,noheader'])
    except subprocess.CalledProcessError:
        return f"无法获取PID {pid}的GPU信息"

    target_gpu_uuid = None

    # 寻找当前PID使用的GPU UUID
    for line in result.decode('utf-8').strip().split('\n'):
        if line:
            parts = [part.strip() for part in line.split(',')]
            if len(parts) >= 2 and parts[0] == str(pid):
                target_gpu_uuid = parts[1]
                break

    if not target_gpu_uuid:
        return f"找不到PID {pid}关联的GPU"

    # 获取所有GPU的信息（索引和UUID）
    try:
        gpu_info = subprocess.check_output(['nvidia-smi', '--query-gpu=index,uuid,name,memory.used', '--format=csv,noheader'])
    except subprocess.CalledProcessError:
        return f"找到GPU UUID {target_gpu_uuid}，但无法获取详细信息"

    # 根据UUID找到对应的索引号和名称
    for line in gpu_info.decode('utf-8').strip().split('\n'):
        if line:
            parts = [part.strip() for part in line.split(',')]
            if len(parts) >= 2 and parts[1] == target_gpu_uuid:
                return f"PID {pid} 正在使用物理GPU {parts[0]}: {parts[2]}, 内存使用: {parts[3] if len(parts) > 3 else '未知'}"

    return f"找到UUID {target_gpu_uuid}，但无法在GPU列表中匹配"


def format_now(format_str: str = "%Y-%m-%d_%H:%M:%S"):
    import datetime
    # 获取当前时间
    current_time = datetime.datetime.now()

    # 格式化当前时间
    formatted_time = current_time.strftime(format_str)

    # 打印格式化后的时间
    # print(formatted_time)
    return formatted_time


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
    print(f"check_package_import: {package_name}")
    try:
        import importlib
        importlib.import_module(package_name)
        return True
    except ImportError as e:
        print(f"Import {package_name} failed: {e}")
        return False


def setMyProcTitle(title):
    if check_package_import("setproctitle"):
        # 设置进程名
        # 使用 # noinspection 来禁用单行警告
        # noinspection PyUnresolvedReferences
        from setproctitle import setproctitle
        setproctitle(title)
        import os
        pid = os.getpid()
        print(f"Current process pid: {pid}")
        # 读取 /proc/{pid}/comm 文件获取进程名称
        with open(f'/proc/{pid}/comm', 'r') as f:
             process_name = f.read().strip()
        print(f"Current process name: {process_name}")
        print("Set proc title:", title)
    else:
        print(f"There is no setproctitle, setproctitle {title} failed.")