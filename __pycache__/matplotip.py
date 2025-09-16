import matplotlib.pyplot as plt

sn=['sanjay','kiran','jacob','pruthvi','akshat','pranav','mukilan','harshan']
sm=[79,78,77,76,75,74,72,71]
mp=[]
for x in sm:
    r=(x/80)*100
    mp.append(r)

print(mp)

def mlc():
    plt.plot(sn,sm)
    plt.title('STUDENT MARKS GRAPH')
    plt.xlabel('student name')
    plt.ylabel('student marks')
    plt.show

mlc()

def pbc():
    plt.bar(sn,sm)
    plt.title('STUDENTPERCENTAGE GRAPH')
    plt.xlabel('student name')
    plt.ylabel('student percentage')
    plt.show

pbc()
