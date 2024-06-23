#KBC
ques = ['What is the color of orange?\n1) Orange\n2) Red\n3) Yellow\n4) Green',
        'What is the color of Red Rose?\n1) Orange\n2) Red\n3) Yellow\n4) Green',
        'What is the color of Lemon?\n1) Orange\n2) Red\n3) Yellow\n4) Green',
        'What is the color of Grapes? \n1) Orange\n2) Red\n3) Yellow\n4) Green',
        'Who is the Iron Man? \n1) Tony Stark\n2) Loki\n3) Thor\n4) Shield',
        'Who can Teleport?\n1) Tony Stark\n2) Loki\n3) Thor\n4) Shield',
        'Who has Mijoneer?\n1) Tony Stark\n2) Loki\n3) Thor\n4) Shield',
        'What Captian Amearica has?\n1) Tony Stark\n2) Loki\n3) Thor\n4) Shield'
        ]
ans = [1,2,3,4,1,2,3,4]

level=0
lev={
    0:"Bhaag yaha se",
    1:'₹10,000',
    2:'₹25,000',
    3:'₹50,000',
    4:'₹1,00,000',
    5:'₹5,00,000',
    6:'₹50,00,000',
    7:'₹1,00,00,000',
    8:'₹7,00,00,000'
    }

ll=(2,4,6,8)

for i in range(len(ques)):
    print(ques[i])
    a=int(input('Konsa answer lock keya jaye (1,2,3,4) | type "9" to quit : '))
    if a == None:
        print(f'Smart move\nYour prize money is {lev[level]}')
        print(f"the correct option is {ans[i]}")
    if a==ans[i]:
        level+=1
    else:
        if level%2==0:
            print(f'Your Prize Money is {lev[level]}')
            break
        else:
            print(f'oops! you fell to lower level : {level-1}')
            print(f'Your Prize money is {lev[level-1]}')
            break
