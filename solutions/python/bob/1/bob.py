def response(hey_bob):
    # Strip whitespace for silence check
    stripped = hey_bob.strip()
    
    # Check for silence (empty or just whitespace)
    if not stripped:
        return "Fine. Be that way!"
    
    # Check if it's a question (ends with ? after stripping)
    is_question = stripped.endswith('?')
    
    # Check if it's yelling (all uppercase letters, ignoring non-letters)
    def is_yelling(text):
        letters = [c for c in text if c.isalpha()]
        return letters and all(c.isupper() for c in letters)
    
    # Yelling question
    if is_yelling(stripped) and is_question:
        return "Calm down, I know what I'm doing!"
    
    # Yelling statement
    elif is_yelling(stripped):
        return "Whoa, chill out!"
    
    # Normal question
    elif is_question:
        return "Sure."
    
    # Anything else
    else:
        return "Whatever."
