class Cliente:
    def __init__(self, 
                 nome: str, 
                 idade: int, 
                 renda: float, 
                 score_bvs: int | None, 
                 score_serasa: int | None, 
                 score_quod: int | None
                 ):
        self.nome = nome
        self.idade = idade
        self.renda = renda
        self.score_bvs = score_bvs
        self.score_serasa = score_serasa
        self.score_quod = score_quod