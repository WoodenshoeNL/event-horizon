
## install gdb peda framework

```bash
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit
```

## Create pattern with Peda

```bash
gdb-peda$ pattern arg 100
Set 1 arguments to program
gdb-peda$ r
Starting program: /home/htb-woodenshoe/htb/rop 'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL'

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x79 ('y')
EBX: 0xffffd1c0 --> 0x2
ECX: 0x0
EDX: 0x5f ('_')
ESI: 0xf7fb3000 --> 0x1e4d6c
EDI: 0xf7fb3000 --> 0x1e4d6c
EBP: 0x31414162 ('bAA1')
ESP: 0xffffd190 ("AcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
EIP: 0x41474141 ('AAGA')
EFLAGS: 0x10286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x41474141
[------------------------------------stack-------------------------------------]
0000| 0xffffd190 ("AcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0004| 0xffffd194 ("2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0008| 0xffffd198 ("AAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0012| 0xffffd19c ("A3AAIAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0016| 0xffffd1a0 ("IAAeAA4AAJAAfAA5AAKAAgAA6AAL")
0020| 0xffffd1a4 ("AA4AAJAAfAA5AAKAAgAA6AAL")
0024| 0xffffd1a8 ("AJAAfAA5AAKAAgAA6AAL")
0028| 0xffffd1ac ("fAA5AAKAAgAA6AAL")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x41474141 in ?? ()
gdb-peda$ pattern search 0x41474141
Registers contain pattern buffer:
EBP+0 found at offset: 48
EIP+0 found at offset: 52
Registers point to pattern buffer:
[ESP] --> offset 56 - size ~44
Pattern buffer found at:
0x0804b1cc : offset    5 - size   95 ([heap])
0xffffd158 : offset    0 - size  100 ($sp + -0x38 [-14 dwords])
0xffffd405 : offset    0 - size  100 ($sp + 0x275 [157 dwords])
References to pattern buffer found at:
0xffffcbc0 : 0x0804b1cc ($sp + -0x5d0 [-372 dwords])
0xffffcca8 : 0xffffd158 ($sp + -0x4e8 [-314 dwords])
0xffffd124 : 0xffffd158 ($sp + -0x6c [-27 dwords])
0xffffd130 : 0xffffd158 ($sp + -0x60 [-24 dwords])
0xffffd140 : 0xffffd158 ($sp + -0x50 [-20 dwords])
0xffffcb10 : 0xffffd405 ($sp + -0x680 [-416 dwords])
0xffffccc0 : 0xffffd405 ($sp + -0x4d0 [-308 dwords])
0xffffd144 : 0xffffd405 ($sp + -0x4c [-19 dwords])
0xffffd268 : 0xffffd405 ($sp + 0xd8 [54 dwords])
gdb-peda$
```
