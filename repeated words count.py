sentence = input("Enter the sentence: ")

words_split = sentence.lower().split()

count_of_words= {}

for i in words_split:
    count_of_words[i]= count_of_words.get(i,0)+1

highest=max(count_of_words.values())

for key, value in count_of_words.items():
    if value == highest:
        print(key, value)