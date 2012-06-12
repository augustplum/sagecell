from forking_kernel_manager import ForkingKernelManager

class UntrustedMultiKernelManager:
    def __init__(self):
        self.fkm = ForkingKernelManager()
        self._kernels = {}
    
    def start_kernel(self):
        x = self.fkm.start_kernel()
        self._kernels[x["kernel_id"]] = None #just need to track kernel_ids
        return x

    def kill_kernel(self, kernel_id):
        return self.fkm.kill_kernel(kernel_id)

    def interrupt_kernel(self, kernel_id):
        return self.fkm.interrupt_kernel(kernel_id)

    def restart_kernel(self, kernel_id, *args, **kwargs):
        return self.fkm.restart_kernel(kernel_id)
        

if __name__ == "__main__":
    x = UntrustedMultiKernelManager()
    y = x.start_kernel()
    print y
    from time import sleep 
    sleep(2)
    print x.restart_kernel(y["kernel_id"])
    sleep(2)
    x.kill_kernel(y["kernel_id"])
