import speech_recognition as sr
import difflib
import control

# Function to match recognized command to the closest known command
def match_command(command, options):
    words = command.split()
    for word in words:
        closest = difflib.get_close_matches(word, options, n=1, cutoff=0.6)
        if closest:
            return closest[0]
    return None

def recognize_speech():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  # Sensitivity to ambient noise

    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak now!")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio).lower()

            print(f"[DEBUG] Recognized: '{text}'")

            # Log to file
            with open("commands_log.txt", "a") as log:
                log.write(f"{text}\n")

            return text

        except sr.UnknownValueError:
            print("Could not understand the audio. Try again.")
        except sr.RequestError:
            print("Could not request results. Check your internet connection.")
        except sr.WaitTimeoutError:
            print("No speech detected. Try again.")

    return None

if __name__ == "__main__":
    valid_commands = ["left", "right", "forward", "backward", "stop", "exit", "quit", "stop listening"]

    while True:
        command = recognize_speech()

        if command:
            matched = match_command(command, valid_commands)

            if matched == "left":
                control.move("left")
                print("Turning left")
            elif matched == "right":
                control.move("right")
                print("Turning right")
            elif matched == "forward":
                control.move("forward")
                print("Moving forward")
            elif matched == "backward":
                control.move("backward")
                print("Moving backward")
            elif matched == "stop":
                control.move("stop")
                print("Stopping")
            elif matched in ["exit", "quit", "stop listening"]:
                print("Exiting voice recognition.")
                break
            else:
                print("Command not recognized.")