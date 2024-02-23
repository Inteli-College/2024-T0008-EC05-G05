import json, time
from yaspin import yaspin

class DataMenager:
    def __init__(self, db_path) -> None:
        self.db_path = db_path
        self.loader = yaspin()

    def read_db(self):
        with open(self.db_path, "r") as data_to_read:
            self.db = json.load(data_to_read)
    
    def read_data(self, index:str):
        if(index == None):
            return self.db
        else:
            data_to_handle = self.db[index]
            return data_to_handle   

    def get_data(self, index:str, element:str):
        print(index)
        time.sleep(3)

        match index:
            case "Positions":
                for el in self.read_data(index):
                    if el["name"] == element:
                        return el
            case "Itens":
                print("\nItens\n")
            
    def save_data(self, index:str, data:dict):
        self.db[index].append(data)
        try:
            with open(self.db_path, "w+") as data_to_write:
                json.dump(self.db, data_to_write, indent=4)
                self.loader.ok("\n✅ Dado salvo co sucesso")
        except KeyError:
            self.loader.fail(f"❌ Erro encontrado --> {KeyError}")
        
        time.sleep(1.25)