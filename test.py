### =================
### Mocking functions
### =================

# 1. Installation
# ~~~~~~~~~~~~~~~

from unittest import mock  # Python 3.3+
import mock  # backport, necessary to run pip install mock

# Universal import
try:
    from unittest import mock
except ImportError:
    import mock

# 2. Essentials
# ~~~~~~~~~~~~~

m = mock.Mock()
m.return_value = 42
print(m(84, foo=3))  # ==> 42
m.assert_called_once_with(84, foo=3)
assert m.call_args == mock.call(84, foo=3)

# 3. Raising exceptions
# ~~~~~~~~~~~~~~~~~~~~~

m = mock.Mock()
m.side_effect = KeyError
# print(m())  # ==> KeyError

# 4. Returning Multiple Values
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

m = mock.Mock()
m.side_effect = [1, 2, KeyError, 3]
print(m())  # ==> 1
print(m())  # ==> 2
# print(m())  # ==> KeyError

### 5. Mocking with Lambda

# The following code ...

m = mock.Mock()
m.side_effect = lambda x: x+2
print(m(5))  # ==> 7

# ... is equivalent to:

def my_lambda(x):
    return x + 2

m = mock.Mock()
m.side_effect = my_lambda
print(m(5))

### 6. Assertions

m = mock.Mock()
m(10)
m(20)
m.assert_called_with(20)
# m.assert_called_once_with(20)  # ==> AssertionError
m.assert_any_call(10)
# m.assert_not_called()  # ==> AssertionError

### 7. Other Notable Attributes

m = mock.Mock()
m(5)
m(7)
print(m.called)  # ==> True
print(m.call_count)  # ==> 2
print(m.call_args)  # ==> call(7)
print(m.call_args_list)  # ==> [call(5), call(7)]
assert m.call_args_list == [
    mock.call(5),
    mock.call(7),
]
