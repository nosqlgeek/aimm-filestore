import sys
import os
sys.path.append('..')
from client import FSClient
from config import CONFIG as cfg

def test_store(c):
    print("Running test_store ...")
    r = c.store("test-1.png", "./logo.png")
    print(r)
    assert os.path.exists("../data/test-1.png")

def test_retrieve(c):
    print("Running test_retrieve ...")
    r = c.retrieve("test-1.png", "../data/output.png")
    print(r)
    assert os.path.exists("../data/output.png")

def test_list(c):
    print("Running test_list ...")
    r = c.list()
    print(str(r))
    assert "['_README.md', 'test-1.png', 'output.png']" == str(r)

def test_delete(c):
    print("Running test_delete ...")
    print(c.delete("test-1.png"))
    print(c.delete("output.png"))
    assert not os.path.exists("../data/output.png")
    assert not os.path.exists("../data/test-1.png")


if __name__ == "__main__":
    c = FSClient("localhost", 5000, cfg.get("access_key"), cfg.get("access_secret"), False)
    test_store(c)
    test_retrieve(c)
    test_list(c)
    test_delete(c)





