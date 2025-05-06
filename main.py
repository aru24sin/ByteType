import time

def type_speed():
    print("Welcome to the Typing Speed Test!")
    print("You will be given a sentence to type. Type it as fast as you can.")
    input("Press Enter to start...")
    
    # Sample text for typing test
    sample_text = "The quick brown fox jumps over the lazy dog."
    print(f"Type this: {sample_text}")
    
    start_time = time.time()
    user_input = input("Your input: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words_per_minute = (len(user_input.split()) / elapsed_time) * 60
    
    print(f"Your typing speed is {words_per_minute:.2f} words per minute.")
    return

def type_accuracy():
    print("Welcome to the Typing Accuracy Test!")
    print("You will be given a sentence to type. Type it as accurately as you can.")
    input("Press Enter to start...")
    
    # Sample text for typing test
    sample_text = "The quick brown fox jumps over the lazy dog."
    print(f"Type this: {sample_text}")
    
    user_input = input("Your input: ")
    
    correct_chars = sum(1 for a, b in zip(sample_text, user_input) if a == b)
    accuracy = (correct_chars / len(sample_text)) * 100
    
    print(f"Your typing accuracy is {accuracy:.2f}%.")
    return

def main():
    print("Welcome to the Typing Test!")
    while True:
        options = int(input("1. Type Speed\n2. Type Accuracy\n3. Quit\nChoose an option (1, 2, or 3): "))
        if options == 1:
            type_speed()
        elif options == 2:
            type_accuracy()
        elif options == 3:
            print("Thank you for using the Typing Test!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")
            break 

if __name__ == "__main__":
    main()