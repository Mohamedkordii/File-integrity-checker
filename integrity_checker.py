import hashlib
import os

def calculate_hash(file_path):
"""Calculate the SHA-256 hash of a file."""
sha256 = hashlib.sha256()

try:
with open(file_path, "rb") as file:
while True:
data = file.read(4096)

if not data:
break

sha256.update(data)

return sha256.hexdigest()

except FileNotFoundError:
return None


def save_hash(file_path, hash_value):
"""Save the original hash for later comparison."""
with open("file_hash.txt", "w") as file:
file.write(hash_value)


def check_integrity(file_path):
"""Check whether the file has been modified."""

current_hash = calculate_hash(file_path)

if current_hash is None:
print("File not found.")
return

if not os.path.exists("file_hash.txt"):
save_hash(file_path, current_hash)
print("Baseline hash created.")
print("SHA-256:", current_hash)
return

with open("file_hash.txt", "r") as file:
original_hash = file.read().strip()

print("Original hash:", original_hash)
print("Current hash: ", current_hash)

if current_hash == original_hash:
print("\n[OK] File integrity verified.")
print("No changes were detected.")
else:
print("\n[WARNING] File integrity check failed!")
print("The file has been modified.")


print("=== File Integrity Checker ===")

file_path = input("Enter the path of the file to check: ")

check_integrity(file_path)
