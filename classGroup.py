import Person
class Group:
    friends = []
    curr_group_points = 0
    group_point_goal = 0
    goal_fulfilled = False

    def __init__(self, friends, group_point_goal, goal_fulfilled):
        self.friends = friends
        self.group_point_goal = group_point_goal
        self.goal_fulfilled = goal_fulfilled

    def add_friend(self, object_friend):
        self.friends.append(object_friend)

    def remove_friend(self, friends, object_friend):
        for x in friends:
            if x == self.friends.remove(object_friend.name):
                friends.pop(x)

    def goal_Fulfilled(self):
        if self.curr_group_goal >= self.group_point_goal:
            self.goal_fulfilled = True
