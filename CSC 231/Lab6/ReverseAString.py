__author__ = 'guinnc'

def reverse(s):
    if len(s) == 0:
        return s
    if len(s) == 1:
        return s

    return reverse(s[1:]) + s[0]

print(reverse("UNCW Seahawks"))
