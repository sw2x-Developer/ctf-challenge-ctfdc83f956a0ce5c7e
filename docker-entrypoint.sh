#!/bin/bash
exec socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 /app/main.py",pty,echo=0

