
def make_numeric(s):
    if "." in s:
        return float(s)
    else:
        return int(s)


def read_matrix(number_matrix=""):
    shape_matrix = input("Enter size of {} matrix:".format(number_matrix))
    n = int(shape_matrix.split()[0])
    m = int(shape_matrix.split()[1])
    print("Enter {} matrix:".format(number_matrix))
    matrix = []
    for i in range(n):
        row_matrix = []
        row_str = input().split()
        for el in row_str:
            row_matrix.append(make_numeric(el))
        matrix.append(row_matrix)
    return matrix, n, m


def sum_matrix(A, B, n1, m1, n2, m2):
    if (n1 == n2) and (m1 == m2):
        result_matrix = []
        for i in range(n1):
            row = []
            for j in range(m1):
                row.append(A[i][j] + B[i][j])
            result_matrix.append(row)
        return result_matrix
    else:
        return None


def multiply_on_scalar(A, c):
    return [[c*el for el in row] for row in A]


def multiply_on_vectors(a, b):
    n = len(a)
    lst = []
    for i in range(n):
        lst.append(a[i]*b[i])
    return sum(lst)


def multiply_on_matrix(A, B, n, m, l, k):
    if m != l:
        return None
    else:
        res = [[] for i in range(n)]
        for i in range(n):
            for j in range(k):
                v1 = [A[i][ind] for ind in range(m)]
                v2 = [B[ind][j] for ind in range(m)]
                res[i].append(multiply_on_vectors(v1, v2))
        return res


def horisontal_tr(A, n, m):
    res = [[] for i in range(n)]
    for i in range(n):
        for j in range(m):
            res[i].append(A[n-i-1][j])
    return res


def vertical_tr(A, n, m):
    res = [[] for i in range(n)]
    for i in range(n):
        for j in range(m):
            res[i].append(A[i][m-j-1])
    return res


def main_tr(A, n, m):
    res = [[] for i in range(m)]
    for j in range(m):
        for i in range(n):
            res[j].append(A[i][j])
    return res

def said_tr(A, n, m):
    res = [[] for i in range(m)]
    for j in range(m):
        for i in range(n):
            res[j].append(A[n-i-1][m-j-1])
    return res

def comatrix(A, n, i, j):
    if n < 2:
        return None
    else:
        B = []
        for k in range(n):
            if k != i:
                row = []
                for l in range(n):
                    if l!=j:
                        row.append(A[k][l])
                B.append(row)
        return B, n - 1, n - 1

def det(A, n, m):
    if n != m:
        return None
    elif n == 0:
        return  0
    elif n == 1:
        return A[0][0]
    elif n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    else:
        s = 0
        for j in range(n):
            C, n1, m1 = comatrix(A, len(A), 0, j)
            s += A[0][j]*((-1)**j)*det(C, n1, m1)
        return s

def adj(A, n):
    if n == 1:
        return A, n
    elif n == 2:
        return [[A[1][1], -A[1][0]],[-A[0][1], A[0][0]]], n
    else:
        B = []
        for i in range(n):
            row = []
            for j in range(n):
                C, n1, m1 = comatrix(A, n, i, j)
                element = det(C, n1, m1)*((-1)**(i + j))
                row.append(element)
            B.append(row)
        return B, n

def print_matrix(C):
    print("The result is:")
    for row in C:
        for el in row:
            print(el, end=" ")
        print()


if __name__ == "__main__":
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ")
        if choice == "3":
            A, n1, m1 = read_matrix("first")
            B, n2, m2 = read_matrix("second")
            C = multiply_on_matrix(A, B, n1, m1, n2, m2)
            if C is None:
                print("The operation cannot be performed.")
            else:
                print_matrix(C)
        elif choice == "1":
            A, n1, m1 = read_matrix("first")
            B, n2, m2 = read_matrix("second")
            C = sum_matrix(A, B, n1, m1, n2, m2)
            if C is None:
                print("The operation cannot be performed.")
            else:
                print_matrix(C)
        elif choice == "4":
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            method = input("Your choice:")
            A, n, m = read_matrix()
            if method == "1":
                C = main_tr(A, n, m)
                print_matrix(C)
            elif method == "2":
                C = said_tr(A, n, m)
                print_matrix(C)
            elif method == "3":
                C = vertical_tr(A, n, m)
                print_matrix(C)
            else :
                C = horisontal_tr(A, n, m)
                print_matrix(C)
        elif choice == "2":
            A, n1, m1 = read_matrix()
            scalar = make_numeric(input("Enter constant: "))
            C = multiply_on_scalar(A, scalar)
            print_matrix(C)
        elif choice == "5":
            A, n1, m1 = read_matrix()
            determinant = det(A, n1, m1)
            if determinant is None:
                print("The determinant does not exist!")
            else:
                print("The result is:")
                print(determinant)
        elif choice == "6":
            A, n1, m1 = read_matrix()
            determinant = det(A, n1, m1)
            if determinant != 0:
                adj_matrix, n2 = adj(A, n1)
                C_trans = main_tr(adj_matrix, n2, n2)
                A_convers = multiply_on_scalar(C_trans, 1 / determinant)
                print_matrix(A_convers)
            else:
                print("This matrix doesn't have an inverse.")
        else:
            break
