if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    coordinates_list = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                coordinates_list.append([i, j, k])
    print [coordinates for coordinates in coordinates_list if coordinates[0] + coordinates[1] + coordinates[2] != n]
