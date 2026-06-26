import random
subjects = [
    "alakh pandey",
    "modi ji",
    "rajiv talwar",
    "sushant",
    "india"
]
actions = [
    "brings revolution in education",
    "said wah modi ji wah",
    "yelling on a man saying hm gandu logo se baat nhi krte",
    "is aiming to becoming succesfuck",
    "is good"
]
place_times = [
    "in kanpur at 7 bje",
    "at nalasopara 9 bje subah",
    "on road time dont know timing",
    "everwhere everytime",
    "from ages"
]
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_time = random.choice(place_times)

    headline = f"BREAKING NEWS:{subject} {action} {place_time}"

    print(headline)
    user_input = input("u want to another(y/n)").strip().lower()

    if user_input == "n":
        break







