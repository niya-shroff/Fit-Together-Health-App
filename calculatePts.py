import math
#function is called every hour
#function takes in steps, amount of time in an hour that BPM is over 130 and calculates points for one person in that hour

def calc_pts(steps: int, exercise_time: int):
    step_pts = math.floor(steps / 100)
    exercise_pts = math.floor(exercise_time / 10) * 20
    return step_pts + exercise_pts

print(calc_pts(150, 20))