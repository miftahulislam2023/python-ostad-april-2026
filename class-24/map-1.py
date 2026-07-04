# map(function, iterable)
def double(number):
    return number * 2

numbers = [1, 2, 3, 4, 5]
result = map(double, numbers)
final_list = list(result)
print(final_list) 

print(result) # <map object at 0x...>
"""
১. map -> ইটারেবল (iterable)-এর প্রতিটি উপাদানের ওপর একই কাজ করবে।
২. result হিসেবে আরেকটি ইটারেবল রিটার্ন করবে।
"""