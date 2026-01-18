# Before there were emoji, there were emoticons, whereby text like :) was a happy face and text like :( was a sad face. 
# Nowadays, programs tend to convert emoticons to emoji automatically!

def main():
    userin = convert(input(""))
    print(userin)

# Accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and 
# any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.
def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x

main()