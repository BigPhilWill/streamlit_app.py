import streamlit as st
import random

# Define the functions to generate random elements for each category
def generate_compliment():
    compliments = ["Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Do you have a map? I keep getting lost in your eyes.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Are you a Wi-Fi signal? Because I'm feeling a connection.",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you believe in love at first sight, or should I walk by again?",
    "Is your name Wi-Fi? Because I'm really feeling a connection.",
    "If you were a fruit, you'd be a fine-apple.",
    "I must be a snowflake because I've fallen for you.",
    "Can I follow you home? Cause my parents always told me to follow my dreams.",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "If you were a cat, you'd purr-fectly match my lap.",
    "I must be a snowflake because I've fallen for you.",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Ariel? Because we were mer-made for each other.",
    "Can you take me to the doctor? Because I just broke my leg falling for you.",
    "Do you have a name, or can I call you mine?",
    "Are you a time traveler? Because I can see you in my future.",
    "Is your name Cinderella? Because your smile is magical.",
    "Do you have a name, or can I call you mine?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "I'm not a photographer, but I can definitely picture us together.",
    "Are you a camera? Every time I look at you, I smile.",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "Is your name Honey? Because you're the sweetest thing I've ever met.",
    "If you were a star, you'd be the brightest one in the sky.",
    "Are you a bank loan? Because you have my interest.",
    "Do you have a name or can I call you mine?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Ariel? Because we were mer-made for each other.",
    "Are you made of copper and tellurium? Because you're Cu-Te.",
    "I must be a snowflake because I've fallen for you.",
    "Do you have a name or can I call you mine?",
    "Is your name Honey? Because you're the sweetest thing I've ever met.",
    "If you were a star, you'd be the brightest one in the sky.",
    "Are you a bank loan? Because you have my interest.",
    "Is your name Cinderella? Because your smile is magical.",
    "Do you have a map? I keep getting lost in your eyes.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Do you believe in love at first sight, or should I walk by again?",
    "Are you a Wi-Fi signal? Because I'm feeling a connection.",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "If you were a cat, you'd purr-fectly match my lap.",
    "I must be a snowflake because I've fallen for you.",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Ariel? Because we were mer-made for each other.",
    "Can you take me to the doctor? Because I just broke my leg falling for you.",
    "Do you have a name, or can I call you mine?",
    "Are you a time traveler? Because I can see you in my future.",
    "Is your name Cinderella? Because your smile is magical.",
    "Do you have a name, or can I call you mine?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "I'm not a photographer, but I can definitely picture us together.",
    "Are you a camera? Every time I look at you, I smile.",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "Is your name Honey? Because you're the sweetest thing I've ever met.",
    "If you were a star, you'd be the brightest one in the sky.",
    "Are you a bank loan? Because you have my interest.",
    "Do you have a name or can I call you mine?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Ariel? Because we were mer-made for each other.",
    "Are you made of copper and tellurium? Because you're Cu-Te.",
    "I must be a snowflake because I've fallen for you.",
    "Do you have a name or can I call you mine?",
    "Is your name Honey? Because you're the sweetest thing I've ever met.",
    "If you were a star, you'd be the brightest one in the sky.",
    "Are you a bank loan? Because you have my interest.",
    "Is your name Cinderella? Because your smile is magical.",
    "Do you have a map? I keep getting lost in your eyes.",
    "Is your name Google? Because you have everything I've been searching for.",
    "Do you believe in love at first sight, or should I walk by again?",
    "Are you a Wi-Fi signal? Because I'm feeling a connection.",
    "If you were a vegetable, you'd be a cute-cumber!",
    "Do you have a Band-Aid? Because I just scraped my knee falling for you.",
    "If you were a cat, you'd purr-fectly match my lap.",
    "I must be a snowflake because I've fallen for you.",
    "Do you have a sunburn, or are you always this hot?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Ariel? Because we were mer-made for each other.",
    "Can you take me to the doctor? Because I just broke my leg falling for you.",
    "Do you have a name, or can I call you mine?",
    "Are you a time traveler? Because I can see you in my future.",
    "Is your name Cinderella? Because your smile is magical.",
    "Do you have a name, or can I call you mine?",
    "If you were a vegetable, you'd be a cute-cumber!",
    "I'm not a photographer, but I can definitely picture us together.",
    "Are you a camera? Every time I look at you, I smile.",
    "Do you have a pencil? Cause I want to erase your past and write our future.",
    "Is your name Honey? Because you're the sweetest thing I've ever met.",
    "If you were a star, you'd be the brightest one in the sky.",
    "Are you a bank loan? Because you have my interest.",
    "Do you have a name or can I call you mine?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Ariel? Because we were mer-made for each other.",
    "Are you made of copper and tellurium? Because you're Cu-Te.",]
    return random.choice(compliments)

def generate_backhanded_compliment():
    backhanded_compliments = ["You're almost as smart as you look.",
    "You're not as annoying as I expected.",
    "You clean up well!",
    "You're actually pretty funny for someone with no sense of humor.",
    "I'm impressed; you're not as terrible as they say.",
    "You have a unique personality, to say the least.",
    "I wouldn't call you ugly, but I wouldn't call you attractive either.",
    "You're not the worst person I've ever met.",
    "You're not completely useless; you can always serve as a bad example.",
    "I wouldn't say you're terrible at your job, but you're not great either.",
    "I'm surprised; you're not as annoying in small doses.",
    "You're not as dumb as you look, which isn't saying much.",
    "You're not a complete waste of space.",
    "You're actually more interesting than I thought you'd be.",
    "I don't hate spending time with you as much as I thought I would.",
    "You're not the worst roommate I've ever had.",
    "You're not entirely useless; you can be used as a bad example.",
    "You have a certain charm, in a very strange way.",
    "I wouldn't say you're terrible, but you're not great either.",
    "You're not as bad as I expected, which is a pleasant surprise.",
    "You're almost likable when I'm in the right mood.",
    "You're not as terrible as people make you out to be.",
    "I have to admit, you're not as annoying as I thought you'd be.",
    "You're actually more tolerable than I originally thought.",
    "You're almost as interesting as you think you are.",
    "You're not completely unbearable; I can stand you for a while.",
    "I wouldn't call you the worst person ever, but you're not the best either.",
    "You're not the dumbest person I know, but you're not the smartest either.",
    "I didn't expect much from you, but you've exceeded my low expectations.",
    "You're not entirely useless, just mostly.",
    "I wouldn't say you're terrible, but you're not great either.",
    "You're not as terrible as I thought you'd be, which is something, I guess.",
    "You're not as awful as you seem, though that's not saying much.",
    "I thought you'd be worse, but you're surprisingly tolerable.",
    "You're not the worst coworker I've had; just one of the not-so-great ones.",
    "You're not as bad as you look.",
    "You're not completely useless; you can always serve as a bad example.",
    "I wouldn't call you the worst roommate I've had, but you're not the best either.",
    "You're not the most incompetent person I've met, but you're close.",
    "I don't hate spending time with you as much as I thought I would.",
    "You're not the worst person I know, but you're far from the best.",
    "You're not entirely useless, just mostly.",
    "I wouldn't say you're terrible, but you're not great either.",
    "You're not as terrible as I thought you'd be, which is something, I guess.",
    "You're not as awful as you seem, though that's not saying much.",
    "I thought you'd be worse, but you're surprisingly tolerable.",
    "You're not the worst coworker I've had; just one of the not-so-great ones.",
    "You're not as bad as you look.",
    "You're not completely useless; you can always serve as a bad example.",
    "I wouldn't call you the worst roommate I've had, but you're not the best either.",
    "You're not the most incompetent person I've met, but you're close.",
    "You're not the most unpleasant person to be around.",
    "You're not the worst driver I've ever ridden with, but close.",
    "You're not as annoying as I expected you to be.",
    "You're not the worst cook I've ever met, just not the best.",
    "You're not as bad as I thought you'd be, which is something, I guess.",
    "You're not as terrible as you look, at least on the outside.",
    "You're not the worst person to be stuck in an elevator with, just close.",
    "You're not as useless as I originally thought.",
    "I wouldn't call you the worst neighbor, but you're not the best either.",
    "You're not the worst date I've been on, but you're not the best either.",
    "You're not completely unbearable; I can stand you for a while.",
    "I wouldn't say you're terrible, but you're not great either.",
    "You're not as terrible as I thought you'd be, which is something, I guess.",
    "You're not as awful as you seem, though that's not saying much.",
    "I thought you'd be worse, but you're surprisingly tolerable.",
    "You're not the worst coworker I've had; just one of the not-so-great ones.",
    "You're not as bad as you look.",
    "You're not completely useless; you can always serve as a bad example.",
    "I wouldn't call you the worst roommate I've had, but you're not the best either.",
    "You're not the most incompetent person I've met, but you're close.",
    "You're not the most unpleasant person to be around.",
    "You're not the worst driver I've ever ridden with, but close.",
    "You're not as annoying as I expected you to be.",
    "You're not the worst cook I've ever met, just not the best.",
    "You're not as bad as I thought you'd be, which is something, I guess.",
    "You're not as terrible as you look, at least on the outside.",
    "You're not the worst person to be stuck in an elevator with, just close.",
    "You're not as useless as I originally thought.",
    "I wouldn't call you the worst neighbor, but you're not the best either.",
    "You're not the worst date I've been on, but you're not the best either.",
    "You're not as terrible as people make you out to be.",
    "I have to admit, you're not as annoying as I thought you'd be.",
    "You're actually more tolerable than I originally thought.",
    "You're almost as interesting as you think you are.",
    "You're not completely unbearable; I can stand you for a while.",
    "I wouldn't say you're terrible, but you're not great either.",
    "You're not as terrible as I expected, which is a pleasant surprise.",
    "You're almost likable when I'm in the right mood.",
    "You're not as terrible as people make you out to be.",
    "I have to admit, you're not as annoying as I thought you'd be.",
    "You're actually more tolerable than I originally thought.",
    "You're almost as interesting as you think you are.",
    "You're not completely unbearable; I can stand you for a while."]
    return random.choice(backhanded_compliments)

def generate_animal_fact():
    animal_facts = ["The mantis shrimp has the world's fastest punch, delivering a blow with the acceleration of a .22 caliber bullet.",
    "Octopuses have three hearts, two pump blood to the gills, while the third pumps it to the rest of the body.",
    "A newborn kangaroo is about 1 inch long and weighs less than a gram.",
    "Sloths can hold their breath for up to 40 minutes.",
    "A group of flamingos is called a 'flamboyance.'",
    "Honeybees can recognize human faces.",
    "Penguins can jump up to 6 feet in the air.",
    "The electric eel can generate shocks of up to 600 volts.",
    "A newborn giraffe falls about 6 feet to the ground when it's born.",
    "The unicorn is Scotland's national animal.",
    "The star-nosed mole can eat worms faster than the human eye can follow.",
    "A group of jellyfish is called a smack.",
    "Bees can see ultraviolet light, allowing them to spot nectar patterns on flowers.",
    "Female mosquitoes are the ones that bite, while male mosquitoes primarily feed on nectar.",
    "The archerfish can spit a stream of water to knock insects into the water, where they become a tasty meal.",
    "The proboscis monkey has an unusually long nose that can reach up to 7 inches.",
    "A group of hummingbirds is called a charm.",
    "The glass frog's transparent skin allows you to see its internal organs, including its heart.",
    "The leaf-tailed gecko has evolved to look just like a dead leaf to avoid predators.",
    "The Aye-aye, a lemur from Madagascar, has a long, bony middle finger used for extracting insects from tree bark.",
    "The axolotl can regrow entire lost limbs, making it a remarkable regenerator.",
    "A group of kangaroos is called a mob, and they are known for their powerful hopping abilities.",
    "Ravens are incredibly intelligent birds and have been observed using tools in the wild.",
    "Some species of cuttlefish can change the color and pattern of their skin to blend into their surroundings.",
    "Axolotls are neotenic, which means they retain their juvenile characteristics throughout their lives.",
    "The mimic octopus can imitate the appearance and behavior of other sea creatures to evade predators.",
    "Seahorses are monogamous and often mate for life, performing intricate courtship dances.",
    "The Galapagos tortoise can live for more than 100 years, with some individuals reaching 200 years.",
    "Some ants can carry objects up to 50 times their body weight, showcasing incredible strength.",
    "Chameleons can move their eyes independently, allowing them to focus on different objects simultaneously.",
    "The narwhal, often referred to as the 'unicorn of the sea,' has a long spiral tusk that can grow up to 10 feet in length.",
    "Some species of ants farm fungi, cultivating them as a food source within their colonies.",
    "A group of lemurs is called a conspiracy, reflecting their social and cooperative nature.",
    "The octopus has three hearts – two pump blood to the gills, while the third pumps it to the rest of the body.",
    "Red-eyed tree frogs have bright red eyes and vibrant green skin, making them one of the most colorful amphibians in the world.",
    "The slow loris is one of the only known venomous primates, producing a toxic secretion from its elbows.",
    "In the animal kingdom, the cheetah is the fastest land mammal, capable of reaching speeds up to 75 miles per hour.",
    "The frilled lizard uses its distinctive frill as a display of intimidation when threatened.",
    "The harpy eagle, a powerful raptor, has talons larger than the claws of a grizzly bear.",
    "The platypus is one of the few mammals that lay eggs and has a bill similar to that of a duck."]
    return random.choice(animal_facts)

def generate_chat_up_line():
    chat_up_lines = [    "Are you a magician? Because whenever I look at you, everyone else disappears.",
    "Do you have a map? I keep getting lost in your eyes.",
    "Do you believe in love at first sight, or should I walk by again?",
    "Are you made of copper and tellurium? Because you're Cu-Te.",
    "Is your name Google? Because you have everything I've been searching for.",
    "I must be a snowflake because I've fallen for you.",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Is your name Wi-Fi? Because I'm really feeling a connection.",
    "Do you have a name, or can I call you mine?",
    "Are you a time traveler? Because I can see you in my future.",
    "Can you take a picture with me? I want to prove to my friends that angels are real.",
    "Are you a bank loan? Because you have my interest.",
    "If you were a vegetable, you'd be a cute-cumber.",
    "Is your name Cinderella? Because I see that dress disappearing at midnight.",
    "I must be a snowstorm because I've fallen for you.",
    "Are you a camera? Every time I look at you, I smile.",
    "Is your name Honey? Because you're the sweetest thing I've ever met.",
    "Are you a campfire? Because you're hot and I can't resist getting closer.",
    "If you were a fruit, you'd be a fine-apple.",
    "Do you have a name or can I call you mine?",
    "Are you a campfire? Because you're hot and I want s'more.",
    "Do you believe in love at first sight, or should I walk by again?",
    "Is your name Google? Because you have everything I've been searching for.",
    "I must be a snowflake because I've fallen for you.",
    "Is your name Wi-Fi? Because I'm really feeling a connection."]
    return random.choice(chat_up_lines)

def generate_famous_quote():
    famous_quotes = ["The only way to do great work is to love what you do. - Steve Jobs",
    "In three words, I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment. - Ralph Waldo Emerson",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. - Jordan Belfort",
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "The only true wisdom is in knowing you know nothing. - Socrates",
    "It is during our darkest moments that we must focus to see the light. - Aristotle Onassis",
    "To succeed in life, you need two things: ignorance and confidence. - Mark Twain",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson",
    "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
    "You can't go back and change the beginning, but you can start where you are and change the ending. - C.S. Lewis",
    "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
    "The secret of getting ahead is getting started. - Mark Twain",
    "It is not the strongest of the species that survive, nor the most intelligent, but the one most responsive to change. - Charles Darwin",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "A journey of a thousand miles begins with a single step. - Lao Tzu",
    "The only thing worse than being blind is having sight but no vision. - Helen Keller",
    "If you want to achieve greatness stop asking for permission. - Anonymous",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "We become what we think about. - Earl Nightingale",
    "The best revenge is massive success. - Frank Sinatra",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "It is never too late to be what you might have been. - George Eliot",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The power of imagination makes us infinite. - John Muir",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Do one thing every day that scares you. - Eleanor Roosevelt",
    "Simplicity is the ultimate sophistication. - Leonardo da Vinci",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "In order to succeed, we must first believe that we can. - Nikos Kazantzakis",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William B. Sprague",
    "It's not what happens to you, but how you react to it that matters. - Epictetus",
    "The best revenge is to be unlike him who performed the injury. - Marcus Aurelius",
    "Opportunity does not knock, it presents itself when you beat down the door. - Kyle Chandler",
    "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Courage is resistance to fear, mastery of fear, not absence of fear. - Mark Twain",
    "When one door is closed, don't you know, another is open. - Bob Marley",
    "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
    "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
    "It is never too late to be what you might have been. - George Eliot",
    "Success is walking from failure to failure with no loss of enthusiasm. - Winston Churchill",
    "The power of imagination makes us infinite. - John Muir",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Do one thing every day that scares you. - Eleanor Roosevelt",
    "Simplicity is the ultimate sophistication. - Leonardo da Vinci",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
    "In order to succeed, we must first believe that we can. - Nikos Kazantzakis",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William B. Sprague",
    "It's not what happens to you, but how you react to it that matters. - Epictetus",
    "The best revenge is to be unlike him who performed the injury. - Marcus Aurelius",
    "Opportunity does not knock, it presents itself when you beat down the door. - Kyle Chandler",
    "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston S. Churchill",
    "The only place where success comes before work is in the dictionary. - Vidal Sassoon",
    "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
    "Courage is resistance to fear, mastery of fear, not absence of fear. - Mark Twain",
    "When one door is closed, don't you know, another is open. - Bob Marley",
    "The only thing that stands between you and your dream is the will to try and the belief that it is actually possible. - Joel Brown",
    "Don't be pushed around by the fears in your mind. Be led by the dreams in your heart. - Roy T. Bennett",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "When the power of love overcomes the love of power, the world will know peace. - Jimi Hendrix",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "It does not matter how slowly you go as long as you do not stop. - Confucius",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "I find that the harder I work, the more luck I seem to have. - Thomas Jefferson",
    "The only true wisdom is in knowing you know nothing. - Socrates",
    "It is during our darkest moments that we must focus to see the light. - Aristotle Onassis",
    "To succeed in life, you need two things: ignorance and confidence. - Mark Twain",
    "The best way to predict your future is to create it. - Abraham Lincoln",
    "Life is really simple, but we insist on making it complicated. - Confucius",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "A journey of a thousand miles begins with a single step. - Lao Tzu",
    "The only thing worse than being blind is having sight but no vision. - Helen Keller"]
    return random.choice(famous_quotes)

# Create the Streamlit app
st.title("Random Generator App")
category = st.sidebar.selectbox("Select a category:", ["Compliment Generator", "Backhanded Compliment Generator", "Animal Fact Generator", "Chat Up Line Generator", "Famous Quote Generator"])

if category == "Compliment Generator":
    st.header(category)
    if st.button("Generate Compliment"):
        st.write(generate_compliment())
elif category == "Backhanded Compliment Generator":
    st.header(category)
    if st.button("Generate Backhanded Compliment"):
        st.write(generate_backhanded_compliment())
elif category == "Animal Fact Generator":
    st.header(category)
    if st.button("Generate Animal Fact"):
        st.write(generate_animal_fact())
elif category == "Chat Up Line Generator":
    st.header(category)
    if st.button("Generate Chat Up Line"):
        st.write(generate_chat_up_line())
elif category == "Famous Quote Generator":
    st.header(category)
    if st.button("Generate Famous Quote"):
        st.write(generate_famous_quote())
