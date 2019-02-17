# Pynada - getnada.com Unofficial API

Pynada is an unofficial [getnada.com](https://getnada.com/) API documentation and python wrapper.

NOTE: The API was reverse engineered and is therefore subject to change and break without notice. (Scroll down to see the endpoints etc.)

# Python Wrapper Usage

## Get available domains

```python

from pynada import Pynada

nada = Pynada()
print nada.get_domains() # returns a list of all available domains
```

## Check if email is valid
```python
from pynada import Pynada

nada = Pynada()
test_email = "someoddemail@getnada.com"
if nada.is_valid_email(test_email):
    print "{} is valid!".format(test_email)
```

## Get emails from inbox
```python
from pynada import Pynada

nada = Pynada()
my_email = "my_email@getnada.com"
for email in nada.inbox(my_email).get_emails():
    print email.from_name
    print email.from_email
    print email.subject
    print email.timestamp
    print email.get_contents()
```

## Delete email
```python
from pynada import Pynada

nada = Pynada()
my_email = "my_email@getnada.com"
for email in nada.inbox(my_email).get_emails():
    # if the email contains the keyword
    if "Instagram" in email.get_contents():
        email.delete()
```


# About getnada.com

"nada is a free temporary email service, you are given a random email address or you can choose one you like, and you can use it when registering to new websites or test-driving untrusted services which require an email for login.

nada is operated by Oron Ogdan-Adam (@oronoa). This is another weekend project that blew out of proportion :-) I chose the name - nada (means nothing in Spanish) to describe the nature of the service, all incoming emails are deleted and turn into nothing after they expire. Instead of filling up your precious real inbox. It's the best spam trap ever."


# API

* base_url : https://getnada.com/api/v1

----

## [GET] /domains

Returns a list of all possible email domains

Response:
- \_id : Domain id
- name : Domain name
- keep : 1 if domain will always be available, 0 if domain might be deleted

Example:
`[{"_id":"1","name":"getnada.com"},{"_id":"5c2e3ad6c08a59d11f3292bc","name":"nada.ltd","keep":"0"},{"_id":"5c2e3ad8c08a59d11f3292d3","name":"tempmail.space","keep":"0"} [...] ]`

`curl https://getnada.com/api/v1/domains`

----

## [GET] /inboxes/<email>

- <email> must be of the form <username>@<valid domain> where <valid domain> is a domain returned from /domains

Returns a list of email metadata from the specified inbox


`curl https://getnada.com/api/v1/inboxes/test@getnada.com`

----

## [GET] /messages/<email uid>

- <email uid> is <uid> returned from /inboxes/<email>

Returns the email contents and metadata

----

## [DELETE] /messages/<email uid>

- <email uid> is <uid> returned from /inboxes/<email>

Deletes the specified email
