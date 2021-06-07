# Grep

## grep key from /dev/sdb device

```bash
grep -a '[a-z0-9]\{32\}' /dev/sdb
```

## grep text inclusief 2 lines before and 3 lines after

```bash
grep -a -A3 -B2 '[a-z0-9]\{32\}' /dev/sdb
```
