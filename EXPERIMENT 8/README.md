## EXPRIMENT 8
## AIM: To implement all the function in a Red Black Trees
## PROCEDURE: 
### The insertion operation in red black tree is performed using the following steps:
### Step 1 - Check whether tree is Empty.
### Step 2 - If tree is Empty then insert the newNode as Root node with color Black and exit from the operation.
### Step 3 - If tree is not Empty then insert the newNode as leaf node with color Red.
### Step 4 - If the parent of newNode is Black then exit from the operation.
### Step 5 - If the parent of newNode is Red then check the color of parentnode's sibling of newNode.
### Step 6 - If it is colored Black or NULL then make suitable Rotation and Recolor it.
### Step 7 - If it is colored Red then perform Recolor. Repeat the same until tree becomes Red Black Tree.

### Deleting an element from a Red-Black Tree
### 1.Let the nodeToBeDeleted be:
### 2.Save the color of nodeToBeDeleted in origrinalColor.
### 3. If the left child of nodeToBeDeleted is NULL
#### a.Assign the right child of nodeToBeDeleted to x.
#### b. Transplant nodeToBeDeleted with x
### 4. Else if the right child of nodeToBeDeleted is NULL
#### a.Assign the left child of nodeToBeDeleted into x.
#### b.Transplant nodeToBeDeleted with x.
### 5.Else
#### a. Assign the minimum of right subtree of noteToBeDeleted into y.
#### b. Save the color of y in originalColor.
#### c. Assign the rightChild of y into x.
#### d. If y is a child of nodeToBeDeleted, then set the parent of x as y.
#### e. Else, transplant y with rightChild of y.
#### f. Transplant nodeToBeDeleted with y.
#### g.Set the color of y with originalColor.
### 6.If the originalColor is BLACK, call DeleteFix(x).

