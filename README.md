## Automation project to test UI/API [demoblaze](https://www.demoblaze.com/) website.

Тhe following frameworks have been used in the creation of this project

```
- Pytest-Selenium
- Selene
```

The following Libraries have been used to make writing this test easier

```
- Faker - Library to generate fake data.
- WebDriverManager - Automated driver management.
- busypie - Easy and expressive busy-waiting for Python.
- PyHamcrest - Core API and libraries of hamcrest matcher.
- allure-pytest - Flexible lightweight multi-language test report tool.
- pip - pip is the package installer for Python.
- Flake8 - flake8 is a python tool that glues together pycodestyle, pyflakes, mccabe, and third-party plugins to check 
    the style and quality of some python code.
- Requests - Requests is a simple, yet elegant, HTTP library.
- pytest-tldr - Plugin that gives you minimalist output, in monochrome, while still giving an indication of test suite progress.
- loguru - Loguru is a library which aims to bring enjoyable logging in Python.
```

## How to run

You could use the following command
> pytest -v -s tests/ 
 
## Cross browsing
You can run tests with different browsers. To run tests with specific browser you can change property value in [definitions.py](definitions.py) file.
> browser_name = 'chrome'

Available browsers are:

```
chrome
firefox
```

<p style='color:green'>Note: Selected browser should be installed on your local machine.</p>

### GH_TOKEN

webdriver_manager downloading some webdrivers from their official GitHub repositories but GitHub has [limitations](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting) like 60
requests per hour for unauthenticated users. In case not to face an error related to github credentials, you need to 
[create](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) github token and place it into your environment: (*)

In case you face this issue you can specify `GH_TOKEN` in [definition.py](definition.py) file
> gh_token = ''

# Generating Allure report using pytest
1. In your project directory, you first need to generate a folder to save the allure reports, you can automatically generate this with a command
> allure generate

This will create a folder named allure-report in your project directory.

2. You are now set to run your test with pytest runner by specifying the directory path to save your allure report, for example :
> pytest -v -s tests/ --alluredir=allure-report/

Once test execution completes, all the test results would get stored in allure-report directory.

3. You can now view the allure-report in the browser with the command –
> allure serve allure-report/