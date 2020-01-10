from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

### AND演算を学習させるsample.

# input data(=説明変数)
lean_data = [[0,0],[1,0],[0,1],[1,1]]

# Result label(=目的変数)
lean_label = [0,0,0,1]

# Specified Algorism (=アルゴリズム選択)
# チートシートから目的に合うアルゴリズムを選択
# 今回はクラス分けということでLinearSVC
# https://qiita.com/sugulu/items/e3fc39f2e552f2355209
clf = LinearSVC()

# Learning (input, label)
clf.fit(lean_data, lean_label)

# Test
test_data = [[2,2],[3,1],[1,1],[0,0]]
test_label = clf.predict(test_data)

# Result 正解との比較
print(test_data , "の予測結果：", test_label)
print("正解率 = " , accuracy_score([1, 0, 1, 0], test_label))