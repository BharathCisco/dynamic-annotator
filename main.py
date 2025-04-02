import os
import sys
import re
import json
import importlib.util
from beartype import beartype
import traceback

def remove_ansi_escape_sequences(text):
    """Remove ANSI escape sequences from a string."""
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def apply_beartype(file_path):
    print(f"Applying @beartype to functions in {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        updated_lines = []
        has_beartype_import = any("from beartype import beartype" in line for line in lines)
        func_pattern = re.compile(r'^\s*def\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\(.*\)\s*->\s*[a-zA-Z_][a-zA-Z0-9_]*\s*:')

        if not has_beartype_import:
            updated_lines.append("from beartype import beartype\n\n")

        for i, line in enumerate(lines):
            if func_pattern.match(line):
                if i > 0 and "@beartype" in lines[i - 1]:
                    updated_lines.append(line)
                else:
                    updated_lines.append("@beartype\n" + line)
            else:
                updated_lines.append(line)

        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(updated_lines)

        return {"status": "Applied @beartype decorators successfully"}
    except Exception as e:
        return {"error": str(e)}

def import_and_test_module(module_path):
    errors = {}
    module_name = os.path.splitext(os.path.basename(module_path))[0]
    repo_dir = os.path.dirname(module_path)
    sys.path.insert(0, repo_dir)

    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec and spec.loader:
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except ModuleNotFoundError as e:
            errors["import_error"] = f"ModuleNotFoundError: {e}"
            return errors
        except Exception as e:
            errors["import_error"] = f"Other Import Error: {remove_ansi_escape_sequences(str(e))}"
            return errors

        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if callable(attr) and hasattr(attr, "__annotations__"):
                try:
                    param_types = list(attr.__annotations__.values())
                    if param_types:
                        test_args = [None] * (len(param_types) - 1)
                        attr(*test_args)
                except TypeError as e:
                    errors[attr_name] = remove_ansi_escape_sequences(str(e))
    return errors

def analyze_repo(repo_path):
    print(f"Analyzing repository: {repo_path}")
    analysis_results = {}

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                beartype_result = apply_beartype(file_path)
                errors = import_and_test_module(file_path)

                analysis_results[file_path] = {
                    "apply_beartype": beartype_result,
                    "type_errors": errors if errors else "No errors found"
                }

    with open("dynamic_results.json", "w", encoding="utf-8") as f:
        json.dump(analysis_results, f, indent=4)

    print("Results saved in dynamic_results.json")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dynamic.py <repo_path>")
        sys.exit(1)

    repo_path = sys.argv[1]
    analyze_repo(repo_path)
