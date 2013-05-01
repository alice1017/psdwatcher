.. image:: https://raw.github.com/alice1017/psdwatcher/master/psdwatcher_logo.jpg

What is psdwatcher?
#####################

**psdwatcher** はPhotoshopで扱う **PSDファイル** の変更を **git** を使ってステージングやコミットを行い、 *いつでも前のバージョン見れるようにする* Pythonスクリプトです。

How to Use?
############

**psdwatcher** は、わずか **2 Step** で使用出来ます。

1. ウォッチリストにPSDファイルを登録する
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ psdwatcher add sample.psd

まず、psdwatcherに変更を追って欲しいPSDファイルを登録します。
psdwatcherの **add** コマンドを使ってください。

add [PSD_FILE]
    PSDファイルをpsdwatcherに登録する

2. psdwatcherをrunする
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ psdwatcher run

PSDファイルを登録したら、あとはpsdwatcherを **run** するだけです。

psdwatcherはPSDファイルの変更を追うためのトリガーとしてrunコマンドを使用しています。
このトリガーは後々変更するかもしれません。
    
run [, [-o [LOG_FILE]], [--dev]]
    PSDファイルのウォッチングを始める。

    :-o:    psdwatcherが出力したログをログファイルに書き出す。
    :--dev: 開発者向けログレベルに設定

Other Comamnd Usage
#####################

上記で挙げた以外のコマンドの説明です。

list
    psdwatcherが所持しているウォッチリストに登録されているPSDファイルを出力します。


