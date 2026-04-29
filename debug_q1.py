
import re

file_path = "/home/0xjb/Documents/my-knowledge-base/securityplus-questions.md"

# Re-reading original state is not possible since I overwrote it. 
# I will assume the current state has the right content but needs better extraction.
# Actually, I should probably ask the user to revert one more time if I messed up Question 1 text.
# Let's check Question 1 again.
with open(file_path, "r") as f:
    current_lines = f.readlines()

print("".join(current_lines[:15]))
