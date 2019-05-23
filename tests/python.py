# Comment

import module as othername
from package import submodule

@decorator
class Class(object):
    """Doc-string"""

    def __init__(self, value):
        self.var = value

    def method(self):
        pass

# type: (int) -> Type
@property
async def function(param: int) -> Type:
    '''Doc-string'''
    global name
    nonlocal name

    return Ellipsis
    return None
    return NotImplemented
    yield value from other

assert cond
await awaitable
del name

Class.__init__(val)

"string"
'string'
b"byte string"
b'byte string'
f"f-string"
f'f-string'
r"raw string {}"
r'raw string'
u"unicode string"
u'unicode string'

"\n"

0
0o0
0x0
0.0
0.0j

var + value
var - value
var * value
var / value
var // value
var % value
var ** value
var | value
var << value
var >> value
var & value
var ^ value
var ~ value
var @ value

var = value
var += value
var -= value
var *= value
var /= value
var //= value
var %= value
var **= value
var |= value
var <<= value
var >>= value
var &= value
var ^= value
var ~= value
var @= value

var and var
var or var
not var
var in collection
var is value

var == value
var != value
var < value
var <= value
var > value
var >= value

lambda param: param

if True:
    print("true")
elif False:
    print("false")
else:
    raise Error("language is broken!")

try:
    function()
except Exception as exc:
    print("exception!")
finally:
    print("done")

while cond:
    break

for i in iter:
    continue

with context as ctx:
    print("received context")

error++
