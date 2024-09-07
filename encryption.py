import random

if __name__=="__main__":
    def enc(st):
        characters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', 
        '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', 
        '_', '`', '{', '|', '}', '~', ' ']
        

        message=""
        l=st.split(" ")
        for i in l:
            if len(i)<=3:
                x=i[-1: :-1]
                message+=x
                message+=" "
            
            else:
                x=""
                c1=random.sample(characters,3)
                for z in c1:
                    x+=z
                x=x+i[1: ]+i[0]
                c2=random.sample(characters,3)
                for s in c2:
                    x+=s
                
                message+=x
                message+=" "
        print("Here is your encrypted message:")
        print(message)
        
    def dec(code):
        message=""
        
        l=code.split(" ")
        for i in l:
            if len(i)<=3:
                x=i[-1: :-1]
                message+=x
                message+=" "
        
            else:
                x1=""
                x2=""
                le=len(i)
                x1=i[3:le-3]
                le1=len(x1)
                x2=x2+x1[-1]+x1[0:le1-1]
                message+=x2
                message+=" "
        print("Here is your decrypted message:")
        print(message)
        

    print("ENCRYPTION AND DECRYPTION OF MESSAGES")
    print("Press 1 for encryting your message")
    print("Press 2 for decrypting your message")
    print("Press 0 for ending the program")
    print()

    while True:
        choice=input("Enter a choice:")
        if choice=="1":
            mes=input("Enter the message you wan to get encrypted:")
            enc(mes)
        elif choice=="2":
            co=input("Enter the encrytped message you wish to get decrypted:")
            dec(co)
        elif choice=="0":
            print("Program exited successfully")

            break
        else:
            print("Enter a valid choice!")


