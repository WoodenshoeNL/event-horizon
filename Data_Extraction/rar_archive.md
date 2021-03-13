# Crack RAR archive

## Get Hash from Rar file

```bash
rar2john archive.rar > hash
```

## Crack hash with john the ripper

```bash
john --wordlist=1000000-password-seclists.txt hash
```

## Convert hash file to hashcat format

$rar5$16$50d889a2c6441510dd0c8ab76dde4fd6$15$697757daca178f6f88135491827bdad6$8$e13f0c4d2f8286d5

## Crack hash with hashcat

```bash
hashcat -m 13000 hash -a 0 1000000-password-seclists.txt
```

Explanation
-m 13000 : RAR format
-a 0 : Dictionary mode
