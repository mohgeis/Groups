from random import shuffle

class Group(object):
    """

    """
    def __init__(self, name):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.members = []

    def size(self):
        return len(self.members)

    def add_member(self, member):
        self.members.extend(member)
        shuffle(self.members)
        return self

    def remove_member(self):
        """Return the balance remaining after depositing *amount*
        dollars."""
        try:
            return self.members.pop()
        except:
            return None

    def __str__(self):
        return self.members.__str__()

    def __repr__(self):
        return "%s : %s" % (self.name, self.members.__repr__())

    def shuffle(self):
        shuffle(self.members)

if __name__ == "__main__":
    group_a = Group("Group_a")
    print (group_a.name, " : ", group_a.size())
    group_a.add_member("D")
    print (group_a)

    print (group_a.remove_member())
    print (group_a.remove_member())
    print (group_a.remove_member())
    print (group_a.remove_member())
