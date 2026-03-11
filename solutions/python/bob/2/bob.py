"""Module for Bob's lackadaisical responses to various inputs."""

def response(input_text):
    """
    Determine Bob's response based on input characteristics.
    
    Rules:
    - Empty/whitespace: "Fine. Be that way!"
    - Yelling question: "Calm down, I know what I'm doing!"
    - Yelling: "Whoa, chill out!"
    - Question: "Sure."
    - Anything else: "Whatever."
    
    Args:
        input_text (str): What someone says to Bob
        
    Returns:
        str: Bob's response
    """
    # Strip whitespace for silence check
    cleaned_input = input_text.strip()
    
    # Check for silence (empty or just whitespace)
    if not cleaned_input:
        return "Fine. Be that way!"
    
    # Check if it's a question (ends with ? after stripping)
    is_question = cleaned_input.endswith("?")
    
    # Check if it's yelling (all uppercase letters, ignoring non-letters)
    def is_uppercase_text(text):
        letters = [char for char in text if char.isalpha()]
        return bool(letters) and all(char.isupper() for char in letters)
    
    # Yelling question
    if is_uppercase_text(cleaned_input) and is_question:
        return "Calm down, I know what I'm doing!"
    
    # Yelling statement
    if is_uppercase_text(cleaned_input):
        return "Whoa, chill out!"
    
    # Normal question
    if is_question:
        return "Sure."
    
    # Anything else
    return "Whatever."
