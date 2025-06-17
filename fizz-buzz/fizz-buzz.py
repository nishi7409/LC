class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = list()

        for value in range(1, n+1):
            if value % 3 == 0 and value % 5 == 0:
                result.append("FizzBuzz")
            elif value % 3 == 0 and value % 5 != 0:
                result.append("Fizz")
            elif value % 3 != 0 and value % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(value))
        return result