#Given an input num as a string. You need to typecast into an integer and double it.
#Just write the syntax to typecast num and double it. The input and output are handled by the given code itself.
#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function2 Template for python3

def utility():
    #The line below takes the input
    num=input()
    
    #Complete the syntax below. Convert num to int and double it
    num=int(num)
    ans=num+num
    #Complete the syntax above
    
    #The line below prints the output
    print(ans)


#{ 
#Driver Code Starts.

def main():
    t = int(input())
    while(t > 0):
        utility()
        t-=1

if __name__ == "__main__": 
    main()
#} Driver Code Ends