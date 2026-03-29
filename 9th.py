stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)

# Pop
print(stack.pop())   # 30

# Peek
print(stack[-1])     # 20

# Check empty
print(len(stack) == 0)