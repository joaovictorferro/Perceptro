#Equipe:
#Arthur Savio
#Guilherme Amaral
#João Victor Ribeiro
#tabela: 15

import pandas as pd
from sklearn.neural_network import MLPClassifier


table15 = [[1, 1, 1, 1],# 1 pra True e 0 pra false
            [1, 1, 0, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 1],
            [0, 1, 1, 1],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1]]

columns = ["p", "q", "r", "(p or r) or !q"]
features = ["p", "q", "r"]
result = ["(p or r) or !q"]

df = pd.DataFrame(data = table15, columns = columns)

X = df[features]
y = df[result]

clf = MLPClassifier(solver='sgd', activation = 'logistic', hidden_layer_sizes=(9, 9), learning_rate_init = 1,
                    learning_rate = 'constant', random_state=1,max_iter=500)

clf.fit(X, [1, 1, 1, 1, 1, 1, 0, 1])


test = [[1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
            [1, 0, 0],
            [0, 1, 1],
            [0, 1, 0],
            [0, 0, 1],
            [0, 0, 0]]

clf.predict(test)

print(clf.score(test,[1,1,1,1,1,1,0,1]))
