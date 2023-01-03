import subprocess
from pathlib import Path

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
