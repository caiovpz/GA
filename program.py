from populacao import Cromossomo
import copy


class AG:
    def __init__(self):
        self.custo_r = [60, 40, 40, 30, 20, 20, 25, 70, 50, 20]  # Custo por release
        self.importancia = []
        self.relevancia = [[10, 8, 6, 5, 7, 8, 6, 9, 6, 10],
                           [10, 10, 4, 9, 7, 6, 6, 8, 7, 10],
                           [5, 6, 8, 1, 5, 2, 4, 3, 5, 7]]       # Matriz relevância (v)
        self.risco = [3, 6, 2, 6, 4, 8, 9, 7, 6, 6]              # Risco por release
        self.cromossomo = []
        self.n_gen = 0
        self.taxa_mut = 0

        # Fazer as coisas acontecerem
        self.initpop(self)
        self.crossover(self)
        self.mutacao(self)
        self.selecao(self)
        # Fazer as coisas acontecerem
        pass

    def initpop(self):
        for i in range(0, 10):
            self.cromossomo.append(Cromossomo(self.relevancia))
#           self.score.append(AG.fitness(self.cromossomo[i]))

    def crossover(self, cromossomo):
        pass

    def mutacao(self, cromossomo, taxa_mut):
        pass

    def selecao(self, cromossomo):
        pass

    def newgen(self):
        self.n_gen += 1
        for i in range(0, len(self.cromossomo)):
            self.cromossomo.append(copy.deepcopy(self.cromossomo[i]))  # Cria uma nova geração
        pass


if __name__ == '__main__':
    ag = AG()
    ag.initpop()
    for n in range(0, 10):
        print(ag.cromossomo[n].values)