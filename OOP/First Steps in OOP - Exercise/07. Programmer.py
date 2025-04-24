
class Programmer:
    def __init__(self,name,language,skills):
        self.name=name
        self.language = language
        self.skills = skills

    def watch_course(self,course_name, language_t, skills_earned):
        if self.language == language_t:
            self.skills += skills_earned
            return f"{self.name} watched {course_name}"

        return f'{self.name} does not know {language_t}'


    def change_language(self,new_language, skills_needed):
        if new_language != self.language and self.skills >= skills_needed:
            g = self.language
            self.language = new_language
            self.skills -= skills_needed
            return f"{self.name} switched from {g} to {new_language}"
        elif self.language == new_language and self.skills >= skills_needed:
            return f'{self.name} already knows {self.language}'
        elif self.skills < skills_needed:
            return f'{self.name} needs {skills_needed - self.skills} more skills'



programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
