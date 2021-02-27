import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines

def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos + 2:]
		temp_c = float(temp_string) / 1000.0
		temp_f = temp_c * 9.0 / 5.0 + 32.00
		return temp_c, temp_f

while True:
	struct_time = time.localtime()
	timestamp = time.strftime("%d%H%M%S",struct_time)
	data_raw = open("data_raw.txt", "a")
	L = f'{timestamp} {read_temp()[0]} {read_temp()[1]} \n'
	data_raw.writelines(L)
	print(timestamp, read_temp()[0], read_temp()[1])
	data_raw.close()
	time.sleep(1)
