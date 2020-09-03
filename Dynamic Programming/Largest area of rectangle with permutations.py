class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        if not A :
            return 0 
        def nsl(arr):
            index = -1
            stack,vector = [],[]
            for i in range(len(arr)):
                if not stack :
                    vector.append(index)
                elif stack and stack[-1][0] >= arr[i]:
                    while stack and stack[-1][0]>= arr[i]:
                        stack.pop()
                    if not stack :
                        vector.append(index)
                    else:
                        vector.append(stack[-1][1])
                elif stack and stack[-1][0] < arr[i]:
                    vector.append(stack[-1][1])
                stack.append((arr[i],i))    
            return vector

        def nsr(arr):
            index = len(arr)
            stack,vector = [],[]
            for i in range(len(arr)-1,-1,-1):
                if not stack :
                    vector.append(index)
                elif stack and stack[-1][0] >= arr[i]:
                    while stack and stack[-1][0] >= arr[i]:
                        stack.pop()
                    if not stack :
                        vector.append(index)
                    else:
                        vector.append(stack[-1][1])
                elif stack and stack[-1][0] < arr[i]:
                    vector.append(stack[-1][1])
                
                stack.append((arr[i],i))
                
            return vector[::-1]
        def histogram(arr):
            l,r = nsl(arr),nsr(arr)
            # print(l,r)
            maxx = 0 
            for i in range(len(arr)):
                maxx = max(maxx,(r[i]-l[i]-1)*arr[i])
            return maxx
        
        for i in range(1,len(A)):
            for j in range(len(A[0])):
                if A[i][j] :
                    A[i][j] += A[i-1][j]
                  
        # With Permutations :p    
        for i in range(len(A)) :
            A[i] = sorted(A[i])
        
        ans = histogram(A[0])
        for i in range(1,len(A)):
            ans = max(ans,histogram(A[i]))
        
        return ans
            
                
                
# C++ Easy Solution 
'''
int Solution::solve(vector<vector<int> > &A) {
    int n=A.size(),m=A[0].size();
    int count[n][m];
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(j==0)
             count[j][i]=A[j][i];
            else if(A[j][i]==1)
             count[j][i]=count[j-1][i]+1;
            else
             count[j][i]=0;
        }
    }
    int ans=0;
    for(int i=0;i<n;i++){
        sort(count[i],count[i]+m);
        int maxrow=count[i][0]*m;
        for(int j=1;j<m;j++){
            maxrow=max(maxrow,count[i][j]*(m-j));
        }
        ans=max(ans,maxrow);
    }
    return ans;
    '''
                        
                
        
