from applications import salary as s
from applications.db import people as p

if __name__ == '__main__':
    s.calculate_salary()
    p.get_employees()