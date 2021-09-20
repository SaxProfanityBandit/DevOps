#imports
import psutil

#class definition

class CPUSnapshot(object):
	def __init__(self):
		self.cpu_usage = psutil.cpu_percent()
		self.memory_usage = psutil.virtual_memory().used / 1024
		self.disk_usage = psutil.disk_usage('/').used / 1024
	def __repr__(self):
		return "CPU Usage: {}% of 100%.\nMemory Used: {} MBs\nDisk Usage: {} MBs".format(self.cpu_usage, self.memory_usage, self.disk_usage)


snapshot = CPUSnapshot()
print(snapshot)

