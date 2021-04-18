class Student:

    # 初期化メソッド
    def __init__(self,name = ""):
        # nameのアトリビュートを初期化する
        # selfにインスタンスが渡されて、そこで全体の変化を出せるイメージ
        self.name = name



    # メソットでの引数は、selfを最初に書く
    # それは、pythonでのプログラムを走らせるときに使われる。
    def ave(self,math,en):
        print((math + en)/2)


# インスタンスの作成
a001 = Student()

a001.ave(30,70)

a001.name = "sato"
print(a001.name)

# インスタンスの作成
# インスタンスと同時に、初期化メソッドにtanakaも送って代入させる
a002 = Student("tanaka")
print(a002.name)