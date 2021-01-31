#!/bin/sh

# pip
which pip > /dev/null 2>&1
if [ $? -ne 0 ]; then
    # curl
    which curl > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        # brew
        which brew > /dev/null 2>&1
        if [ $? -ne 0 ]; then
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        brew install curl
    fi
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py
fi

python3 -m pip install -U pygame --user
