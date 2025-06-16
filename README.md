# QA Automation Project with Python+Selenium and Docker

## 🟣 Project Description

This is a UI automation testing project for the **[Ivory.co.il](https://www.ivory.co.il)** online store.  
It utilizes **Python + Selenium + Pytest** with **Page Object Model (POM)** to implement clear, scalable, and maintainable UI tests.

The main goals of this project were:

- To practice designing UI tests following POM principles.
- To implement Docker Compose for reproducible test runs.
- To create a small **Flask mock server** to handle operations without affecting the production environment.
- To generate simple **log files** to track test actions.

---

## 🟣 Tech Stack

- **Python 3.x**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **Docker Compose**
- **Flask** (for mock server in sanity test)
- **Logger** (to generate text files with test run details)

---

## 🟣 Features

✅ **6 UI Tests** implemented with Selenium and Pytest:

- `sanity_test.py`
- `test_adding_to_cart.py`
- `test_choose_self_pickup.py`
- `test_filtering.py`
- `test_remove_from_cart.py`
- `test_limit_testing.py`

✅ **Page Object Model (POM)** to streamline code maintenance and readability.  
✅ **Flask mock server** to handle requests during sanity test instead of touching production.  
✅ **Custom logging** to track test actions in `.log` files under `logs/`.  
✅ **Docker Compose** to spin up a reproducible test environment.

## **Project Structure**

### **Folder Structure**

```
├── base/
│ └─ base_class.py
├── data/
│ ├─ test_data.py
│ └─ urls.py
├── logs/
├── pages/
│ ├─ main_page.py
│ ├─ product_page.py
│ └─ catalog_checkout_page.py
├── tests/
│ ├─ base_test.py
│ ├─ sanity_test.py
│ ├─ test_adding_to_cart.py
│ ├─ test_choose_self_pickup.py
│ ├─ test_filtering.py
│ ├─ test_remove_from_cart.py
│ └─ test_limit_testing.py
├── utilities/
│ ├─ logger.py
│ ├─ mock_server.py
│ └─ decorators.py
├── conftest.py
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
├── README.md
```

## 🟣 Installation

### 🔹 1. Clone this repository:

```bash
git clone https://github.com/sinrabanse/QA_Automation_POM_Python_Project.git
cd QA_Automation_POM_Python_Project
```

### 🔹 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 🔹 3. (Optional) Build and run with Docker Compose:

```bash
docker compose up --abort-on-container-exit --exit-code-from tests
```

### 🔹 4. Alternatively, run directly with Pytest:

```bash
pytest
```

## 🟣 Tests Run Flow

- Tests follow the Page Object Model, accessing page elements through methods defined in page classes.
- The Flask mock server is used in sanity_test.py to avoid placing a real order.
- Logs for each test are generated under logs/.

## 🟣 Docker Compose (optional)

```bash
docker compose up --abort-on-container-exit --exit-code-from tests
```

This command performs the following:

- Initializes a container with all necessary components.
- Initializes a mock server alongside the test environment.
- Initializes and executes the tests.
- Shuts everything down once the tests are finished and exits with the test's exit code.

## 🟣 License

This project is for educational purposes only.
You may use it to practice UI automation with Selenium, Pytest, and POM.
