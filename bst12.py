class Tree: 
  
    def __init__(node, value): 
        node.value = value  
        node.left = None
        node.right = None
    
    def Inorder( node, Root ): 
        if( Root is None ): 
            return
        node.Inorder(Root.left) 
        print(Root.value,end = ' ') 
        node.Inorder(Root.right) 
  
    def Insert(node, value): 
        if node is None: 
            node = Tree(value)
        elif value < node.value:
            if node.left is None:
                node.left = Tree(value)
            else:
               node.left.Insert(value) 
        else:
            if node.right is None:
                node.right = Tree(value)
            else:
                node.right.Insert(value)

    def Delete(node,temp, value):
        if value < node.value:
            temp = node
            node.left.Delete(temp,value)
        elif(value > node.value):
            temp = node
            node.right.Delete(temp, value)
            
        else:
            if (node.left is None and node.right is None):
                if(temp.left == node):
                    temp.left = None
                else:
                    temp.right = None
                node = None
        
            elif node.right is None :
                if(temp.left == node):
                    temp.left = node.left
                else:
                    temp.right = node.left
                node = None
    
            elif node.left is None :
                if(temp.left == node):
                    temp.left = node.right
                else:
                    temp.right = node.right
                node = None
                
            else:
                temp = node.right
                while(temp.left is not None):
                    temp = temp.left 
                node.value = temp.value
                node.right.Delete(temp,temp.value)


    def searching(self,root ,key):
        if root is None:
            return None
        if root.value == key:
            return root
        elif root.value > key:
            return self.searching(root.left, key)
        else:
            return self.searching(root.right, key)


Root = Tree(5) 
Root.Insert(3) 
Root.Insert(2) 
Root.Insert(1) 
Root.Insert(8) 
Root.Insert(4) 

  
print ("Inorder traversal after insertion: ",end = '')
Root.Inorder(Root) 

Root.Delete(Root, 4) 
print ('\n 4 is deleted: ',end ='')
Root.Inorder(Root) 
  
Root.Delete(Root, 3) 
print ('\n 3 is deleted: ',end ='')
Root.Inorder(Root) 
  
Root.Delete(Root, 8) 
print ('\n 8 is deleted: ',end ='')
Root.Inorder(Root)

print()
print("After searching 1")
n = Root.searching(Root,1)
if (n != None):
    print(f"{n.value} Found")
else:
    print("Not present in tree")
