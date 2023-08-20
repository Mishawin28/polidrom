def is_pallindrome(string):
    return string == string[::-1]


print(is_pallindrome('bochka'))