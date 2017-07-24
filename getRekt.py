import time

def get_rekt():
    length = input("How rekt did you get?\n")
    while length <= 0:
        length = input("Listen, we both know you got rekt, tell me the truth\n")
    i = 0
    while i < length:
        print("rekt")
        time.sleep(0.1)
        i += 1
    print("LOLOLOLOLOLOL")



if __name__ == "__main__":
    get_rekt()
