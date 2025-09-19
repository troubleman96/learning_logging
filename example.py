import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

file_handler = logging.FileHandler("employee.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)




class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f"Employee created: {self.fullname} - {self.email}")

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com".lower()

emp_1 = Employee("juma", "Doe")
emp_2 = Employee("jane", "Smith")