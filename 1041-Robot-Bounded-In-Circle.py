class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        def update_current_D(current, D, inst):
            if inst == 'G':
                if D == 0:
                    current = (current[0],current[1]+1)
                if D == 1:
                    current = (current[0]+1,current[1] )
                if D == 2:
                    current = (current[0],current[1]-1)
                if D == 3:
                    current = (current[0]-1,current[1])
            elif inst == 'R':
                D += 1
                D %= 4
            elif inst == 'L':
                D -= 1
                D %= 4
            
            return current, D

        current = (0, 0)  # Starting position
        D = 0  # Starting direction: 0 = north, 1 = east, 2 = south, 3 = west

        # Process the instructions once
        for inst in instructions:
            current, D = update_current_D(current, D, inst)

        # The robot is bounded if:
        # 1. It returns to the origin (0, 0).
        # 2. It doesn't face north after one cycle (indicating it will loop eventually).
        return current == (0, 0) or D != 0