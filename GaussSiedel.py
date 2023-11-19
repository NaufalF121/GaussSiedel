
import sympy as sym

from pprint import pprint
eq = [
    "10*x1 - x2 + 2*x3 - 6",
    "-x1 + 11*x2 - x3 + 3*x4 - 25",
    "2*x1 - x2 + 10*x3 - x4 + 11",
    "3*x2 - x3 + 8*x4 - 15",
]


import copy
import sympy as sym
from pprint import pprint

class Gauss:
    def __init__(self, _val:list) -> None:
        self._val = []
        self.__log = {0:
                      self._val}
    def include (self, __input:list, iter:int):
        self._val = __input
        self.__log[iter]= __input
        
    def output(self):
        return self.__log
class iterate:
    def __init__(self, _eq: list) -> None:
        self.eq = []

        for i in range(len(_eq)):
            _eq[i] = sym.sympify(_eq[i])
            _eq[i] = sym.solve(_eq[i], sym.Symbol(f"x{i + 1}"))[0]

        for i in range(len(_eq) + 1):
            globals()[f"x{i+1}"] = sym.Symbol(f"x{i+1}")

        for i in range(len(_eq)):
            self.eq.append(sym.sympify(str(_eq[i])))

        self.x = {0: ["0"] * len(_eq)}

       
        
    def solve(self, n_iter: int) -> list:
        self.process = Gauss(self.x[0])

        for i in range(n_iter):
            curr = copy.deepcopy(self.x[i])
            for j in range(len(self.eq)):
                subs_dict = {
                    sym.Symbol(f"x{k+1}"): float(curr[k])
                    for k in range(len(curr))
                }

                curr[j] = (self.eq[j].subs(subs_dict).evalf())
            self.x[i+1] = curr
            self.process.include(curr, i+1)

        self.hasil = self.x[n_iter]
    def output(self):
        return self.eq, self.hasil
    def log(self ):
        return self.process.output()
if __name__ == "__main__":
    gauss = iterate(eq)
    gauss.solve(5)
    eq, ans = gauss.output()
    pprint(eq)
    pprint(ans)
    pprint(gauss.log())
