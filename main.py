def on_button_pressed_a():
    for index in range(5):
        right.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        cuteBot.singleheadlights(cuteBot.RGBLights.RGB_L, 255, 255, 0)
        basic.pause(500)
        right.show_color(neopixel.colors(NeoPixelColors.BLACK))
        cuteBot.singleheadlights(cuteBot.RGBLights.RGB_L, 0, 0, 0)
        basic.pause(500)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index2 in range(5):
        left.show_color(neopixel.colors(NeoPixelColors.YELLOW))
        cuteBot.singleheadlights(cuteBot.RGBLights.RGB_R, 255, 255, 0)
        basic.pause(500)
        left.show_color(neopixel.colors(NeoPixelColors.BLACK))
        cuteBot.singleheadlights(cuteBot.RGBLights.RGB_R, 0, 0, 0)
        basic.pause(500)
input.on_button_pressed(Button.B, on_button_pressed_b)

right: neopixel.Strip = None
left: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P15, 2, NeoPixelMode.RGB)
left = left.range(0, 1)
right = right.range(1, 1)