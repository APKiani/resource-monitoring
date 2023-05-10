import time
import psutil
import platform

# processor type and number of cores
print(f"processor type : {platform.processor()}")
print(f"number of physical cores: {psutil.cpu_count(logical=False)}")
print(f"number of logical cores: {psutil.cpu_count(logical=True)}")
# processor current frequency
print(f"current cpu frequency : {psutil.cpu_freq().current}")


# note that this part of the code should be operated in terminal!
def display_usage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '$' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = '$' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    # Apologizes for the dollar sign I don't have numpad for putting a rectangular!!
    print(f"\rCPU usage: |{cpu_bar}|{cpu_usage:.2f}% ", end="")
    print(f"MEM usage: |{mem_bar}|{mem_usage:.2f}% ", end="\r")


while True:
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent, 30)
    time.sleep(0.5)  # you can change the periods
