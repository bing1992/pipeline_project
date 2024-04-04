from string import Template

import pytest
import time
import os


if __name__ == '__main__':
    pytest.main(["-vs"])
    time.sleep(3)
    os.system("allure generate ./temps -o ./reports --clean")
