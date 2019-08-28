# Given a target integer T and an integer array A sorted in ascending order, 
# find the index of the first occurrence of T in A or return -1 if there is no such index.

# [2,4,7,7,7,7,9,11]
#  0              7
 
# [4,5] T=6, T=3
# l=0, r=-1
# [7,7,7]

class Solution(object):
    def firstOccur(array, target):
        """
        input: int[] array, int target
        return: int
        """
        # write your solution here
        L=0
        R=len(array)-1
        while L<R:
            mid=(L+R)/2
            if array[mid]<target:
                L=mid+1
            elif array[mid]>target:
                R=mid-1
            else:
                R=mid
        if L==R and array[L]==target:
            return L
        return -1
        

# Given a target integer T and an integer array A sorted in ascending order, 
# find the index of the last occurrence of T in A or return -1 if there is no such index.

class Solution(object):
    def lastOccur(self, array, target):
        """
        input: int[] array, int target
        return: int
        [2,4,7,7,7,7,9,11]
         0              7
         [4,5] T=6, T=3
          l=0, r=-1
          [7,7,7]
        """
        # write your solution here
        if len(array)==0:
              return -1
        L=0
        R=len(array)-1
        while R-L>1:
            mid=(L+R)/2
            if array[mid]<target:
                L=mid+1
            elif array[mid]>target:
                R=mid-1
            else:
                L=mid
        if array[R]==target:
            return R      
        if array[L]==target:
            return L  
        return -1
        
# Given a target integer T and an integer array A sorted in ascending order, find the index i in A such that A[i] is closest to T.
# Assumptions:There can be duplicate elements in the array, and we can return any of the indices with same value.

class Solution(object):
    def closest(self, array, target):
        """
        input: int[] array, int target
        return: int
        [2,4,7,7,7,7,9,11]  8
         0              7
        [4,5] T=6, T=3
         
        [7,7,7]
        """
        # write your solution here
        if len(array)==0:
            return -1
        L=0
            R=len(array)-1
            while R-L>1:
                mid=(L+R)/2
                if array[mid]<target:
                    L=mid
                elif array[mid]>target:
                    R=mid
                else:
                    return mid
            if abs(array[L]-target)<=abs(array[R]-target):
                return L 
            return R
           
       

# Given a target integer T, a non-negative integer K and an integer array A sorted in ascending order, find the K closest numbers to T in A.
# Assumptions: A is not null; K is guranteed to be >= 0 and K is guranteed to be <= A.length

class Solution(object):
    def kClosest(self, array, target, k):
        """
        input: int[] array, int target, int k
        return: int[]
        [2,4,7,7,7,7,9,11] t=8,k=3
         0              7
        """
        # write your solution here
        L=0
        R=len(array)-1
        ls=[]
        while R-L>k-1:
            mid=(L+R)/2
            if array[mid]<target:
                L=mid-k+1
                if L<0:
                    L=0
            if array[mid]>target:
                R=mid+k-1   
                    if R>len(array)-1:
                        R=len(array)-1
            

# Given a target integer T and an integer array A sorted in ascending order, Find the total number of occurrences of T in A.
class Solution(object):
    def totalOccurrence(self, array, target):
        """
        input: int[] array, int target
        return: int
        """
        [2,4,5,7,7,7,9,11] t=7
         0              7
        L=0
        R=len(array)-1
        while L<R:
            mid=(L+R)/2
            if array[mid]<target:
                L=mid+1
            elif array[mid]>target:
                R=mid-1       
            else:
                L,R=mid,mid
                while L!=0 and array[L-1]==target:
                    L-=1
                while R!=len(array)-1 and array[R+1]==target:
                    R+=1
                return R-L+1
        if L==R and array[L]==target:
            return 1
        return 0
        

# Given a 2D matrix that contains integers only, which each row is sorted in an ascending order. The first element of next row is larger than (or equal to) the last element of previous row.
# Given a target number, returning the position that the target locates within the matrix. If the target number does not exist in the matrix, return {-1, -1}.

# Assumptions: The given matrix is not null, and has size of N * M, where N >= 0 and M >= 0.
# Examples: matrix = { {1, 2, 3}, {4, 5, 7}, {8, 9, 10} }  target = 7, return {1, 2}
#[[1, 2,  4,  6],
# [7, 9, 10, 11],
# [12,14,17, 18]]  T=11
 
class Solution(object):
    def search(self, matrix, target):
        """
        input: int[][] matrix, int target
        return: int[]
        """
        N=len(matrix)       #=3
        M=len(matrix[0])    #=4
        L=0
        R=M*N-1
        while L<R:
            mid=(L+R)/2
            if matrix[mid/M][mid%M]<target:
                L=mid+1
            elif matrix[mid/M][mid%M]>target:
                R=mid-1
            else:
                return [mid/M,mid%M]
        if L==R and matrix[L/M][L%M]==target: 
            return [L/M,L%M]
        return [-1,-1]


# Given an array of integers, sort the elements in the array in ascending order. The selection sort algorithm should be used to solve this problem.

class Solution(object):
    def solve(self, array):
        """
        input: int[] array
        return: int[]
        """
        [3,1,5,9,2]
        # write your solution here
        def get_max(array):
            max=array[0]
            indx=0
            for i in range(len(array)):
                if array[i]>max:
                    max=array[i]
                    indx=i
            return indx
        
        if (array is None) or len(array)==0:
            return array    
        for i in range(len(array)):
            max_index=get_max(array[:len(array)-i])
            array[max_index],array[len(array)-i-1]=array[len(array)-i-1],array[max_index]
        return array



class _ListNode(object):
    def __init__(self,val):
        self.val=val
        self.next=None
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head=None
        self._tail=None
        self._size=0
        
    def _get(self,index):
        """
        Return the node of the corresponding index
        """
        #Assuming the index is in range [0,self._size)
        node=self._head
        for i in range(index):
            node=node.next
        return node
  
      def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self._size:
            return -1
        return self._get(index).val
        
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size==0:
            self._head=self._tail=_ListNode(val)
        else:
            new_head=_ListNode(val)
            new_head.next=self._head
            self._head=new_head
        self._size+=1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self._size==0:
            self._head=self._tail=_ListNode(val)
        else:
            self._tail.next=_ListNode(val)
            self._tail=self._tail.next
        self._size+=1
    
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index>=self._size or index<0:
            return
        if index==0:
            self.addAtHead(val)
        if index>0:
            prev=self._get(index-1)
            node=_ListNode(val)
            node.next=prev.next
            prev.next=node
            self._size+=1
      
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index>=self._size or index<0:
            return
        if self._size==1:
            self._head=self._tail=None
            
        elif index==0:
            self._head=self._head.next    
        elif index==self._size-1:
            prev=self._get(index-1)
            prev.next=None
            self._tail=prev
        else:
            prev=self._get(index-1)
            prev.next=prev.next.next
        self._size-=1
      
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverse(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        prev=None
        cur=head
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev
        
def remove_vowels(head):
    fake_head=ListNode(None)     
    fake_head.next=head
    prev=fake_head
    cur=head
    while cur:
        if cur.val in ['a','e','i','o','u']:
            prev.next=cur.next
            cur=cur.next
        else:
            prev=cur
            cur=cur.next
    return fake_head.next
        
def find_mid_node(head):
    if head is None or head.next is None:
        return head
    F=head
    S=head
    while F.next and F.next.next:
        F=F.next.next
        S=S.next
    return S

def is_palindrome(head):
    if head is None or head.next is None:
        return True
    mid= find_mid_node(head)   # call find_mid_node function
    head2=reverse(mid.next)    # call reverse function
    mid.next=None
    cur1=head
    cur2=head2
    while cur2:
        if cur2.val!=cur1.val:
            return False
        cur2=cur2.next
        cur1=cur1.next    
    return True

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def merge(self, one, two):
        """
        input: ListNode one, ListNode two
        return: ListNode
        """
        # write your solution here
        if one is None:
            return two
        if two is None:
            return one
        cur1=one
        cur2=two
        fake_head=ListNode(None)
        cur=fake_head
        while cur1 and cur2:
            if cur1.val<=cur2.val:
                cur.next=ListNode(cur1.val)
                cur1=cur1.next
            else:
                cur.next=ListNode(cur2.val)
                cur2=cur2.next
            cur=cur.next
            
        if not cur1:
            cur.next=cur2
        else:
            cur.next=cur1
        return (fake_head.next)
            

    
def square_root(n):
    """"
    take n as a non-negative integer, return the largest integer whose square is smaller or equal to n
    n=9
    range(n+1)
    [0,1,2,3,4,5,6,7,8,9]
    
    [0,1,2,3]
    """"
    L,R=0,n
    while R-L>1:
        mid=(L+R)/2
        if mid**2<n:
            L=mid
        elif mid**2>n:
            R=mid-1
        else:
            return mid
        
    if R==L:
        return R
    elif R**2<=n:
        return R
    else:
        return L
                 
def count_frequency(words):
    dict1={}
    for i in words:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
    return dict1

def most_frequent_word(words):
    freq=count_frequency(words)
    maxi=max(freq.values())
    return ([i for (i,j) in freq.items() if j==maxi],maxi)

def case_insensitive_frequency(words):
    #['A','B','b','B','C','c','d','d','D']
    freq=count_frequency(words)
    dict1={i.upper():freq.get(i.lower(),0)+freq.get(i.upper(),0) for i in freq}
    return dict1

def topKFrequent(combo, k):
    """
    input: string[] combo, int k
    return: string[]
    """
    def frequency(combo):
        d={}
        for i in combo:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return d
    d1=frequency(combo)
    if k>=len(d1):
        return [k for k,v in sorted(d1.items(),key=lambda x:-x[1])]
    return [k for k,v in sorted(d1.items(),key=lambda x: -x[1])[:k]]

def missing(array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    def frequency(array):
        d={}
        for i in array:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        return d
        
    if len(array)==0:
        return 1
    d1=frequency(array)
    for i in range(1,len(array)+2):
        if i not in d1:
            return i 
            
####################################################                   
############# above is First bulkupload ############
####################################################        
                    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

