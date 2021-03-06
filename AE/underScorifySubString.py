def underscorifySubstring(string, substring):
    location = collapse(getLocations(string, substring))


def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
            break
    print("getLC", locations)
    return locations


def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    print("newlx", newLocations)
    previous = newLocations[0]
    print("prex", previous)
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            newLocations.append(current)
            previous = current
    print(newLocations)
    return newLocations


def underScorify(string, locations):
    locationIdx = 0
    stringIdx = 0
    inBetweenUnderscores = False
    finalChars = []
    i = 0
    while stringIdx < len(string) and locationIdx < len(locations):
        if stringIdx == locations[locationIdx][i]:
            finalChars.append("_")
            inBetweenUnderscores = not inBetweenUnderscores
            if not inBetweenUnderscores:
                locationIdx += 1
            i == 0 if i == 1 else 1
        finalChars.append(string[stringIdx])
        stringIdx += 1
    if locationIdx < len(locations):
        finalChars.append("_")
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx:])
    return "".join(finalChars)


print(underscorifySubstring("testthis is a testtest to see if testestest it works", "test"))

ls = [[0, 4], [14, 18], [18, 22], [33, 37], [36, 40], [39, 43]]
print(ls[0])
print("pre", ls[0][0])
