## EXPERIMENT 1b
## AIM: To delete an element in a binary search tree
### PROCEDURE : Delete function is used to delete the specified node from a binary search tree. However, we must delete a node from a binary search tree in such a way, that the property of binary search tree doesn't violate. There are three situations of deleting a node from binary search tree.
                a) The node to be deleted is a leaf node: It is the simplest case, in this case, replace the leaf node with the NULL and simple free the allocated space.
                b) The node to be deleted has only one child.: In this case, replace the node with its child and delete the child node, which now contains the value which is to be deleted. Simply replace it with the NULL and free the allocated space.
                c) The node to be deleted has two children. :  It is a bit complexed case compare to other two cases. However, the node which is to be deleted, is replaced with its in-order successor or predecessor recursively until the node value (to be deleted) is placed on the leaf of the tree. After the procedure, replace the node with NULL and free the allocated space.
