let A1 = [0, 0]
let B1 = [0, 0]
let C1 = [0, 0]
let D1 = [0, 0]
let A2 = []
let B2 = []
let C2 = []
let D2 = []
stred_soumernost()
function stred_soumernost() {
    
    A1 = [0, 0]
    B1 = [0, 1]
    C1 = [1, 1]
    D1 = [1, 0]
    Plotting()
}

basic.forever(function stred() {
    led.plotBrightness(2, 2, 127)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (C1[0] - B1[0] == 3) {
        Unplotting()
        stred_soumernost()
    } else {
        Unplotting()
        B1[1] += 1
        D1[0] += 1
        C1[0] += 1
        C1[1] += 1
        Plotting()
    }
    
})
function Plotting() {
    led.plot(A1[0], A1[1])
    led.plot(B1[0], B1[1])
    led.plot(C1[0], C1[1])
    led.plot(D1[0], D1[1])
    let A2 = [4 - A1[0], 4 - A1[1]]
    let B2 = [4 - B1[0], 4 - B1[1]]
    let C2 = [4 - C1[0], 4 - C1[1]]
    let D2 = [4 - D1[0], 4 - D1[1]]
    led.plot(A2[0], A2[1])
    led.plot(B2[0], B2[1])
    led.plot(C2[0], C2[1])
    led.plot(D2[0], D2[1])
}

function Unplotting() {
    led.unplot(B1[0], B1[1])
    led.unplot(C1[0], C1[1])
    led.unplot(D1[0], D1[1])
    led.unplot(4 - B1[0], 4 - B1[1])
    led.unplot(4 - C1[0], 4 - C1[1])
    led.unplot(4 - D1[0], 4 - D1[1])
}

