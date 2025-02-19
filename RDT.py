# Define variables
startcrds = [0, 0]
rvrlocs = []
count = 0

# Set direction dictionaries
directions1 = {
    "N" : 0,
    "E" : 90,
    "S" : 180,
    "W" : 270,
}
directions2 = {
    0 : "N",
    90 : "E",
    180 : "S",
    270 : "W",
}

# Rover movement function - queries command and moves / turns rover as requested
def mover(rvrstart, rvrmove):
    for cmnd in rvrmove:
        if cmnd == "M":
            if rvrstart[2] == 0 and rvrstart[1] < endcrds[1]:
                rvrstart[1] += 1
            elif rvrstart[2] == 90 and rvrstart[0] < endcrds[0]:
                rvrstart[0] += 1
            elif rvrstart[2] == 180 and rvrstart[1] > 0:
                rvrstart[1] -= 1
            elif rvrstart[2] == 270 and rvrstart[0] > 0:
                rvrstart[0] -= 1

        elif cmnd == "R":
            rvrstart[2] += 90
            if rvrstart[2] == 360:
                rvrstart[2] = 0
        elif cmnd == "L":
            rvrstart[2] -= 90
            if rvrstart[2] == -90:
                rvrstart[2] = 270
    return rvrstart
print("##########################################")
print("####      RDT Mars Rover Project      ####")
print("##########################################")
print("####          Instructions:           ####")
print("####  Enter two numbers with a space  ####")
print("####  between as coordinates e.g(5 5) ####")
print("####                                  ####")
print("####  Enter coordinates and direction ####")
print("####  for start point e.g(0 1 N)      ####")
print("####                                  ####")
print("####  Use L or R to rotate the rover  ####")
print("####  90 degrees left(L) or right(R)  ####")
print("####  and use M to move the rover in  ####")
print("####  the direction it's facing       ####")
print("####                                  ####")
print("##########################################")
# Upper right coordinate input and validation 42
loop = True
while loop:
    endcrds = input("Enter the upper right coordinates: ").split()
    try:
        endcrds = [int(item) for item in endcrds]
        if endcrds[0] >= 0 and endcrds[1] > 0 and len(endcrds) == 2:
                loop = False
    except:
        print("Error please try again")


#
for i in range (0,2):
    count = count+1
    loop = True
    while loop:

        rvrstart = input("Enter Rover " + str(count) + " start point and heading: ").split()
        rvrmove = input("Enter Rover " + str(count) + " movement commands: ").upper()
        try:
            rvrstart[2] = directions1[rvrstart[2]]
            rvrstart = [int(item) for item in rvrstart]

            rvrmove = list(rvrmove)
            rvrloc = mover(rvrstart, rvrmove)

            rvrloc[2] = directions2[rvrloc[2]]
            rvrlocs.append(rvrloc)
            loop = False
        except:
            print("Error please try again")



print(*rvrlocs[0])
print(*rvrlocs[1])











