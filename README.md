# Python Logging Tutorial

This repository contains a comprehensive tutorial on Python logging, demonstrating various logging concepts and best practices.

## 📋 Overview

This tutorial covers:
- Basic logging setup and configuration
- Custom logger creation
- File handlers and formatters
- Multi-module logging
- Log level management
- Real-world examples with Employee class and mathematical operations

## 📁 Project Structure

```
logging/
├── README.md           # This file
├── example.py          # Employee class with logging
├── tut.py             # Main tutorial with mathematical operations
├── employee.log       # Log file for Employee operations
├── app.log           # Log file for mathematical operations
└── __pycache__/      # Python cache directory
```

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Basic understanding of Python classes and functions

### Running the Tutorial

1. **Clone or download this repository**
   ```bash
   cd /path/to/logging/tutorial
   ```

2. **Run the main tutorial**
   ```bash
   python3 tut.py
   ```

3. **Run the employee example separately**
   ```bash
   python3 example.py
   ```

## 📚 Tutorial Components

### 1. Employee Logger (`example.py`)

This module demonstrates:
- Creating a named logger using `__name__`
- Setting log levels (INFO)
- Custom formatting with timestamps
- File handler configuration
- Property-based logging in classes

**Features:**
- Logs employee creation events
- Captures full name and email generation
- Writes to `employee.log`

**Sample Output:**
```
2025-09-19 10:19:48,533 - example - INFO - Employee created: juma Doe - juma.doe@company.com
2025-09-19 10:19:48,533 - example - INFO - Employee created: jane Smith - jane.smith@company.com
```

### 2. Mathematical Operations Logger (`tut.py`)

This module demonstrates:
- DEBUG level logging
- Multi-operation logging
- Module importing with logging
- Comprehensive mathematical function logging

**Features:**
- Four basic mathematical operations (add, subtract, multiply, divide)
- DEBUG-level result logging
- Integration with the Employee module
- Writes to `app.log`

**Sample Output:**
```
2025-09-19 10:27:11,197 - __main__ - DEBUG - Addition Result: 19
2025-09-19 10:27:11,197 - __main__ - DEBUG - Subtraction Result: 3
2025-09-19 10:27:11,197 - __main__ - DEBUG - Multiplication Result: 88
2025-09-19 10:27:11,197 - __main__ - DEBUG - Division Result: 1.375
```

## 🔧 Key Concepts Demonstrated

### Logger Configuration
```python
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
```

### Custom Formatting
```python
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```

### File Handler Setup
```python
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
```

### Log Levels Used
- **INFO**: For significant events (employee creation)
- **DEBUG**: For detailed diagnostic information (calculation results)

## 📖 Learning Outcomes

After completing this tutorial, you will understand:

1. **Basic Logging Setup**: How to configure loggers, handlers, and formatters
2. **Log Levels**: When to use INFO vs DEBUG vs other levels
3. **File Logging**: How to write logs to files for persistence
4. **Multi-Module Logging**: How logging works across different Python modules
5. **Custom Formatters**: How to create meaningful log message formats
6. **Real-World Applications**: Practical examples of logging in classes and functions

## 🛠️ Customization

You can modify this tutorial by:

- Changing log levels in either file
- Adding console handlers for terminal output
- Implementing rotating file handlers
- Adding more complex formatting
- Including additional log levels (WARNING, ERROR, CRITICAL)

### Adding Console Output

To also see logs in the terminal, add a console handler:

```python
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
```

## 📝 Common Issues and Solutions

### Issue: "No attribute 'debug'" Error
**Solution**: Ensure your file is not named `logging.py` as this shadows the built-in logging module.

### Issue: No log files generated
**Solution**: Check file permissions and ensure the script has write access to the directory.

### Issue: Logs not appearing
**Solution**: Verify log levels - DEBUG messages won't appear if logger is set to INFO level.

## 🔗 Additional Resources

- [Python Logging Documentation](https://docs.python.org/3/library/logging.html)
- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)
- [Real Python Logging Guide](https://realpython.com/python-logging/)

## 📄 License

This tutorial is provided for educational purposes. Feel free to use and modify as needed.

---

*Happy Learning! 🐍*