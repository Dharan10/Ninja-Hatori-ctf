# Cavern Walkthrough

## Challenge Overview
**Difficulty**: Easy  
**Vulnerability**: Information Disclosure  
**Flag**: nhc{ech0es_1n_th3_d4rkn3ss}

## Story Context
Hattori enters the Whispering Cavern, where echoes of the past reveal hidden truths through careful observation.

## Solution Steps

### Step 1: Access the Challenge
1. Navigate to `/challenge/cavern`
2. Observe the page content and story

### Step 2: Inspect Source Code
1. Right-click on the page and select "View Page Source" or "Inspect Element"
2. Look through the HTML source code

### Step 3: Find the Flag
1. In the `<head>` section, locate the CSS link:
   ```html
   <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
   ```
2. Navigate to the CSS file or inspect the styles
3. Look for comments in the CSS file

### Step 4: Extract the Flag
The flag is hidden in a CSS comment:
```css
.container {
    /* nhc{ech0es_1n_th3_d4rkn3ss} */
}
```

## Hints

### Hint 1
> The cavern whispers secrets that can only be heard by those who listen carefully to the source.

### Hint 2
> What you see on the surface is not always the full story. Look deeper into the code that styles the page.

### Hint 3
> CSS files often contain more than just styling rules. Comments can hide valuable information.

## Educational Notes

### What You Learned
- **Information Disclosure**: Sensitive data can be accidentally exposed in client-side code
- **Source Code Inspection**: Always check HTML, CSS, and JavaScript files for hidden information
- **Browser Developer Tools**: Essential for web security testing

### Prevention
- Never store sensitive information in client-side code
- Use server-side storage for secrets
- Regularly audit code for accidental disclosures
- Minify and obfuscate production code

## Alternative Methods
- Use browser dev tools to inspect the CSS
- Download the CSS file directly via URL
- Use curl or wget to fetch the stylesheet

## Common Mistakes
- Looking only at the visible page content
- Forgetting to check linked resources
- Not examining CSS and JavaScript files

## Next Steps
Once you have the flag, submit it on the map and go to next challenge 
