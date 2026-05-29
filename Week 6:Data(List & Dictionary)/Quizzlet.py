def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    
      # Delete this line and write your code here! :)
    score = 0

    for english in translations:
        answer = input(f"What is the Spanish translation for {english}? ")

        if answer == translations[english]:
            print("That is correct!")
            score += 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {translations[english]}.")

        print()   # blank line

    print(f"You got {score}/8 words correct, come study again soon!")


if __name__ == '__main__':
    main()
