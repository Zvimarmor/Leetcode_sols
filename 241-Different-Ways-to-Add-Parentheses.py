class Solution(object):
    def diffWaysToCompute(self, expression):
        \\\
        :type expression: str
        :rtype: List[int]
        \\\
        answer_dict = dict()

        def helper(expression):
            if expression in answer_dict:
                return answer_dict[expression]

            length = len(expression)

            results = []

            for i in range(length):
                if expression[i] in '+-*':
                    rights = helper(expression[i+1:])
                    lefts = helper(expression[:i])

                    for left in lefts:
                        for right in rights:
                            if expression[i] == '+':
                                results.append(left+right)
                            elif expression[i] == '-':
                                results.append(left-right)
                            elif expression[i] == '*':
                                results.append(left*right)

            #recursion stopping point
            if not results:
                results.append(int(expression))

            answer_dict[expression] = results
            return results

        return helper(expression)
                

                    

        