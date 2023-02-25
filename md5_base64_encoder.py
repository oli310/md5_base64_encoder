import sys
import hashlib
import base64
import urllib.parse

if len(sys.argv) < 2:
    print("Usage: python script.py input_file output_file")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
    for line in input_file:
        line = line.strip()
        md5 = hashlib.md5(line.encode()).hexdigest()
        md5_str = md5.encode('ascii')    
        base64_encoded = base64.b64encode(md5_str).decode()
        output_file.write(base64_encoded + '\n')
print("[+]Succesful conversion")