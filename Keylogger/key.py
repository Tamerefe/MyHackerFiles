import pynput.keyboard

totalwords = ""
def order(words):
    global totalwords

    try:
        totalwords += str(words.char)
    except AttributeError:
        if words == words.space:
            totalwords += " "
        elif words == words.backspace:
            num = len(totalwords)
            num -=1
            dgr = 0
            ttl = ""
            while num > dgr:
                ttl += totalwords[dgr]
                dgr += 1
            totalwords = ttl
        elif words == words.enter:
            totalwords += "\n"
        else:    
            totalwords += str(words)

    print(totalwords)

inputter = pynput.keyboard.Listener(on_press=order)

with inputter:
    inputter.join()