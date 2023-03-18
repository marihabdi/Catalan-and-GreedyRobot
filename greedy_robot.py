
#Mariama Abdi
#CSS 310
#Instructor Dimpsey


def PathToTreasure(x1, y1, x2, y2, path_string):

    #variable to store the total number of paths
    #the robot has taken
    total_paths = 0

    #base case for when it reaches it's target
    if x1 == x2 and y1 == y2:
        total_paths += 1
        print(path_string)
        return total_paths

    #Move in south direction
    if y1 > y2:
        path = PathToTreasure(x1, y1 - 1, x2, y2, path_string + 'S')
        total_paths += path
    #Move in North direction
    elif y1 < y2:
        path = PathToTreasure(x1, y1 + 1, x2, y2, path_string + 'N')
        total_paths += path
    #Move in east direction
    if x1 < x2:
        path = PathToTreasure(x1 + 1, y1, x2, y2, str(path_string) + 'E')
        total_paths += path
    #Move in west direction
    elif x1 > x2:
        path = PathToTreasure(x1 - 1, y1, x2, y2, path_string + 'W')
        total_paths += path

    return total_paths

#Takes an input of numbers with space in between them, 
numbers = input()
#numbers is then stored in points as a list   
points = list(map(int, numbers.split()))

# points are split into the correct
# coordinates, x1, y1, x2, and y2
x1 = points[0]
y1 = points[1]
x2 = points[2]
y2 = points[3]

#empty string to store the directions
#the robot has went in
path_string = ''

# The function PathToTreasure is called
print(PathToTreasure(x1, y1, x2, y2, path_string))