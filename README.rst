.. image:: https://raw.github.com/alice1017/psdwatcher/master/logo.jpg

What is psdwatcher?
#####################

-----

|build| |coverage| |license|

-----

**psdwatcher** はPhotoshopで扱う **PSDファイル** の変更を **git** を使ってステージングやコミットを行い、 *いつでも前のバージョン見れるようにする* Pythonスクリプトです。

Install
########

::
    
    $ git clone git://github.com/alice1017/psdwatcher.git
    $ cd psdwatcher
    $ python setup.py build install


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

runコマンドを起動したら、さっそくphotoshopを開いてpsdwatcherに登録したpsdファイルを編集してください。
psdwatcherがその編集を監視し、gitへステージング・コミットします。

psdwatcherはPSDファイルの変更を追うためのトリガーとしてrunコマンドを使用しています。
このトリガーは後々変更するかもしれません。
    
run [, [-o [LOG_FILE]], [--not-output-log], [--dev]]
    PSDファイルのウォッチングを始める。

    :-o:                psdwatcherが出力したログをログファイルに書き出す。
    :--dev:             開発者向けログレベルに設定

    :--not-output-log:  ログを出力しない

Other Comamnd Usage
#####################

上記で挙げた以外のコマンドの説明です。

list
    psdwatcherが所持しているウォッチリストに登録されているPSDファイルを出力します。


.. include:: changelog.rst

TODO
#############

Add **--background** option at run command
    **python-daemon** モジュールを使ってrunコマンドの動きをbackgroundで行うオプションを作る



.. |build| image:: https://img.shields.io/travis/alice1017/psdwatcher/v2.svg?style=flat-square
    :target: https://travis-ci.org/alice1017/psdwatcher
    :alt: Travis-CI

.. |coverage| image:: https://img.shields.io/coveralls/alice1017/psdwatcher/v2.svg?style=flat-square&label=coverage
    :target: https://coveralls.io/r/alice1017/psdwatcher?branch=v2
    :alt: Test coverage

.. |license| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
    :target: https://raw.githubusercontent.com/alice1017/psdwatcher/master/LICENSE
    :alt: License
　　
