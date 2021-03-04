# WiktionaryからIPAの情報を取得

## 機能
文を入力すると，それぞれの語に対応するIPAを英語版Wiktionaryから取得し，これを連ねて出力します．Wiktionaryに立項されていない場合は，当該位置に404を返します．それが活用形であって，原形のページに発音が示されていたとしても，それには対応していません．目下フランス語のみに対応します．  
入力には句読点を含めず，文頭は固有名詞でない限りは小文字にしてください．

## 要件
Python 3.0, the library Requests (introduce via `pip install requests`)