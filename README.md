# How to use?

## Calculate the frequency of words

```python
import HandyToolsPy.DataProcess as dp

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
import HandyToolsPy.Translator as tr

text = "你好"
res = tr.translate_text(text, "en")
print(res)
```

output:

```bash
'Hello'
```
