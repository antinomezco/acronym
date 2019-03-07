import re

def abbreviate(words):
    words = re.split(r'[^a-zA-Z\']', words)
    return ''.join([i[0].upper() for i in words if i])