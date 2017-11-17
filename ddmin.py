import random
import string
def test(s):
    print("%s %d" % (s, len(s)))
    return set('()') <= set(s)

def some_complement_is_failing(s, n, testfn):
    start = 0
    subset_length = len(s) // n
    while start < len(s):
        complement = s[:start] + s[start + subset_length:]
        if testfn(complement): return complement
        start += subset_length
    return None


def ddmin(s, fn):
    n = 2
    while len(s) >= 2:
        v = some_complement_is_failing(s, n, fn)
        if v:
            n = max(n - 1, 2)
            s = v
        else:
            if n == len(s): break
            n = min(n * 2, len(s))
    return s

def fuzzer(): return ''.join(random.choices(string.digits + string.ascii_letters + string.punctuation, k=1024))

mystr = fuzzer()
minimized = ddmin(mystr, test)
print("%s => %s" % (mystr, minimized))

