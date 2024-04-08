try:
    import os
    import platform

except ImportError as e:
    print(e)


os_type = platform.system()


def execute_codes() -> None:
     # Get the current directory path
    raw_current_dir_path = os.getcwd()
    current_dir_path = raw_current_dir_path.replace("\\", "/")

    print(current_dir_path)
    
    if os_type == "Windows":
        try:
            os.system(f"{current_dir_path}/src/controllers/windows_starter.bat")
        except FileNotFoundError as e:
            print(e)
    elif os_type == "Linux":
        try:
            os.system(f"{current_dir_path}/src/controllers/linux_starter.bat")
        except FileNotFoundError as e:
            print(e)
    else:
        print("OS not supported")



if __name__ == "__main__":
    execute_codes() 