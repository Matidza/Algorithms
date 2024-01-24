#Stacks use the LiFo principle
#Example
stacks  = ["Zwivhuya", "Wanga", "Mukona"]

print(stacks)
stacks.append("Todani")
stacks.append("What")
print(f"last in: {stacks}")

stacks.pop()
print(f"First out: {stacks}")


#Queues use the FiFo priciple

queues  = ["Zwivhuya", "Wanga", "Mukona"]
queues.append("Hello")
queues.append("John")
print(queues)

print(queues.pop(0))
print(queues)