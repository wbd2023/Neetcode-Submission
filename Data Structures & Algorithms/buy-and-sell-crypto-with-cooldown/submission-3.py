from enum import Enum


class Solution:
    class Action(Enum):
        BUYABLE = "BUYABLE"
        SELLABLE = "SELLABLE"

        def __repr__(self) -> str:
            return self.name

        def __str__(self) -> str:
            return self.name

    def maxProfit(self, prices: List[int]) -> int:
        # (total, action, cooldown)
        states = deque([(0, self.Action.BUYABLE, 0)])

        memo = {}

        for price in prices:
            n = 1
            length = len(states)

            while n <= length:
                total, action, cooldown = states.popleft()

                states.append((total, action, cooldown - 1 if cooldown > 0 else 0))
                n += 1

                if action == self.Action.BUYABLE and cooldown <= 0:
                    states.append((total - price, self.Action.SELLABLE, 0))

                if action == self.Action.SELLABLE:
                    states.append((total + price, self.Action.BUYABLE, 1))

        return max(total for total, *_ in states)
