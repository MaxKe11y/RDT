startcrds = [0,0]
rvrlocs = []
count=0

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

endcrds=input("Enter the upper right coordinates: ").split()
endcrds = [int(item) for item in endcrds]
for i in range (0,2):
    count = count+1
    rvrstart = input("Enter Rover " + str(count) + " start point and heading: ").split()
    rvrmove = input("Enter Rover " + str(count) + " movement commands: ").upper()
    rvrstart[2] = directions1[rvrstart[2]]
    rvrstart = [int(item) for item in rvrstart]

    rvrmove = list(rvrmove)
    rvrloc = mover(rvrstart, rvrmove)

    rvrloc[2] = directions2[rvrloc[2]]
    rvrlocs.append(rvrloc)


print(*rvrlocs[0])
print(*rvrlocs[1])











