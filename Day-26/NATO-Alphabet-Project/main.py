import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_data_frame = pandas.DataFrame(data)

# Coverting the pandas dataframe into a dictionary | Dictionary Comprehension
nato_dict = {
   row.letter: row.code for (_, row) in nato_phonetic_data_frame.iterrows()
}

# Converting the word into the NATO phonetic code list | List Comprehension
def nato_converter():
   word = input("Enter the word: ").upper()
   try:
      nato_code_list = [nato_dict[letter] for letter in word]
   except KeyError:
      print("Only letters are valid input numbers are not allowed")
      nato_converter()
   else:
      print(nato_code_list)

nato_converter()