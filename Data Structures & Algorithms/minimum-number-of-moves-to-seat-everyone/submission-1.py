class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        result = 0

        for seat, student in zip(sorted(seats), sorted(students)):
            result += abs(seat - student)

        return result
