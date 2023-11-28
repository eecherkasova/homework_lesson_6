from datetime import time


def test_dark_theme_by_time():
    current_time = time(hour=23)

    if time(hour=6) < current_time < time(hour=22):
        is_dark_theme = False
    else:
        is_dark_theme = True

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    current_time = time(hour=23)
    dark_theme_enabled_by_user = None

    if dark_theme_enabled_by_user:
        is_dark_theme = True
    elif dark_theme_enabled_by_user is None:
        if time(hour=6) < current_time < time(hour=22):
            is_dark_theme = False
        else:
            is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user_by_name():
    suitable_users = []
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    for user in users:
        if user["name"] == "Olga":
            suitable_users = user
            break

    assert suitable_users == {"name": "Olga", "age": 45}


def test_find_suitable_user_by_age():
    suitable_users = []

    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)


    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


def return_readable_name(func, *args):
    func_name = func.__name__.replace("_", " ").title()
    args_name = ", ".join([*args])
    print(f"{func_name} [{args_name}]")
    return f"{func_name} [{args_name}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = return_readable_name(open_browser, "Chrome")
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = return_readable_name(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = return_readable_name(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
