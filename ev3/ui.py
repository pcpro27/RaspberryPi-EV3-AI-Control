from ev3dev2.display import Display
from ev3dev2.button import Button

display = Display()
btn = Button()

display.text_pixels("Appuyez pour", 10, 10, font="small")
display.text_pixels("connecter", 10, 30, font="small")
btn.wait_for_pressed("center")
display.text_pixels("Connecté !", 10, 50, font="small")