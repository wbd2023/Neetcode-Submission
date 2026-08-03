from enum import auto, Enum


class Solution:
    class Action(Enum):
        BUYABLE = "BUYABLE"
        SELLABLE = "SELLABLE"

        def __repr__(self) -> str:
            return f"{self.name}"

        def __str__(self) -> str:
            return f"{self.name}"

    def maxProfit(self, prices: List[int]) -> int:
        states = deque()
        states.append((0, self.Action.BUYABLE, 0))  # (price, action, cooldown)

        memo = {}

        for price in prices:
            # print(price)
            # print(states)

            n, length = 1, len(states)

            while n <= length:
                total, action, cooldown = states.popleft()

                # print(total, action, cooldown)

                states.append((total, action, cooldown - 1))
                n += 1

                if action == self.Action.BUYABLE and cooldown <= 0:
                    states.append((total - price, self.Action.SELLABLE, 0))

                if action == self.Action.SELLABLE:
                    states.append((total + price, self.Action.BUYABLE, 1))

            # print(states)
            # print()

        return max([total for total, *_ in states])
