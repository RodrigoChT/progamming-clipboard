-
bar <user.number>:
    app.window_next()
    sleep(250ms)
    key(number)
    sleep(250ms)
    app.window_next()
    sleep(250ms)
    edit.paste()
bar <user.letter>:
    app.window_next()
    sleep(250ms)
    key(letter)
    sleep(250ms)
    app.window_next()
    sleep(250ms)
    edit.paste()
funk <user.number>:
    app.window_next()
    sleep(250ms)
    key("ctrl-{number}")
    sleep(250ms)
    app.window_next()
    sleep(250ms)
    edit.paste()
funk <user.letter>:
    app.window_next()
    sleep(250ms)
    key("ctrl-{letter}")
    sleep(250ms)
    app.window_next()
    sleep(250ms)
    edit.paste()2
