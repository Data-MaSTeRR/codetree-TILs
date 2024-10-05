s = input()

def check_palindrome(s):

    reverse = s[::-1]

    if s == reverse:
        return "Yes"
    else:
        return "No"

print(check_palindrome(s))