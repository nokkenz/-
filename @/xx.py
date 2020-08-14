import tcod #http://rogueliketutorials.com/tutorials/tcod/v2/part-1/
from actions import EscapeAction,Movement
from input import eventHandler
from entity import Entity
from engine import Engine
from worldMap import gameMap

def main() -> None:
    W = 80
    H = 60 

    w = 80
    h = 55

    # PlayerX = int(W/2)
    # PlayerY = int(H/2)

    titeset = tcod.tileset.load_tilesheet(
        "img.png",32, 8, tcod.tileset.CHARMAP_TCOD
    )

    EventHandler = eventHandler()
    
    player = Entity(int(W/2), int(H/2), '-_-',(130,255,80))
    npc = Entity(int(W/2-5),int(H/2), '@', (255,255,255))
    entities = {player, npc}

    worldMap = gameMap(w,h)
     
    # engine = Engine(entities= entities, EventHandler=EventHandler, player= player)
    engine = Engine(entities=entities, EventHandler=EventHandler, gameMap=gameMap, player=player)

    with tcod.context.new_terminal(
        W,
        H,
        tileset=titeset,
        title='********',
        vsync=True,
    ) as context:
        root_console = tcod.Console(W,H, order='F')
        while True:
            #root_console.print(x=PlayerX,y=PlayerY,string='-_-')
            # root_console.print(x=player.x, y=player.y, string=player.char,fg=player.color)
            #context.present(root_console)
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.Eventos(events)
            # root_console.clear()

            # for event in tcod.event.wait():
            #     if event.type == 'QUIT':
            #         raise SystemExit()
                
            #     action = EventHandler.dispatch(event)

                # if action is None:
                #     continue

                # if isinstance(action, Movement):
                #     #PlayerX += action.dx
                #     #PlayerY += action.dy
                #     player.move(dx=action.dx, dy=action.dy)

                # elif isinstance(action, Movement):
                #     raise SystemError()          

if __name__=='__main__':
    main()