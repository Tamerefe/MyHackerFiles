import pynput.keyboard

totalwords = ""
def order(words):
    global totalwords

    try:
        totalwords += str(words.char)
    except AttributeError:
        if words == words.space:
            totalwords += " "
        # elif words == words.backspace:
        #     totalwords
        else:    
            totalwords += str(words)

    print(totalwords)

inputter = pynput.keyboard.Listener(on_press=order)

with inputter:
    inputter.join()