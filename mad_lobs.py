templates_list = ["It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation).\
The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). \
If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). \
Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. \
The most ( Adjective3) thing about being in the hospital is the (Silly Word ) !", 
"This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun).\
I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a (Animal), I hear they’re kind of dangerous.\
While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ).\
Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking,\
I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!",
"Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest.\
I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here!\
In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4).\
It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!"]
    
string = "Choose a template. You have 3 options. Insert 1, 2 or 3\n\n\
1)It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation).\n\
The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body ). \n\
If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). \n\
Today I talked to a doctor and they were wearing a (Noun3) on their ( Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. \n\
The most ( Adjective3) thing about being in the hospital is the (Silly Word ) (Noun) !\n\n\
2)This weekend I am going camping with ( Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun).\n\
I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous.\n\
While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for ( Verb (ending in ing) ).\n\
Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking,\n\
I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!\n\n\
3)Dear (Proper Noun (Person’s Name) ), I am writing to you from a (Adjective) castle in an enchanted forest.\n\
I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here!\n\
In the ( Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) ( Noun (Plural)4).\n\
It feels as though I have lived here for (Number) ( Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!\n\n"

def find_closing_location(argument: str)-> int:
    """
    Finds the location of scope's closing parenthesis
    """
    closing_pos = 0
    count = 0
    while closing_pos < len(argument):
        if argument[closing_pos] == '(':
            count += 1
        elif argument[closing_pos] == ')':
            count -= 1
            if count == 0:
                break    
        closing_pos += 1
    return closing_pos + 1

def find_tokens(argument: str)-> list[str]:
    """
    Finds the words to replace
    """
    result = []
    while argument.find("(") != -1:
        closing_parenthesis = find_closing_location(argument)
        substring = argument[argument.find("("):closing_parenthesis]
        result.append(substring[1: -1])
        argument = argument.replace(substring, '')
    return result

def choose_template()->int:
    """
    Choose the text template you want to work with
    """
    template = ""
    int_template = 0
    template = input(string)
    if template.isnumeric():
        int_template = int(template)
    while not template.isnumeric():
        try:
            template = input("Enter 1, 2 or 3\n")
            int_template = int(template)
        except ValueError:
            template = ""
    while int_template > 3 or int_template < 1 :
        int(input("Wrong input, you can insert 1,2 or 3\nTry again\n"))
    return int_template

def input_params(template: int)->dict[str: str]:
    """
    Creates a dictianary of placeholders and their actual values
    """
    tokens = find_tokens(templates_list[template - 1])
    inputs = dict()
    i = 0
    while i < len(tokens):
        inputs[tokens[i]] = input("Enter a " + tokens[i] + ": ")
        i += 1
    return(inputs)

def generate_story(template: int, param_list: dict[str: str]):
    """
    Generates the story, replacing the placeholders with their values
    """
    closing_parenthesis = 0
    temp_str = templates_list[template - 1]
    while temp_str.find('(') != -1:   
        closing_parenthesis = find_closing_location(temp_str)
        substring = temp_str[temp_str.find("("):closing_parenthesis]
        temp_str = temp_str.replace(substring, param_list[substring[1:-1]])
    print(temp_str)    

def main():
    template = choose_template()
    param_list = input_params(template)
    generate_story(template, param_list)

if __name__ == "__main__":
    main()
