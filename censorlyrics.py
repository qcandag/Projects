text = "We're no strangers to love&You know the rules and so do I@A full\
        commitment's what I'm thinking of@You wouldn't get this from any\
          other guy%I just wanna tell you how I'm feeling&Gotta make you\
       understand$Never gonna give you up$Never gonna let you down@Never\
    gonna run around and desert you%Never gonna make you cry&Never gonna\
        say goodbye%Never gonna tell a lie and hurt you@We've known each\
    other for so long%Your heart's been aching but you're too shy to say\
        it$Inside we both know what's been going on$We know the game and\
     we're gonna play it@And if you ask me how I'm feeling&Don't tell me\
     you're too blind to see$Never gonna give you up%Never gonna let you\
    down&Never gonna run around and desert you$Never gonna make you cry%\
     Never gonna say goodbye@Never gonna tell a lie and hurt you$No, I'm\
       never gonna give you up%No, I'm never gonna let you down&No, I'll\
   never run around and hurt you$Never, ever desert you&We've known each\
     other for so long@Your heart's been aching but$Never gonna give you\
       up%Never gonna let you down@Never gonna run around and desert you\
    $Never gonna make you cry$Never gonna say goodbye@Never gonna tell a\
    lie and hurt you%No, I'm never gonna give you up%No, I'm never gonna\
    let you down@No, I'll never run around and hurt you&I'll never, ever\
                                                              desert you"


def lyrics_fix(text):    
    wrong = ["%","&","@","$"]    
    list1 = []
    
    for i in text:
        list1.append(i)
    for a in range(len(list1)):
        for b in wrong:
            if list1[a] == b:
                list1[a] = "\n"

    list2 = ""
    
    for i in range(len(list1)):
        list2 += list1[i]
    print("Lyrics:")            
    print(list2)
    
    return list2
text = lyrics_fix(text)

def lyrics_censor(text):
    while True:    
        list3 = []
        syc = 0
        for i in range(len(text)):
            if text[i] == " ":
                list3.append(text[syc:i])
                syc = i+1                
        syc2 = 0
        data = input("Enter the word you want to censor:\n")
        
        for i in range(len(list3)):
            if list3[i].upper() == data.upper():
                syc2 += 1
                list3[i] = len(list3[i])*"*" 
        new_text = ""
        for i in list3:
            new_text += i + " "        
        print(new_text)        
        print("{} incident(s) found \n".format(syc2))        
        text = new_text        
        Q = input("Do you want to censor more words?:")    
        if Q.upper() == "N":
            print("\nCensored lyrics:")
            print(new_text)
            break
re = lyrics_censor(text)






















