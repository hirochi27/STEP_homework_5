# TSPの実装（貪欲法＆2-opt）
## ファイルについて

自身で実装したコード
* google-steo-tsp/solver.py　:　貪欲法＆2-opt

その他、```https://github.com/hayatoito/google-step-tsp```よりcloneしたコード
* google-step-tsp/input_{0~6}.csv : 都市の座標、solver.pyに渡す値
* google-step-tsp/output_{0~6}.csv　: inputを受け取ったsolver.pyの実行結果


## 実行方法
実行結果をoutput_{0~6}.csvに保存
```
python3 solver.py input_0.csv > output_0.csv
```

ビジュアライザーの起動
```
python3 -m http.server 8000
```

URL
```
http://localhost:8000/visualizer/build/default/
```

## 現状

