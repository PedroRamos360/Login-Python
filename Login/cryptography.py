def cryptograph(string):
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    letters_codification = ["1","2","3","4","5","6","7","8","9","0", '1!', '2@', '3#', '4$', '6¨', '7&', '8*', '9(', '0)', '{', '}', '[', ']', '?', '/']
    numbers_codification = ["!","@","#","$","%","^","&","*","(",")","_","+","-","="]
    
    new_string = ''
    for character in string:
        try:
            int(character)
            character = numbers_codification[numbers.index(character)]
        except:
            character = character.lower()
            character = letters_codification[letters.index(character)]
        finally:
            new_string += character
            
    return new_string
