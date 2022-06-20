import config
from connection import *
# import vision_getandsaveimage as vg
# import find_ball as fb
import kick_ball
import time
names = list()
times = list()
keys = list()

names.append("HeadYaw")
times.append([ 2.40000])
keys.append([ -0.00158])

names.append("HeadPitch")
times.append([ 2.40000])
keys.append([ 0.51487])

motion.angleInterpolation(names, keys, times, True);
# print "Kick Left"
kick_ball.kick_left()  

# print "Kick Right"
# kick_ball.kick_right()

# adjust = fb.findball()
# print adjust[0]
# print adjust[1]
# if (adjust[1]==1):
#     kick_ball.adjust_front()
#     print "Moving Front to adjust"
# if (adjust[0]==5):
#     kick_ball.adjust_right()
#     kick_ball.kick_right()      
# elif (adjust[0]==4):
#     kick_ball.adjust_left()
#     kick_ball.kick_left()      
# elif (adjust[0]==3):
# 	kick_ball.kick_right()
# elif (adjust[0]==2):
# 	kick_ball.kick_left()
# elif (adjust[0]==1):
# 	kick_ball.adjust_left()
# 	kick_ball.kick_right()
# elif (adjust[0]==0):
# 	kick_ball.adjust_right()
# 	kick_ball.kick_left()
time.sleep(5)
config.PoseInit(motion)
	
	

		
		











