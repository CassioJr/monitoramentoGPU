import psutil
import humanize
import os
import GPUtil as GPU
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np
import GPUtil as lpz
GPUs = GPU.getGPUs()
# XXX: only one GPU on Colab and isn’t guaranteed
gpu = GPUs[0]
def printm():
 process = psutil.Process(os.getpid())
 print("Gen RAM Free: " + humanize.naturalsize( psutil.virtual_memory().available ), " | Proc size: " + humanize.naturalsize( process.memory_info().rss))
 print("GPU RAM Free: {0:.0f}MB | Used: {1:.0f}MB | Util {2:3.0f}% | Total {3:.0f}MB".format(gpu.memoryFree, gpu.memoryUsed, gpu.memoryUtil*100, gpu.memoryTotal))
 lpz.showUtilization()
printm()


df_1 = psutil.virtual_memory()
df_2 = psutil.cpu_percent()
df_3 = psutil.cpu_count()
df_4 = psutil.cpu_count(logical=False)
df_5 = psutil.cpu_times()
df_6 = psutil.cpu_times_percent()
df_7 = psutil.cpu_stats()
df_8 = psutil.cpu_freq()
df_9 = psutil.cpu_count()
df_10 = psutil.cpu_stats()



plt.plot(df_1 ,color='red')
plt.plot(df_2,color='blue')
plt.plot(df_3,color='green')
plt.plot(df_4,color='yellow')
plt.plot(df_5,color='black')
plt.plot(df_6,color='orange')
plt.plot(df_7,color='purple')
plt.plot(df_8,color='pink')
plt.plot(df_9,color='brown')
plt.plot(df_10,color='grey')
plt.title('Controle de memória de vídeo')
plt.ylabel('GPU Memory Usage')
plt.xlabel('Time')
plt.show()

