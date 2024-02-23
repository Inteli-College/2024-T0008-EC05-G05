from modules import *
bot = CardioBot("src/data.json")

def main():
    bot.read_db()

    inputs = [
        inquirer.List("Inputs", choices=["Connect", "Move", "Go to Position","Get position", "Sequantial", "Save Position", "Save Item", "Save Kit", "Restart", "Disconnect", "Exit"])
        ]

    answer = inquirer.prompt(inputs)
    action = answer["Inputs"]


    def move_bot():
                print("Iniciando leirura")
                bot.loader.start()
                sleep(1.5)
                bot.loader.stop()

                x = float(input("X : "))
                y = float(input("Y : "))
                z = float(input("Z : "))
                r = float(input("R : "))

                movement = {
                    "x" : x,
                    "y" : y,
                    "z" : z,
                    "r" : r
                }
            
                try:
                    bot.move(movement)
                except:
                    bot.loader.fail("❌ Dispositivo desconectado")
                    sleep(1.5)
                    bot.connect()
                    main()


    match action:

    
        case "Disconnect":
            bot.disconnect()
        

        case "Connect":
            bot.connect()
        

        case "Move":
            move_bot()

        case "Go to Position":
            seted_position = bot.read_data("Positions")
            positions = []
            for i in seted_position:
                positions.append(i["name"])

            position_choice = [
                inquirer.List(
                    "Position", choices=positions
                )
            ]

            prompt = inquirer.prompt(position_choice)
            position = prompt["Position"]

            print(position)

            movement = bot.get_data(index="Positions", element=position)
            
            index = movement["cordenates"]
            jump  = movement["jump-factor"]
            
            cordenates = {
                "x" : index["x"],
                "y" : index["y"],
                "z" : index["z"],
                "r" : index["r"]
            }

            bot.move(cordenates, jump)


        case "Get position":
            print(bot.get_position())
            

        case "Save Position":
            actual_position = bot.get_position()
            name = input("\nQual o nome da posição : ")
            jump_factor = float(input("Fator de pulo da movimentação : "))


            position_data = {
                "name" : name,
                "cordenates" : actual_position,
                "jump-factor" : jump_factor
            }

            bot.save_data("Positions", position_data)

        
        case "Save Item":
            name = input("\nNome do item : ")
            seted_position = bot.read_data("Positions")

            positions = []
            for i in seted_position:
                positions.append(i["name"])

            position_choice = [
                inquirer.List(
                    "Position", choices=positions
                )
            ]

            prompt = inquirer.prompt(position_choice)
            item_position = prompt["Position"]

            new_item = {
                "name" : name,
                "position" : item_position,
                "cad-date" : localtime()
            }

            bot.save_data("Itens", new_item)


        
        case "Save Kit":
            add:bool = True

            print("\nCriando um novo kit\n")
            sleep(0.5)
            name = input("Nome do kit : ")
            saved_itens = bot.read_data("Itens")
            
            itens_to_select = ["Finalizar", "Adicionar novo item"]
            for i in saved_itens:
                itens_to_select.append(i["name"])


            itens = [
                inquirer.List(
                    "Itens",
                    choices=itens_to_select)
            ]

            selected_itens:list = []

            # while add == True:
            #     prompt = inquirer.prompt(itens)
            #     if(prompt["Itens"] == "Finalizar"):
            #         add = False
            #     elif(prompt["Itens"] == "Adicionar novo item"):
            #         pass

            #     quant = int(input("Quantidade desse item no kit : "))

            # itens_quant:dict = {
            #     "item" : prompt["Itens"],
            #     "quant" : quant
            # }

            # selected_itens.append(itens_quant)





            kit_to_save:dict = {
                "name" : name,
                "itens" : selected_itens
            }    
            
            print(kit_to_save)

            bot.save_data("Kits", kit_to_save)


        case "Restart":
            python = sys.executable
            os.execl(python, python, * sys.argv)


        case "Exit":
            print("Fechando programa")
            bot.loader.start()
            sleep(1.2)
            bot.loop = False
            bot.disconnect()
            bot.loader.stop()
            sleep(0.1)
            exit()
        

if __name__ == "__main__":
    while(bot.loop == True):
        main()