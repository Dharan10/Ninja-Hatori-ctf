# Challenges Overview

## Challenge Structure

The CTF consists of 6 progressive challenges, each teaching a different web vulnerability:

### 1. Cavern (Easy)
- **Vulnerability**: Information Disclosure
- **Skill**: Source code inspection
- **Flag Location**: CSS comment
- **Difficulty**: Beginner

### 2. Graveyard (Medium)
- **Vulnerability**: Data Encoding
- **Skill**: Decoding techniques
- **Flag Location**: Double-encoded string
- **Difficulty**: Intermediate

### 3. Shrine (Medium)
- **Vulnerability**: SQL Injection
- **Skill**: Database exploitation
- **Flag Location**: Hidden table
- **Difficulty**: Intermediate

### 4. Spirit (Medium)
- **Vulnerability**: Reflected XSS
- **Skill**: JavaScript injection
- **Flag Location**: Server endpoint
- **Difficulty**: Intermediate

### 5. Shadows (Hard)
- **Vulnerability**: Command Injection
- **Skill**: Shell escaping
- **Flag Location**: File system
- **Difficulty**: Advanced

### 6. Flame (Hard)
- **Vulnerability**: Local File Inclusion
- **Skill**: Path traversal
- **Flag Location**: Restricted directory
- **Difficulty**: Advanced

## Challenge Flow

```
Landing Page → Map → Challenge 1 → Challenge 2 → ... → Challenge 6 → Forge → Victory → Confrontation → Post-Credits
```

## Flag Format

All flags follow the format: `nhc{description_here}`

## Scoring System

- Each solved challenge unlocks the next
- All 6 must be solved to access the finale
- Progress is tracked via session

## Educational Goals

- Learn common web vulnerabilities
- Understand exploitation techniques
- Practice secure coding principles
- Experience real-world attack scenarios

## Security Measures

- Rate limiting (5 requests/minute for map, 10 for challenges)
- CSRF protection on forms
- Content Security Policy
- Input validation and sanitization
- Session management
- Docker hardening (non-root user, minimal attack surface)
