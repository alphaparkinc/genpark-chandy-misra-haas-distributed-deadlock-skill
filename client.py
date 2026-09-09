class ChandyMisraHaasDetector:
    """Edge-chasing distributed deadlock detection algorithm."""
    def detect_cycle(self, wait_graph: dict[int, list[int]], initiator: int) -> dict:
        visited = set()
        queue = list(wait_graph.get(initiator, []))
        probes_sent = 0

        while queue:
            curr = queue.pop(0)
            probes_sent += 1
            if curr == initiator:
                return {
                    "deadlock_detected": True,
                    "initiator": initiator,
                    "probes_forwarded": probes_sent
                }
            if curr not in visited:
                visited.add(curr)
                queue.extend(wait_graph.get(curr, []))

        return {
            "deadlock_detected": False,
            "initiator": initiator,
            "probes_forwarded": probes_sent
        }
