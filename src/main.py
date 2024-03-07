from  modules import *


def __connect(): # connects the arm to the computer
    start_spiner("Connecting Arm...", 1.5)
    try:
        available_ports = list_ports.comports() 
        port = available_ports[0].device 

        global bot # Globalize the variable 
        bot = CardioBot(port, False)

        success_message("Arm connected with success :)")
    except KeyError as e:
        fail_message(f'{e}')


def main(): # Loop

    start_spiner("Carregando commandos")

    # Command options
    options = inquirer.prompt([
        inquirer.List("CLI", "Chose your command", ["Connect Arm", "Home", "Acutal Position", "Move Linear", "Move Join", "Tougle Tool Status", "Diconnect Arm", "Exit Program"])
    ])["CLI"]


    match options: # Matchs the command
        case "Connect Arm":
            __connect()
        
        case "Home":
            start_spiner("Backing to home position...", 1)
            try:
                bot.home()
            except Exception as e:
                fail_message(f"{e}", 1.5)
                __connect()
                bot.home()

        case "Acutal Position":
            start_spiner("Getting arm actual positions...", 1)
            try:
                x,y,z,r,j1,j2,j3,j4 = bot.pose()
                print(f"Arm in --> X:{x} Y:{y} Z:{z} R:{r}")
            except:
                __connect()
                x,y,z,r,j1,j2,j3,j4 = bot.pose()
                print(f"Arm in --> X:{x} Y:{y} Z:{z} R:{r}")


        case "Move Linear":
            try:
                x = float(input("X : "))
                y = float(input("Y : "))
                z = float(input("Z : "))
                r = float(input("R : "))

                bot._move_l(x,y,z,r)
                success_message()
                
            except Exception as e:
                fail_message(f"{e}", 1.5)
                __connect()
                bot._move_l(x,y,z,r)
                

        case "Move Join":
            try:
                x = float(input("X : "))
                y = float(input("Y : "))
                z = float(input("Z : "))
                r = float(input("R : "))

                bot._move_j(x,y,z,r)
            except Exception as e:
                fail_message(f"{e}", 1.5)
                try:
                    __connect()
                except:
                    bot
                bot._move_j(x,y,z,r)


        case "Tougle Tool Status":
            try:
                # Displays the tools choice to be tougled
                tool = inquirer.prompt(
                    [inquirer.List("Tool", message="Chose the current tool", choices=["Suck", "Grip"])]
                )["Tool"].lower()

                bot.tougle_tool(tool=tool)
            except Exception as e:
                fail_message(f"{e}", 1.5)
                __connect()
        

        case "Exit Program":
            start_spiner("Exiting...", 1.5)
            try:
                bot.home()
                exit()
            except Exception as e:
                fail_message(f"{e}", 1.5)
                __connect()
                bot.home()
                exit()
                

    main() # Recursive to mantain the loop


if __name__ == "__main__":
    main()