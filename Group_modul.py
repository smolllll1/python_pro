import Student_modul
import Incorrect_number_modul

class Group:
    def __init__(self, title, max_limit=10):
        self.title = title
        self.max_limit = max_limit
        self.__students = []

    def add_student(self, arg: Student_modul.Student):
        if len(self.__students) >= self.max_limit:
             raise Incorrect_number_modul.Incorrect_number('limit exceeded!!!', f'  maximum value: {self.max_limit}')
        for item in self.__students:
            if (item.surname, item.name, item.phon) == (arg.surname, arg.name, arg.phon):
                return None
        self.__students.append(arg)
        Incorrect_number_modul.logger.info(f'appending student!      {arg}')

    def remove_student(self, arg: Student_modul):
        if arg in self.__students:
            self.__students.remove(arg)
            Incorrect_number_modul.logger.info(f'removing student!       {arg}')

    def search(self, surname: str):
        res = []
        for item in self.__students:
            if item.surname == surname:
                res.append(item)
        return res

    def __str__(self):
        return f'{self.title}\nStudents:\n' + '\n'.join(map(str, self.__students))

