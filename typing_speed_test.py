import time

# Text for the typing test
text_to_type = "The quick brown fox jumps over the lazy dog."

print("Type the following text as fast as you can:")
print(text_to_type)
input("Press Enter to start...")

start_time = time.time()

user_input = input("Start typing: ")

end_time = time.time()
elapsed_time = end_time - start_time

# Calculate words per minute (WPM)
word_count = len(text_to_type.split())
wpm = (word_count / elapsed_time) * 60

# Calculate accuracy
correct_characters = sum(a == b for a, b in zip(user_input, text_to_type))
accuracy = (correct_characters / len(text_to_type)) * 100

print(f"Time taken: {elapsed_time:.2f} seconds")
print(f"Words per minute (WPM): {wpm:.2f}")
print(f"Accuracy: {accuracy:.2f}%")
