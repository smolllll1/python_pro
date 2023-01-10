# 1. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.

def concatenation (a, b, string):
    return (f'{a + b}' + string)
print(concatenation(int(input('a= ')), int(input('b= ')), input('text= ')))

# 2. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*».
# Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.

def rectangle(width, height):
    for i in range(height):
        if i == 1:
            print('*' * width)
        if i < (height - 1) and i != 0:
            print('*' + ' ' * (width - 2) + '*')
        if i == (height - 1):
            print('*' * width)
rectangle(int(input('width= ')), int(input('height= ')))

# 3. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел.
# Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».

is_list = [1,2,3,4,5]
a = int(input('search number= '))
def search(text, list):
    if text in list:
        return list.index(text)
    return -1
print(search(a, is_list))

# 4. Напишіть функцію, яка поверне кількість слів у текстовому рядку.

def sum(text):
    return (len(text.split()))
print(sum(input('text: ')))

# 5. Напишіть функцію, яка переводить число, що означає кількість доларів і центів, в прописний формат. Наприклад:
# > 123,34
# > one hundred twenty three dollars thirty four cents

a = input('enter the dollar amount (max 999999999.99): ')
def conversion(value: str):
    dollars = {1: 'one',2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
               20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
               100:'hundred', 1000:'thousand', 1000000:'million', 0:'zero'}
    for i in value:
        if i == '.':
            b = value.split('.')
            break
        else:
            b = value.split(',')
    if len(b) == 1:
        b.append('00')
    def cents(c: int):
        cents = c % 10
        if c < 10 and (c//10) != 0:
            return ' '.join((dollars[c * 10], 'cents'))
        if c < 10 and (c//10) == 0 and len(str(c)) < 2:
            return ' '.join((dollars[c * 10], 'cents'))
        if c < 10 and (c // 10) == 0:
            return ' '.join((dollars[c], 'cents'))
        if c >= 10 and c < 20:
            return ' '.join((dollars[c], 'cents'))
        if c >= 19:
            return ' '.join((dollars[c - cents], dollars[cents], 'cents'))

    def tens(t):
        if t == 0:
            pass
        tens = t % 10
        if t < 20 and t != 0:
            return ''.join(dollars[t])
        if t >= 19 and t < 100:
            return ' '.join((dollars.get(t - tens), dollars.get(tens)))
        if t >= 100 and t < 1000:
            if t % 100 >= 19:
                return ' '.join((dollars.get(t // 100), dollars[100], dollars.get((t % 100 - tens)), dollars.get(tens)))
            if t % 100 < 20 and t % 100 != 0:
                return ' '.join((dollars.get(t // 100), dollars[100], dollars.get(t % 100)))
            if t % 100 < 20 and t % 100 == 0:
                return ' '.join((dollars.get(t // 100), dollars[100]))
    u = [tens((int(b[0]) // 1000000) % 1000000), dollars[1000000], tens((int(b[0]) // 1000)%1000), dollars[1000], tens(int(b[0]) % 1000), 'dollars', cents(int(b[1]))]
    o = []
    for i in range(len(u)):
        if u[i] != None and u[i-1] != None:
            o.append(u[i])
    return ' '.join(o)
print(conversion(a))

# 6. Напишіть функцію, яка переводить ціле число з римського запису до десяткового.
# Наприклад: XXII -> 22

a = input('Roman numerals: ')
def roman(value: str):
    units = {'I': '1', 'II': '2', 'III': '3', 'IV': '4', 'V': '5', 'VI': '6', 'VII': '7', 'VIII': '8', 'IX': '9'}
    tens = {'X': '1', 'XX': '2', 'XXX': '3', 'XL': '4', 'L': '5', 'LX': '6', 'LXX': '7', 'LXXX': '8', 'XC': '9'}
    hundreds = {'C': '1', 'CC': '2', 'CCC': '3', 'CD': '4', 'D': '5', 'DC': '6', 'DCC': '7', 'DCCC': '8', 'CM': '9'}
    thousands = {'M': '1', 'MM': '2','MMM': '3'}
    u = []
    t = []
    n = []
    s = []
    l = 0
    r = 0
    b = 0
    for i in value:
        if i in thousands and r <= 3:
            r += 1
            u.append(i)
        if i in hundreds and b <= 3:
            b += 1
            t.append(i)
        if i in tens and l <= 3:
            l += 1
            n.append(i)
        if i in units:
            s.append(value[value.index(i):])
            break
    f = []
    m = [thousands.get(''.join(u)), hundreds.get(''.join(t)), tens.get(''.join(n)), units.get(''.join(s))]
    for i in range(len(m)):
        if m[i]:
            f.append(m[i])
        if m[i] == None and f:
            f.append('0')
    return ''.join(f)
print(roman(a))