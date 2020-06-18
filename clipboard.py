from tkinter import *
import tkinter.font as font
from copy import copy
import sys

from utils import scan_line
from utils import check_and_create
from utils import create_labels

# parameters
font_family = 'Times'
font_size = 20
objective_file = str(sys.argv[1])

# tkinter setup
root = Tk()
root.title('Clipboard')
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame = Frame(root)
frame.focus_set()
frame.grid(row=0, column=0, sticky=N+S+E+W)
button_font = font.Font(family = font_family, size=font_size)

# column names
Label(frame, text = 'Hotkey', font = button_font).grid(row=0, column = 0)
Label(frame, text = 'Variables', font = button_font).grid(row=0, column = 1)
Label(frame, text = 'Funcs & Pckgs', font = button_font).grid(row=0, column = 2)

# create buttons
clip_list = set()
func_clip_list = set()
j = 0
num_vars = 0
num_funcs = 0
comma_end = None

# read file with elements of the clipboard
while True:
    clip_list_prev = copy(clip_list)
    clip_list_func_prev = copy(func_clip_list)
    # read file
    with open(objective_file) as file:
        file_lines = file.readlines()
    # search for variables, functions, and packages
    clip_list_temp = []
    clip_list_func_temp = []
    for line in file_lines:
        comma_end_prev = comma_end
        var, func, comma_end = scan_line(line.strip())
        if func is not None:
            clip_list_func_temp.append(func.group(1))
        if var is not None and comma_end_prev is None:
            var_contains_paren = var.group(0).find('(')
            var_contains_comp = var.group(0).find('==')
            if var_contains_paren == -1 and var_contains_comp == -1:
                all_selec = var.group(0).replace('=', '').split(',')
                all_selec = [x.strip() for x in all_selec if x.strip() != '']
                clip_list_temp.extend(all_selec)

    # create variable buttons
    num_vars_prev = num_vars
    clip_list, num_vars = check_and_create(clip_list_temp,
                                           clip_list_prev,
                                           frame,
                                           1,
                                           num_vars,
                                           '',
                                           button_font)

    # create function buttons
    num_funcs_prev = num_funcs
    func_clip_list, num_funcs = check_and_create(clip_list_func_temp,
                                                clip_list_func_prev,
                                                frame,
                                                2,
                                                num_funcs,
                                                'Control',
                                                 button_font)

    # create labels
    create_labels([num_vars, num_funcs],
                  [num_vars_prev, num_funcs_prev],
                  frame,
                  button_font)

    # update tk
    root.update_idletasks()
    root.update()