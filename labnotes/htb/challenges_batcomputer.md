
Python pwn script for [batcomputer](/labnotes/htb/scripts/ch-batcomputer.py)

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
