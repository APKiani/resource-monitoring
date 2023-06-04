# this code is operable in terminal
import psutil
import time
import GPUtil


# note that this part of the code should be operated in terminal!
gpus = GPUtil.getGPUs()
for gpu in gpus:
    gpu_load = f"{gpu.load * 100}%"
    print(f"gpu usage : {gpu_load}")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")


def display_usage(cpu_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '$' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    # Apologizes for the dollar sign I don't have numpad for putting a rectangular!!
    print(f"\rCPU usage: |{cpu_bar}|{cpu_usage:.2f}% ", end="")


while True:
    display_usage(psutil.cpu_percent(), 30)
    time.sleep(0.5)  # you can change the periods


