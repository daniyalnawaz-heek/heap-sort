def heap_sort(list1,n):
  
  
  build_max_heap(list1,n)
  for k in range(n-1,0,-1):
    list1[0],list1[k]=list1[k],list1[0]
    
    heapify(list1,k,0)
  
  

def build_max_heap(list1,n):
  start =(n//2)-1
  
  
  for i in range(start,-1,-1):
    heapify(list1,n,i)

def heapify (list1,n,i):
      left=2*i+1 
      right=2*i+2
      largest=i
      if left <= n-1 and list1[left]>list1[i]:
        largest=left
      
      if right <= n-1 and list1[right]>list1[largest]:
        largest=right
      
      if largest!=i:
        list1[largest],list1[i]=list1[i],list1[largest]
        heapify(list1,n,largest) 
        
         
list2=[35,73,85,95,2,32,63,75,865,63,6848,6833,8,4,8,37,85,33]
n=len(list2)  
heap_sort(list2,n)
print(list2)