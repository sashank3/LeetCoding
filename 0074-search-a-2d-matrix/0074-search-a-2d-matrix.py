class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Set l,r,u,d pointers. first find u,d target between l and r. Then find l,r target. 


        l, r, u, d = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        flag = False

        if(r == 0 and d == 0):
            if(matrix[0][0] == target):
                return True
            else:
                return False

        while u <= d:

            mid = (u + d) // 2
            if(matrix[mid][r] < target):
                u = mid + 1
            elif(matrix[mid][l] > target):
                d = mid - 1
            else:
                while l <= r:

                    mid2 = (l + r) // 2
                    if(matrix[mid][mid2] < target):
                        l = mid2 + 1
                    elif(matrix[mid][mid2] > target):
                        r = mid2 - 1
                    else:
                        return True
                
                flag = True
                break
            
            if flag:
                return False
