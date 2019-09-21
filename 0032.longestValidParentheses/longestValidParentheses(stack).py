import string

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = []
        st.append(-1)
        slen = len(s)
        mx = 0
        for i in range(slen):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if len(st) == 0:
                    st.append(i)
                else:
                    mx = max(mx, i - st[-1])
        
        return mx

'''
import string

class Solution:
    def mergest(self, st: list):
        slen = len(st)
        #print(st)
        for i in range(slen - 2, -1, -1):
            if st[i] not in ['(', ')']:
                st[i] = st[i] + st[i + 1]
                st.pop()
            else:
                break
    def longestValidParentheses(self, s: str) -> int:
        st = []
        for i in s:
            #print(i)
            if i == '(':
                st.append(i)
            else: # current char is ')'
                sl = len(st)

                # if stack is empty
                if sl == 0:
                    continue
                
                if st[-1] == ')':
                    pass
                elif st[-1] == '(':
                    st.pop()

                    if sl == 1 or st[-1] in ['(', ')']:
                        st.append(2)
                        self.mergest(st)
                    else:
                        st[-1] += 2
                        self.mergest(st)
                else:
                    if sl == 1 or st[-2] == ')':
                        st.append(')')
                    elif st[-2] == '(':
                        st[-2] = st[-1] + 2
                        st.pop()
                        self.mergest(st)
                    else:
                        st.append(2)
                        self.mergest(st)

        mx = 0
        for i in st:
            if i not in ['(', ')'] and i > mx:
                mx = i
                
        return mx     
'''