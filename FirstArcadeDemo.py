import arcade


def main ():
    arcade.open_window(800, 800, "Hey We Have a Window")
    arcade.set_background_color(arcade.color.ALMOND)
    # now create objects
    main_house = arcade.create_rectangle(400, 200, 400, 400, arcade.color.ANTIQUE_BRASS)
    door = arcade.create_rectangle(400, 75, 100, 150, arcade.color.ARMY_GREEN)
    window1 = arcade.create_ellipse(300, 300, 50, 50, arcade.color.BABY_BLUE)
    window2 = arcade.create_ellipse(500, 300, 50, 50, arcade.color.BABY_BLUE)
    roof_points = [(200, 400), (400, 600), (600, 400)]
    roof = arcade.create_polygon(roof_points, arcade.color.DARK_GRAY)

    # now we will begin to draw
    arcade.start_render()
    # draw everything here
    main_house.draw()
    door.draw()
    window1.draw()
    window2.draw()
    roof.draw()

    arcade.finish_render()

    arcade.run()





main()