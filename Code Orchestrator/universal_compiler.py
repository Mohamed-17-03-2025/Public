import re
import subprocess
import tempfile
import os
import shutil

def parse_code_blocks(input_file):

    with open(input_file, 'r') as f:
        content = f.read()
    
    pattern = r'--(\w+) begins--\n(.*?)\n--\1 ends--'
    matches = re.findall(pattern, content, re.DOTALL)
    
    return [(lang.lower(), code.strip()) for lang, code in matches]

def run_java_code(code):
 
    try:

        temp_dir = tempfile.mkdtemp()
        

        java_file = os.path.join(temp_dir, 'Main.java')
        class_file = os.path.join(temp_dir, 'Main.class')
        

        with open(java_file, 'w') as f:
            f.write(code)
        

        compile_result = subprocess.run
        (
            ['javac', java_file],
            capture_output=True, text=True, timeout=10
        )
        
        if compile_result.returncode != 0:
            return f"Java compilation error:\n{compile_result.stderr}"
        

        run_result = subprocess.run
        (
            ['java', '-cp', temp_dir, 'Main'],
            capture_output=True, text=True, timeout=10
        )
        
        if run_result.returncode != 0:
            return f"Java runtime error:\n{run_result.stderr}"
        
        return run_result.stdout
    
    except subprocess.TimeoutExpired:
        return "Java execution timed out"
    
    except Exception as e:
        return f"Java execution failed: {str(e)}"
    
    finally:

        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)

def run_python_code(code):

    try:
        result = subprocess.run
        (
            ['python3', '-c', code],
            capture_output=True, text=True, timeout=10
        )
        
        if result.returncode != 0:
            return f"Python error:\n{result.stderr}"
        return result.stdout
    
    except subprocess.TimeoutExpired:
        return "Python execution timed out"
    
    except Exception as e:
        return f"Python execution failed: {str(e)}"

def run_code_block(lang, code):

    if lang == 'java':
        return run_java_code(code)
    
    elif lang == 'python':
        return run_python_code(code)
    
    else:
        return f"Unsupported language: {lang}"

def main(input_file):

    try:
        
        blocks = parse_code_blocks(input_file)
        
        if not blocks:
            print("No valid code blocks found.")
            return
        
        for lang, code in blocks:
            print(f"\nRunning {lang.upper()} code:")
            print("-" * 40)
            print(code)
            print("-" * 40)
            output = run_code_block(lang, code)
            print("Output:")
            print(output)
            print("=" * 40)
    
    except FileNotFoundError:
        print(f"Input file {input_file} not found.")
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":

    import sys
    if len(sys.argv) != 2:
        print("Usage: python universal_compiler.py <input_file>")
    else:
        main(sys.argv[1])
