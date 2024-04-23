# Tree constructor
def treeConstructor(strArr):
    """
    Validates if the given list of strings represents a valid binary tree.

    Args:
        strArr (list): A list of strings representing the relationships between nodes in the binary tree.
                       Each string in the list should be in the format "(child, parent)".

    Returns:
        bool: True if the given list represents a valid binary tree, False otherwise.
    """
    parentList = []
    for node in strArr:
        child, parent = eval(node)
        parentList.append(parent)
        if parentList.count(parent) > 2:
            return False
    return True

print(treeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,2)"]))
