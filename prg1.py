def reverse_string(text):
    return text[::-1]
def count_words(text):
    words=text.split()
    return len(words)
print("flow control,funtion and string manipulation")
input_text=input("Enter a sentence:")
if input_text.startswith("Hello"):
    print("Greeting:Hello!")
elif input_text.startswith("goodBye"):
    print("parting:",goodbye)
else:
    print("customer message:",input_text)
reverse_string=reverse_string(input_text)
print("reverse_string:",reverse_string)
words_count=count_words(input_text)
print("words_count:",words_count)
