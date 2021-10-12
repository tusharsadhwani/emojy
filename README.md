# emojy

Write Python with emojis!

Inspired by [this tweet][1], so blame Paul, not us.

## Installation / Usage

```console
$ pip install emojy
[...]
Successfully installed emojy.
$ cat code.emojy
📺('Hello 👋!')
$ emojy code.emojy
Hello 👋!
```

## Examples

Code:

```python
📺('✅' if 👍 👐 👎 else '❌')
```

Output:

```python
✅
```

---

Code:

```python
🤞:
    👍/👎
💣:
    📺('Boom💥')
```

Output:

```python
Boom💥
```

[1]: https://twitter.com/ptmcguire/status/1447588788465815557
