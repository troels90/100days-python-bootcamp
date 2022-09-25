import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("A word, please: ").upper()
    try:
        phonetic = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Only letters please")
        generate_phonetic()
    else:
        print(phonetic)

generate_phonetic()

