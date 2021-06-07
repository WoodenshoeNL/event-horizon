# Fuff

## Install Fuff

### Install with Apt-Get

```bash
sudo apt-get install ffuf
```

### Get Lastest, install from source with go

```bash
go get github.com/ffuf/ffuf
```

### Install Golang

```bash
sudo apt install golang
```

## Using Fuff

### Simple usage

```bash
ffuf -w /path/to/wordlist -u https://target/FUZZ
```

-w    = wordlist

-u    = target (FUZZ will be replaced by word from wordlist)

### HTB Parrot simple example

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt

ffuf -w /usr/share/dirb/wordlists/big.txt -u http://10.10.10.95/FUZZ
ffuf -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -u https://10.10.10.60/FUZZ
```

### Recursion and recursion-depth

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt -recursion -recursion-depth 3
```

### search for extension .bak

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt -recursion -e .bak
```

### Search for multiple extensions

```bash
ffuf -w /usr/share/dirb/wordlists/big.txt -e .sh,.cgi,.php,.htb,.py,.pl -u http://10.10.10.56/cgi-bin/FUZZ
```

### run in silent mode

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt -s
```

### use silent mode with tee to output in a file

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt -s | tee ./output.txt
```

### using Multiple Fuzzing locations

```bash
ffuf -u http://W1.com/W2 -w /usr/share/dirb/wordlists/big.txt:W2 -w /home/user/domains.txt:W1
```

### Add Cookie

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt -b "NAME1=VALUE1;NAME2=VALUE2;NAME3=VALUE3"
```

### Add Headers

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt -H "NAME1=VALUE1;NAME2=VALUE2;NAME3=VALUE3"
```

### Use POST HTTP method

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt -X POST
```

### Use POST HTTP method with post data, fuzzing character in post data

```bash
ffuf -u http://10.10.10.153/moodle/login/index.php -w /home/htb-woodenshoe/htb/wordlist/SecLists/Fuzzing/special-chars.txt -X POST -H "Content-Type: application/x-www-form-urlencoded" -d 'anchor=&username=Giovanni&password=Th4C00lTheachaFUZZ' -mc all -v -fs 440
```

### Replay proxy -Run ffuf through a local proxy(burp)

```bash
ffuf -u http://10.10.10.48/FUZZ -w /usr/share/dirb/wordlists/big.txt --replay-proxy http://127.0.0.1:8080
```

### Match status code 200

```bash
ffuf -w /usr/share/dirb/wordlists/big.txt -mc 200 -u http://10.10.10.60/FUZZ
```

### Using a request file

Save a request to a file in burp. Add the FUZZ keyword in the right location in the file

```bash
ffuf -w /usr/share/dirb/wordlists/big.txt -request /tmp/request.txt
```

### Wordlists mode

By default ffuf runs in cluster bomb mode. Running ffuf in pitch fork mode to match wordlists

### Options

```bash
MATCHER OPTIONS:
  -mc              Match HTTP status codes, or "all" for everything. (default: 200,204,301,302,307,401,403)
  -ml              Match amount of lines in response
  -mr              Match regexp
  -ms              Match HTTP response size
  -mw              Match amount of words in response

FILTER OPTIONS:
  -fc              Filter HTTP status codes from response. Comma separated list of codes and ranges
  -fl              Filter by amount of lines in response. Comma separated list of line counts and ranges
  -fr              Filter regexp
  -fs              Filter HTTP response size. Comma separated list of sizes and ranges
  -fw              Filter by amount of words in response. Comma separated list of word counts and ranges
```
