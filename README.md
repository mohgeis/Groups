# Groups
Create mixed teams from already existing groups (list from lists, or Fika list from teams) 

link: https://github.com/mohgeis/Groups

### Example:

Group 1:
 a1,b1,c1

Group 2:
 a2,b2,c2,d2

Group 3:
 a3,b3

Group 4:
 a4,b4,c4

Gruop 5:
 a5,b5,c5,d5,e5

- Teams of 3:
  * ['a3', 'c1', 'b4']
  * ['c5', 'b2', 'a4']
  * ['a5', 'a2', 'a1']
  * ['e5', 'd2', 'b1']
  * ['d5', 'c2', 'c4']
  * ['b3', 'b5']

- Teams of 4:
  * ['a3', 'b1', 'b4', 'a2']
  * ['e5', 'b2', 'a4', 'a1']
  * ['d5', 'd2', 'c4', 'c1']
  * ['a5', 'b3', 'c5', 'c2']
  * ['b5']
  
### how to use:
simply fill the example file list.txt with the original lists, then run the main file.

In "list.txt" use the format (#Group_name) to specify the group name, then list all the group members below (just like the example file)

eg. 

-#group 1

member 1

member 2

member 3
