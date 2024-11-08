from json_to_xml import replaceSolution, libSolution, regExSolution, grammarSolution
import time
from xml_to_json import parse_xml
from xml_to_jsonLib import xmltojsonLib


def idealTime():
    with open(r"ITMO_Labs\Informatics\lab4\response.json", 'r', encoding='utf-8') as f, open(r"ITMO_Labs\Informatics\lab4\idealSolutionReturn.xml", "w",encoding='utf-8') as f2:
        f2.write(f.read())




def test(func,numOfTests):
    start = time.perf_counter()
    for _ in range(numOfTests):
        func()
    end = time.perf_counter()
    print(f'{func.__name__} time in {numOfTests} tests: {end-start}')

for function in [replaceSolution, libSolution, regExSolution, grammarSolution,idealTime]:
    test(function,1000)
