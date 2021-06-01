# put your python code here
hour_one = int(input())
minute_one = int(input())
second_one = int(input())
hour_two = int(input())
minute_two = int(input())
second_two = int(input())
hour = (hour_two - hour_one) * 60 * 60
minute = (minute_two - minute_one) * 60
second = (second_two - second_one)
print(hour + minute + second)
