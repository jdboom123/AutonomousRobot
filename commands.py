from picarx import Picarx
import time
import readchar
from picarx.stt import Vosk

SPIN_TIME = 5.75
TILT_ANGLE = -5

def main():
	try:
		px = Picarx()
		stt = Vosk(language="en-us")
		
		while True:
			# key = readchar.readkey()
			# key = key.lower()   
			tilt_angle = 0          
			
			res = stt.listen(stream=False)
			text = res.get("text", "") if isinstance(res, dict) else str(res)
			text = text.lower().strip()
			words = text.split(" ")
			if not text:
				continue
			
			print("Heard:", text)

			
			#if key == 'p':
			if 'spin' in words:
				px.set_dir_servo_angle(50)
				px.forward(85)
				time.sleep(SPIN_TIME)
				px.forward(0)
				px.set_dir_servo_angle(0)
				
			elif 'good' in words:
				good_position = text.index('good')
				if good_position+1 < len(words) and words[good_position+1] == 'boy':
					for i in range(5):
						px.set_cam_tilt_angle(TILT_ANGLE)
						time.sleep(0.3)
						px.set_cam_tilt_angle(-1*TILT_ANGLE)
						time.sleep(0.3)
				px.set_cam_tilt_angle(0)
	finally:
		px.set_cam_tilt_angle(0)
		px.set_cam_pan_angle(0)  
		px.set_dir_servo_angle(0)  
		px.stop()
		time.sleep(.2)
	


if __name__ == "__main__":
    main()
