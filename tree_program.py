def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")

    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")

    for i in preorder:
        if preorder.count(i) > 1:
            raise ValueError("traversals must contain unique items")

    return tree(preorder, inorder)


def tree(preorder, inorder):
    if not preorder:
        return {}

    breakpoint()
    val = preorder[0]
    ind = inorder.index(val)

    return {"v": val, "l": tree(preorder[1: ind + 1], inorder[:ind]), "r": tree(preorder[ind + 1:], inorder[ind + 1:])}





pre = ["a", "i", "x", "f", "r"]
inor = ["i", "a", "f", "x", "r"]
obj = tree_from_traversals(pre, inor)
print(obj)


