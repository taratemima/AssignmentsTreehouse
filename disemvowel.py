'''Remove vowels from items in list and capitalize as needed'''

vowels = list('aeiou')
words = ["Arcadia","vision","xylophone","polymer"]
output_list = list()

for w in words:
    wLetters = list(w.lower())
    for v in vowels:
        while True:
            try:
                wLetters.remove(v)
            except:
                break
    output_list.append(''.join(wLetters).capitalize())

print(output_list)

#OK, with Kenneth Love's feedback, it worked

    #for wl in wLetters:
     #   if wl in vowels:
      #      wLetters.remove(wl)
       # else:
        #    continue
        #newWord = str(wLetters).join('')
        #newWord = str(wLetters)
        #output_list.append(newWord.title())

#for ou in output_list:
 #   print(ou)

    #What I got for output
    #['R', 'C', 'A', 'D', 'I', 'A']
#['R', 'C', 'D', 'I', 'A']
#['R', 'C', 'D', 'A']
#['V', 'S', 'I', 'O', 'N']
#['V', 'S', 'O', 'N']
#['X', 'Y', 'L', 'P', 'H', 'O', 'N', 'E']
#['X', 'Y', 'L', 'P', 'H', 'N', 'E']
#['X', 'Y', 'L', 'P', 'H', 'N']
#['P', 'L', 'Y', 'M', 'E', 'R']
#['P', 'L', 'Y', 'M', 'R']

    #not ready for prime time yet, but 

#try:
 #   pass
#except:
 #   pass
