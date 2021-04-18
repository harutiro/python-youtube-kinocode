class Student:

    # コンストラクタ　初期化メソッド
    def __init__(self):

        # アトリビュート
        self.name = ""

    # メソッド
    def avg(self,math,en):
        print((math + en)/2)

# インスタンス
a001 = Student()　#クラス
a001.name = "sato"
print(a001.name)