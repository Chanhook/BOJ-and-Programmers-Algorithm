t = int(input())


def check_pseudo_palindrome(p, left, right):
    while left < right:
        if palindrome[left] == palindrome[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def check_palindrome(palindrome):
    left = 0
    right = len(palindrome) - 1

    while left < right:
        if palindrome[left] == palindrome[right]:
            left += 1
            right -= 1
        else:
            if check_pseudo_palindrome(
                palindrome, left + 1, right
            ) or check_pseudo_palindrome(palindrome, left, right - 1):
                return print(1)

            else:
                return print(2)

    return print(0)


for i in range(t):
    palindrome = str(input())
    check_palindrome(palindrome)
