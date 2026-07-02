import os

import pytest


class TestFiles:
    @pytest.mark.smoke
    def test_file_exists(self, setup):
        assert os.path.exists("test.txt")
        with open('test.txt', 'r') as f:
            line = f.readline()

            assert line == 'This is a test\n'

    @pytest.mark.regression
    def test_file_exists_and_writes(self, setup):
        assert os.path.exists("test.txt")
        with open('test.txt', 'a') as f:
            f.write('love the game\n')

        with open('test.txt', 'r') as f:
            contents = f.read()

            assert contents == 'This is a test\nlove the game\n'
