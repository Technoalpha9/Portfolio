import time, sys
try:
	while True:
		for i in range(1,9):
			print("_"*i*i)
			time.sleep(0.04)
		for i in range(9,1,-1):
			print("_"*i*i)
			time.sleep(0.02)
except KeyboardInterrupt:
    print("program ending!")
    sys.exit()
