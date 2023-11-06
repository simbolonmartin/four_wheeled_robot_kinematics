import math

class Solution:
    def go(self, velocity, rotation_speed):
        WHEEL_RADIUS = 0.127
        ROBOT_RADIUS = 0.362 

        v_x = velocity * math.cos(math.pi/4)
        v_y = velocity * math.sin(math.pi/4)

        v_wheel_1 = v_y + ROBOT_RADIUS * rotation_speed
        v_wheel_2 = -v_x + ROBOT_RADIUS * rotation_speed
        v_wheel_3 = -v_y + ROBOT_RADIUS * rotation_speed
        v_wheel_4 = v_x + ROBOT_RADIUS * rotation_speed

        w_wheel_1_rpm = (v_wheel_1 * 30) / (math.pi * WHEEL_RADIUS)
        w_wheel_2_rpm = (v_wheel_2 * 30) / (math.pi * WHEEL_RADIUS)
        w_wheel_3_rpm = (v_wheel_3 * 30) / (math.pi * WHEEL_RADIUS)
        w_wheel_4_rpm = (v_wheel_4 * 30) / (math.pi * WHEEL_RADIUS)

        w_wheel =  [w_wheel_1_rpm, w_wheel_2_rpm, w_wheel_3_rpm, w_wheel_4_rpm]
        print(w_wheel)

sol = Solution()
sol.go(1, 0)