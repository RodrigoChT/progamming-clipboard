# progamming-clipboard
Create a [clipboard](https://github.com/RodrigoChT/progamming-clipboard/blob/master/example.png) of all the variables, functions, and packages used in a python file.

## How to use
1. Run ``clipboard.py`` with the full path of the python file that will be the source of the clipboard as an argument.
2. These will create a window with all the variables, functions, and packages used in the source file.
3. Click on any of the buttons to copy their text. You can also copy the variables by pressing their associated hotkey and the functions and packages by pressing their Ctrl+hotkey.
4. Everytime the source file is changed (and saved), any new variables or functions will appear in the clipboard.
5. Deleted variables will not dissapear from the clipboard, you can relaunch it for that.

## Use with [talon](https://talonvoice.com/)
The file ``clipboard.talon`` contains commands to copy and paste any of the values in the clipboard using voice commands. For now you need to have the clipboard as the "next window" (one alt+tab away). To copy and paste variables say ``"bar <number|letter>"`` and for functions and packages say ``"funk <number|letter>"``

## Pending features
- Create the clipboard with a voice command using the file in focus as the source.
- Make talon focus the clipboard with it having to be the "next window".
- Check more edge cases for the regex rules.
- Add functionality for R files.
- Make the font size change with the button size.
- Add button to delete variables no longer present in the source file.
- Add hotkeys when the amount of elements is greater than (10 + alphabet).
