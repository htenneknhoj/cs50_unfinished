#WRITING IN ALL CAPS IS LIKE YELLING.

#Best to use your “indoor voice” sometimes, writing entirely in lowercase.

def main():
    uservoice = voice()
    print(uservoice)
    
# Outputs the same input in lowercase
def voice():
    return input("").casefold().strip()

main()
