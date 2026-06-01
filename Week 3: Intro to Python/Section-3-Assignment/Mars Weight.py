"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():
    # Fill this function out!
    weight_earth=float(input("Enter a weight on Earth: "))
    weight_mars=round(weight_earth*0.378,2)
    print(f"The equivalent weight on Mars: {weight_mars}")

if __name__ == "__main__":
    main()
