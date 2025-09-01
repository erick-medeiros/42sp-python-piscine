import os


def build():
    os.system("pip3 install --upgrade pip")
    os.system("pip3 install build")
    os.system("python3.10 -m build")


def install():
    os.system("pip3 install ./dist/ft_package-0.0.1.tar.gz")


def show():
    os.system("pip3 show -v ft_package")


def test():
    os.system("python3.10 tests/tester.py")


if __name__ == "__main__":
    build()
    install()
    show()
    test()
