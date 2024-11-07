# from testable import to_call
import os


def test_pytest_installed():
    assert os.getcwd() == "/app/share/leaftracker-gtk/leaftracker_gtk_tests"
    # assert to_call()
