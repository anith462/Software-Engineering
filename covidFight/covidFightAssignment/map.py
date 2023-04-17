from settings import *

text_map = [
    'AACACDAACAAA',
    'A..........E',
    'B..C.A.BBA.A',
    'A..A.A..cA.C',
    'A..B....A..A',
    'B..A..BAAA.C',
    'A..B...C...A',
    'ADAAAAEAAAcA'
]

world_map = {}
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == 'A':
                world_map[(i * TILE, j * TILE)] = 'a'
            elif char == 'B':
                world_map[(i * TILE, j * TILE)] = 'b'
            elif char == 'C':
                world_map[(i * TILE, j * TILE)] = 'c'
            elif char == 'E':
                world_map[(i * TILE, j * TILE)] = 'e'
            else:
                world_map[(i * TILE, j * TILE)] = 'd'