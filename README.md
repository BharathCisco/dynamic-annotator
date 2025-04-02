# Dynamic Annotation Tools

This repository compares three dynamic annotation tools for Python:

1. **beartype**  
2.  
3. 

---

# Dynamuc Annotation Tools Comparison

## 📚 Summary of Findings
- All three tools (**beartype**, ) successfully identified issues related to:
    - Undefined variables.
    - Type mismatches in return values.
    - Attribute errors.

---

## 🛠️ Tool Breakdown

### ✔️ BearType
- Highly customizable using `mypy.ini` to:
    - Ignore paths.
    - Modify strictness.
- Suitable for large-scale projects with gradual typing.



## 📚 Test Results while scanning taskManagerCli
### ✅ `repo scan` Results
```json
{
    ".\\taskManagmentCli\\main.py": {
        "apply_beartype": {
            "status": "Applied @beartype decorators successfully"
        }
    },
    ".\\taskManagmentCli\\task_manager.py": {
        "apply_beartype": {
            "status": "Applied @beartype decorators successfully"
        }
    }
}
```

### ✅ `with introduced error for testing` Results
```json
{
    ".\\taskManagmentCli\\main.py": {
        "apply_beartype": {
            "status": "Applied @beartype decorators successfully"
        },
        "type_errors": {
            "import_error": "Other Import Error: Function task_manager.add_number() parameter a='1' violates type hint <class 'int'>, as str '1' not instance of int."
        }
    },
    ".\\taskManagmentCli\\task_manager.py": {
        "apply_beartype": {
            "status": "Applied @beartype decorators successfully"
        },
        "type_errors": {
            "import_error": "Other Import Error: Function task_manager.add_number() parameter a='1' violates type hint <class 'int'>, as str '1' not instance of int."
        }
    }
}
```

