from picarx import Picarx
import time
import readchar
from picarx.stt import Vosk

SPIN_TIME = 5.75

def main():
	try:
		px = Picarx()
		stt = Vosk(language="en-us")
		
		while True:
			# key = readchar.readkey()
			# key = key.lower()             
			
			res = stt.listen(stream=False)
			text = res.get("text", "") if isinstance(res, dict) else str(res)
			text = text.lower().strip()
			if not text:
				continue
			
			print("Heard:", text)

			
			#if key == 'p':
			if 'spin' in text:
				px.set_dir_servo_angle(50)
				px.forward(80)
				time.sleep(SPIN_TIME)
				px.forward(0)
				px.set_dir_servo_angle(0)
			
	
	finally:
		px.set_cam_tilt_angle(0)
		px.set_cam_pan_angle(0)  
		px.set_dir_servo_angle(0)  
		px.stop()
		time.sleep(.2)
	


if __name__ == "__main__":
    main()