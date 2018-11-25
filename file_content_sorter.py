import os
def sorter() -> list:
    context = []
    with open(os.getcwd() + '/ga.txt', 'rb') as file:
        for char in file.read().decode("utf-8").lower().split("\n"):
            context.append(sorted(list(char)))
        return context

def write_to_file(data: list) -> None:
    context = ""
    for lines in data:
        context += ''.join(lines) + "\n"
    file = open(os.getcwd() + "/ga_sorted.txt", "w+")
    file.write(context)
    file.close()
    
if __name__ == '__main__':
    sorted_result = sorter()
    write_to_file(sorted_result)
    input('Press ENTER to exit')
