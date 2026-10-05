# File Integrity Checker

A Python-based cybersecurity tool that uses SHA-256 hashing to detect unauthorized modifications to files.

## Features

- Calculates the SHA-256 hash of a file
- Creates a baseline hash for integrity verification
- Stores the original hash for future comparisons
- Detects whether a file has been modified
- Displays the original and current hashes
- Provides clear integrity verification and warning messages
- Uses Python's built-in `hashlib` library

## How It Works

The program calculates a unique SHA-256 hash for the selected file.

When the file is checked for the first time, the program saves its hash as a baseline in `file_hash.txt`.

During future checks, the program calculates the file's current hash and compares it with the saved baseline.

If the hashes match, the file has not changed.

If the hashes are different, the program warns that the file has been modified.

## Requirements

- Python 3.x
- No external libraries required

## How to Run

Clone the repository:

git clone https://github.com/Mohamedkordii/File-integrity-checker.git

Navigate to the project directory:

cd File-integrity-checker

Run the program:

python integrity_checker.py

Then enter the path of the file you want to monitor.

## Example

First check:

File Integrity Checker 
Enter the path of the file to check: test.txt
Baseline hash created.

After modifying the file:

=== File Integrity Checker ===
Enter the path of the file to check: test.txt
[WARNING] File integrity check failed!
The file has been modified.

## Cybersecurity Concept

File integrity monitoring is used to detect unexpected or unauthorized modifications to important files.

Hashing algorithms such as SHA-256 generate a fingerprint of a file. Even a small modification to the file produces a different hash, allowing changes to be detected.

## Ethical Use

This project was created for educational and cybersecurity learning purposes.

## Author

Mohamed Kordi
Cybersecurity Engineering Student
University of Sharjah
