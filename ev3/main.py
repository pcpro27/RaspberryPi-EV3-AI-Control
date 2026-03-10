#!/usr/bin/env python3
from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C
from ev3dev2.bluetooth import BluetoothMailbox
import time

# Initialiser les moteurs
tank = MoveTank(OUTPUT_B, OUTPUT_C)

# Connexion Bluetooth
mb = BluetoothMailbox("server")
mb.wait()

print("EV3 prêt à recevoir des commandes !")

while True:
    if mb.is_empty():
        time.sleep(0.1)
        continue
    command = mb.read()
    print(f"Commande reçue : {command}")

    # Interpréter les commandes
    if command.startswith("MOVE:"):
        direction, speed = command.split(":")[1], int(command.split(":")[2])
        if direction == "FORWARD":
            tank.on(speed, speed)
        elif direction == "BACKWARD":
            tank.on(-speed, -speed)
    elif command.startswith("TURN:"):
        side, angle = command.split(":")[1], int(command.split(":")[2])
        if side == "LEFT":
            tank.on_for_degrees(-speed, speed, angle * 2)
        elif side == "RIGHT":
            tank.on_for_degrees(speed, -speed, angle * 2)
    elif command == "STOP":
        tank.off()