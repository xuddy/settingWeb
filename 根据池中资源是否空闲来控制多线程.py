# 根据池中资源是否空闲来控制多线程
import threading
import time
import random

ip_pool_dict = {
    "192.168.1.2": True,
    "192.168.1.3": True
}

def func_use_ip(ip: str):
    ip_pool_dict[ip] = False  # 将资源池中该ip的状态设置为：忙
    time.sleep(random.randint(1, 3))  # 使用ip
    ip_pool_dict[ip] = True  # ip使用完成，将资源池中该ip的状态设置为：闲


if __name__ == '__main__':
    i = 1
    while i <= 10000:
        ip_now = ""
        for ip, status in ip_pool_dict.items():
            if status:
                ip_now = ip
                break
        if ip_now:
            threading.Thread(target=func_use_ip, args=(ip_now,)).start()
            print(f"第{i}个任务，正在使用 {ip_now}\n")
            print("当前ip的机器状态是：%s。" % ("闲" if ip_pool_dict[ip_now] else "忙"))
            i += 1
        else:
            time.sleep(2)
