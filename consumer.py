from sensorsLib import sensors

sen = sensors()
sen.start()
print sen.get_queue()

sen.stop()

