# Process

## Tracing processes with strace and ltrace

ltrace shows parameters of invoked functions and system calls.
The strace command can be used to intercept and record the system calls made, and the signals received by a process.

get sys calls with ltrace:

```bash
ltrace ./executable
```

## Get the current working directory from process by ID

```bash
ls -la /proc/<pid> | grep cwd
```

## Get process overview with forest

```bash
ps -aef -forest
```

## get ports that are used by Process

```bash
ss -anp | grep <pid>
```
