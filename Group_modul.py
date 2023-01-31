import Student_modul
import Incorrect_number_modul

class GroupIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0
    def __next__(self):
        if self.index < len(self.students):
            self.index += 1
            return self.students[self.index - 1]
        raise StopIteration
class Group:
    def __init__(self, title, max_limit=10):
        self.title = title
        self.max_limit = max_limit
        self.__students = []

    def __iter__(self):
        return GroupIterator(self.__students)
    def __getitem__(self, item):
        if isinstance(item, int):
            if item < len(self.__students):
                return self.__students[item]
            raise IndexError()
        if isinstance(item, slice):
            if item.start < 0:
                raise Incorrect_number_modul.Incorrect_number(f'{item}', ' the number cannot be negative!')
            if item.stop > len(self.__students):
                raise Incorrect_number_modul.Incorrect_number(f'{item}', f'the number cannot be greater {len(self.__students)}')
            start = item.start or 0
            stop = item.stop or len(self.__students)
            step = item.step or 1
            res = []
            for i in range(start, stop, step):
                res.append(f'{self.__students[i]}')
            return res
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

