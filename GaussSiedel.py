
import sympy as sym

from pprint import pprint
eq = [
    "10*x1 - x2 + 2*x3 - 6",
    "-x1 + 11*x2 - x3 + 3*x4 - 25",
    "2*x1 - x2 + 10*x3 - x4 + 11",
    "3*x2 - x3 + 8*x4 - 15",
]

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

        self.__log_iter = {
            0: {
                "iter": 0,
                "xi": self.x[0],
            }
        }
    def solve(self, n_iter: int) -> list:
        for i in range(n_iter):
            curr = self.x[i]
            for j in range(len(self.eq)):
                subs_dict = {
                    sym.Symbol(f"x{k+1}"): float(curr[k])
                    for k in range(len(curr))
                }

                curr[j] = (self.eq[j].subs(subs_dict).evalf())
            
            self.x[i+1] = curr
            self.__log_iter[i + 1] = {
                "iter": i + 1,
                "xi": self.x[i + 1],
            }

        return self.x[n_iter]
    def output(self):
        return self.eq, self.x
    

if __name__ == "__main__":
    jacobi = iterate(eq)
    pprint(jacobi.solve(5))
