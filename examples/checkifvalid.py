#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pynada import Pynada

nada = Pynada()
test_email = "someoddemail@getnada.com"
if nada.is_valid_email(test_email):
    print "{} is valid!".format(test_email)
