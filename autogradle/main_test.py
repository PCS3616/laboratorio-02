import subprocess
from pathlib import Path

submission_path = Path("./submission")

def test_1_1():
    filecode = submission_path / 'fatorial.c'
    filebin = submission_path / 'fatorial'
    assert(filecode.exists())

    # Compile
    subprocess.call(["gcc", "-o", filebin.absolute(), filecode.absolute()])

    def check_exec(inp, out):
        p = subprocess.run([filebin.absolute()], input=inp, capture_output=True, text=True)
        assert(p.stdout == out)

    check_exec('0', '1')
    check_exec('1', '1')
    check_exec('5', '120')

def test_2_2():
    file = submission_path / '2_2.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        assert(content == "/home/ubuntu")

def test_2_3():
    file = submission_path / '2_3.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        assert(content == "mkdir: não foi possível criar o diretório “baz”: Arquivo existe")

def test_2_4():
    file = submission_path / '2_4.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        files = content.split('\n')

        assert('bin' in files)
        assert('tmp' in files)
        assert('dev' in files)

def test_2_5():
    file = submission_path / '2_5.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        files = content.split('\n')

        assert('Desktop' in files)


def test_2_6():
    file = submission_path / '2_6.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        files = content.split('\n')

        assert('.bashrc' in files)
        assert('.bash_history' in files)

def test_2_7():
    file = submission_path / '2_7.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        assert(content == "/root")

def test_desafio():
    file = submission_path / 'clmystery.sh'

    with open(file) as fp:
        lines = fp.readlines()

    assert(len(lines) > 5)

    assasino = lines[-1].strip()
    assert('Rienne Lemeda' in assasino)
