def on_button_pressed_a():
    global menu_num
    menu_num += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global clicked
    clicked = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global menu_num
    menu_num += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_received_value(name, value):
    if receiving == 1:
        basic.show_string("" + str((value)))
radio.on_received_value(on_received_value)

receiving = 0
clicked = 0
menu_num = 1
loop = 0

def on_forever():
    global menu_num
    if loop == 0:
        if menu_num > 0 or menu_num < 4:
            if menu_num == 1:
                basic.show_string("Send")
            if menu_num == 2:
                basic.show_string("Receive")
            if menu_num == 3:
                basic.show_string("Group")
        else:
            menu_num = 1
basic.forever(on_forever)

def on_forever2():
    global loop, clicked, menu_num, receiving
    if clicked == 1:
        basic.pause(100)
        loop = 1
        clicked = 0
        if menu_num == 3:
            menu_num = 1
            while loop == 1:
                if menu_num > 0 and menu_num < 11:
                    basic.show_string("" + str((menu_num)))
                    if clicked == 1:
                        radio.set_group(menu_num)
                        basic.show_string("Connected to... " + str(menu_num))
                        basic.pause(100)
                        clicked = 0
                else:
                    if menu_num == 11:
                        loop = 0
                        menu_num = 1
                    else:
                        menu_num = 1
        if menu_num == 2:
            receiving = 1
            while loop == 1:
                music.play_melody("E G F G E G F G ", 130)
                if clicked == 1:
                    receiving = 0
                    clicked = 0
                    loop = 0
basic.forever(on_forever2)
