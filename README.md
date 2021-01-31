# Joystick Test Script

The joystick.py dumps inputs of joystick's buttons, analog levers, and + leaf keys with using pygame.

## Install required tools for Mac

    ./prepare_mac.sh

## Test Joystick

    python3 joystick.py

An execution example is below. The 0 is for no-input, 1 is for pushed, and the decimal velues from -1 to 1 are for analog stick values.

    pygame 2.0.1 (SDL 2.0.14, Python 3.9.0)
    Hello from the pygame community. https://www.pygame.org/contribute.html
    Joystick Name: Logicool Cordless RumblePad 2
    Number of Button : 12
    Number of Axis : 4
    Number of Hats : 1
    Btn[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  Axe[0.0, -0.0, 0.0, -0.0]  Hat[(0, 0)]
    Btn[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  Axe[0.0, -0.0, 0.0, -0.0]  Hat[(0, 0)]
    Btn[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  Axe[0.0, -0.0, 0.0, -0.0]  Hat[(0, 0)]
    Btn[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  Axe[0.0, -0.0, 0.0, -0.0]  Hat[(0, 0)]
    Btn[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  Axe[-0.58, -1.0, 0.68, 1.0]  Hat[(0, 0)]
    Btn[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  Axe[-1.0, -0.0, 0.64, 0.57]  Hat[(0, 0)]
    Btn[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  Axe[-1.0, 0.51, 0.0, -0.0]  Hat[(0, 0)]
    Btn[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  Axe[0.0, -0.0, 0.0, -0.0]  Hat[(-1, -1)]

