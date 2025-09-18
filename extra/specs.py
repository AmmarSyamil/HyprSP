# specs_plus.py
import wmi
import datetime
from typing import Dict, Any, List, Tuple

class Specs:
    def __init__(self):
        self.wmi = wmi.WMI()

    def bytes_converter(self, size_bytes) -> str:

        try:
            n = int(size_bytes)
        except Exception:
            return "Unknown"
        if n < 0:
            return "Unknown"
        for unit in ("B", "KB", "MB", "GB", "TB", "PB"):
            if n < 1024 or unit == "PB":
                return f"{n:.2f} {unit}"
            n /= 1024.0
        return f"{n:.2f} PB"

    def safe_get(self, obj, attr, default="Unknown"):
        try:
            return getattr(obj, attr, default)
        except Exception:
            return default

    def device_os(self) -> str:
        try:
            p = self.wmi.Win32_OperatingSystem()[0]
            name = self.safe_get(p, "Caption", "Unknown")
            ver = self.safe_get(p, "Version", "")
            arch = self.safe_get(p, "OSArchitecture", "")
            return f"{name} {ver} ({arch})".strip()
        except Exception:
            return "Unknown"

    def device_system(self) -> str:
        try:
            p = self.wmi.Win32_ComputerSystem()[0]
            man = self.safe_get(p, "Manufacturer", "Unknown")
            model = self.safe_get(p, "Model", "Unknown")
            return f"{man} / {model}"
        except Exception:
            return "Unknown"

    def device_cpu(self) -> List[str]:
        out = []
        try:
            cpus = self.wmi.Win32_Processor()
            for i, cpu in enumerate(cpus, start=1):
                name = self.safe_get(cpu, "Name", "Unknown")
                cores = self.safe_get(cpu, "NumberOfCores", "?")
                threads = self.safe_get(cpu, "NumberOfLogicalProcessors", "?")
                speed = self.safe_get(cpu, "MaxClockSpeed", "?")
                out.append(f"CPU {i}: {name} - {cores} cores / {threads} threads @ {speed} MHz")
        except Exception:
            out.append("Unknown")
        return out

    def device_gpu(self) -> List[str]:
        out = []
        try:
            gpus = self.wmi.Win32_VideoController()
            if not gpus:
                return ["Not found"]
            for i, g in enumerate(gpus, start=1):
                name = self.safe_get(g, "Name", "Unknown")
                ram = self.safe_get(g, "AdapterRAM", None)
                if ram not in (None, "None"):
                    try:
                        ram = self.bytes_converter(int(ram))
                    except Exception:
                        ram = str(ram)
                else:
                    ram = "Unknown"
                out.append(f"GPU {i}: {name} - {ram}")
        except Exception:
            out.append("Unknown")
        return out

    def total_ram(self) -> str:
        try:
            osinfo = self.wmi.Win32_OperatingSystem()[0]
            kb = int(self.safe_get(osinfo, "TotalVisibleMemorySize", 0))
            return self.bytes_converter(kb * 1024)
        except Exception:
            return "Unknown"

    def disk_info(self) -> List[str]:
        out = []
        try:
            for d in self.wmi.Win32_LogicalDisk(DriveType=3):  # 3 = local disk
                name = self.safe_get(d, "DeviceID", "Unknown")
                fs = self.safe_get(d, "FileSystem", "Unknown")
                total = self.safe_get(d, "Size", None)
                free = self.safe_get(d, "FreeSpace", None)
                out.append(
                    f"{name} ({fs}) - total: {self.bytes_converter(total)}, free: {self.bytes_converter(free)}"
                )
        except Exception:
            out.append("Unknown")
        return out

    def uptime(self) -> str:
        try:
            osinfo = self.wmi.Win32_OperatingSystem()[0]
            last = self.safe_get(osinfo, "LastBootUpTime", None)
            if not last:
                return "Unknown"
            try:
                tz = None
                if "+" in last or "-" in last[14:]:
                    core = last.split(".")[0]
                    dt = datetime.datetime.strptime(core, "%Y%m%d%H%M%S")
                else:
                    core = last.split(".")[0]
                    dt = datetime.datetime.strptime(core, "%Y%m%d%H%M%S")
            except Exception:
                return str(last)
            now = datetime.datetime.now()
            delta = now - dt
            days = delta.days
            hours, rem = divmod(delta.seconds, 3600)
            minutes, seconds = divmod(rem, 60)
            return f"Last boot: {dt.strftime('%Y-%m-%d %H:%M:%S')} ({days}d {hours}h {minutes}m ago)"
        except Exception:
            return "Unknown"

    def as_dict(self) -> Dict[str, Any]:
        return {
            "os": self.device_os(),
            "system": self.device_system(),
            "cpu": self.device_cpu(),
            "gpu": self.device_gpu(),
            "total_ram": self.total_ram(),
            "disks": self.disk_info(),
            "uptime": self.uptime(),
        }

    def to_plain_text(self) -> str:
        d = self.as_dict()
        lines = []
        lines.append(f"OS: {d['os']}")
        lines.append(f"System: {d['system']}")
        lines.extend(d["cpu"])
        lines.extend(d["gpu"])
        lines.extend(d["disks"])
        lines.append(f"Uptime: {d['uptime']}")
        return "\n".join(lines)

    def to_html(self) -> str:
        """Return a small HTML fragment with colored labels for nicer QLabel/QTextEdit rendering"""
        d = self.as_dict()
        label_style = "color:#8b9dbf;font-weight:600"
        value_style = "color:#e6eef8;font-weight:500"
        html_lines = []
        html_lines.append(f'<div style="font-family:Segoe UI, Arial, sans-serif; font-size:12pt">')
        html_lines.append(f'<div><span style="{label_style}">OS:</span> <span style="{value_style}">{d["os"]}</span></div>')
        html_lines.append(f'<div><span style="{label_style}">System:</span> <span style="{value_style}">{d["system"]}</span></div>')
        for cpu_line in d["cpu"]:
            html_lines.append(f'<div><span style="{label_style}">CPU:</span> <span style="{value_style}">{cpu_line}</span></div>')
        for gpu_line in d["gpu"]:
            html_lines.append(f'<div><span style="{label_style}">GPU:</span> <span style="{value_style}">{gpu_line}</span></div>')
        # html_lines.append(f'<div><span style="{label_style}">RAM:</span> <span style="{value_style}">{d["total_ram"]} (free {d["free_ram"]})</span></div>')
        for disk in d["disks"]:
            html_lines.append(f'<div><span style="{label_style}">Disk:</span> <span style="{value_style}">{disk}</span></div>')
        html_lines.append(f'<div><span style="{label_style}">Uptime:</span> <span style="{value_style}">{d["uptime"]}</span></div>')
        html_lines.append("</div>")
        return "\n".join(html_lines)

    def compare_with(self, other: "Specs") -> List[Tuple[str, Any, Any]]:
        """
        Compare this snapshot with another Specs instance.
        Returns list of tuples: (field_name, value_self, value_other)
        Only returns entries that differ.
        """
        a = self.as_dict()
        b = other.as_dict()
        diffs = []
        for key in a:
            if a[key] != b.get(key):
                diffs.append((key, a[key], b.get(key)))
        return diffs
