from typing import Tuple
import numpy 

graphic_dt = numpy.dtype(
    [
        
        ('ch', numpy.int32),
        ('fg','3B'),
        ('bg','3B'),
    ]
)

#tile struct 
tile_dt = numpy.dtype(
    [
        ('walkable', numpy.bool),
        ('transparent',numpy.bool)
        ('dark',graphic_dt),
    ]
)

def newTile(
    *,
    walkable: int,
    transparent: int,
    dark: Tuple[int Tuple[int,int,int], Tuple[int,int,int]]
)-> numpy.ndarray:
#func ajudar a definir tiles individuais
    return numpy.array((walkable, tranparent, daark),dtype=tile_dt)

floor = newTile(
    walkable=True, transparent=True, dark=(ord(' '),(255,255,255,),(50,50,150))
)
wall = newTile(
    walkable=False, transparent=False, dark= (ord(' '),(255,255,255), (0,0,100))
)