from Group import Group
from random import shuffle

class Groups(object):

    def __init__(self):
        self.groups_list = []

    def __str__(self):
        return self.groups_list.__str__()

    def find_order(self,group):
        group_size = group.size()
        i=0
        for g in self.groups_list:
            if group_size < g.size():
                return i
            i = i+1
        return i

    def sort_groups(self):
        shuffle(self.groups_list)
        self.groups_list.sort(key=lambda g: g.size(), reverse=True)
        return self

    def add_group(self,  group):

        group.shuffle()
        order = self.find_order(group)
        self.groups_list.insert(order, group)
        return self

    def get_team(self, team_size):
        """
        get a member from each group
        :param team_size: howmany members to get
        :return: members names
        """
        team = []
        for num in range(0,team_size):
            try:
                i = num % len(self.groups_list)
                team.append(self.groups_list[i].remove_member())
                if self.groups_list[i].size() < 1:
                    self.groups_list.pop(i)
            except Exception:
                return team
        return team


if __name__ == "__main__":
    all_groups = Groups()
    all_groups.add_group(Group("H").add_member(["h1", "h2"]))
    all_groups.add_group(Group("M").add_member(["m1","m2","m3","m4"]))
    all_groups.add_group(Group("Z").add_member(["z1","z2","z3"]))
    print (all_groups)
    print (all_groups.sort_groups())

    while True:
        t = all_groups.get_team(2)
        print ()
        print ("team: ", t)
        if len(t) < 2:
            break
        print("left: " ,all_groups.sort_groups())
