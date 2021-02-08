#!/usr/local/bin/python3
import subprocess
import argparse

parser = argparse.ArgumentParser(
    description='Send a message to a phone number using imessage.')
parser.add_argument(
    "-phone", help="The phone number of the recipient.", required=True)
parser.add_argument("-message", help="The message to send.", required=True)
args = parser.parse_args()

if args.phone and args.message:
    subprocess.run(
        ["osascript", "sendMessage.applescript", args.phone, args.message])
