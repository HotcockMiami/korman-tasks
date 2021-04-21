def main(A, u):
    for i in range(len(A)):
        if A[i]==u:
            return i
    return None
            
print(main([1, 3, 5], 3))
print(main([1, 3, 5], 0))
        