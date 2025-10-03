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
