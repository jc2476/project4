import pytest
import unittest


class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def initdir(self, tmpdir):
        tmpdir.chdir()
        tmpdir.join("music.csv").write("# testdata")

    def test_method(self):
        with open("music.csv") as f:
            s = f.read()
        assert "testdata" in s
