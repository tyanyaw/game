# tiles = {0: " ", 1: "⎕", 2: "⎺", 3: "-", 4: "⎽"}
"""
num_tiles = {}
for key,value in tiles.items():
    num_tiles[key] = next(iter(value.values()))
"""

tiles = {
    0 : {"sky": " "},
    1 : {"city": "⎕"},
    2 : {"top_road": "⎺"},
    3 : {"middle_road": "-"},
    4 : {"bottom_road": "⎽"}
}

map_city = [
[0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0],
[0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0],
[0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]
]

def draw_map(tile_map, tile_sprite):
    render_map = []
    for row in tile_map:
        render_row = [ next(iter(tile_sprite.get(col, "?").values())) for col in row ]
        render_map.append(render_row)

    # print(render_map)
    screen_render = "\n".join("".join(item) for item in render_map)
    print(screen_render)

draw_map(map_city, tiles)
