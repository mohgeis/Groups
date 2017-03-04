from Groups import Groups
from Group import Group

def read_file(file_path):
    with open(file_path, 'r') as myfile:
        groups_list = Groups()
        group_str_lst = myfile.read().split(sep="#")
        for g in group_str_lst:
            if len(g)==0:
                continue
            g_list = g.splitlines()
            group = Group(g_list.pop(0))
            group.add_member(g_list)
            groups_list.add_group(group)
        return groups_list

if __name__ == "__main__":
    groups = read_file("/home/mg/PycharmProjects/Groups/list.txt")
    groups.sort_groups()
    print(groups)