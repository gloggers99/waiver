# waiver

[![forthebadge](https://forthebadge.com/images/badges/designed-in-etch-a-sketch.svg)](https://forthebadge.com)

## usage

As long as you have python (preferrably 3.1X) and flask (`pip install flask`) installed, and you have followed the email routing setup below, all you need to do is run the following command in the same directory as `app.py`: `flask run`. for debug mode, just run the command with the `--debug` flag appended. ex: `flask run --debug`

## dependencies

- python 3.1X
- flask (for webserver)
- dominate (for python html)
- dotenv (loading up .env file)

quick install:

`pip3 install flask dominate python-dotenv`

## email routing setup

Waiver routes responses to an admin provided email. In order to provide this email, you will need to either:

- Create an environment variable for each configurable variable: `export VARIABLE=blah`
- Create a .env file in the SAME directory as waiver. ex:  
```bash
EMAIL_SERVER=your.email.server.com
# the port is 465 by default, this option will be configurable in the future

BOT_ADDRESS=asdf@your.email.server.com
BOT_PASSWORD=password12345

RECIPIENT_ADDRESS=recipient@your.email.server.com
```

## features

- [X] basic "waiver"/"form" viewing and responding
- [X] the ability to create forms using a simple JSON file
- [X] SSL encrypted email routing for form responses
- [ ] input sanitization (top of priorities)
- [ ] interface to create forms
- [ ] right & wrong (test like forms)
- [ ] other forms of response routing

## use cases

Waiver is meant to have absolutely zero hardcoding, therefore it is highly customizable and dynamic. Here are some example use cases
if you think you might want to try out waiver as your form/test/submission solution:

- signup forms (what I personally use waiver for.)
- testing (right and wrong & answers will be added as a feature to waiver in the future)
- reviews
- probably anything google forms does?
