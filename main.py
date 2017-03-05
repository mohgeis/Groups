import sys, getopt
from FileHandler import read_file,write_file
from time import sleep

def read_args(argv):
   inputfile = 'list.txt'
   outputfile = 'output.json'
   teamsize = '3'
   try:
      opts, args = getopt.getopt(argv,"hs:i:o:",["tsize=","ifile=","ofile="])
   except getopt.GetoptError:
      print ('main.py -s <teamsize> -i <inputfile> [-o <outputfile>]')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('main.py -s <teamsize> -i <inputfile> [-o <outputfile>]')
         sys.exit()
      elif opt in ("-s", "--tsize"):
         teamsize = arg
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   return teamsize,inputfile,outputfile


if __name__ == "__main__":
    team_size_str,input_file,output_file = read_args(sys.argv[1:])
    team_size = int(team_size_str)
    print (team_size,input_file,output_file)
    all_groups = read_file(input_file)
    print (all_groups)

    teams_list = []
    print("Teams:")
    print("======")
    while True:
        team = all_groups.get_team(team_size)
        all_groups.sort_groups()
        if len(team) == 0:
            break
        if len(team) < team_size:
            print (team)
            teams_list.append(team)
            break
        print(team)
        teams_list.append(team)
        sleep (0.3)
    write_file(output_file, teams_list)
