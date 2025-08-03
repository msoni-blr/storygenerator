with open("raw_story.txt", "r") as f:
    raw_story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

# enumerate index and character at that index
for i, char in enumerate(raw_story):
    if char == target_start:
        start_of_word = i
    if (char == target_end
        and start_of_word != -1
            and start_of_word < i):
        word = raw_story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

# print(answers)

for word in words:
    raw_story = raw_story.replace(word, answers[word])

generated_story = raw_story

with open("generated_story.txt", "w") as f:
    f.write(generated_story)

print(generated_story)
