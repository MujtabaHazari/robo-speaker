import pyttsx3

engine = pyttsx3.init()

print("Welcome to Robo speaker 1.1 created by Mujtaba")

while True:
    x = input("Enter what you want me to speak (or type 'q' to quit): ")

    if x == "q":
        engine.say("Bye friend")
        engine.runAndWait()
        break
    else:
        engine.say(x)
        engine.runAndWait()
