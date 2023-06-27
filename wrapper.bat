@echo off
ping 8.8.8.8 -n 1 > nul

if errorlevel 0 (
    python renewer.py
)