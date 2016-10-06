# KaprekarsNumber
Little project to learn Python and calculate Kaprekar's numbers for any amount of digits.


Code sample: 
```python
>>> import kaprekar
>>> mapping = kaprekar.createFirstMapping(4)
>>> mapping.performMapping()
>>> kaprekar.printMapping(mapping)
>>> kaprekar.drawMapping(mapping)
```

... or, more simply:

```python
>>> from kaprekar import *
>>> demo()
```

Structure:
<pre>
KaprekarsNumber/
|- src
|    |- kaprekar.py
|    |- prototypemapping.py
|
|- README.md
|- LICENSE
</pre>
