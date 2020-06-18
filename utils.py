from tkinter import *
import re

def scan_line(line):
    var = re.search(r'[(\w, +]+=+', line)
    func = re.search(r' *def *(\w+)', line)
    if not func:
        func = re.search(r' *from *[\w]+ *import *(\w+)', line)
    if not func:
        func = re.search(r' *import.*as *(\w+)', line)
    if not func:
        func = re.search(r' *import (\w+)', line)
    comma_end = re.search(r'(,)$', line)
    return var, func, comma_end

def row_to_key(row):
    if row < 10:
        key = str(row)
    else:
        key = chr(row + 87)
    return key

def check_and_create(clip_list, prev, TK, column, num, modifier, button_font):
    # check if any new variables are created
    clip_list = sorted(set(clip_list), key=clip_list.index)
    new_clips = [x for x in clip_list if x not in prev]
    total = num
    # make buttons for new variables
    for i, clip in enumerate(new_clips):
        total = num + i
        button_key = row_to_key(total)
        if modifier != '':
            button_key = '<' + modifier + '-Key-' + button_key + '>'
        new_button = Button(TK,
                                text=clip,
                                width=20,
                                anchor='w',
                                command=lambda a=' ', clip_i=clip: [TK.clipboard_clear(),
                                                                    TK.clipboard_append(clip_i)])
        new_button['font'] = button_font
        TK.bind(button_key, lambda a=' ', clip_j=clip: [TK.clipboard_clear(),
                                                             TK.clipboard_append(clip_j)])
        Grid.rowconfigure(TK, total + 1, weight =1)
        Grid.columnconfigure(TK, column, weight =1)
        new_button.grid(row=total + 1, column=column, sticky=N+S+E+W)
    if len(new_clips) > 0:
        total = total + 1

    return clip_list, total

def create_labels(buttons, prev_buttons, TK, button_font):
    new_max_label = max(buttons)
    prev_max_label = max(prev_buttons)
    for i in range(prev_max_label, new_max_label):
        key = row_to_key(i)
        # Grid.rowconfigure(TK, i + 1, weight=1)
        # Grid.columnconfigure(TK, 0, weight=1)
        new_label = Label(TK, text=key)
        new_label['font'] = button_font
        new_label.grid(row=i + 1, column=0)

