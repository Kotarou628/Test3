def fizzbuzz(num):
"""
引数が3の倍数なら'Fizz'、5の倍数なら'Buzz'、両方の倍数なら
'FizzBuzz'を返す。
 いずれの倍数でもない場合は受け取った数値をそのまま返す。
 """
if num % 3 == 0 and num % 5 == 0:
return 'FizzBuzz'
if num % 3 == 0:
return 'Fizz'
if num % 5 == 0:
return 'Buzz'
return num
