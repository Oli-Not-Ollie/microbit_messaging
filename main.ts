input.onButtonPressed(Button.A, function () {
    menu_num += -1
})
input.onButtonPressed(Button.AB, function () {
    clicked = 1
})
radio.onReceivedString(function (receivedString) {
    if (receiving == 1) {
        basic.showString(receivedString)
    }
})
input.onButtonPressed(Button.B, function () {
    menu_num += 1
})
let message = ""
let loop = 0
let receiving = 0
let clicked = 0
let menu_num = 1
radio.setGroup(1)
basic.forever(function () {
    if (clicked == 1) {
        basic.pause(100)
        loop = 1
        clicked = 0
        if (menu_num == 3) {
            menu_num = 1
            while (loop == 1) {
                if (menu_num > 0 && menu_num < 11) {
                    basic.showString("" + (menu_num))
                    if (clicked == 1) {
                        radio.setGroup(menu_num)
                        basic.showString("Connected to... " + ("" + menu_num))
                        basic.pause(100)
                        clicked = 0
                    }
                } else if (menu_num == 11) {
                    loop = 0
                    menu_num = 1
                } else {
                    menu_num = 1
                }
            }
        }
        if (menu_num == 2) {
            receiving = 1
            while (loop == 1) {
                music.playMelody("E G F G E G F G ", 130)
                if (clicked == 1) {
                    receiving = 0
                    clicked = 0
                    loop = 0
                }
            }
        }
        if (menu_num == 1) {
            menu_num = 1
            while (loop == 1) {
                if (menu_num > 0 || menu_num < 8) {
                    if (menu_num == 1) {
                        message = "Hello"
                        basic.showString("Hello")
                    } else if (menu_num == 2) {
                        message = "How are you?"
                        basic.showString("How are you?")
                    } else if (menu_num == 3) {
                        message = "Good"
                        basic.showString("Good")
                    } else if (menu_num == 4) {
                        message = "Bad"
                        basic.showString("Bad")
                    } else if (menu_num == 5) {
                        message = "Yes"
                        basic.showString("Yes")
                    } else if (menu_num == 6) {
                        message = "No"
                        basic.showString("No")
                    } else {
                        message = "Goodbye"
                        basic.showString("Goodbye")
                    }
                } else {
                    loop = 0
                }
                if (clicked == 1) {
                    radio.sendString(message)
                    clicked = 0
                }
            }
        }
    }
})
basic.forever(function () {
    if (loop == 0) {
        if (menu_num > 0 || menu_num < 4) {
            if (menu_num == 1) {
                basic.showString("Send")
            }
            if (menu_num == 2) {
                basic.showString("Receive")
            }
            if (menu_num == 3) {
                basic.showString("Group")
            }
        } else {
            menu_num = 1
        }
    }
})
