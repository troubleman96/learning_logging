import logging

logging.basicConfig(filename="employee.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s"
                    )

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info(f"Employee created: {self.fullname} - {self.email}")

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com".lower()

emp_1 = Employee("juma", "Doe")
emp_2 = Employee("jane", "Smith")