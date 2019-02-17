#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from pynada import Pynada

nada = Pynada()
my_email = "my_email@getnada.com"
for email in nada.inbox(my_email).get_emails():
    # if the email contains the keyword "butterfly", delete it
    if "butterfly" in email.get_contents():
        email.delete()
