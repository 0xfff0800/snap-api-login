## Reverse engineered Snapchat gRPC login protobuf tool 🛠
Researched and built by 0xfff0800 (FaLaH) — https://t.me/xfff0800


Description
-----------

This tool decodes a captured Snapchat gRPC login request (protobuf binary),
allows you to modify the username and password fields, re-encodes it back
to base64, and sends it to the Snapchat login endpoint.

It was built for educational and security research purposes to understand
how Snapchat encodes login credentials using Protocol Buffers over gRPC.


Requirements
------------

    pip install blackboxprotobuf requests


Files
-----

    hex.py    — Decode, modify, and re-encode the protobuf payload
    login.py  — Send the payload to the Snapchat gRPC login endpoint


How to Use
----------

Step 1 : Open hex.py
Step 2 : Find the following two lines and set your values:

    decoded['1'] = b'USERNAME'
    decoded['4'] = b'PASSWORD'

Step 3 : Run:

    python3 hex.py

Step 4 : Copy the output printed after [NEW BASE64 READY TO COPY]

Step 5 : Open login.py and paste the copied value inside:

    PAYLOAD_B64 = "PASTE_HERE"

Step 6 : Run:

    python3 login.py

Step 7 : Read the response status code printed in the terminal.


Legal Disclaimer
----------------

This tool is provided for EDUCATIONAL and SECURITY RESEARCH purposes ONLY.

- Do NOT use this tool against accounts you do not own.
- Do NOT use this tool to access systems without explicit written permission
  from the owner.
- Unauthorized access to computer systems is a criminal offense under
  applicable law (CFAA, CMA, and local equivalents).
- The author holds NO responsibility for any misuse, damage, or legal
  consequences resulting from the use of this tool.
- By using this tool, you agree that you are solely responsible for your
  own actions.


Author
------

0xfff0800 / FaLaH
Telegram : https://t.me/xfff0800
