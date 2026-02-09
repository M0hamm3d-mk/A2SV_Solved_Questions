class Solution:
    res = ''
    def intToRoman(self, num: int) -> str:
        def helper(num):
            roman = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
            roman_num = ''
            while num > 0:
                if num == 0:
                    return roman_num
                str_num = str(num)
                n = len(str_num)
                if n == 4:
                    self.res += roman[1000]
                    num -= 1000
                    return helper(num)
                elif n == 3:
                    if num >= 500:
                        if str_num[0] != '9':
                            self.res += roman[500]
                            num -= 500
                            return helper(num)
                        else:
                            self.res += 'CM'
                            num -= 900
                        
                    elif num >= 100:
                        if str_num[0] != '4' :
                            self.res += roman[100]
                            num -= 100
                            return helper(num)
                        else:
                            self.res += 'CD'
                            num -= 400
                            return helper(num)
                elif n == 2:
                    if num >= 50:
                        if str_num[0] != '9':
                            self.res += roman[50]
                            num -= 50
                            return helper(num)
                        else:
                            self.res += 'XC'
                            num -= 90
                            return helper(num)
                    elif num >= 10:
                        if str_num[0] != '4':
                            self.res += roman[10]
                            num -= 10
                            return helper(num)
                        else:
                            self.res += 'XL'
                            num -= 40
                            return helper(num)
                elif n == 1:
                    if num != 4 and num != 9:
                        if num >= 5:
                            self.res += roman[5]
                            num -= 5
                            return helper(num)
                        elif num >= 1:
                            self.res += roman[1]
                            num -= 1
                            return helper(num)
                    elif num == 4:
                        self.res +=roman[1] + roman[5]
                        num -= 4
                        return helper(num)
                    elif num == 9:
                        self.res +=roman[1] + roman[10]
                        num -= 9
                        return helper(num)
        helper(num)
        return self.res  
            

                        


                    




