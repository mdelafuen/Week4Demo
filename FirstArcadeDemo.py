import arcade


def main ():
    arcade.open_window(800, 800, "Hey We Have a Window")
    arcade.set_background_color(arcade.color.ALMOND)
    # now create objects
    main_house = arcade.create_rectangle(400, 200, 400, 400, arcade.color.ANTIQUE_BRASS)
    door = arcade.create_rectangle(400, 75, 100, 150, arcade.color.ARMY_GREEN)
    window1 = arcade.create_ellipse(300, 300, 75, 75, arcade.color.BABY_BLUE)

    # now we will begin to draw
    arcade.start_render()
    # draw everything here
    main_house.draw()
    door.draw()
    window1.draw()

    arcade.finish_render()

    arcade.run()





main()