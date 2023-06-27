#!/bin/bash

# Check for internet connection
if ping -q -c 1 -W 1 google.com >/dev/null; then
    # Internet connection is available, execute the task script
    python3 login.py
fi
