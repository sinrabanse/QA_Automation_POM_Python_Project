import pytest
from selenium import webdriver
import subprocess
import time
import signal
import os

# 2 Browsers

# @pytest.fixture(params=["chrome", "firefox"])
# def initialize_driver(request):

#     #Defining driver for all tests
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
    
#     request.cls.driver = driver
#     print("Browser: ", request.param)


#     #Quitting in the end of test
#     yield driver
#     driver.quit()

# 1 Browser

@pytest.fixture()
def initialize_driver(request):
    selenium_server_url = os.getenv("SELENIUM_SERVER")

    #Defining driver for all tests
    if selenium_server_url:
        # For docker
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Remote(command_executor=selenium_server_url, options=options, desired_capabilities=options.to_capabilities())
    else:
        # Locally
        driver = webdriver.Chrome()
    request.cls.driver = driver
    #Quitting in the end of test
    yield driver
    driver.quit()

def pytest_collection_modifyitems(config, items):
    config._has_sanity = any(item.get_closest_marker("sanity") for item in items)

@pytest.fixture(scope="session")
def mock_server(request):
    # Running only if we have sanity tests
    if not getattr(request.config, "_has_sanity", False):
        return
    
    if not os.path.exists("utilities/mock_server.py"):
        raise FileNotFoundError("mock_server.py not found!")
    
    # Running Flask Server
    print("\n[MOCK SERVER] Running Flask-server for sanity tests...")
    server = subprocess.Popen(["python", "utilities/mock_server.py"])
    time.sleep(1)

    yield

    # Close server after tests
    print("\n[MOCK SERVER] Closing Flask-server after sanity tests.")
    server.send_signal(signal.SIGINT)
    server.wait()