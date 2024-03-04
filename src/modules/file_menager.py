import json, time
from yaspin import yaspin

class DataMenager:
    def __init__(self, db_path) -> None:
        # Inicializa o caminho do banco de dados e o loader para exibir o status de carregamento
        self.db_path = db_path
        self.loader = yaspin()

    def read_db(self):
        # Lê o banco de dados do arquivo JSON
        with open(self.db_path, "r") as data_to_read:
            self.db = json.load(data_to_read)
    
    def read_data(self, index:str):
        # Lê os dados do banco de dados para um índice específico
        if(index == None):
            return self.db
        else:
            data_to_handle = self.db[index]
            return data_to_handle   

    def get_data(self, index:str, element:str):
        # Obtém dados específicos do banco de dados com base no índice e no elemento
        print(index)
        time.sleep(3)

        # Utiliza a sintaxe de correspondência de padrões para diferentes índices
        match index:
            case "Positions":
                # Se o índice for "Positions", procura pelo elemento especificado
                for el in self.read_data(index):
                    if el["name"] == element:
                        return el
            case "Itens":
                # Se o índice for "Itens", imprime uma mensagem indicando isso
                print("\nItens\n")
            
    def save_data(self, index:str, data:dict):
        # Salva os dados fornecidos no banco de dados para o índice especificado
        self.db[index].append(data)
        try:
            # Tenta escrever os dados atualizados de volta no arquivo JSON
            with open(self.db_path, "w+") as data_to_write:
                json.dump(self.db, data_to_write, indent=4)
                self.loader.ok("\n✅ Dado salvo co sucesso")
        except KeyError:
            # Se ocorrer um erro de chave, exibe uma mensagem de falha
            self.loader.fail(f"❌ Erro encontrado --> {KeyError}")
        
        time.sleep(1.25)
