



## Finding file (.bashrc)
```bash
find /home -name .bashrc
```


## Finding file (.bashrc) and do grep on results
```bash
find /home -name .bashrc -exec grep check_ptlab_key {} \;
find /home -name .bashrc -exec grep <pattern> {} \;
```


## Finding file (.bashrc) and do grep on results, and second grep to remove pattern02
```bash
find /home -name .bashrc -exec grep <pattern> {} \; grep -v <pattern02>
```


## Find file and do grep. include line after the match and search for lines that start with the pattern
```bash
find . -name .bash_history -exec grep -A 1 '^passwd' {} \;
```



## Search with sudo other user and cat the result
```bash
sudo -u victim find /home/victim -name key.txt -exec cat {} \;
```


## Find all world readable files
```bash
find / -perm -o+r
```


## Find all world writable files
```bash
find / -perm -o+w
```


## Find all world writable files that are not symbolic links
```bash
find / -not -type l -perm -o+w
```


## Find files all files that has the group bugtracker
```bash
find / -type f -group bugtracker 2>/dev/null
```


## Find all binaries with the setuid bit set, and forward errors to /dev/null
```bash
find / -perm -4000  2>/dev/null
```



## Find all binaries with the setuid bit set, and forward errors to /dev/null, and get extra info
```bash
find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```



## Find directories with permissions other than 775 / 664
```bash
find -type d -not -perm 775 -o -type f -not -perm 664
```



## Find directory where specific user has write permissions, get all the permisions. and forward errors to dev null
```bash
find / -type d -user james -perm -u+w  -exec ls -ldb {} \; 2> /dev/null
```


## Find options
* find / -type f    #files
* find / -type d    #dirs

