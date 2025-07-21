class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = list()

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = index-stack_index
            stack.append([temp, index])
        return result
        
        # result = list()
        # for first_day in range(len(temperatures)):
        #     flag = False

        #     # 22
        #     current_temperature = temperatures[first_day]

        #     counter = 0
        #     for next_day in range(first_day+1, len(temperatures)):
        #         counter += 1

        #         # 21
        #         next_temperature = temperatures[next_day]

        #         if current_temperature < next_temperature:
        #             result.append(counter)
        #             flag = True
        #             break
                
            
        #     if flag == False:
        #         result.append(0)
        # return result