#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import re

BASE_API_URL = "https://getnada.com/api/v1"

GET_DOMAINS_URL = BASE_API_URL + "/domains"

GET_INBOX_URL_TEMPLATE = BASE_API_URL + "/inboxes/{}"

GET_EMAIL_URL_TEMPLATE = BASE_API_URL + "/messages/{}"
DELETE_EMAIL_URL_TEMPLATE = BASE_API_URL + "/messages/{}"

class Pynada():
    """Main class for Pynada."""
    def __init__(self):
        self.domain_names = None
        self.inboxes = None

    def get_domains(self):
        if self.domain_names == None:
            r = requests.get(GET_DOMAINS_URL)
            if r.status_code != 200:
                raise ValueError("Can't get domains")
            self.domain_names = [item["name"] for item in r.json()]
        return self.domain_names

    def is_valid_email(self, email):
        return email[email.find("@")+1:] in self.get_domains()

    def inbox(self, email):
        if self.inboxes != None:
            for ibx in self.inboxes:
                if ibx.email == email:
                    return ibx
        else:
            self.inboxes = []

        new_ibx = PynadaInbox(email)
        self.inboxes.append(new_ibx)

        return new_ibx

class PynadaInbox(object):
    """Inbox for an email address for PynadaInbox."""
    def __init__(self, email):
        self.inbox_email = email
        self.emails = None

    def get_emails(self):
        if self.emails == None:
            self.emails = []
            r = requests.get(
                GET_INBOX_URL_TEMPLATE.format(self.inbox_email))
            if r.status_code != 200:
                raise ValueError("Can't get inbox {}".format(self.inbox_email))

            for email in r.json()["msgs"]:
                self.emails.append(
                    PynadaEmail(
                        email['uid'],
                        email['f'],
                        email['fe'],
                        email['s'],
                        email['r']))

        return self.emails

class PynadaEmail(object):
    """Email for PynadaEmail."""
    def __init__(self, uid, from_name,
            from_email, subject, timestamp):
        self.uid = uid
        self.from_name = from_name
        self.from_email = from_email
        self.subject = subject
        self.timestamp = timestamp
        self.contents = None

    def get_contents(self):
        if self.contents == None:
            r = requests.get(
                GET_EMAIL_URL_TEMPLATE.format(self.uid))
            if r.status_code != 200:
                raise ValueError("Can't get email contents : {}".format(self.uid))

            self.contents = r.json()['html']

        return self.contents

    def delete(self):
        r = requests.delete(
            DELETE_EMAIL_URL_TEMPLATE.format(self.uid))
        print r.text
        print r.status_code
        if r.status_code != 201:
            raise ValueError("Couldn't delete email : {}".format(self.uid))

def main():
    emails = Pynada().inbox("test@getnada.com").get_emails()

    # contents = emails[0].get_contents()

    # find instagram confirmation_email
    # contents = re.search("https://instagram.com/accounts/confirm_email/[^\"]+", contents).group()
    # contents = contents.replace("&amp;", "&")
    # print contents

    # delete all emails in inbox
    # for email in emails:
    #     email.delete()

if __name__ == '__main__':
    main()
