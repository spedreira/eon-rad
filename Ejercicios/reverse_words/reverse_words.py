def reverse_words(a_text):
    lista = []
    palabra = ''
    SEPARATORS = [',', ';', ' '] 
    for i in a_text:
        #print (i)
        #print (lista)
        #print (palabra)
        
        if i in SEPARATORS:
            palabra = palabra[::-1]
            #print (palabra)
            lista.append(palabra)
            
            palabra = ''
            lista.append(i)
            #print (lista)         
        
        else:
            palabra += str(i)
            #print (palabra)

    palabra = palabra[::-1]
    #print (palabra)
    lista.append(palabra)
    #print (lista)
    return print(''.join(lista))
                    
    #raise Exception("not implemented yet.")

reverse_words('aloh')
reverse_words('siht si a lamron ecnetnes')
reverse_words('siht,ecnetnes,si,ton;yrev;lamron;')
reverse_words('    0,23,xxx,89')
reverse_words('0,23;,,xyz,89')
reverse_words('hola,holamundo')