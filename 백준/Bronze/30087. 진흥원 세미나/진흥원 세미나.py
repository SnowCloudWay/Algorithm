import sys
input = sys.stdin.readline

d = {"Algorithm":204, "DataAnalysis":207, "ArtificialIntelligence":302, "CyberSecurity":"B101", "Network":303, "Startup":501, "TestStrategy":105}
N = int(input())

for i in range(0, N):
    seminar = input().strip()
    print(d[seminar])