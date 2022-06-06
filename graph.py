import matplotlib.pyplot as plt
from Code import Ear_Values, Mar_Values,Time_value
# ,start_time,end_time
import cv2
# class detect(object):
# # total_time=end_time-start_time
#     # def __init__(self):
#     #     self.video = cv2.VideoCapture(0)
#     def get_frame(self):
#         ret,frame = self.video.read()
#         ret, jpeg = cv2.imencode('.jpg',frame)
#         return jpeg.tobytes()


print(len(Ear_Values))
print(len(Mar_Values))
print(len(Time_value))
# print(total_time)
print(Time_value)

# print(Ear_Values)
plt.plot(Time_value, Ear_Values,label="EAR Values")
plt.xlabel('Time')
plt.ylabel('MAR & EAR')
plt.title("E.A.R. & M.A.R. ratios with respect to time")
plt.plot(Time_value, Mar_Values, label="MAR Values")
plt.legend()
plt.show()
