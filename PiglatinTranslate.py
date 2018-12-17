pyg = 'ay' #adds ay to the end of the word

original = input('Enter a word:') #prompts user to type a word

if len(original) > 0 and original.isalpha(): #makes sure only letters are typed in and that characters exist
    print(original) #prints out the typed word
    word = original.lower() #converts words to lowercase
    first = word[0] #indicates first letter
    new_word = word + first + pyg #for instance: if the word is "Hello", then it converts it to hello + h + ay which equals "hellohay"
    new_word = new_word[1:len(new_word)] #converts "hellohay" to "ellohay" by only reading from the 2nd letter on.
    print(new_word) #prints out translated word
else:
    print('Please only use alphabetical letters. No numbers, spaces, or symbols!') #reminder if anythin
