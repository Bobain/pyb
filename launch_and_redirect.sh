#!/usr/bin/env bash
/home/tonigor/py3/bin/python3.4 ./manage.py & > out.txt
tails -f out.txt