""" Statstical data and model's details from
https://hexaco.org/hexaco-inventory. """

questions120 = {
   "1": "My attitude toward people who have treated me badly is 'forgive and forget'.",
   "2": "I find it hard to fully forgive someone who has done something mean to me.",
   "3": "I find it easy to forgive those who have wronged me.",
   "4": "I find it easy to strike up conversations with strangers in various social settings.",
   "5": "I am quick to forgive and believe in giving second chances, even when others have wronged me",
   "6": "People sometimes tell me that I am too critical of others.",
   "7": "I tend to be lenient in judging other people.",
   "8": "Even when people make a lot of mistakes, I rarely say anything negative.",
   "9": "I believe in treating others with kindness and tenderness, even in difficult situations",
   "10": "I enjoy being the center of attention and receiving positive feedback from others.",
   "11": "I rarely feel anger, even when people treat me quite badly.",
   "12": "I am known for my patience in dealing with challenging individuals.",
   "13": "I tend to stay calm under pressure and avoid getting frustrated easily",
   "14": "I avoid confrontation and try to keep the peace in social situations.",
   "15": "I find it hard to compromise with people when I really think I’m right.",
   "16": "I struggle to accept opinions and beliefs that differ from my own.",
   "17": "Minor annoyances easily bother me, often disrupting harmony.",
   "18": "I can be impatient and closed-minded in group settings, dismissing diverse perspectives.",
   "19": "I am tolerant of others' imperfections and shortcomings.",
   "20": "I stay calm in challenging situations, avoiding unnecessary conflict",
   "21": "When working, I often set ambitious goals for myself.",
   "22": "I often push myself very hard when trying to achieve a goal.",
   "23": "Often when I set a goal, I end up quitting without having reached it.",
   "24": "I do only the minimum amount of work needed to get by.",
   "25": "I plan ahead and organize things, to avoid scrambling at the last minute.",
   "26": "I clean my office or home quite frequently.",
   "27": "When working, I sometimes have difficulties due to being disorganized.",
   "28": "I am meticulous in organizing my schedule and tasks.",
   "29": "I value efficiency and am always looking for ways to streamline processes.",
   "30": "I often check my work over repeatedly to find any mistakes.",
   "31": "I often check my work over repeatedly to find any mistakes.",
   "32": "When working on something, I don't pay much attention to small details.",
   "33": "People often call me a perfectionist.",
   "34": "I pay attention to the smallest details in my work to ensure accuracy.",
   "35": "I make a lot of mistakes because I don't think before I act.",
   "36": "I make decisions based on the feeling of the moment rather than on careful thought.",
   "37": "I make a lot of mistakes because I don't think before I act.",
   "38": "I don’t allow my impulses to govern my behavior.",
   "39": "I am highly disciplined in sticking to my routines and habits.",
   "40": "I pay attention to the smallest details in my work to ensure accuracy.",
   "41": "I sometimes can't help worrying about little things.",
   "42": "I worry a lot less than most people do.",
   "43": "I rarely, if ever, have trouble sleeping due to stress or anxiety.",
   "44": "I get very anxious when waiting to hear about an important decision.",
   "45": "I sometimes can't help worrying about little things.",
   "46": "I can handle difficult situations without needing emotional support from anyone else.",
   "47": "I rarely discuss my problems with other people.",
   "48": "When I suffer from a painful experience, I need someone to make me feel comfortable.",
   "49": "I often seek reassurance and support from others when facing challenges or uncertainties.",
   "50": "I find comfort in relying on close relationships for emotional support and guidance.",
   "51": "I would feel afraid if I had to travel in bad weather conditions.",
   "52": "When it comes to physical danger, I am very fearful.",
   "53": "Even in an emergency I wouldn't feel like panicking.",
   "54": "I can handle difficult situations without needing emotional support from anyone else.",
   "55": "I would feel afraid if I had to travel in bad weather conditions.",
   "56": "I feel reasonably satisfied with myself overall.",
   "57": "When I suffer from a painful experience, I need someone to make me feel comfortable.",
   "58": "I remain unemotional even in situations where most people get very sentimental.",
   "59": "On most days, I feel cheerful and optimistic.",
   "60": "I feel like crying when I see other people crying.",
   "61": "I prefer jobs that involve Active social interaction to those that involve working alone.",
   "62": "I have a high level of physical and mental energy, and I prefer to keep myself busy with various activities rather than being idle",
   "63": "I am often the one who initiates social activities and encourages others to join in.",
   "64": "I enjoy being the center of attention in social gatherings and feel energized by interacting with a large group of people.",
   "65": "Spontaneous activities and last-minute plans excite me, and I am always ready to jump into new experiences.",
   "66": "I am energetic nearly all the time.",
   "67": "Most people are more upbeat and dynamic than I generally am.",
   "68": "I am highly energetic and find it difficult to sit still for long periods.",
   "69": "I often take on the role of the 'life of the party' in social gatherings.",
   "70": "I enjoy having lots of people around to talk with.",
   "71": "I rarely express my opinions in group meetings.",
   "72": "I avoid making 'small talk' with people.",
   "73": "In social situations, I'm usually the one who makes the first move.",
   "74": "I enjoy having lots of people around to talk with.",
   "75": "I tend to feel quite self-conscious when speaking in front of a group of people.",
   "76": "I feel confident in social settings.",
   "77": "Being around others boosts my self-esteem.",
   "78": "I actively seek social interactions.",
   "79": "Positive feedback in social situations is important to me.",
   "80": "Social approval positively impacts my self-worth.",
   "81": "I believe in treating everyone fairly, regardless of their status or background.",
   "82": "I avoid taking advantage of others to achieve personal gain.",
   "83": "It's important to me to play by the rules, even when no one is watching.",
   "84": "I think it's wrong to manipulate situations for my benefit at the expense of others.",
   "85": "Being honest and fair in my interactions is a fundamental principle in my life.",
   "86": "If I knew that I could never get caught, I would be willing to steal a million dollars.",
   "87": "Having a lot of money is not especially important to me.",
   "88": "I would be tempted to buy stolen property if I were financially tight.",
   "89": "I’d be tempted to use counterfeit money, if I were sure I could get away with it.",
   "90": "It wouldn’t bother me to harm someone I didn’t like.",
   "91": "I prefer to let my actions speak for themselves rather than seeking attention or praise from others",
   "92": "I think that I am entitled to more respect than the average person is.",
   "93": "I am an ordinary person who is no better than others.",
   "94": "I wouldn’t want people to treat me as though I were superior to them.",
   "95": "I feel that I am an unpopular person.",
   "96": "If I want something from a person I dislike, I will act very nicely toward that person in order to get it.",
   "97": "I wouldn't pretend to like someone just to get that person to do favors for me.",
   "98": "I believe that honesty is the most important quality in any relationship.",
   "99": "I value integrity and would never compromise my principles for personal gain.",
   "100": "People see me as a hard-hearted person.",
   "101": "I would be quite bored by a visit to an art gallery.",
   "102": "I wouldn't spend my time reading a book of poetry.",
   "103": "I find beauty and inspiration in the smallest details of the world around me.",
   "104": "I want people to know that I am an important person of high status.",
   "105": "I would like to live in a very expensive, high-class neighborhood.",
   "106": "I would enjoy creating a work of art, such as a novel, a song, or a painting.",
   "107": "If I had the opportunity, I would like to attend a classical music concert.",
   "108": "I often engage in creative pursuits, such as writing, drawing, or playing a musical instrument.",
   "109": "I enjoy exploring new and unconventional ideas through imaginative thinking and artistic expression.",
   "110": "I have a knack for thinking outside the box and approaching situations from unique perspectives",
   "111": "When faced with a complex problem, I dive deep into it, exploring various possibilities and solutions",
   "112": "I'm interested in learning about the history and politics of other countries.",
   "113": "I enjoy looking at maps of different places.",
   "114": "I have a keen interest in understanding different philosophical perspectives.",
   "115": "I am open to trying new and exotic foods, even if they are outside my comfort zone.",
   "116": "I would like a job that requires following a routine rather than being creative.",
   "117": "I think that paying attention to radical ideas is a waste of time.",
   "118": "I like people who have unconventional views.",
   "119": "I enjoy exploring new and unconventional ideas that challenge traditional norms.",
   "120": "I find the pursuit of personal success and status symbols to be important for my sense of achievement and recognition."
}


reversal = [ 15, 16, 17, 18, 23, 24, 27, 32, 33, 35, 36, 37, 38, 42, 43, 44, 45, 46, 47, 48, 52,
            53, 55, 58, 67, 71, 72, 75, 86, 88, 89, 90, 92, 94, 96, 97, 102, 104, 116, 117, 120 ]

# domains_questions = {
#     'h': [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100 ],
#     'e': [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60 ],
#     'x': [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80 ],
#     'a': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ],
#     'c': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 ],
#     'o': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120 ],
#     # 'altruism':[97, 98, 99, 100],
# }

facets_questions = {
   "Honesty-Humility (H)": {
      "Fairness (H2)": [81, 82, 83, 84, 85],
      "Greed Avoidance": [86, 87, 88, 89, 90],
      "Modesty": [91, 92, 93, 94, 95],
      "Sincerity": [96, 97, 98, 99, 100]
   },
   "Emotionality (E)": {
      "Anxiety": [41, 42, 43, 44, 45],
      "Dependence": [46, 47, 48, 49, 50],
      "Fearfulness": [51, 52, 53, 54, 55],
      "Sentimentality": [56, 57, 58, 59, 60]
   },
   "eXtraversion (X)": {
      "Activeness": [61, 62, 63, 64, 65],
      "Liveliness": [66, 67, 68, 69, 70],
      "Sociable": [71, 72, 73, 74, 75],
      "Social Self-Esteem (X1)": [76, 77, 78, 79, 80]
   },
   "Agreeableness (A)": {
      "Forgiveness": [1, 2, 3, 4, 5],
      "Gentleness": [6, 7, 8, 9, 10],
      "Patience": [11, 12, 13, 14, 15],
      "Tolerance": [16, 17, 18, 19, 20]
   },
   "Conscientiousness (C)": {
      "Diligence": [21, 22, 23, 24, 25],
      "Organization": [26, 27, 28, 29, 30],
      "Precision": [31, 32, 33, 34, 35],
      "Reliability": [36, 37, 38, 39, 40]
   },
   "Openness to Experience (O)": {
      "Aesthetic Appreciation": [101, 102, 103, 104, 105],
      "Creativity": [106, 107, 108, 109, 110],
      "Inquisitiveness": [111, 112, 113, 114, 115],
      "Unconventionality": [116, 117, 118, 119, 120]
   }
}


