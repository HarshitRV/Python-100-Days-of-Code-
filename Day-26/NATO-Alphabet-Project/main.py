import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_data_frame = pandas.DataFrame(data)

# Coverting the pandas dataframe into a dictionary | Dictionary Comprehension
nato_dict = {
   row.letter: row.code for (index, row) in nato_phonetic_data_frame.iterrows()
}

word = input("Enter the word: ").upper()

# Converting the word into the NATO phonetic code list | List Comprehension
nato_code_list = [nato_dict[letter] for letter in word]
print(nato_code_list)