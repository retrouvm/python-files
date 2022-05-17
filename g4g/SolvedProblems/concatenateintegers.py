#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


def utility():
    #The two lines below take input.
    a=int(input())
    b=int(input())
    
    #Complete the code below to concatenate a and b
    a=str(a)
    b=str(b)
    ans=a+b
    #Complete the code above to concatenate a and b
    
    #The line below prints the output.
    print(ans)

#{ 
#Driver Code Starts.

def main():
    t=int(input())
    while(t>0):
        utility()
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends