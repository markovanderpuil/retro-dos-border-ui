#!/usr/bin/env python3
# MIT License
#
# Copyright (c) 2025 Marko van der Puil
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import curses
import time
from retro_dos_border_ui import RetroUI

def main(stdscr):
    ui = RetroUI(stdscr)
    ui.scr.nodelay(True)  # non-blocking getch

    # Define data outside the loop
    columns = [("Color", 12), ("Example", 12)]
    data_rows = [
        ["Success", "Green text"],
        ["Error", "Red text"],
        ["Warning", "Yellow text"],
        ["Info", "Blue text"],
        ["Secondary", "Magenta text"],
        ["Accent", "Cyan text"],
        ["Default", "White text"]
    ]
    row_colors = {
        0: RetroUI.Colors.SUCCESS,
        1: RetroUI.Colors.ERROR,
        2: RetroUI.Colors.WARNING,
        3: RetroUI.Colors.INFO,
        4: RetroUI.Colors.SECONDARY,
        5: RetroUI.Colors.ACCENT,
        6: RetroUI.Colors.DEFAULT
    }

    highlight_row = 0
    last_update = time.time()

    while True:
        current_time = time.time()
        if current_time - last_update >= 1.0:
            highlight_row = (highlight_row + 1) % len(data_rows)
            last_update = current_time

            # Redraw the entire UI
            ui.scr.clear()
            ui.current_y_pos = 0  # reset position

            # Draw borders
            ui.draw_border_top()
            ui.draw_vertical_borders()
            ui.draw_border_bottom()

            # Add content
            ui.add_title("My App !!!")
            ui.add_table(
                columns=columns,
                data_rows=data_rows,
                row_colors=row_colors,
                highlight_row=highlight_row
            )
            ui.add_status_bar("Status line 1", "Status line 2 at current time: "+time.strftime("%H:%M:%S"))

            ui.refresh()

        key = ui.scr.getch()
        if key != -1:
            break
        time.sleep(0.1)  # pause briefly to avoid high CPU usage

if __name__ == "__main__":
    curses.wrapper(main)
