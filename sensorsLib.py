
import time
import threading
import Queue

class sensors(threading.Thread):

	def __init__(self):
		self.queue = Queue.Queue()
		self.gpio = 44
		self.stopsign = None
		threading.Thread.__init__(self)
		self.tm = 0.1

	def run(self):
		#checking cycle
		while True:	
			try:
				if self.stopsign == 'stopScanning':
					print 'stop of checking cycle'
					break
				checkValue = open('/sys/class/gpio/gpio%s%s' %(self.gpio, '/value'), 'r')
				if int(checkValue.read()) == 1:
					self.queue.put(time.time())
				checkValue.close()
				time.sleep(self.tm)
			except IOError:
				export = open('/sys/class/gpio/export', 'w') 	
				export.write(str(self.gpio))
				export.close()
				print 'export of gpio%s is performed' %(self.gpio)

	# Returns a queue object 
	def get_queue(self):
		return self.queue.get()

	def stop (self):
		self.stopsign = 'stopScanning'
		export = open('/sys/class/gpio/unexport', 'w') 	
		export.write(str(self.gpio))
		export.close()
		print 'unexport of gpio%s is performed' %(self.gpio)
	
	def setTime(self, tm = 0.1):
		self.tm = tm





		





























