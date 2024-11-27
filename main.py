def on_button_pressed_a():
    global menu_num
    menu_num += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global clicked
    clicked = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_received_string(receivedString):
    if receiving == 1:
        basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    global menu_num
    menu_num += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def MENU():
    global menu_num, loop
    while loop == 0:
        if menu_num > 0 or menu_num < 4:
            if menu_num == 1:
                basic.show_string("Send")
            if menu_num == 2:
                basic.show_string("Receive")
            if menu_num == 3:
                basic.show_string("Group")
        else:
            menu_num = 1
        if clicked == 1:
            loop = 1
message = ""
receiving = 0
clicked = 0
menu_num = 0
loop = 0
loop = 0
menu_num = 1
radio.set_group(1)
MENU()

def on_forever():
    global loop, clicked, menu_num, receiving, message
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
                        basic.show_string("Connected to... " + ("" + str(menu_num)))
                        basic.pause(100)
                        clicked = 0
                elif menu_num == 11:
                    loop = 0
                    menu_num = 1
                    MENU()
                else:
                    menu_num = 1
        if menu_num == 2:
            receiving = 1
            clicked = 0
            while loop == 1:
                music.play_melody("E G F G E G F G ", 130)
                if clicked == 1:
                    receiving = 0
                    clicked = 0
                    loop = 0
                    MENU()
        if menu_num == 1:
            menu_num = 1
            while loop == 1:
                message = ""
                if menu_num > 0 or menu_num < 9:
                    if menu_num == 1:
                        message = "Hello"
                        basic.show_string("Hello")
                    elif menu_num == 2:
                        message = "How are you?"
                        basic.show_string("How are you?")
                    elif menu_num == 3:
                        message = "Good"
                        basic.show_string("Good")
                    elif menu_num == 4:
                        message = "Bad"
                        basic.show_string("Bad")
                    elif menu_num == 5:
                        message = "Yes"
                        basic.show_string("Yes")
                    elif menu_num == 6:
                        message = "No"
                        basic.show_string("No")
                    elif menu_num == 7:
                        message = "Goodbye"
                        basic.show_string("Goodbye")
                    elif menu_num == 8:
                        message = "Goodbye"
                else:
                    loop = 0
                    MENU()
                if clicked == 1:
                    radio.send_string(message)
                    clicked = 0
basic.forever(on_forever)
