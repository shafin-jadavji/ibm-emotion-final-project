from emotion_detection import emotion_detector

def detector(text_to_analyse):
        response = emotion_detector(text_to_analyse)
        print(response)

if __name__ == "__main__":
    detector("I am glad this happened")
    # detector("I am really mad about this")
    # detector("I feel disgusted just hearing about this")
    # detector("I am so sad about this")
    # detector("I am really afraid that this will happen")