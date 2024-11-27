# How to use?

## 1. Data Process

### 1.1 Calculate the frequency of words

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
from HandyToolsPy import DataProcess as dp
import pandas as pd

words = pd.read_csv('./sample.csv', names=["word"])
res = dp.count_words_freq(words["word"])
print(res)
```

output:

```text
{'hello': 3, 'haha': 2, 'world': 1}
```

## 2. A Translator

It can automaticly detect the language of the input text and translate it to the target language.

```python
from HandyToolsPy import translator

text = "你好"
res = translator(text, "en")
print(res)
```

output:

```bash
'Hello'
```

## 3. A Drawer

It can draw a BingDunDun.

```python
from HandyToolsPy import Draw as dw

dw.draw_BingDunDun(10)
```

## 4. A Dir Tree Generator

It can generate a dir tree.

```python
from HandyToolsPy import dir_tree

path = "Sample Path"
dir_tree(path)
```

output:

```text
D:/Sample/
├── sample.exe
└── xxx
    ├── hhh
    ├── hhh.zip
    ├── xh.bmp
    ├── xxx.pptx
    └── xxx.txt
```
