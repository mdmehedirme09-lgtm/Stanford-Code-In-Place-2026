from ai import call_gpt

def main():
    # TODO: your code here
    name=input("Enter your name: ")
    topic=input("Enter a topic: ")
    print("Creating your haiku...")
    result=call_gpt(f"Turn the {name} and {topic} into a haiku")
    print(result)

if __name__ == "__main__":
    main()
