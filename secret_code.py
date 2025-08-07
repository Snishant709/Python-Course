
def decode(word):
        if len(word)>3:
            first=word[0]
            decode="abc"+word[1:]+first
            print(f"Decode of {word} is {decode}")
            encode(decode)
        else:
            decode=word[::-1]
            print(f"Decode of {word} is {decode}")
            encode(decode)

def encode(word):
        if len(word)>3:
            last=word[len(word)-1]
            encode=last+word[-4:len(word)-1]
            print(f"Encode of {word} is {encode}")
        else:
            encode=word[::-1]
            print(f"Encode of {word} is {encode}")

letter=input("Enter the word to encode and decode ")
decode(letter)


