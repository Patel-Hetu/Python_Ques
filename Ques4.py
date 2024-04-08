'''Write a function repeatPhrase(phrase, n), which prints the given phrase n times, alternating
between lowercase and uppercase. Recall, that if aString is a string, then a.upper() is the uppercase of that string, and a.lower() is the lower case of the string. For example, repeat('The sky is blue', 5) would print:
the sky is blue
THE SKY IS BLUE the sky is blue
THE SKY IS BLUE the sky is blue'''

phrase = input("Enter the phrase: ")
n = int(input("Enter the number of times you want ot repeat the phrase: "))

def repeatPhrase(phrase, n):
    for i in range(n):
        if i%2 == 1:
            print(phrase.lower())
        else:
            print(phrase.upper())
            
repeatPhrase(phrase, n)