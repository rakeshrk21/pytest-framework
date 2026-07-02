import os
import pytest

@pytest.fixture()
def setup():
    path = 'test.txt'
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write('This is a test\n')
    print('before---')
    yield
    print('after---')
    os.remove(path)