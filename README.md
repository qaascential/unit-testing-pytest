# unit-testing-pytest
Unit testing using Pytest for Python.

## How to install?

#### Prerequisites:
```python
execute --> pip install -r requirements.txt (inside src folder)
```

### In Linux:

#### 1: Go to the src folder:

#### 2: Activate environment:

```python
source venv_test/bin/activate
```

#### 3: Run tests:

```python
pytest
```
#### 4. Run Allure Report:

```python
py.test --alluredir=allure_result
allure serve allure_result/
```

| Python Venv Active - Differents OS                                             |
| ------------------------------------------------------------------------------ |
| On Unix or MacOS, using the bash shell: source /path/to/venv/bin/activate      |
| On Unix or MacOS, using the csh shell: source /path/to/venv/bin/activate.csh   |
| On Unix or MacOS, using the fish shell: source /path/to/venv/bin/activate.fish |
| On Windows using the Command Prompt: path\to\venv\Scripts\activate.bat         |
| On Windows using PowerShell: path\to\venv\Scripts\Activate.ps1                 |

[About Venv](https://www.infoworld.com/article/3239675/virtualenv-and-venv-python-virtual-environments-explained.html)
