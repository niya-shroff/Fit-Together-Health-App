import math
#function is called every hour
#function takes in steps, amount of time in an hour that BPM is over 130 and calculates points for one person in that hour

def calc_pts(person):
    step_pts = math.floor(person.steps / 100)
    exercise_pts = math.floor(person.exercise_time / 10) * 20
    person.points += step_pts + exercise_pts

#takes in a group of people and calculates their total points
def calc_group_pts(group):
    group_pts = group.curr_group_points
    friends_arr = group.friends
    for friend in friends_arr:
        group_pts += friend.pts
