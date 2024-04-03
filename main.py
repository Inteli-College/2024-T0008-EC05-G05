try:
    from os import system
    import platform

except ImportError as e:
    print(e)


os_type = platform.system()


def execute_codes() -> None:
    if os_type == "Windows":
        try:
            system("C:/Users/caiot/Documents/GitHub/2024-T0008-EC05-G05/src/controllers/windows_starter.bat")
        except FileNotFoundError as e:
            print(e)
    elif os_type == "Linux":
        try:
            system("cd /home/caio/Documents/GitHub/2024-T0008-EC05-G05/src/controllers/linux_starter.sh")
        except FileNotFoundError as e:
            print(e)
    else:
        print("OS not supported")



if __name__ == "__main__":
    execute_codes() 