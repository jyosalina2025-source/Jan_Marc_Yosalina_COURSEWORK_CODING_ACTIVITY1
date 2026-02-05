Friends = ["Alice", "Bob", "Carol", "Dave"]
print("Friends List:", Friends)

for index, name in enumerate(Friends):
    if index == len(Friends) - 1:
        print(name)
    elif index == len(Friends) - 2:
        print(name + " and ", end="")
    else:
        print(name + ", ", end="")

        
Friends.append("Eve")
Friends.insert(1, "Jan Marc")
Friends.remove("Carol")
        
print("\nUpdated Friends List:", Friends)
        
Friends.sort()
print("Sorted Friends List:", Friends)