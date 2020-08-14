from typing import Set, Iterable, Any
from tcod.context import Context
from tcod.console import Console
from actions import EscapeAction, Movement
from entity import Entity
from input import eventHandler
from worldMap import gameMap

class Engine:
    #def __init__(self, entities: Set[Entity], EventHandler : eventHandler(), player : Entity):
    def __init__(self, entities: Set[Entity], eventHandler: eventHandler,gameMap=gameMap, player: Entity):
    #def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):    
        self.entities = entities
        self.EventHandler = EventHandler
        self.player = player
        self.gameMap = gameMap

    def Eventos(self,events: Iterable[Any]) -> None:
        for event in events:
            action =  self.EventHandler.dispatch(event)

            if action is None:
                continue
            
            if isinstance(action, Movement):
                # self.player.move(dx=action.dx, dy=action.dy)
                if self.gameMap.tiles['walkable'][self.player.x + action.dx,self.player + action.dy]:
                    self.player.move(dx=action.dx, dy=action.dy)

            elif isinstance(action, EscapeAction):
                raise SystemError()

    def render(self, console: Console, context: Context) -> None:
        self.gameMap.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg = entity.color)

            context.present(console)

            console.clear()