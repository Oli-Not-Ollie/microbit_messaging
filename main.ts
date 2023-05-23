input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    menu_num += -1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    clicked = 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    menu_num += 1
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    if (receiving == 1) {
        basic.showString("" + ("" + value))
    }
    
})
let receiving = 0
let clicked = 0
let menu_num = 1
let loop = 0
basic.forever(function on_forever() {
    
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
basic.forever(function on_forever2() {
    
    if (clicked == 1) {
        basic.pause(100)
        loop = 1
        clicked = 0
        if (menu_num == 3) {
            menu_num = 1
            while (loop == 1) {
                if (menu_num > 0 && menu_num < 11) {
                    basic.showString("" + ("" + menu_num))
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
        
    }
    
})
