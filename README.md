# atcoder-myenv
本リポジトリは，AtCoderをPythonで取り組むための仮想環境をまとめたものです．主に個人利用を目的としています．


## 環境作成方法
1. [Docker Engineのインストール](https://docs.docker.com/engine/install/)
    1. Homebrewの場合は
    ```
    brew install --cask docker
    ```
1. [VSCodeのインストール](https://code.visualstudio.com/download)
    1. Homebrewの場合は
    ```
    brew install --cask visual-studio-code
    ```
1. [VSCode拡張機能```Remote-Containers```のインストール](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
1. 本リポジトリのclone
    ```
    git clone https://github.com/hrt0809/atcoder-myenv
    ```


## 使用方法
1. VSCodeを起動し，```Reopen in Container: Remote-Containers```選択．
1. atcoder-cli, online-judge-toolsにログイン(コンテナ作成直後の初回のみ)．
    1. ```acc login```
    1. ```oj login https://atcoder.jp/```(```acc s```時に必要)
1. AtCoderから問題を取得しサンプルケース等をダウンロード．
    1. ```newprob ${ContestID}```(ex: ```newprob AHC001```で```acc new AHC001 && cd AHC001```を実行)
1. 解答を作成．
    1. ```cd ${Problem}```
    1. ```${Problem}/main.py```に記述
1. サンプルケースでテスト．
    1. ```testoj```
    1. あるいは```testpy ${SampleID}```(ex: ```testpy 1```で```python3 main.py < test/sample-1.in```を実行)
1. 解答を提出．
    1. ```acc s```
1. 次の問題へ．
    1. acc add (最初に全ての問題を取得する場合は，```acc config default-task-choice all```へと変更する)

## Dockerコンテナ内で使用しているパッケージへのリンク
1. [atcoder-cliチュートリアル](http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/)
1. [online-judge-tools](https://github.com/online-judge-tools/oj/blob/master/README.ja.md)
