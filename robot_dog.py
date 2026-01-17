from picarx import Picarx
import time
import readchar
from picarx.stt import Vosk
import threading

SPIN_TIME = 5.75
TILT_ANGLE = -5

def command_handler():
	stt = Vosk(language="en-us")
	
	while True:	
		res = stt.listen(stream=False)
		text = res.get("text", "") if isinstance(res, dict) else str(res)
		text = text.lower().strip()
		words = text.split(" ")
		if not text:
			continue	
		print("Heard:", text)
	
def main():
	try:
		px = Picarx()
		
		com_hand = threading.Thread(target = command_handler)
		com_hand.start()
		
		counter = 0
		while True:
			print("Awaiting command for " + str(counter) + " secs")
			time.sleep(1)
			counter += 1
		
		

	finally:
		px.set_cam_tilt_angle(0)
		px.set_cam_pan_angle(0)  
		px.set_dir_servo_angle(0)  
		px.stop()
		time.sleep(.2)
		


if __name__ == "__main__":
    main()
