'''Provides basic operations for Binary Search Trees using
a tuple representation.  In this representation, a BST is
either an empty tuple or a length-3 tuple consisting of a data value,
a BST called the left subtree and a BST called the right subtree
'''

def is_bintree(T):
    if type(T) is not tuple:
        return False
    if T == ():
        return True
    if len(T) != 3:
        return False
    if is_bintree(T[1]) and is_bintree(T[2]):
        return True
    return False

def bst_min(T):
    if T == ():
        return None
    if not T[1]:
        return T[0]
    return bst_min(T[1])

def bst_max(T):
    if T == ():
        return None
    if not T[2]:
        return T[0]
    return bst_max(T[2])

def is_bst(T):
    if not is_bintree(T):
        return False

    if T == ():
        return True

    if not is_bst(T[1]) or not is_bst(T[2]):
        return False

    if T[1] == () and T[2] == ():
        return True

    if T[2] == ():
        return bst_max(T[1]) < T[0]
    if T[1] == ():
        return T[0] < bst_min(T[2])
    return bst_max(T[1]) < T[0] < bst_min(T[2])

def bst_search(T,x):
    if T == ():
        return T
    if T[0] == x:
        return T
    if x < T[0]:
        return bst_search(T[1],x)
    return bst_search(T[2],x)

def bst_insert(T,x):
    if T == ():
        return (x,(),())
    elif x < T[0]:
        return (T[0],bst_insert(T[1],x),T[2])
    else:
        return (T[0],T[1],bst_insert(T[2],x))

def delete_min(T):
    if T == ():
        return T
    if not T[1]:
        return T[2]
    else:
        return (T[0],delete_min(T[1]),T[2])

def bst_delete(T,x):
    assert T, "deleting value not in tree"

    if x < T[0]:
        return (T[0],bst_delete(T[1],x),T[2])
    elif x > T[0]:
        return (T[0],T[1],bst_delete(T[2],x))
    else:
        # T[0] == x
        if not T[1]:
            return T[2]
        elif not T[2]:
            return T[1]
        else:
            return (bst_min(T[2]),T[1],delete_min(T[2]))

def print_bintree(T,indent=0):
    if not T:
        print('*')
        return
    else:
        print(T[0])
        print(' '*(indent + len(T[0])-1)+'---', end = '')
        print_bintree(T[1],indent+3)
        print(' '*(indent + len(T[0])-1)+'---', end = '')
        print_bintree(T[2],indent+3)

def print_func_space(x):
    print(x,end=' ')

def inorder(T,f):
    if not is_bst(T):
        return
    if not T:
        return
    inorder(T[1],f)
    f(T[0])
    inorder(T[2],f)

# Programming project: provide implementations for the functions below,
# i.e., replace all the pass statements in the functions below.
# Then add tests for these functions in the block
# that starts "if __name__ == '__main__':"

def preorder(T,f):
    if not is_bst(T):
        return
    if not T:
        return
    f(T[0])
    preorder(T[1],f)
    preorder(T[2],f)

def postorder(T,f):
    if not is_bst(T):
        return
    if not T:
        return
    postorder(T[1],f)
    postorder(T[2],f)
    f(T[0])

def tree_height(T):
    # Empty tree has height -1
    if T == ():
        return -1
    if T[0] is not None and T[1] == () and T[2] == ():
        return 0
    return 1 + max(tree_height(T[1]), tree_height(T[2]))

def balance(T):
    # returns the height of the left subtree of T
    # minus the height of the right subtree of T
    # i.e., the balance of the root of T
    if T == ():
        return 0
    else:
        return tree_height(T[1]) - tree_height(T[2])

def minBalance(T):
    # returns the minimum value of balance(S) for all subtrees S of T
    if not is_bst (T):
        return 1
    if not T:
        return 0
    if not T[1] and not T[2]:
        return balance(T)
    else:
        return min(balance(T), minBalance(T[1]), minBalance(T[2]))

def maxBalance(T):
    # returns the maximum value of balance(S) for all subtrees S of T
    if not is_bst (T):
        return 1
    if not T:
        return 0
    if not T[1] and not T[2]:
        return balance(T)
    else:
        return max(balance(T), maxBalance(T[1]), maxBalance(T[2]))

def is_avl(T):
    # Returns True if T is an AVL tree, False otherwise
    # Hint: use minBalance(T) and maxBalance(T)
    if -1 <= maxBalance(T) <= 1 and -1 <= minBalance(T) <= 1:
        return True
    else:
        return False

# Add tests for the above seven functions below
if __name__ == '__main__':
    K = ()
    for x in ['Joe','Bob', 'Phil', 'Paul', 'Marc', 'Jean', 'Jerry', 'Alice', 'Anne']:
        K = bst_insert(K,x)

    print('\nTree elements in sorted order\n')
    inorder(K,print_func_space)
    print()

    print('\nPrint full tree\n')
    print_bintree(K)

    print("\nDelete Bob and print tree\n")
    K = bst_delete(K,'Bob')
    print_bintree(K)
    print()

    print("\nPrint subtree at 'Phil'\n")
    print_bintree(bst_search(K,'Phil'))
    print()

    # TEST CODE FOR THE FUNCTIONS YOU IMPLEMENTED GOES BELOW:
    print('\nTree elements in preorder sorted\n')
    preorder(K,print_func_space)
    print()

    print('\nTree elements in postorder sorted\n')
    postorder(K,print_func_space)
    print()

    print('\nTree height\n')
    height = tree_height(K)
    print(height)

    print('\nTree Balance on root\n')
    bal = balance(K)
    print(bal)

    print('\nMin Balance for all subtrees S of T\n')
    minBal = minBalance(K)
    print(minBal)

    print('\nMax Balance for all subtrees S of T\n')
    maxBal = maxBalance(K)
    print(maxBal)

    print('\nAVL TEST\n')
    test = is_avl(K)
    print(test)
