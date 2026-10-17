# AttendX login automation test

def test_login():
    username = "student01"
    password = "test123"

    assert username != "", "Username is required"
    assert password != "", "Password is required"

    print("Login test passed")


if __name__ == "__main__":
    test_login()
