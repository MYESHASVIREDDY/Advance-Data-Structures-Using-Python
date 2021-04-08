## EXPRIMENT 3
## AIM: To implement B-Tree
## PROCEDURE: Insertion
### 1) Initialize x as root.
### 2) While x is not leaf, do following
### ..a) Find the child of x that is going to be traversed next. Let the child be y.
### ..b) If y is not full, change x to point to y.
### ..c) If y is full, split it and change x to point to one of the two parts of y. If k is smaller than mid key in y, then set x as the first part of y. Else second part of y. When we split y, we move a key from y to its parent x.
### 3) The loop in step 2 stops when x is leaf. x must have space for 1 extra key as we have been splitting all nodes in advance. So simply insert k to x.
### Deletion process:
### Deletion from a B-tree is more complicated than insertion, because we can delete a key from any node-not just a leaf—and when we delete a key from an internal node, we will have to rearrange the node’s children.



