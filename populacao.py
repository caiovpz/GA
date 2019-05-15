from random import randint


class Cromossomo:
    def __init__(self, rlv, peso):
        self.values = []
        self.imp = []
        self.rlv = rlv
        self.peso = peso
        self.fill(10)                # Preenche o cromossomo
        self.fitness = self.score()  # Calcula o fitness do cromossomo
        pass

    def fill(self, n_cromossomos):
        for i in range(0, n_cromossomos):
            self.values.append(randint(0, 3))
        self.reparar()      # Repara o cromossomo já na criação
        pass

    def reparar(self):
        cst1 = []       # Vetor custo da release 1
        cst2 = []       # Vetor custo da release 2
        cst3 = []       # Vetor custo da release 3
        for n in range(0, 10):  # Separa o cromossomo por release
            if self.values[n] == 0:
                cst1.append(0)
                cst2.append(0)
                cst3.append(0)
            elif self.values[n] == 1:
                cst1.append(self.custo_r[n])
                cst2.append(0)
                cst3.append(0)
            elif self.values[n] == 2:
                cst1.append(0)
                cst2.append(self.custo_r[n])
                cst3.append(0)
            elif self.values[n] == 3:
                cst1.append(0)
                cst2.append(0)
                cst3.append(self.custo_r[n])
        while sum(cst1) > 125:                      # Apaga dos cromossomos as releases de maior custo
            self.values[cst1.index(max(cst1))] = 0
            cst1[cst1.index(max(cst1))] = 0
        while sum(cst2) > 125:
            self.values[cst2.index(max(cst2))] = 0
            cst2[cst2.index(max(cst2))] = 0
        while sum(cst3) > 125:
            self.values[cst3.index(max(cst3))] = 0
            cst3[cst3.index(max(cst3))] = 0
        pass

    def score(self):
        fitness = 0
        for i in range(0,10):
            self.imp.append(0)
            for j in range(0, 10):
                self.imp[i] += self.peso[j] * self.rlv[i][j]
        return fitness




"""     def fitness(self):
            fitness = 0
            for i in range(len(cromossomo)):
                self.importancia.append(0)
                for j in range(len(self.peso)):
                    self.importancia[i] += self.peso[j] * self.relevancia[i][j]
                if cromossomo[i] == 0:
                    y = 0
                else:
                    y = 1
                fitness += (self.importancia[i] * (len(cromossomo[i]) - cromossomo[i] + 1) - self.risco[i] * cromossomo[
                    i]) * y
                self.importancia[i] = 0
            return fitness
           len(cromossomo[i]) - cromossomo[i] deveria ser o len(k) """
