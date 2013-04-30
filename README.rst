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
    
run [, [--dev]]
    PSDファイルのウォッチングを始める。
    *--dev* オプションをつけると詳細なログを出力します。

