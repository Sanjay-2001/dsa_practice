def find_rod_pair(rod_heights):
    maxHeight = max(rod_heights)
    found = False
    for i in range(len(rod_heights)):
        for j in range(i+1, len(rod_heights)):
            if rod_heights[i] + rod_heights[j] == maxHeight:
                print("Fencing will be done with rods {} and {}. (Max height:{})".format(
                    rod_heights[i], rod_heights[j], maxHeight))
                found = True
                return

    if found == False:
        print("No two rods found whose heights sum up to the maximum height.")


find_rod_pair([5, 10, 3, 7])
