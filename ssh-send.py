#!/usr/bin/python3
import os
import subprocess
import argparse

parser = argparse.ArgumentParser(
    description='Send a message to a phone number using imessage.')
parser.add_argument(
    "-phone", help="The phone number of the recipient.", required=True)
parser.add_argument("-message", help="The message to send.", required=True)
parser.add_argument("-host", help="The host to connect to.", required=True)
parser.add_argument(
    "-password", help="The password of the host computer.", required=True)
parser.add_argument(
    "-location", help="The full path to the imessage/send.py file.", required=True)

args = parser.parse_args()

os.system(
    f'sshpass -p {args.password} ssh {args.host} python3 {args.location} -phone {args.phone} -message \\"{args.message}\\"')
