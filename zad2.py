








def get_grades():
    return [5, 4, "3", 2, 1]

def calculate_average(grades):
    return sum(grades) / len(grades)

###poprawiony kod
###problem był gdy chciało się wykonywać operacje na liczbowe na stringu, więc trzebabyło
###przekonwertować tą listę na liczby
def calculate_average_poprawiony(grades):
    grades_numeric = [int(grade) for grade in grades]
    return sum(grades_numeric) / len(grades_numeric)

def to_word_grade(avg):
    if avg >= 4.5:
        return "bardzo dobry"
    elif avg >= 3.5:
        return "dobry"
    elif avg >= 2.5:
        return "dostateczny"
    else:
        return "niedostateczny"

def show_result():
    grades = get_grades()
    avg = calculate_average_poprawiony(grades)
    word = to_word_grade(avg)
    print(f"Średnia: {avg:.2f}, Ocena: {word}")

show_result()


def test_calculate_average_poprawiony(test_grades):
    assert calculate_average_poprawiony(test_grades) == 5, "Test dla średniej jest niepoprawny"
    assert to_word_grade(4.8) == "bardzo dobry", "Test na słowną interpretacje 1 jest niepoprawny"
    assert to_word_grade(3.8) == "dobry", "Test na słowną interpretacje 2 jest niepoprawny"
    print("Wszystkie testy przeszly pomyslnie!")

def get_test_grades():
    return [4,6,"4",5,"6"]

test_grades_1 = get_test_grades()

test_calculate_average_poprawiony(test_grades_1)