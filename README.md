# imessage

Script to send imessages.

## Usage

### Send imessage from MacOS terminal

```bash
python3 /path/to/send.py -phone 1234567890 -message "Some message"

# further simplified
alias sendMom="python3 /path/to/send.py -phone 1234567890 -message"
sendMom "hello"
```

### Send imessage through remote MacOs server

```bash
python3 /path/to/ssh-send.py -password somepassword -host user@host -location /path/to/send.py -phone 1234567890 -message "Some message"

# further simplified
alias sendMom="python3 /path/to/ssh-send.py -password somepassword -host user@host -location /path/to/send.py -phone 1234567890 -message"
sendMom "hello"
```
