import math
from fractions import Fraction

from random import randrange

def solution(pegs):
    # Pegs contains contains anywhere from 2 to 20 points.
    # the locations will be between 1 to 10000
    # The radii of the gears on the pegs must connect from first to last given

    #r = {2 if odd, 2/3 if even} * sum ((-1)^n * x_n + (-1)^(n+1) * x_(n+1)) on n from 1 to i-1
    n = len(pegs);
    if (n < 2): return [-1,-1]
    r = 0;
    a = 0
    b = 1
    for i in range(1,n):
        r +=((-1)**(i))*pegs[i-1] + ((-1)**(i+1))*pegs[i];
        #print("i: {} X{}: {} + X{}: {} + r: {}".format(i,i,pegs[i-1],i+1,pegs[i],r))
    if (len(pegs)%2 == 0):
        if (r%3==0):
            r/=3
            b=1
        else:
            if (r == int(r)):
                b = 3
            else:
                r*=3
                b = 3
    r*=2
    print (r)
    #print (r == int(r))

    a = r;
    # Reduce if possible
    print (a,b)
    if (a%3 == 0 and b ==3):
        a/=3
        b/=3
    # Validate all peg radii
    # r_i = x_(i+1) - x_i - r_(i+1)
    # So: r_(i+1) = x_(i+1) - x_i - r_i
    if a/float(b) < 2:
        print("Failed on a/b < 2")
        return [-1,-1]
    radius = r/float(b)
    for i in range(1,n):
        if (radius < 1):
            print("Failed on radius check {}".format(radius))
            return [-1,-1]

        next_radius = pegs[i] - pegs[i-1] - radius
        print("{} = {} - {} - {}/{}".format(next_radius,pegs[i],pegs[i-1],radius,b))
        radius = next_radius

    return [int(a),int(b)]

def alt_solution(pegs):
    """
            returns the radius of cog i
            ri = Xi -/+ r0
            also sets the ans for the fractional requirement.
        """

    def helper(X, i):
        if i == len(pegs) - 1:  # last cog, we need to make sure its half of r0
            X = 2 * (pegs[i] - pegs[i - 1] - X)
            if i % 2:
                ans[0], ans[1] = [X, 3] if (X) % 3 else [X / 3, 1]
                return X / 6.0
            else:
                ans[0], ans[1] = [-X, 1]
                return -X / 2
        # recursively calculate the radius of next cog
        r_next = helper(pegs[i] - pegs[i - 1] - X, i + 1) if i > 0 else helper(0, 1)

        # radius of r = gap bitween the pegs - r of next cog
        r = pegs[i + 1] - pegs[i] - r_next

        if r < 1:
            ans[0], ans[1] = [-1, -1]
            raise Exception('Invalid Cog')
        return r

    try:
        ans = [-1, -1]
        helper(0, 0)
    finally:
        return ans

class DoomsDayGearValidator:
    def _validate_answer(self,peg_positions,first_radius):
        current_radius = first_radius
        for peg_position, next_position in zip(peg_positions, peg_positions[1:]):
            current_radius = next_position - peg_position - current_radius
        if 2 * current_radius == first_radius:
            return True
        return False

    def _get_random_radius(self):
        return randrange(0,1000)//4

    def _get_randum_n(self):
        return randrange(2,20)

    def _get_radii(self):
        first_radius = randrange(2,100,2)
        radii_random = [self._get_random_radius() for n in range(self._get_randum_n())]
        rs = [first_radius] + radii_random + [int(first_radius/2)]
        newList = [x//4 for x in rs]
        return newList

    def _get_peg_positions_from_radius(self, radii):
        peg_positions = [self._get_random_radius()]
        for radius, next_radius in zip(radii, radii[1:]):
            peg_positions.append(peg_positions[-1] + radius + next_radius)
        return peg_positions

    def _get_test_case(self):
        return self._get_peg_positions_from_radius(self._get_radii())

    def run(self, solution_function, alt_sol, number_of_tests=1000):
        for i in range(number_of_tests):
            pos = self._get_test_case()
            sol = solution_function(pos)
            alt = alt_sol(pos)

            if self._validate_answer(pos, sol[0]/sol[1]) is False and sol != [-1,-1]:
                print("Failed: {}\n My result{} Alt Result:{}".format(pos,sol,alt));
                return False
            print("Passed: {} \nMy Result: {} Alt Result:{}".format(pos, sol,alt));
        return True



# print(solution([4,30,50]))
# print(solution([4,17,50]))
# print(solution([1,51]))
# print(solution([5,10]))
# print(solution([1,31]))
# print(solution([1,31,51,71]))
# print(solution([1,31,51,71,91]))
# print(solution([4,9,17,31,40]))
print(solution([87, 146, 213, 235, 297, 384, 474, 590, 666, 688, 742, 817, 845, 908, 984, 1009]))

validator = DoomsDayGearValidator()

#validator.run(solution_function=solution, alt_sol=alt_solution,number_of_tests=100)
