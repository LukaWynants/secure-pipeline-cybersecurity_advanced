print("Hello World!")

# Vulnerability: Insecure hashing algorithm
import hashlib
hash = hashlib.md5(b"password").hexdigest()  # MD5 is weak