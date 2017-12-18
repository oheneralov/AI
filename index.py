from nltk.chat.util import Chat, reflections
#generate the frequently asked questions
#read data from autobiography


pairs = [
    [
        r"My name is (.*)",
        ['hello %1', '%1 mabuhay ka'],
    ],
	[
        r"What is your name(.*)",
        ['My name is Robot35908', 'Robot35908'],
    ], 
	[
        r"Alex|Bob|Clark|David|Edward|James|John|Robert|Michael|William|Richard|Charles|Joseph|Thomas|Christopher|Daniel|Paul|Mark|Donald",
        ['hello', 'Hi'],
    ], 
	[
        r"Who are you?(.*)",
        ['I am Robot35908', 'Robot35908'],
    ],
    [
        r'hello|hi|Good morning|Good afternoon|Good evening|Good night',
        ['hello', 'kamusta', 'mabuhay', 'hi', "%1"],
    ],
	[
        r'(.*)How do you do?(.*)',
        ['Pleased to meet you', 'hello', 'kamusta', 'mabuhay', 'hi', "%1"],
    ],
	[
        r'(.*)How are you?(.*)',
        ['I am fine thanks. And you?'],
    ],
	[
        r'(.*)Really?(.*)',
        ['Yes'],
    ],
    [
        r'(.*) (hungry|sleepy|groot)',
        [
            "%1 %2"
        ]
    ],
    [
        r'(.*)(mahal|love)(.*)',
        [
            "https://goo.gl/ndTZVq",
            "I always thought Love was a static class until you made an instance of it.",
            "I love user interfaces it's because that's where U and I are always together.",
        ],
    ],
    [
        r'(.*)(relationship)(.*)',
        [
            "Mabuti pa sa database may relationship. Eh tayo, wala.",
        ],
    ],
    [
        r'(meron|mayron|ano|does|is there|what) (.*) (forever)(.*)',
        [
            "Loading...",
            "None",
            "while True: pass",
        ],
    ],
    [
        r'(.*)', # default response if no patterns from above is found
        [
            "I know nothing about %1",
            "Sorry I don't know what `%1` is?",
        ],
    ],
]

def hugot_bot():
    print("Hi what's your name?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    hugot_bot()