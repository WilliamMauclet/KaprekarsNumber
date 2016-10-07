# KaprekarsNumber
Little project to learn Python and calculate Kaprekar's numbers for any amount of digits.


Code sample (go to src/ and open the python interpreter): 

```python
>>> from kaprekar import *
>>> demo()
```

... or, more elaborately:

```python
>>> import kaprekar
>>> mapping = kaprekar.createMapping(4)
>>> kaprekar.printMapping(mapping)
>>> kaprekar.drawMapping(mapping)
```

Structure:
<pre>
KaprekarsNumber/
|- src
|    |- kaprekar.py
|    |- prototypemapping.py
|    |- mappingsprinter.py
|    |- treebuilder.py
|    |- treedrawer.py
|
|- README.md
|- LICENSE
</pre>
