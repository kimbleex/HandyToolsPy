# How to use?

## Calculate the frequency of words

```python
from HandyToolsPy import DataProcess as dp

words = ["a","a","a","a","b","b","c"]
res = dp.count_words_freq(words)
print(res)
```

output:

```text
{'a': 4, 'b': 2, 'c': 1}
```

It also support csv file (`DataFrame` format):

Here is a csv file named `sample.csv`:

```csv
hello
world
haha
haha
hello
hello
```

the code will be:

```python
import HandyToolsPy.DataProcess as dp
import pandas as pd

words = pd.read_csv('./sample.csv', names=["word"])
res = dp.count_words_freq(words["word"])
print(res)
```

output:

```text
{'hello': 3, 'haha': 2, 'world': 1}
```

## A Translator

It can automaticly detect the language of the input text and translate it to the target language.

```python
from HandyToolsPy import translator

text = "你好"
res = Translator(text, "en")
print(res)
```

output:

```bash
'Hello'
```

## A Drawer

It can draw a BingDunDun.

```python
from HandyToolsPy import Draw as dw

dw.draw_BingDunDun(10)
```
