import random

choice = input("NICHE: politics,sports,technology (write in small letters) ")

if choice == "politics":
    p_subjects = [
    "The Prime Minister",
    "The Chief Minister",
    "A senior minister",
    "The opposition leader",
    "A government spokesperson",
    "A local MLA",
    "A Member of Parliament",
    "The election commission",
    "A political party",
    "A cabinet minister",
    "A party worker",
    "A city mayor",
    "A state governor",
    "A district collector",
    "A political strategist"
]
    
    p_actions = [
    "announced free Wi-Fi for cows",
    "declared Monday a holiday for everyone",
    "forgot their own speech",
    "promised to build roads on the Moon",
    "challenged aliens to an election debate",
    "started dancing during a press conference",
    "accidentally liked every social media post",
    "claimed that tea increases Wi-Fi speed",
    "held a meeting that lasted only 2 minutes",
    "introduced a new 'nap break' policy",
    "asked citizens to smile for better GDP",
    "celebrated a victory before the results",
    "launched a campaign to plant chocolate trees",
    "arrived at the rally on a bicycle",
    "mistook a movie script for an official document"
]
    p_place_times = [
   "in Parliament at 10:00 AM",
    "outside the Parliament building at midnight",
    "during a press conference in Delhi",
    "at a public rally in Lucknow",
    "inside the Chief Minister's office",
    "near India Gate at sunset",
    "during an election campaign in Jaipur",
    "at the party headquarters",
    "at a roadside tea stall at 6:30 AM",
    "inside a secret meeting room",
    "on the steps of the assembly building",
    "at a railway station during rush hour",
    "in front of thousands of supporters",
    "during a live TV interview",
    "at the airport before boarding a flight",
    "on Independence Day celebrations",
    "during a budget meeting",
    "while visiting a local village",
    "at a five-star hotel conference",
    "during a surprise inspection"
]
    while True:
        subject = random.choice(p_subjects)
        action = random.choice(p_actions)
        place_time = random.choice(p_place_times)
        headline = f"BREAKING NEWS:{subject} {action} {place_time}"
        print(headline)
        user_input = input("u want to another(y/n)").strip().lower()
        if user_input == "n":
            break

elif choice == "sports":
    s_subjects = [
    "Virat Kohli",
    "Rohit Sharma",
    "MS Dhoni",
    "Jasprit Bumrah",
    "Hardik Pandya",
    "Shubman Gill",
    "Neeraj Chopra",
    "PV Sindhu",
    "The Indian Cricket Team",
    "The football coach",
    "A star footballer",
    "A tennis champion",
    "The team captain",
    "The head coach",
    "The match referee",
    "An IPL franchise",
    "A cricket commentator",
    "The Olympic champion",
    "The national hockey team",
    "A young cricket sensation"

]
    
    s_actions = [
    "scored a century",
    "hit six sixes in one over",
    "won the championship",
    "broke a world record",
    "lifted the trophy",
    "made an unbelievable comeback",
    "took a stunning hat-trick",
    "won the match in the last over",
    "surprised everyone with a bicycle kick",
    "celebrated the victory with fans",
    "accidentally dropped the trophy",
    "forgot to bring the cricket bat",
    "challenged the coach to a race",
    "gave an emotional retirement speech",
    "won the Player of the Match award",
    "scored the fastest goal of the season",
    "hit the longest six of the tournament",
    "led the team to a historic victory",
    "received a standing ovation from the crowd",
    "started dancing after winning the match"
]
    
    s_place_times = [
    "at Wankhede Stadium",
    "at Eden Gardens",
    "during the IPL final",
    "during the World Cup final",
    "at the Olympics",
    "at the Asian Games",
    "during a practice session",
    "in the dressing room",
    "at a post-match press conference",
    "during the last over of the match",
    "at Lord's Cricket Ground",
    "at Narendra Modi Stadium",
    "during the opening ceremony",
    "at a packed stadium",
    "in front of 80,000 spectators",
    "during the award ceremony",
    "at the national training camp",
    "during the semi-final match",
    "under the floodlights at 8:00 PM",
    "while warming up before the match"
]

    while True:
        subject = random.choice(s_subjects)
        action = random.choice(s_actions)
        place_time = random.choice(s_place_times)
        headline = f"BREAKING NEWS:{subject} {action} {place_time}"
        print(headline)
        user_input = input("u want to another(y/n)").strip().lower()
        if user_input == "n":
            break


elif choice == "technology":

    t_subjects = [
        "OpenAI",
        "Google",
        "Microsoft",
        "Apple",
        "Tesla",
        "NVIDIA",
        "A software engineer",
        "An AI chatbot",
        "A hacker",
        "A cybersecurity expert",
        "A tech startup",
        "A robot",
        "A programming student",
        "A data scientist",
        "A cloud engineer",
        "A YouTuber",
        "A gamer",
        "A smartphone company",
        "An AI assistant",
        "A coding instructor"
    ]

    t_actions = [
        "launched a revolutionary AI model",
        "accidentally deleted the internet",
        "released a buggy software update",
        "built a robot that makes tea",
        "created an app in just 10 minutes",
        "forgot the Wi-Fi password",
        "hacked their own website",
        "developed a flying laptop",
        "made a computer run without electricity",
        "trained an AI to write poetry",
        "invented a keyboard with only one key",
        "created a phone that never needs charging",
        "built a drone that delivers pizza",
        "discovered a secret programming language",
        "made an AI that tells dad jokes",
        "found a bug that became a feature",
        "coded for 48 hours without sleeping",
        "launched a transparent smartphone",
        "created a robot that does homework",
        "accidentally made the computer laugh"
    ]

    t_place_times = [
        "at a global tech conference",
        "inside a secret research lab",
        "at Silicon Valley",
        "during a live product launch",
        "at Google's headquarters",
        "at Microsoft's office",
        "during a coding competition",
        "at an AI summit",
        "inside a data center",
        "during a hackathon",
        "at a robotics exhibition",
        "while live streaming",
        "at a university tech fest",
        "during a software update",
        "inside a server room",
        "at a startup office",
        "during an online meeting",
        "at midnight while coding",
        "during a product demonstration",
        "on GitHub"
    ]

    while True:
        subject = random.choice(t_subjects)
        action = random.choice(t_actions)
        place_time = random.choice(t_place_times)

        headline = f"BREAKING NEWS: {subject} {action} {place_time}"

        print(headline)

        user_input = input("Do you want another? (y/n): ").strip().lower()

        if user_input == "n":
            break


print("thankyou")



