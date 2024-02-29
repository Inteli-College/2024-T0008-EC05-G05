from . import DataMenager

class KitsMenager(DataMenager):
    def __init__(self, db_path) -> None:
        super().__init__(db_path)