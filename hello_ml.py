import platform
import os


print("Hello, ML Worrld from Jenkins!")
print(f"Python Version:{platform.python_version()}")
print(f"Operating System :{platform.system()}{platform.release()}")
print(f"CPU Cores:{os.cpu_count()}")

