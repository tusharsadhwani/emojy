# emojy

Write Python with emojis!

Inspired by [this tweet][1], so blame Paul, not us.

## Installation / Usage

```console
$ pip install emojy
[...]
Successfully installed emojy.
$ cat code.emojy
ðº('Hello ð!')
$ emojy code.emojy
Hello ð!
```

## Examples

Code:

```python
ðº('â' if ð ð ð else 'â')
```

Output:

```python
â
```

---

Code:

```python
ð¤:
    ð/ð
ð£:
    ðº('Boomð¥')
```

Output:

```python
Boomð¥
```

[1]: https://twitter.com/ptmcguire/status/1447588788465815557
