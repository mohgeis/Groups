from FileHandler import read_file
from time import sleep

if __name__ == "__main__":
    all_groups = read_file("Fika_list.txt")
    print (all_groups)

    while True:
        team = all_groups.get_team(3)
        all_groups.sort_groups()
        if len(team) == 0:
            break
        if len(team) < 3:
            print (team)
            break
        print(team)
        sleep (0.5)