# Graveyard Walkthrough

## Challenge Overview
**Difficulty**: Medium  
**Vulnerability**: Data Encoding  
**Flag**: nhc{l3g4cy_d3c0d3d_fr0m_run3s}

## Story Context
Hattori explores the Dragon's Graveyard, where ancient runes hold encoded secrets from the past.

## Solution Steps

### Step 1: Access the Challenge
1. Navigate to `/challenge/graveyard`
2. Observe the encoded flag displayed on the tombstone

### Step 2: Understand the Encoding
The flag appears as a long string of characters. The page indicates it's double-encoded:
- First encoding: Base32
- Second encoding: Base64

### Step 3: Decode the Base64 Layer
1. Copy the encoded string from the page
2. Use an online Base64 decoder or Python:
   ```python
   import base64
   encoded = "YOUR_ENCODED_STRING_HERE"
   decoded_base64 = base64.b64decode(encoded).decode()
   print(decoded_base64)
   ```

### Step 4: Decode the Base32 Layer
1. Take the result from step 3
2. Decode it as Base32:
   ```python
   import base64
   base32_string = "RESULT_FROM_STEP_3"
   decoded_base32 = base64.b32decode(base32_string).decode()
   print(decoded_base32)
   ```
Another simple step is jsut copy the base and go to cyber chef and paste it below on the output field it will show a wand click it it will automaticaly decode and show the flag 
### Step 5: Get the Flag
The final decoded string should be: `nhc{l3g4cy_d3c0d3d_fr0m_run3s}`

## Hints

### Hint 1
> The tombstone shows runes that need to be translated. Look for clues about the encoding method on the page.

### Hint 2
> Two layers of encoding protect the ancient secret. Start with the outer layer and work your way in.

### Hint 3
> Base64 uses A-Z, a-z, 0-9, +, /, and = for padding. Base32 uses A-Z, 2-7, and = for padding.

## Educational Notes

### What You Learned
- **Data Encoding**: Common technique to obscure sensitive information
- **Base64 Encoding**: Used for binary-to-text conversion
- **Base32 Encoding**: Similar to Base64 but with different character set
- **Decoding Tools**: Online decoders and programming languages

### Real-World Applications
- Email attachments use Base64 encoding
- Data URLs in HTML use Base64
- Configuration files may use encoding for obfuscation
- Malware may use encoding to evade detection

### Prevention
- Use proper encryption instead of simple encoding
- Implement access controls
- Monitor for unusual decoding activities
- Use secure storage for sensitive data

## Common Mistakes
- Decoding in wrong order (Base32 first instead of Base64)
- Forgetting to handle padding characters (=)
- Using wrong encoding type
- Not copying the full encoded string

## Next Steps
Submit the decoded flag on the map page.
