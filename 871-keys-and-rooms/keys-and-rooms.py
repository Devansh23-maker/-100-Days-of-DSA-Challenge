class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)

            for neighbor in rooms[room]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(0)
        return len(visited) == len(rooms)