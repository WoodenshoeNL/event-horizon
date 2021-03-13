# Using TMUX

TMUX Commands:
* [Sessions](https://github.com/WoodenshoeNL/event-horizon/blob/main/linux/tmux.md#sessions)
* [Windows](https://github.com/WoodenshoeNL/event-horizon/blob/main/linux/tmux.md#windows)
* [Panes](https://github.com/WoodenshoeNL/event-horizon/blob/main/linux/tmux.md#panes)
  
## Install TMUX

```bash
apt-get install tmux
```

## TMUX commands

### Sessions

#### New Session

```bash
tmux
tmux new
tmux new -s sessionname
```

#### Rename Session

```bash
Ctrl + b - $
```

#### Detach Session

```bash
Ctrl + b - D
```

#### Attach session

```bash
tmux a -s sessionname
```

### Windows

#### Create window

```bash
Ctrl + b - c
```

#### Move to next Window

```bash
Ctrl + b - n
```

#### Move to Previous Window

```bash
Ctrl + b - p
```

#### Move to Last Used Window

```bash
Ctrl + b - l
```

#### Move to Window [Number]

```bash
Ctrl + b - 0
Ctrl + b - 1
```

#### List Windows

```bash
Ctrl + b - W
```

#### Kill Window

```bash
Ctrl + b - &
```

#### Rename Window

```bash
Ctrl + b - ,
```

### Panes

#### Split vertically

```bash
Ctrl + b - %
```

#### Split horizontally

```bash
Ctrl + b - “
```

#### Move to pane to the right

```bash
Ctrl + b - <right arrow>
```

#### Move to pane to the left

```bash
Ctrl + b - <left arrow>
```

#### Move to pane above

```bash
Ctrl + b - <up arrow>
```

#### Move to pane below

```bash
Ctrl + b - <down arrow>
```

#### Move pane to the right

```bash
Ctrl + b - }
```

#### Move pane to the left

```bash
Ctrl + b - {
```

#### Convert Pane to window

```bash
Ctrl + b - !
```

#### Kill Pane

```bash
Ctrl + b - X
```
