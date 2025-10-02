#!/usr/bin/env python3
import curses
from retro_dos_border_ui import RetroUI

def main(stdscr):
    ui = RetroUI(stdscr)

    # Draw borders
    ui.draw_border_top()
    ui.draw_vertical_borders()
    ui.draw_border_bottom()

    # Add content
    ui.add_title("My App")
    ui.add_table([("Column1", 10), ("Column2", 10)], [["data1", "data2"]])
    ui.add_status_bar("Status line 1", "Status line 2")

    ui.refresh()
    ui.get_key()

if __name__ == "__main__":
    curses.wrapper(main)
