# Cracking pkzip archive

## extract has from pkzip file

```bash
zip2john archive.zip > hash
```

## crack hash with john the ripper

```bash
john --wordlist=1000000-password-seclists.txt hash
```
