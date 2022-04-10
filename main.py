led.plot_brightness(2, 2, 127)

A1 = [0, 0]
B1 = [0, 0]
C1 = [0, 0]
D1 = [0, 0]
A2 = []
B2 = []
C2 = []
D2 = []

stred_soumernost()

def stred_soumernost():
    global A1, B1, C1, D1, A2, B2, C2, D2
    A1 = [0, 0]
    B1 = [0, 1]
    C1 = [1, 1]
    D1 = [1, 0]
    led.plot(A1[0], A1[1])
    led.plot(B1[0], B1[1])
    led.plot(C1[0], C1[1])
    led.plot(D1[0], D1[1])
    A2 = [4 - A1[0], 4 - A1[1]]
    B2 = [4 - B1[0], 4 - B1[1]]
    C2 = [4 - C1[0], 4 - C1[1]]
    D2 = [4 - D1[0], 4 - D1[1]]
    led.plot(A2[0], A2[1])
    led.plot(B2[0], B2[1])
    led.plot(C2[0], C2[1])
    led.plot(D2[0], D2[1])

def on_button_pressed_a():
    global A1, B1, C1, D1, A2, B2, C2, D2
    if C1[0] - B1[0] == 3:
        led.unplot(B1[0], B1[1])
        led.unplot(C1[0], C1[1])
        led.unplot(D1[0], D1[1])
        led.unplot(4 - B1[0], 4 - B1[1])
        led.unplot(4 - C1[0], 4 - C1[1])
        led.unplot(4 - D1[0], 4 - D1[1])
        stred_soumernost()
    else:
        led.unplot(B1[0], B1[1])
        led.unplot(C1[0], C1[1])
        led.unplot(D1[0], D1[1])
        led.unplot(4 - B1[0], 4 - B1[1])
        led.unplot(4 - C1[0], 4 - C1[1])
        led.unplot(4 - D1[0], 4 - D1[1])
        B1[1] += 1
        D1[0] += 1
        C1[0] += 1
        C1[1] += 1
        led.plot(B1[0], B1[1])
        led.plot(C1[0], C1[1])
        led.plot(D1[0], D1[1])
        A2 = [4 - A1[0], 4 - A1[1]]
        B2 = [4 - B1[0], 4 - B1[1]]
        C2 = [4 - C1[0], 4 - C1[1]]
        D2 = [4 - D1[0], 4 - D1[1]]
        led.plot(A2[0], A2[1])
        led.plot(B2[0], B2[1])
        led.plot(C2[0], C2[1])
        led.plot(D2[0], D2[1])
input.on_button_pressed(Button.A, on_button_pressed_a)