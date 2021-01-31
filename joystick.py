# Copyright (c) 2021 Takenoshin
# Released under the MIT license
# https://opensource.org/licenses/mit-license.php

import time
from decimal import Decimal
import pygame

def main():
    pygame.init()
    joy = pygame.joystick.Joystick(0)
    joy.init()
    try:
        n_btn = joy.get_numbuttons()
        n_axe = joy.get_numaxes()
        n_hat = joy.get_numhats()
        print("Joystick Name: " + joy.get_name())
        print("Number of Button : " + str(n_btn))
        print("Number of Axis : " + str(n_axe))
        print("Number of Hats : " + str(n_hat))

        pygame.event.get()
        s_btn = [0] * n_btn
        s_axe = [0.0] * n_axe
        s_hat = [0] * n_hat
        while True:
            # Buttons
            for i in range(n_btn):
                s_btn[i] = joy.get_button(i)
            # Axes
            for i in range(n_axe):
                #s_axe[i] = round(joy.get_axis(i), 2)
                s_axe[i] = float(Decimal(joy.get_axis(i)).quantize(Decimal('0.01')))
            # Hats
            for i in range(n_hat):
                s_hat[i] = joy.get_hat(i)

            print("Btn", end="")
            print(s_btn, end="")
            print("  Axe", end="")
            print(s_axe, end="")
            print("  Hat", end="")
            print(s_hat)
            #pygame.event.pump()
            pygame.event.get()

            time.sleep(0.1)
    except( KeyboardInterrupt, SystemExit): # Exit with Ctrl-C
        print("Exit")

if __name__ == "__main__":
    main()
