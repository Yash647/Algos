"""=====================Converting MaxHeap to BST===================="""
import math

"""---------------------Utility functions----------------"""
#Maxheapify Procedure : T(n) = O(log(n))
def maxHeapify(currNode, heap, size):
    leftNode = 2*currNode +1
    rightNode = 2*currNode +2
    largest = currNode
    if(leftNode < size and heap[leftNode] > heap[largest]):
        largest = leftNode
    if(rightNode < size and heap[rightNode] > heap[largest]):
        largest = rightNode
    if largest!=currNode:
        #swapping the largest and currNode elements
        heap[largest], heap[currNode] = heap[currNode], heap[largest]
        maxHeapify(largest, heap, size)

#BuildMaxHeap Procedure : T(n) = O(n)
def buildMaxheap(heap):
    pos = len(heap)//2 - 1
    size = len(heap)
    while pos>=0:
        maxHeapify(pos, heap, size)
        pos -=1

#Heap Sort Procedure(Ascending Order) : T(n) = O(nlog(n))
def heapSort(heap):
    buildMaxheap(heap)
    length = len(heap)
    while(length >= 2):
        heap[0], heap[length - 1]= heap[length - 1], heap[0]
        length -=1
        maxHeapify(0, heap, length)

"""---------------Main Functionality--------------"""

heap = [14,9,12,4,7,9,6,2,1,5,3,8]# Input : Max  Heap

heapSort(heap)#--->T(n) = O(nlog(n))<---___________________________(1)

levels = 0 #Number of levels of BST
nodesCount = 1 #Number of nodes at each level if level is full (initially 1 due to root node)

#Calculating number of levels in BST:--->T(n) = O(log(n))<---___________(2)
while(nodesCount<=len(heap)):
    nodesCount = nodesCount * 2
    levels = levels + 1

#Creating new array for result
bst = [None] * ((2 ** levels) - 1)

lb, ub = 0, len(heap) - 1 #lb - lower bound , ub - upper bound

flag = 0
""" flag = 0 means insertion at root
       flag = -1  means insert as left child
       flag = 1 means insert as right child
"""

i = 0 # index in bst

# Creating BST : --->T(n) = 2T(n/2) + 1 = O(n)<----_____________________(3)
def createBST(lb, ub, flag, i):
    if lb <= ub:
        if flag == -1:
            i = 2*i + 1 #left child
        elif flag == 1:
            i = 2*i + 2 #right child
        mid = math.ceil((lb+ub)/2)
        bst[i] = heap[mid]

        #goto left subtree
        createBST(lb, mid-1, -1, i) #n/2

        #goto right part
        createBST(mid+1, ub, 1, i)#n/2

createBST(lb,ub,flag,i)
print(bst)
# Output => [7, 4, 9, 2, 6, 9, 14, 1, 3, 5, None, 8, None, 12, None]
"""                                                                7
                                                                 /    \
                                                             /            \  
                                                         /                    \
                                                     /                            \
                                                 /                                   \
                                               4                                       9
                                            /     \                                 /     \
                                          2         6                             9         14
                                       /     \    /   \                         /   \      /   \ 
                                      1       3  5     None                    8    None  12    None


Total Time Complexity :- From (1), (2), (3) 
T(n) = O(nlog(n)) + O(log(n)) + O(n)
         = O(nlog(n))
"""
