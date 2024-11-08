from json2xml import json2xml
from json2xml.utils import readfromjson
TAB = 8


# Замена тэгов на другие - Задание 1

def replaceSolution(path=r"ITMO_Labs\Informatics\lab4\response.json"):
    with open(path, 'r', encoding='utf-8') as f:
        json_str = f.read()
    
    xml_str = json_str.replace('{', '<item>').replace('}', '</item>')
    xml_str = xml_str.replace('[', '<array>').replace(']', '</array>')
    xml_str = xml_str.replace(': ', '>')
    xml_str = xml_str.replace(' "', '<')
    xml_str = xml_str.replace('"', '')
    xml_str = xml_str.replace('><', '>')
    xml_str = xml_str.replace('<,', '')
    xml_str = xml_str.replace(',', '')
    xml_str = xml_str.replace('> ', '>')
    xml_str = xml_str.replace('>array', ' type="array"')
    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n<root>' + xml_str + '</root>'
    newline = ''
    for line in xml_str.splitlines():
        if line == '<?xml version="1.0" encoding="UTF-8"?>':
            newline+=line+'\n'
            continue
        if line.startswith('<root>'):
            newline+=line+'\n'
            continue
        if 'type="array">' in line:
            newline+=line+'\n'
            continue
        if '<item>' in line or '</item>' in line:
            newline+=line+'\n'
            continue
        if '</' in line:
            newline+=line+'\n'
            continue
        tag_front = line.find('<')
        tag_end = line.find('>')
        line = line + line[tag_front:tag_front+1] + '/' + line[tag_front+1:tag_end+1]+'\n'
        newline+=line
    with open(r"ITMO_Labs\Informatics\lab4\replaceSolutionReturn.xml", "w",encoding='utf-8') as f:
        f.write(newline)

replaceSolution()



# Библиотеки - Задание 2
def libSolution(path=r"ITMO_Labs\Informatics\lab4\response.json"):
    data = readfromjson(path)
    res = json2xml.Json2xml(data).to_xml()
    with open(r"ITMO_Labs\Informatics\lab4\libSolutionReturn.xml", "w",encoding='utf-8') as f:
        f.write(res)

libSolution()



# Регулярные выражения - Задание 3
import re
def regExSolution(path=r"ITMO_Labs\Informatics\lab4\response.json"):
    with open(path, 'r', encoding='utf-8') as f:
        json_str = f.read()
    
    xml_str = json_str.replace('{', '<item>').replace('}', '</item>')
    xml_str = xml_str.replace('[', '<array>').replace(']', '</array>')
    xml_str = re.sub(r'"(\w+)":',r'<\1>',xml_str)
    xml_str = re.sub(r'"(.+)"',r'\1',xml_str)
    xml_str = xml_str.replace(',', '')
    xml_str = xml_str.replace('> ', '>')
    xml_str = xml_str.replace('><array', ' type="array"')
    xml_str = '<?xml version="1.0" encoding="UTF-8"?>\n<root>' + xml_str + '</root>'

    def closeTag(match):
        return '<' + match.group(1)+'>' + match.group(2) +"</" + match.group(1) + ">"
    xml_str = re.sub(r'<(\w+)>(.+)', closeTag, xml_str)

    with open(r"ITMO_Labs\Informatics\lab4\regExSolutionReturn.xml", "w",encoding='utf-8') as f:
        f.write(xml_str)

regExSolution()



# Формальная грамматика (рекурсивный спуск) - Задание 4
def grammarSolution(path=r"ITMO_Labs\Informatics\lab4\response.json"):
    def recursivePrint(node, depth,file):
        if isinstance(node, dict):
            file.write("\n")
            for key, value in node.items():
                file.write(' ' * depth * TAB)
                file.write(f'<{key} type="{str(type(value))[8:-2]}">')
                recursivePrint(value, depth + 1,file)
                file.write(f'</{key}>\n')
            file.write(' ' * (depth-1) * TAB)
        elif isinstance(node, list):
            file.write("\n")
            for item in node:
                file.write(' ' * depth * TAB)
                file.write(f'<item type="{str(type(item))[8:-2]}">')
                recursivePrint(item, depth+1,file)
                file.write(f'</item>\n')
            file.write(' ' * (depth-1) * TAB)
        else:
            file.write(str(node))

    data = readfromjson(path)
    with open(r"ITMO_Labs\Informatics\lab4\grammarSolutionReturn.xml", "w",encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<all>')
        recursivePrint(data, 1,f)
        f.write('</all>\n')

grammarSolution()
