from FileHandler import read_file
from time import sleep

if __name__ == "__main__":
    all_groups = read_file("list.txt")
    print (all_groups)
    team_size = 4

    while True:
        team = all_groups.get_team(team_size)
        all_groups.sort_groups()
        if len(team) == 0:
            break
        if len(team) < team_size:
            print (team)
            break
        print(team)
        sleep (0.3)