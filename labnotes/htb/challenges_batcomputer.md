
Python pwn script for [batcomputer](https://github.com/WoodenshoeNL/black-badge/blob/master/htb/challenges/ch-batcomputer.py)

Python remote pwn script for [batcomputer](https://github.com/WoodenshoeNL/black-badge/blob/master/htb/challenges/ch-batcomputer-remote.py)

Check file type:
```bash
file batcomputer
```

Check Security settings executable:
```bash
checksec batcomputer
```

Create cyclic string with:
```bash
from pwn import *
cyclic(137)
```

Find offset with cyclic find:
```bash
cyclic_find('vaaa')
```
