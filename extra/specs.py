import wmi
from datetime import datetime

class Specs():
    def __init__(self):
        self.wmi = wmi.WMI()
        

    def bytes_converter(self, size):
        for i in ("B", "KB", "MB", "GB", "TB"):
            if not size and size < 1024:
                return f"{size:.2f} {i}" if isinstance(size, (int, float)) else "Unknown"
            size /= 1024

        return f"(n:.2f) PB"

    

    def device_os(self):
        try:
            p = self.wmi.Win32_OperatingSystem()[0]
            return f"OS: "+ getattr(p, "Caption", "Unknown") + "-" + getattr(p, "Version", "")
        except Exception as e:
            return "OS : Unknown"
        
    def device_system(self):
        try:
            p = self.wmi.Win32_ComputerSystem()[0]
            return "System:"+ getattr(p, "Manufacturer", "Unknown") + "/" + getattr(p, "Model", "Unknown")
        except Exception as e:
            return "System: Unknown"
        
    def device_cpu(self):
        try:
            p = self.wmi.Win32_Processor()
            for i, cpu in enumerate(p, start=1):
                name = getattr(cpu, "Name", "Unknown")
                cores = getattr(cpu, "NumberOfCores", "?")
                threads = getattr(cpu, "NumberOfLogicalProcessors", "?")
                speed = getattr(cpu, "MaxClockSpeed", "?")
                return f"CPU {i}: {name} — {cores} cores / {threads} threads @ {speed} MHz"
        except Exception as e:
            return "CPU: Unknown"
        
    def device_gpu(self):
        try:
            p = self.wmi.Win32_VideoController()
            if not p:
                return "GPU: Not found"
            else:
                for idx, g in enumerate(p, start=1):
                    name = getattr(g, "Name", "Unknown")
                    ram = getattr(g, "AdapterRAM", None)
                    if ram:
                        try:
                            ram = self.bytes_converter(int(ram))
                        except Exception:
                            ram = str(ram)
                    else:
                        ram = "Unknown"
                    return f"GPU {idx}: {name} — {ram}"
        except Exception as e:
            return "GPU: Unknown"
        
if __name__ == "__main__":
    a = Specs()
    print(a.device_os())