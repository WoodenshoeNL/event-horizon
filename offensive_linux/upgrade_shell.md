# Upgrade the Shell

## Upgrade shell - 01

```bash
SHELL=/bin/bash script -q /dev/null
Ctrl-Z
stty raw -echo
fg
reset
xterm
```

## Upgrade Shell with script command

```bash
/usr/bin/script -qc /bin/bash /dev/null
```

## upgrade shell with python

```bash
python3 -c "import pty;pty.spawn('/bin/bash')"

python -c "import pty;pty.spawn('/bin/bash')"
```

## Get tab completion to work

```bash
ctrl + Z
stty raw -echo
fg <enter>
<enter>
```
