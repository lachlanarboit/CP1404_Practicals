"""
CP1404 Practical
Programming Language class
"""


class ProgrammingLanguage:
    """Represent information about a programming language"""

    def _init_(self, name, typing, reflection, year):
        """Construct programming language for given values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def _str_(self):
        """Return string representation of a programming language"""
        return "{}, {} Typing, Reflection={}, First appeared in {}" \
            .format(self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Determine if language is dynamically typed"""
        return self.typing == "Dynamic"


def run_rests():
    """Run simple tests/demos on ProgrammingLanguage class"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1991)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if _name_ == "_main_":
    run_tests()
