

## Replace with regex(newline for space):
```bash
:%s/\n/ /g
```


## OS actions from within VIM
open file from command mode
```bash
:r [path]
```

run bash from command mode
```bash
:!/bin/bash
```



## Record and use a Macro:
Start recording:
```bash
q a
```
Do macro stuff:
```bash
<i>
https://<downArrow><Home>
<esc>
<q>
```

Use Macro:
```bash
@a
```

