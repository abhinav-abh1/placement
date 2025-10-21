# test_script.py
# Author: Abhinav A
# Purpose: Basic Python test to verify environment setup and code execution.

import datetime
import platform


def test_environment():
    print("✅ Python Environment Test Successful!")
    print("-" * 40)
    print(f"Python Version: {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Current Date & Time: {datetime.datetime.now()}")
    print("-" * 40)


def add_numbers(a, b):
    """Simple function to test logic"""
    return a + b


def main():
    test_environment()
    x, y = 10, 25
    print(f"🧮 Testing addition: {x} + {y} = {add_numbers(x, y)}")


if __name__ == "__main__":
    main()
