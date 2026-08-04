from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    BUYABLE = "BUYABLE"
    SELLABLE = "SELLABLE"

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name


@dataclass(frozen=True)
class State:
    action: Action
    cooldown: int


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Map each trading state to the greatest balance that reaches it today.
        today = {State(Action.BUYABLE, 0): 0}

        for price in prices:
            # At the end of each day, cache only the most profitable branch for each state (action and cooldown).
            # Branches in the same state have the same possible future actions. For example, if balances 8 and 5
            # reach the same state, applying the same future actions to both changes their balances by the same
            # amount, so the balance of 8 always remains 3 ahead for the aforementioned same action. The less
            # profitable branch can therefore never become optimal and need not be considered.
            tomorrow = {}

            for state, balance in today.items():
                # Do nothing and advance to the next day.
                resting, total = State(state.action, max(0, state.cooldown - 1)), balance
                tomorrow[resting] = max(tomorrow.get(resting, float("-inf")), balance)

                # Buy if no stock is held and the cooldown has ended.
                if state.action == Action.BUYABLE and state.cooldown <= 0:
                    bought, total = State(Action.SELLABLE, 0), balance - price
                    tomorrow[bought] = max(tomorrow.get(bought, float("-inf")), total)

                # Sell the currently held stock and begin the cooldown.
                if state.action == Action.SELLABLE:
                    sold, total = State(Action.BUYABLE, 1), balance + price
                    tomorrow[sold] = max(tomorrow.get(sold, float("-inf")), total)

            today = tomorrow

        return max(today.values())
