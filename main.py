from Car import *


def car_info(car_object=None):
    car = car_object.properties()
    return (
        f"\n================="
        f"\n CAR INFORMATION "
        f"\n================="
        f"\nTYPE : {car['Type']}"
        f"\nWHEEL : Size ( {car['Wheel']['Size']} ), Type ( {car['Wheel']['Type']} )"
        f"\nENGINE : Volume ( {car['Engine']['Volume']} ), Type ( {car['Engine']['Type']} )"
        f"\nSTATE : {car['State']}"
        f"\nSPEED : {car['Speed']}"
        f"\n=================\n"
    )


tiles = {0: " ", 1: "⎕", 2: "⎺", 3: "-", 4: "⎽"}
map_array = [
    [1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
]

my_tiles = {0: " ", 1: "#"}
my_map = [
    [0,0,0,0],
    [0,1,0,0],
    [1,1,1,1],
]
def simple_draw(tile_map):
    for row in range(len(tile_map)):
        print("X")

simple_draw(my_map)

"""
def draw_map():
    global game_map  # Update the global game_map variable
    rendered_rows = []
    for row in map_array:
        rendered_row = "".join([tiles[tile] for tile in row])
        rendered_rows.append(rendered_row)
    game_map = "\n".join(rendered_rows)
    print(game_map)

# draw_map()


# Create a car
car_type = input("Input Car Type (Honda/Toyota/Nissan): ")

my_car = Car(car_type)

# print(car_info(my_car))

while True:
    user_input = input(">>> COMMAND (status/start/move/stop/exit): ").lower()
    match user_input:
        case "exit":
            print("Exiting the program...")
            break
        case "status":
            print(car_info(my_car))
        case "start":
            print(f'... {my_car.change_state("start")}\n')
        case "move":
            print(f'... {my_car.change_state("move")}\n')
        case "stop":
            print(f'... {my_car.change_state("stop")}\n')
        case _:
            print("... Enter a valid command (status/start/move/stop/exit)\n")
            
"""
