import re 

def test(function,assets):
    for i,asset in enumerate(assets):
        result = function(asset)
        print(f'Test {i}: {result};    length: {len(result)}')


 
isu = 467467
print("%6 %4 %8")
print(isu%6,isu%4,isu%8,sep="  ")


#1
#       ;<{|
print("-----------Num 1 ---------------")
reFunction1 = lambda x : re.findall(r';<{\|',x)
assets1 = [
    r'woirjf_;<{|_oiewjoj_;<{|_pdkewpfk_;<{|_powekf;<oiwrjf{|_;<{|_fewrfg',
    r'<{|;<{;<|;<{<{|',
    r'',
    r';<{\|',
    r';\n<\n{\n|'
]
test(reFunction1,assets1)



#2
# Вариант №1
# Довольно распространённая ошибка ошибка – это повтор слова. Вот в предыдущем
# предложении такая допущена. Необходимо исправить каждый такой повтор
print("-----------Num 2 ---------------")

def on_match(match):
    return match.group(0) + " - " + str(len(match.group(0)))

s = re.sub(r'(\b[а-яёЁА-Я]+) \1',r'\1',re.sub(r'\s+',' ',r'Это   пример  пример предложения  с    некоторыми ошибками  .'))
print(s)
reFunction2 = lambda x : re.sub(r'(\b[а-яёЁА-Я]+) \1\b',r'\1',re.sub(r'\s+',' ',x))
assets2 = [
    r'Это   пример  пример предложения  с    некоторыми ошибками  .',
    r'123 123 123 123 123 123 123',
    r'Довольно      распространённая ошибка ошибка – это лишний  повтор    повтор слова   слова. Смешно,   не не правда ли? Не нужно портить хор хоровод.',
    r'Тут все правильно лол',
    r'хорошохор хоровод        водили вод хор а     хор'
]
test(reFunction2, assets2)


#3
# Вариант №3
# Вася решил заменить все целые числа на функцию от этого числа.
# Функцию он придумал не сложную:
#  4(𝑥^2) − 7, где 𝑥 − исходное число

print("-----------Num 3 ---------------")

def process_num(match):
    num = int(match.group(0))
    return str(4 * (num**2) - 7)

reFunction3 = lambda x : re.sub(r'\d+',process_num,x)
assets3 = [
    r'20 + 22 = 42',
    r'1    3',
    r'riuafn33msldkf',
    r'a1a',
    r'()=/.>20?>/.s'
]
test(reFunction3,assets3)
