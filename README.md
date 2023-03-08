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
