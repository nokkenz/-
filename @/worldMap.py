import numpy
from tcod.console import Console
import tilesTypes

class gameMap:
    def __init__(self, w: int, h, int):
        self.w, self.h = w, h
        self.tiles = numpy.full((w,h),fill_value=tilesTypes.floor,order='F')
        self.tiles[30:33, 22] = tilesTypes.wall

    def inbounds(self, x: int, y: int) -> bool:
        #return true se y e x estão dentro do mapa 
        return 0 <= x < self.w and 0 <= y < self.h

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.w, 0: self.h] = self.tiles['dark']
        