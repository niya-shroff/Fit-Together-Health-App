class Person:
    name = ""
    steps = 0
    exercise_time = 0
    points = 0
    bpm = 0

    def __init__(self, name, steps, exercise_time, points, bpm):
        self.name = name
        self.steps = steps
        self.exercise_time = exercise_time
        self.points = points
        self.bpm = bpm

    def add_steps(self, num_steps):
        #updated every hour
        self.steps += num_steps

    def add_exercise_time(self, num_exercise_time):
        #updated every hour
        self.exercise_time += num_exercise_time
    def add_bpm(self, num_bpm):
        self.bpm += num_bpm

