import tcod #http://rogueliketutorials.com/tutorials/tcod/v2/part-1/

def main() -> None:
    W = 80
    H = 60 

    PlayerX = int(W/2)
    PlayerY = int(Y/2)

    titeset = tcod.tileset.load_tilesheet(
        "img.png",32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new_terminal(
        W,
        H,
        tileset=titeset,
        title='Tuto @ Adventures',
        vsync=True
    ) as context:
        root_console = tcod.Console(W,H, order='F')
        while True:
            root_console.print(x=PlayerX,y=PlayerY,string='@')

            context.present(root_console)

            for event in tcod.event.wait():
                if event.type == 'QUIT':
                    raise SystemExit()

if __name__=='__main__':
    main()