# https://leetcode.com/problems/string-to-integer-atoi/
# Medium

# Four errors due to carelessness/edgecases
# error 1(EDGE): Didn't account for edge case of lots of 0's at first. Fixed* with trim
# error 2(EDGE): Trim didn't catch line of 0's. This was because I looked for non zeros and sliced if non-zero was found. A line of zero's never gets sliced because if is never fufilled
# error 3(SLOPPY): used a += instead of taking a slice. Submitted to quickly b/c was impatient
# error 4(SLOPPY): Forgot to break, which led to double slicing which lead to error
# Final solution is faster than only 36.88% but uses good memory. While I believe it solves in n speed since I never backtrack and have a lot of exit conditions, I could probably streamline the trimming process
# Note: This problem has a low completion rate because it has so many edgecases. If in an interview, I would need to think or ask to clarify a lot more.

class Solution:
    def myAtoi(self, str: str) -> int:
        
        int_string = '0123456789'
        
        non_whitespace_index = -1
        
        for index in range(len(str)):
            if str[index] != ' ':
                non_whitespace_index = index
                # print(f'index:{index}')
                str = str[index:]
                # print(f'string:{str}')
                break
        
        if non_whitespace_index < 0:        # you have nothing but whitespace or an empty str
            # print('at whitespace')
            return 0
        
        positive = True  # Assume positive is true
        
        # checking first letter
        if str[0] == '-':
            # print('change pos')
            positive = False
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        elif str[0] in int_string:
            pass
        else:
            # print('at first let check')
            # print(f'first letter:{str[0]}')
            return 0                        # it ain't an int
        
        # trim 0's
        # print(f'string before trim:{str}')
        trimmed_str = ""
        for new_index in range(len(str)):
            if str[new_index] != '0':
                trimmed_str = str[new_index:]
                break
        
        str = trimmed_str
        
        num_val_str = ""
        
        for c in str:
            if c in int_string:
                num_val_str += c
            else:
                break
                
        if not num_val_str:         # no number value
            # print('at no num val')
            return 0
        
        INT_MAX = pow(2,31) - 1
        INT_MIN = -pow(2,31)
        
        if len(num_val_str) > 10:
            return INT_MAX if positive else INT_MIN
        
        int_val = int(num_val_str) if positive else -int(num_val_str)
        
        if int_val > INT_MAX:
            return INT_MAX
        elif int_val < INT_MIN:
            return INT_MIN
        else:
            return int_val