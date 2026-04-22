# Hilltop Community Data processing system

ADULT_AGE = 18

def calculate_average(total_age, total_people):
    if total_people == 0:
        return 0
    else:
        return total_age / total_people

def display_results(total_people, male_count, female_count, adult_count, average_age):
    print("\n" + "=" * 35)
    print("     COMMUNITY DATA REPORT")
    print("        Hilltop Community")
    print("=" * 35)

    print(f"Total People       : {total_people}")
    print(f"Males              : {male_count}")
    print(f"Females            : {female_count}")
    print(f"Adults (18+)       : {adult_count}")
    print(f"Average Age        : {average_age:.2f}")

    print("=" * 35)

def main():
    total_people = 0
    total_age = 0
    male_count = 0
    female_count = 0
    adult_count = 0

    while True:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        gender = input("Enter gender (M/F): ")

        total_people += 1
        total_age += age

        if gender.lower() == 'm':
            male_count += 1
        elif gender.lower() == 'f':
            female_count += 1
        else:
            print("Invalid gender input")

        if age >= ADULT_AGE:
            adult_count += 1

        choice = input("Add another person? (yes/no): ")
        if choice.lower() == 'no':
            break

    avg = calculate_average(total_age, total_people)
    display_results(total_people, male_count, female_count, adult_count, avg)

main()