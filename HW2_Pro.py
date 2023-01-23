import Student_modul
import Group_modul
import Incorrect_number_modul

m1 = Student_modul.Student('Ivanov', 'Ivan', '11111111')
m2 = Student_modul.Student('Stepanov', 'Stepan', '22222222')
m3 = Student_modul.Student('Petrov', 'Petro', '33333333')
m4 = Student_modul.Student('Semenov', 'Semen', '44444444')
m5 = Student_modul.Student('Pavlov', 'Pavlo', '55555555')
m6 = Student_modul.Student('Igorov', 'Igor', '666666666')
m7 = Student_modul.Student('Mashanov', 'Masha', '77777777')
m8 = Student_modul.Student('Olyanov', 'Olya', '88888888')
m9 = Student_modul.Student('Iranov', 'Ira', '9999999999')
m10 = Student_modul.Student('Vityanov', 'Vitya', '1000000000')
m11 = Student_modul.Student('Viktorov', 'Viktor', '21212121212')

gpuop_1 = Group_modul.Group('Gruop 1')
gpuop_2 = Group_modul.Group('Gruop 2')
try:
    gpuop_1.add_student(m1)
    gpuop_2.add_student(m2)
    gpuop_1.add_student(m3)
    gpuop_2.add_student(m4)
    gpuop_1.add_student(m5)
    gpuop_2.add_student(m6)
    gpuop_1.add_student(m7)
    gpuop_1.add_student(m8)
    gpuop_2.add_student(m9)
    gpuop_2.add_student(m10)
except Incorrect_number_modul.Incorrect_number as error:
    print(error)
finally:
    gpuop_2.remove_student(m2)



print(gpuop_2)
print(gpuop_1)

search_name = 'Petrov'
res = gpuop_1.search(search_name)
print('\n', '*'*40, '\n')
print('*'.join(map(str, res)))