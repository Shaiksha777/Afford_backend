import requests,time

window_range = 10
window_current = []

acess_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzQ3MDU5OTE2LCJpYXQiOjE3NDcwNTk2MTYsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjJkMmIxYTIzLWI4NGQtNGU0NC1iOWZiLTExY2RlMjk2ZTVmMyIsInN1YiI6ImNoLmVuLnU0YWllMjIwNjBAY2guc3R1ZGVudHMuYW1yaXRhLmVkdSJ9LCJlbWFpbCI6ImNoLmVuLnU0YWllMjIwNjBAY2guc3R1ZGVudHMuYW1yaXRhLmVkdSIsIm5hbWUiOiJzeWVkIGF5YW4iLCJyb2xsTm8iOiJjaC5lbi51NGFpZTIyMDYwIiwiYWNjZXNzQ29kZSI6IlN3dXVLRSIsImNsaWVudElEIjoiMmQyYjFhMjMtYjg0ZC00ZTQ0LWI5ZmItMTFjZGUyOTZlNWYzIiwiY2xpZW50U2VjcmV0IjoiY0pEY1F2dWFBVWJrbXpTTSJ9.1Y7ebluRuQVELu9hc4sIj-H2CCSKdnmTm6RgzdUiz-M'
url = "http://20.244.56.144/evaluation-service/primes"

headers = {

    "Authorization": f'bearer {acess_token}'
}



def filter_nums(numbers):
    
    global window_current
    prev = window_current.copy()
    
    temp = []
    for num in numbers:
        if num not in temp:
            temp.append(num)

    overflow = len(temp) - window_range
    if overflow > 0:
        temp = temp[overflow:]
    window_current = temp
    return temp,prev
    


def get_num():

    t0 = time.monotonic()
    try:
        response = requests.get(url, headers=headers, timeout=10)
        duration = time.monotonic() - t0
        print(response.status_code)
        
        data = response.json()
        return data['numbers']
    except :
        return []

    


def calculate_avg(nums):
    sum = 0
    avg = 0
    for i in nums:
        sum += i
    if len(nums) > 0:
        avg = sum/len(nums)
    return avg


def display_results(prev,avg,numbers):
    print(f'windowPrevState:{prev}\nwindowCurrState:{window_current}\nnumbers: {numbers}\navg:{avg}')
    

if __name__ == '__main__':
    while True:
        inp = input('enter the type of number: ')
        numbers = get_num()
        filtered_nums,prev = filter_nums(numbers)
        avg = calculate_avg(filtered_nums)

        display_results(prev,avg,numbers)
