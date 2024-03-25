

# Special methods 

## `__repr__()` magic method

> **Python __repr__()** is one of the **magic methods** that returns a printable representation of an [object](https://www.geeksforgeeks.org/object-oriented-programming-in-python-set-1-class-and-its-members/) in [Python](https://www.geeksforgeeks.org/python-programming-language/) that can be customized or predefined, i.e. we can also create the string representation of the object according to our needs.

* Exmaple: venv\Lib\site-packages\pscript\stubs.py

  ```python
  class RawJS:    
      def __init__(self, code, _resolve_defining_module=True):
          if not isinstance(code, str):
              raise TypeError('RawJS requires str input.')
          self._lines = self._str2lines(code)
          
          # Get the globals of the module in which this instance is defined, so
          # that we can set __module__ and later obtain the name by which this 
          # instance is known in that module. We use a trick here to get access
          # to the stack frame while avoiding sys._getframe().
          try:
              raise Exception()
          except Exception as err:
              tb = getattr(err, '__traceback__', None)
              if tb is None:  # Legacy Python 2.x
                  import sys
                  _, _, tb = sys.exc_info()
              self._globals = tb.tb_frame.f_back.f_globals
              del tb
          self.__module__ = self._globals['__name__']
          self._real_name = None
      
      def __repr__(self):
          if len(self._lines) == 1 and len(self._lines[0]) < 60:
              return '<%s "%s">' % (self.__class__.__name__, self.get_code(0))
          else:
              return '<%s with %i lines>' % (self.__class__.__name__, len(self._lines))
      
      def __str__(self):
          return self.get_code(0)
  ```

In short[^1]
* `.__repr__()` provides the **official string representation** of an object, aimed at the programmer.

* `.__str__()` provides the **informal string representation** of an object, aimed at the user.





[^1]: Real Python [When Should You Use .__repr__() vs .__str__() in Python?](https://realpython.com/python-repr-vs-str/#in-short-use-__repr__-for-programmers-vs-__str__-for-users)