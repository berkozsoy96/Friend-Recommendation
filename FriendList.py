def open_file():
    fp = open('C:\\Users\Betül Özsoy\Desktop\yazılım\Python Projeler\Hello\\big_network.txt')
    n = fp.readline()
    n = int(n)
    network = []
    for i in range(n):
        network.append([])

    for oku in fp:
        sp = oku.split(" ")
        network[int(sp[0])].append(int(sp[1]))
        network[int(sp[1])].append(int(sp[0]))

    return network


def num_in_common_between_lists(list1, list2):
    counter = 0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                counter += 1
    return counter


def init_matrix(n):
    """Create an nxn matrix, initialize with zeros, and return the matrix."""
    matrix = []
    for row in range(n):  # for each of the n rows
        matrix.append([])  # create the row and initialize as empty
        for column in range(n):
            matrix[row].append(0)  # append a 0 for each of the n columns
    return matrix


def calc_similarity_scores(network):
    n = len(network)
    matrix = init_matrix(n)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = num_in_common_between_lists(network[i], network[j])

    return matrix


def recommend(user_id, network, similarity_matrix):
    n = len(network)
    biggest = 0
    index = -1
    for i in range(n):
        bayrak = True
        if i != user_id and similarity_matrix[user_id][i] > biggest:
            for j in range(len(network[user_id])):
                if network[user_id][j] == i:
                    bayrak = False
                    break
            if bayrak:
                biggest = similarity_matrix[user_id][i]
                index = i
    return index


"""kullanıcıdan dosya adı al"""
network = open_file()
matrix = calc_similarity_scores(network)
print("\nFacebook Friend Recommendation.")
bayrak = True
while bayrak:
    user = int(input("Enter user who you want to the recommendations for\n(0 to 999):"))
    a = recommend(user, network, matrix)
    print("Most recommended person for", user, "is", a)
    '''Burada bir döngü daha olmalı hatalı giriş yaparsa yeniden giriş istemeli'''
    choice = input("Do you want to continue (yes/no):")
    if choice.lower() == 'yes':
        """Do Noting"""
    elif choice.lower() == 'no':
        print("Bye!")
        bayrak = False
    else:
        print("Inappropriate Input")
        bayrak = False
