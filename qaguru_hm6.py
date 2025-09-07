from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=23)
    if 6 <= current_time.hour >= 22:
        is_dark_theme = True
        print("Dark theme disabled!")

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user == True:
        is_dark_theme = True
        print('Dark theme enabled by user.')
    elif dark_theme_enabled_by_user == None:
        if 6 <= current_time.hour >= 22:
            is_dark_theme = True
            print("Dark theme enabled.")
        else:
            is_dark_theme = False
            print('Dark theme disabled.')
    else:
        is_dark_theme = False
        print('Dark theme disabled by user.')

    assert is_dark_theme is True


def test_find_suitable_user():

    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    for suitable_users in users:
        if suitable_users['name'] == 'Olga':
            print(suitable_users)

            assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = list(filter(lambda user: user["age"] > 30, users))
    print(suitable_users)

    assert suitable_users == [
        {"name": "Oleg", "age": 32},
        {"name": "Olga", "age": 45},
    ]


def print_readable(func, *args, **kwargs):
    name = func.__name__.replace('_', ' ').title()
    values = list(args) + [f"{v}" for v in kwargs.values()]
    result = f"{name} [{', '.join(values)}]"
    print(result)
    return result


def open_browser(browser_name):
    print_function_name_and_args(open_browser, browser_name)


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    print_function_name_and_args(open_browser, browser_name)
    actual_result =  print_function_name_and_args(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result =  print_function_name_and_args(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result =  print_function_name_and_args(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"