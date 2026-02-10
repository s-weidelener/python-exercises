def evaluate_password(password):
    score = 0 
    hints = []
    
    #Length
    if len(password) >= 8: 
        score += 1 
    else:
        hints.append("The password should be at least 8 characters long")
    
    #Upper and lowercase letter
    if any(c.isupper() for c in password):
        score += 1
    else:
        hints.append("At least one Uppercase letter is missing")

    if any(c.islower() for c in password):
        score += 1
    else:
        hints.append("At least one lowercase letter is missing")
    
    #Number
    if any(c.isdigit() for c in password):
        score += 2 
    else:
        hints.append("At least one number please")
        
    #Special character
    if any(not c.isalnum() for c in password):
        score += 2
    else:
        hints.append("At least one special character is missing")
        
    #Recognize patterns
    
    #Double
    def consecutive_letters(text):
        prev_letter = None
        found = False
  
        for letter in text:
            if letter == prev_letter:
                return True
            prev_letter = letter
        return False
        
    if consecutive_letters(password):
        hints.append("Avoid repeated consecutive letters")
        score -= 1
      
    #Score
    if score <= 2:
        level = "Weak"
    elif score <= 4:
        level = "Average"
    else:
        level = "Strong"
        

    results = {
        "score": score,
        "level": level,
        "hints": hints
    }
    

    return results

def main():
    print("Password evaluation (type 'exit' to quit)")

    while True:
        user_input = input("Please enter a password: ")

        if user_input.lower() == "exit":
            print("Program terminated.")
            break

        result = evaluate_password(user_input)

        print("\nResult:")
        print(f"Score: {result['score']}")
        print(f"Level: {result['level']}")

        if result["hints"]:
            print("Hints:")
            for hint in result["hints"]:
                print(f"- {hint}")
        else:
            print("No hints.")

        print("-" * 30)


if __name__ == "__main__":
    main()