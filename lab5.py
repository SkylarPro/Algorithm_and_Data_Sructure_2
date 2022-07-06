import random
import time
MAXPOP = 25

class DiophantineAlg:
    class Gen:
        def __init__(self):
            self.alleles = [random.randrange(30) for _ in range(4)]
            self.fitness = -1
            self.likelihood = -1.0

        def __eq__(self, other):
            for i in range(4):
                if self.alleles != other.alleles:
                    return False
            return True

        def __add__(self, other):
            return self.fitness + other

        def __radd__(self, other):
            return self.fitness + other

    def __init__(self, a, b, c,d, res):
        self.koef = [a, b, c,d]
        self.result = res
        self.population = [self.Gen() for _ in range(MAXPOP)]
        self.rnd_max = 5 * 10 ** 4
        self.n_iteration = 150
        self.res_idx = None
        self.n_iter_res = None

    def GetGen(self, idx):
        return self.population[idx]

    def Fitness(self, gen):
        """Считаем разницу между ответом и 'приближенным решением' для гена"""
        total = sum([allel * koef for allel, koef in zip(gen.alleles, self.koef)])
        gen.fitness = abs(total - self.result)
        return gen.fitness

    def CreateFitnesses(self):
        """
        Считаем для всех генов func Fitness
        :return: idx если решением найдено, else 0
        """
        avgfit = 0
        for idx in range(MAXPOP):
            fitness = self.Fitness(self.population[idx])
            avgfit += fitness
            if fitness == 0:
                return idx
        print(avgfit)
        return -1

    def MultInv(self):
        """Считаем коэффицент для func GenerateLikelihoods"""
        sum = 0
        for gen in self.population:
            sum += 1 / gen.fitness
        return sum

    def GenerateLikelihoods(self):
        """
        Cчитает для каждого решения вероятность пренадлежать решению
        :return:
        """
        multinv = self.MultInv()
        last = 0
        for idx in range(MAXPOP):
            self.population[idx].likelihood = last = last + ((1 / self.population[idx].fitness / multinv) * 100)

    def GetIndex(self, val):
        """

        :param val: вероятность от 0 до 100
        :return: Возращает ту попоуляцию в диапозон likelihood которой попал  val
        """
        last = 0
        for idx in range(MAXPOP):
            if (last <= val and self.population[idx].likelihood):
                return idx
            else:
                last = self.population[idx].likelihood
        return 4

    def Breed(self, parent1, parent2):
        """
        Делаем мутацию гена с 5% вероятностью и остальные гены скрещиваем от родителей. Изначально
         все гены идут от одного родителя
        :param parent1: idx первого родителя
        :param parent2: idx второго родителя
        :return: мутанта
        """

        crossover = random.randrange(self.rnd_max) % 3 + 1
        first = random.randrange(self.rnd_max) % 100

        child = self.population[parent1]
        initial, final = 0, 3
        if first < 50:
            initial = crossover
        else:
            final = crossover + 1
        for idx in range(initial, final):
            child.alleles[idx] = self.population[parent2].alleles[idx]
            if random.randrange(self.rnd_max) % 101 < 5:
                child.alleles[idx] = random.randrange(self.rnd_max) % (self.result + 1)

        return child

    def CreateNewPopulation(self):
        new_population = [self.Gen() for _ in range(MAXPOP)]
        for idx in range(MAXPOP):
            parent1, parent2, iter = 0, 0, 0
            while (parent1 == parent2) or (self.population[parent1] == self.population[parent2]):
                parent1 = self.GetIndex(random.randrange(self.rnd_max) % 101)
                parent2 = self.GetIndex(random.randrange(self.rnd_max) % 101)
                if (iter > MAXPOP**2):
                    break
                iter+=1

            new_population[idx] = self.Breed(parent1, parent2)

        for idx in range(MAXPOP):
            self.population[idx] = new_population[idx]

    def Solve(self):
        fitness = self.CreateFitnesses()
        iteration = 0
        if fitness != -1:
            self.res_idx = fitness
            self.n_iter_res = iteration
            return True
        while fitness == -1 or iteration < self.n_iteration:
            self.GenerateLikelihoods()
            self.CreateNewPopulation()
            fitness = self.CreateFitnesses()
            if fitness != -1:
                print("OK")
                self.res_idx = fitness
                self.n_iter_res = iteration
                return True
            iteration += 1
        return False

    @property
    def get_param(self):
        if not self.res_idx is None:
            return self.population[self.res_idx].alleles, self.n_iter_res
        else:
            return None

if __name__ == "__main__":
    alg = DiophantineAlg(1, 2, 3,4, 30)
    start = time.time()
    alg.Solve()
    stop = time.time()
    print(stop - start)
    print(alg.get_param)
