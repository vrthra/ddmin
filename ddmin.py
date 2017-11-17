import random
import string

random.seed(0)
def test(s):
    print("%s %d" % (s, len(s)))
    return set('()') <= set(s)

def complement(s, i, l):
    return s[:i] + s[i + l:]

def some_complement_is_failing(s, n, testfn):
    subset_length = len(s) // n
    items = range(0,len(s), subset_length)
    complements = (complement(s, i, subset_length) for i in items)
    return next((i for i in complements if testfn(i)), None)


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

