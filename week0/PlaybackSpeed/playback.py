# Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, 
# a la YouTube’s 0.75 playback speed, or even by having them pause between words.

def main():
    slowed = get_lecture()
    print(slowed)

# Adds "..." for every " " in the input of user.
def get_lecture():
    lecture = input("")
    lecture = lecture.replace(" ", "...")
    return lecture

main()
