from sklearn import tree

features = [[140, 0],[130, 0],[150,1],[170,1],[200,0]]

labels = [0,0,1,1,1]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features, labels)

feeling = input('how does it feel by touching - 0 for smooth or 1 for bumpy: ')
weight = input('what is the weight in grams - 130,140,150 or 170: ')  

pred = clf.predict([[weight,feeling]])

if pred == 0:
    print ('it is an apple')
else:
    print ('it is an orange')
