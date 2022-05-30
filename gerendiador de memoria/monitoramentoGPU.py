import GPUtil

class Monitor():
    def getGPUStats():
            GPUs = GPUtil.getGPUs()
            gpu = GPUs[0]
            return (f" Nome da GPU: {gpu.name}\n Total de memoria: {gpu.memoryTotal}\n Memoria livre: {gpu.memoryFree}\n Memoria utilizada: {gpu.memoryUsed}\n Total de uso da GPU: {gpu.memoryUtil:.2f} %")
