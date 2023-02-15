for i in reversed(range(1,5)):
    print(*[int(j) for j in range(1,i+1)],sep=" * ")
