from client import ChandyMisraHaasDetector

def main():
    print("=== Chandy-Misra-Haas Edge-Chasing Deadlock Detector ===")
    detector = ChandyMisraHaasDetector()
    # Distributed cycle: Node 1 waits for Node 2, 2 waits for 3, 3 waits for 1
    g = {1: [2], 2: [3], 3: [1]}

    res = detector.detect_cycle(g, initiator=1)
    print("Detection Result:", res)
    assert res["deadlock_detected"] is True

    print("Chandy-Misra-Haas Detector verified successfully!")

if __name__ == "__main__":
    main()
