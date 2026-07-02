import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        str = input("Enter new coordinates as floats in format 'x,y,z': ")
        lst_str = str.split(',')
        try:
            sx, sy, sz = lst_str
            if "" in lst_str:
                raise (ValueError)
        except ValueError:
            print("Invalid syntax")
            continue
        flag = True
        for cord in lst_str:
            try:
                float(cord)
            except ValueError:
                print(f"Error on parameter '{cord}': ", end="")
                print(f"could not convert string to float: '{cord}'")
                flag = False
                break
        if flag:
            return (
                round(float(sx), 1),
                round(float(sy), 1),
                round(float(sz), 1)
                )


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    first = get_player_pos()
    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    x1, y1, z1 = first
    print(f"Distance to center: {round(math.sqrt(x1*x1+y1*y1+z1*z1), 4)}")
    print()

    print("Get a second set of coordinates")
    second = get_player_pos()
    x2, y2, z2 = second
    print("Distance between the 2 sets of coordinates: ", end="")
    print(round(math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2)), 4))
