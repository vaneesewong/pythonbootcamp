single_quote = 'hello'
double_quote = "World"
triple_quote = """Multi-line 
string"""

print(triple_quote)


text = "Python Programming"

print(text[0])  # First character
print(text[-1]) # Last character
print(text[0:6]) # Slice 0 to 5
print(text[:6]) # From start to 5
print(text[7:]) # 7 to end


name = " bob the builder "
print(len(name))        # Length
print(name.strip())     # Remove whitespace
print(name.upper())     # Uppercase
print(name.lower())     # Lowercase
print(name.title())     # Title Case
print(name.replace("bob", "Jane"))  # Replace 

# f-string 
name = "Vaneese"
age = 27

message = f"My name is {name} and I am {age} years old."
print(message)

# Ex: 
text = """Python is a powerful programming language. It's easy to learn
and versatile!
You can use Python for web development, data science, and
automation. The syntax is clean and readable.
This makes Python perfect for beginners and experts alike."""

char_count = len(text)
char_count_no_spaces = len(text.replace(" ", ""))
word_count = len(text.split())
sentence_count = text.count(".") + text.count("!") + text.count("?")

print(f"Character count (including spaces): {char_count}")
print(f"Character count (excluding spaces): {char_count_no_spaces}")
print(f"Word count: {word_count}")
print(f"Sentence count: {sentence_count}") 
