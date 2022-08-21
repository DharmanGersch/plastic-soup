from buildhat import Motor, Light
import time

motor_a = Motor('A')
light_b = Light('B')
#motor_a.run_for_seconds(4, speed=100)

#this is a loop
for i in range(10):
    #everything indented like this will repeat
    motor_a.run_for_degrees(90)
    light_b.on()
    time.sleep(1)
    light_b.off()
    print(motor_a.get_position())















