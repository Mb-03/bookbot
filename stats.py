

def get_words(string):
    string = string.split()
    count = 0
    for word in string:
        count += 1
    return count

def get_chars(text):
    number_of_chars = {}
    count = 0
    for char in text:
        count += 1
        if char.lower() in number_of_chars:
            number_of_chars[char.lower()] += 1
        else:
            number_of_chars[char.lower()] = 1
    return number_of_chars
    

def formater(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_items:
        print(f"{key}: {value}")
    
    

    


    
