
class accessModifier:
    def __init__(self, name) -> None:
        self.__privateMember = name
        self.__salary = "6lpa"

        self.__codingSkill = "Good"


rutvik = accessModifier("Rutvik")


print(rutvik._accessModifier__privateMember)
