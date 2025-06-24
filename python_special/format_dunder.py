# __format__ dunder or magical method
class Fruits:
    def __init__(self, name:str, grams: float) -> None:
        self.name = name
        self.grams = grams

    def __format__(self, format_specifier: str) -> str:
        # https://youtube.com/shorts/NHquaDS6XQ0?si=MrJrq3UgU54TDJ3O
        match format_specifier:
            case "kg":
                return f"{self.grams/1000:.3f}kg"  ########### .3f is round of 3 in f string representation
            case "mg":
                return f"{self.grams * 1000:.2f}mg" ########### .2f is round of 2 in f string representation
    
def main() -> None:
    apple : Fruits = Fruits(name="Apple", grams=3000)
    fruit_formatted_into_kg = f"{apple:kg}"  ############## for accessing __format__ we need to use f string by calling it in ":" format
    fruit_formatted_into_mgs = f"{apple:mg}" ############## for accessing __format__ we need to use f string by calling it in ":" format
    print(fruit_formatted_into_mgs, fruit_formatted_into_kg)
    return fruit_formatted_into_mgs, fruit_formatted_into_kg

if __name__ == "__main__":
    main()