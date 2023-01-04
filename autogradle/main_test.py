import subprocess
from pathlib import Path
import re

submission_path = Path("./submission")
autogradle_path = Path("./autogradle")

def test_1_1():
    filecode = submission_path / 'fatorial.c'
    filebin = submission_path / 'fatorial'
    assert(filecode.exists())

    # Compile
    subprocess.call(["gcc", "-o", filebin.absolute(), filecode.absolute()])

    def check_exec(inp, out):
        p = subprocess.run([filebin.absolute()], input=inp, capture_output=True, text=True)
        assert(p.stdout.strip() == out)

    check_exec('0', '1')
    check_exec('1', '1')
    check_exec('5', '120')

def test_1_2():
    filescript = submission_path / 'makefile-test.sh'
    fruits = autogradle_path / 'fruits.txt'
    vegetables = autogradle_path / 'vegetables.txt'
    groceries = autogradle_path / 'groceries.txt'

    assert(filescript.exists())

    with open(fruits, mode='w') as f:
        f.write('\n'.join(['Banana', 'Melancia']))

    with open(vegetables, mode='w') as f:
        f.write('\n'.join(['Cebola', 'Tomate']))

    p = subprocess.run([filescript.absolute()], capture_output=True, text=True, cwd=autogradle_path.absolute())

    assert(p.returncode == 0)

    result = """cat groceries.txt
Fruits:
Banana
Melancia
Vegetables:
Cebola
Tomate
"""

    assert(result in p.stdout)
    assert(not groceries.exists())

def test_1_3():
    makefile = submission_path / 'Makefile'
    executable = submission_path / 'fatorial'
    assert(makefile.exists())

    # Tem que ter a dependencia do arquivo, deve rodar dois
    p = subprocess.run(['make', 'run'], input='5', capture_output=True, text=True, cwd=makefile.parent.absolute())
    assert(p.returncode == 0)
    assert(executable.exists())
    assert('120' in p.stdout)

    # Compile
    p = subprocess.run(['make', 'fatorial'], capture_output=True, text=True, cwd=submission_path.absolute())

    assert(p.returncode == 0)
    assert(executable.exists())
    assert('is up to date' in p.stdout)

    p = subprocess.run(['make', 'run_gdb'], input='r\n5\nq\n', capture_output=True, text=True, cwd=makefile.parent.absolute())
    assert(p.returncode == 0)

    p = subprocess.run(['make', 'clean'], capture_output=True, text=True, cwd=makefile.parent.absolute())
    assert(p.returncode == 0)
    assert(not executable.exists())

def test_2():
    regexfile = submission_path / './regex.txt'
    assert(regexfile.exists)

    testes=[[("7581993", True), 
             ("10336827", True), 
             ("7581-993", False), 
             ("Meu número USP é: 10336827", False)],
            [("+55 (11) 999994321", True),
             ("+55 (51) 36975544", True),
             ("55 (11) 99999", False),
             ("+55 (11) 9-9999-4321", False)],
            [("1) Qual o seu nome?", True),
             ("01) Qual o seu nome? E a sua idade?", True),
             ("01) Escreva o seu nome.", False),
             ("(01) Qual o seu nome?", False)],
            [("Alan Mathison Turing", True),
             ("Ada Lovelace", True),
             ("Richard M. Stallman", True),
             ("Ed Dijkstra", False)]]

    with open(regexfile) as f:
        regex=f.read()
    regex=regex.split("\n")[:4]

    acertos=0
    for exp, teste in zip(regex, testes):
        print(f"Testando expressao {exp}:")
        for string, valor in teste:
            try:
                res=len(re.findall(exp.strip(), string))
                if (res==1 and valor) or (res==0 and not valor):
                    print(f"A expressoa passou no teste {string}")
                    acertos+=1
                else:
                    print(f"A expressao nao passou no teste {string}")
            except:
                print(f"Erro na execucao do teste {string}")

    print(f"\nNota final: {round(10*acertos/16, 2)}")
    assert(acertos == 16)
