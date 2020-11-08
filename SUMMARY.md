# SUMMARY

## 第一章 音源分離とは

音源分離のプログラムの構成

- 入力：混合音
- 処理：音源分離
- 出力：きれいな音

音源の分離の目的は, マイクロホンで捉える音の中に混ざって隠れている各音源の音を分離すること.

マイクロホンの観測音は以下の式で表せる.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x_t+%3D+c_1+%2B+c_2%0A" 
alt="x_t = c_1 + c_2
">

x: 観測音(時間情報をもつ), c1: 音源1, c2: 音源2

通常, cはたくさんの音源であることが一般的で, 音源分離では一つのマイクロホンの信号から複数の音源を推定することとなる. 推定の手がかりとしてモデルを使用する.

音源分離では2つのモデルがある.

1. 空間モデル
1. 音源モデル

空間モデルでは, 音の伝播の仕方が場所ごとに異なることを利用して, 音の大小関係・時間差から音源を推定する. これを先ほどの数式を使って表現すると次のようになる.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x_t+%3D+a_%7Bm%2C1%7Ds_1+%2B+a_%7Bm%2C2%7Ds_2%0A" 
alt="x_t = a_{m,1}s_1 + a_{m,2}s_2
">

am,1やam,2は音の減衰もしくは音の遅れを表す係数で, これは音源ごとに決まる.

もし, am,1とam,2がわかっているとすると, 未知の変数は2つということになります. 観測信号が2つあれば, 次の連立方程式を解くことで未知の2変数を求めることができる

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x_1+%3D+a_%7B1%2C1%7Ds_1+%2B+a_%7B1%2C2%7Ds_2" 
alt="x_1 = a_{1,1}s_1 + a_{1,2}s_2">

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x_2+%3D+a_%7B2%2C1%7Ds_1+%2B+a_%7B2%2C2%7Ds_2%0A" 
alt="x_2 = a_{2,1}s_1 + a_{2,2}s_2
">

したがって,

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+s_1+%3D+%5Cfrac%7Bx_1a_%7B2%2C2%7D-x_2a_%7B1%2C2%7D%7D%7Ba_%7B1%2C1%7Da_%7B2%2C2%7D-a_%7B2%2C1%7Da_%7B1%2C2%7D%7D%0A" 
alt="s_1 = \frac{x_1a_{2,2}-x_2a_{1,2}}{a_{1,1}a_{2,2}-a_{2,1}a_{1,2}}
">

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+s_2+%3D+%5Cfrac%7Bx_1a_%7B2%2C1%7D-x_2a_%7B1%2C1%7D%7D%7Ba_%7B1%2C2%7Da_%7B2%2C1%7D-a_%7B1%2C1%7Da_%7B2%2C2%7D%7D%0A" 
alt="s_2 = \frac{x_1a_{2,1}-x_2a_{1,1}}{a_{1,2}a_{2,1}-a_{1,1}a_{2,2}}
">

となる.

しかし, 実際には音源の場所はわからない場合も多いと考えられる. 入力信号しか手に入らない場合はam,1やam,2が事前に分かっているという仮定は強すぎる.

ここで仮にam,1やam,2がわかっていいなくても音を分離できる技術がある. それがブラインド音源分離と呼ばれる技術だ. その際にもう一つのモデルである音源モデルを用いる.

音源モデルを使う場合は, am,1やam,2をとりあえずランダムに設定し, 何かしらのs1,s2を推定します. この推定したs1,s2が音声らしいかどうかを評価できたとする. 逆に推定されたs1, s2が音声らしくなければam,1やam,2が正しくないということになるのでもう一度試す必要があるということになる. これを繰り返していきs1, s2が音声らしいものとなればよいというわけだ.

## 第二章 音声処理の基礎

### 2.1 波形とは

- 周波数
- 振幅
- 位相

によって決まる.

### 2.2 サンプリング定理とは

`サンプリング周波数の半分より上の周波数成分については, サンプリングされた音声データから元々の連続的な波形を正しく復元することができない`

### 2.3 フーリエ変換

ここで時系列データのことを時間領域のデータといい, 周波数成分の振幅と位相のデータを周波数領域のデータという.

`フーリエ変換は時間領域のデータを周波数領域のデータに変換する`

### 2.4 短時間フーリエ変換とは

`元となる音声データを短時間の時系列データに区切り, そのデータごとにフーリエ変換を施すこと`

短時間の時系列データの一つひとつをフレームと呼び, フーリエ変換した各フレームを時間方向に並べることで, 周波数ごとの振幅の変換を捉えることができる. 通常, 数十ミリ秒単位のデータごと(フレーム)にフーリエ変換する. またフレームを時間方向に少しずつオーバーラップさせることでより時間方向の周波数ごとの変化をより連続的に問えることができる.

### 2.5 窓間数とは

短時間フーリエ変換を行うときに, 短時間の時間領域に音声波形をフレームごとに切り出すが, その際に窓間数という関数をかけて波形を切り出す. これにより周波数に変換した祭に, 他の周波数が漏れ込む影響を軽減できる.

ハニング窓

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+w%28n%29+%3D+0.5+-+0.5cos+%5Cfrac%7B2+%5Cpi+n%7D%7BN-1%7D%0A" 
alt="w(n) = 0.5 - 0.5cos \frac{2 \pi n}{N-1}
">

0 <= n <= N-1とする. Nをフレームサイズと呼び, フレーム内のサンプル数とする. nは切り出すフレームの先頭から数えたサンプル数となる.

ハミング窓

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+w%28n%29+%3D+0.54+-+0.46+cos+%5Cfrac%7B2+%5Cpi+n%7D%7BN-1%7D%0A" 
alt="w(n) = 0.54 - 0.46 cos \frac{2 \pi n}{N-1}
">

同様に0 <= n <= N-1とする.

方形窓

単にある区間を区切ったもの.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+w%28n%29+%3D+1%0A" 
alt="w(n) = 1
">

### 2.6 短時間フーリエ変換の解析

音声波形をフレームごとに切り出し, 窓間数を掛けたフレームごとの音声波形は次のようになる.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%27%28l%2Cn%29%3Dw%28n%29x%28l%2AL_shift%2Bn%29" 
alt="x'(l,n)=w(n)x(l*L_shift+n)">

- l：フレームの番号
- n：フレーム内のサンプル数(0<=n<=N-1)
- L_shift：フレームシフト（フレームサイズNの1/2や1/4に設定されることが多い)

このとき短時間フーリエ変換は以下のように実行する.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%28l%2Ck%29%3D%5CSigma%5E%7BN-1%7D_%7Bn%3D0%7Dx%27%28l%2Cn%29exp%28-j%5Cfrac%7B2%7B%5Cpi%7Dnk%7D%7BN%7D%29" 
alt="y(l,k)=\Sigma^{N-1}_{n=0}x'(l,n)exp(-j\frac{2{\pi}nk}{N})">

フレームlにおける周波数fの波形x'(l,n,f)は振幅A_l,fと位相θ_l,fを用いて次のようになる. (Fs：サンプリング周波数, t=n/Fs)

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%27%28l%2Cn%2Cf%29%3DA_%7Bl%2Cf%7Dcos%28%5Cfrac%7B2%7B%5Cpi%7Dfn%7D%7BF_s%7D%29%2B%5Ctheta_%7Bl%2Cf%7D" 
alt="x'(l,n,f)=A_{l,f}cos(\frac{2{\pi}fn}{F_s})+\theta_{l,f}">

ナイキスト周波数Fs/2以下のさまざまな周波数成分で上式を積分すると次のようになる.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%27%28l%2Cn%29%3D%5CSigma_%7Bf%3D0%7D%5E%7B%5Cfrac%7BFs%7D%7B2%7D%7DA_%7Bl%2Cf%7Dcos%28%5Cfrac%7B2%7B%5Cpi%7Dfn%7D%7BF_s%7D%29%2B%5Ctheta_%7Bl%2Cf%7D" 
alt="x'(l,n)=\Sigma_{f=0}^{\frac{Fs}{2}}A_{l,f}cos(\frac{2{\pi}fn}{F_s})+\theta_{l,f}">

オイラーの公式を逆に用いると上式は複素数を用いて次のようになる.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%27%28l%2Cn%29%3D%5CSigma_%7Bf%3D0%7D%5E%7B%5Cfrac%7BFs%7D%7B2%7D%7D%5Cfrac%7BA_%7Bl%2Cf%7Dexp%28j%28%5Cfrac%7B2%7B%5Cpi%7Dfn%7D%7BF_s%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%2BA_%7Bl%2Cf%7Dexp%28-j%28%5Cfrac%7B2%7B%5Cpi%7Dfn%7D%7BF_s%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%7D%7B2%7D" 
alt="x'(l,n)=\Sigma_{f=0}^{\frac{Fs}{2}}\frac{A_{l,f}exp(j(\frac{2{\pi}fn}{F_s})+\theta_{l,f})+A_{l,f}exp(-j(\frac{2{\pi}fn}{F_s})+\theta_{l,f})}{2}">

次に周波数fについて, 次のように0以上の整数k'で決まる離散的な変数を考える.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+f%3D%5Cfrac%7Bk%27F_%7Bs%7D%7D%7BN%7D" 
alt="f=\frac{k'F_{s}}{N}">

このときf:0->Fs/2では, k':0->N/2となり, とするとx'(l,n)は次のようになる.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x%27%28l%2Cn%29%3D%5CSigma_%7Bk%3D0%7D%5E%7B%5Cfrac%7BN%7D%7B2%7D%7D%5Cfrac%7BA_%7Bl%2Cf%7Dexp%28j%28%5Cfrac%7B2%7B%5Cpi%7Dnk%27%7D%7BN%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%2BA_%7Bl%2Cf%7Dexp%28-j%28%5Cfrac%7B2%7B%5Cpi%7Dnk%27%7D%7BN%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%7D%7B2%7D" 
alt="x'(l,n)=\Sigma_{k=0}^{\frac{N}{2}}\frac{A_{l,f}exp(j(\frac{2{\pi}nk'}{N})+\theta_{l,f})+A_{l,f}exp(-j(\frac{2{\pi}nk'}{N})+\theta_{l,f})}{2}">

上式よりさまざまな周波数成分を持つ音声信号は, それぞれの周波数の信号を加算することで表現できる. サンプリング定理と関連するが, 一つの音声波形x'(l,n)に対して, 振幅と位相は1セットのみ存在するということが知られている. 上式を短時間フーリエ変換の式に代入すると,

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%28l%2Ck%29%3D%5CSigma%5E%7BN%2F2%7D_%7Bk%27%3D0%7D%5Cfrac%7BA_%7Bl%2Cf%7D%5CSigma%5E%7BN-1%7D_%7Bn%3D0%7Dexp%28j%28%5Cfrac%7B2%7B%5Cpi%7Dn%28k%27-k%29%7D%7BN%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%2Bexp%28-j%28%5Cfrac%7B2%7B%5Cpi%7Dn%28k%27%2Bk%29%7D%7BN%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%7D%7B2%7D" 
alt="y(l,k)=\Sigma^{N/2}_{k'=0}\frac{A_{l,f}\Sigma^{N-1}_{n=0}exp(j(\frac{2{\pi}n(k'-k)}{N})+\theta_{l,f})+exp(-j(\frac{2{\pi}n(k'+k)}{N})+\theta_{l,f})}{2}">

となる. 短時間フーリエ変換のkは-N/2+1からN/2までの整数とする.

ここで, y(l,k)を計算するためには,

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5CSigma%5E%7BN-1%7D_%7Bn%3D0%7Dexp%28j%28%5Cfrac%7B2%7B%5Cpi%7Dn%28k%27-k%29%7D%7BN%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%0A" 
alt="\Sigma^{N-1}_{n=0}exp(j(\frac{2{\pi}n(k'-k)}{N})+\theta_{l,f})
">

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5CSigma%5E%7BN-1%7D_%7Bn%3D0%7Dexp%28-j%28%5Cfrac%7B2%7B%5Cpi%7Dn%28k%27%2Bk%29%7D%7BN%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%0A" 
alt="\Sigma^{N-1}_{n=0}exp(-j(\frac{2{\pi}n(k'+k)}{N})+\theta_{l,f})
">

この二項をどう計算するかが鍵となる. この計算を行うためには, 以下の性質を利用する. ここでbは-NからNまでの整数とする.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5CSigma%5E%7BN-1%7D_%7Bn%3D0%7Dexp%28-j%28%5Cfrac%7B2%7B%5Cpi%7Dnb%7D%7BN%7D%29%2B%5Ctheta_%7Bl%2Cf%7D%29%3DNexp%28j%5Ctheta_%7Bl%2Ck%27%7D%29%2C%7B%5Crm%7Bif%7D%7Db+%5Cin+%7B0%2CN%2C-N%7D%0A" 
alt="\Sigma^{N-1}_{n=0}exp(-j(\frac{2{\pi}nb}{N})+\theta_{l,f})=Nexp(j\theta_{l,k'}),{\rm{if}}b \in {0,N,-N}
">

bが0,-N,Nのときはexpの位相成分のみが残り, それ以外の時は実部・虚部ともに一周期の整数倍になるため0になる.

次の4つのパターンでy(l,k)を考える.

1 k:1 -> N/2-1のとき

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+1+%5Cleqq+k%27+%2B+k+%5Cleqq+N-1" 
alt="1 \leqq k' + k \leqq N-1">

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+-%5Cfrac%7BN%7D%7B2%7D+%5Cleqq+k%27+-+k+%5Cleqq+%5Cfrac%7BN%7D%7B2%7D" 
alt="-\frac{N}{2} \leqq k' - k \leqq \frac{N}{2}">

となり, bが0,-N,Nのときだけ0以外になることを利用し, 次のようになる.(反時計回りの成分が残る)

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%28l%2Ck%29%3D%5Cfrac%7BNA_%7Bl%2Ck%27%7D%7D%7B2%7Dexp%28j%5Ctheta_%7Bl%2Ck%27%7D%29" 
alt="y(l,k)=\frac{NA_{l,k'}}{2}exp(j\theta_{l,k'})">

2 k:-N/2+1 -> -1のとき

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+-%5Cfrac%7BN%7D%7B2%7D+%5Cleqq+k%27+%2B+k+%5Cleqq+%5Cfrac%7BN%7D%7B2%7D" 
alt="-\frac{N}{2} \leqq k' + k \leqq \frac{N}{2}">

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+1+%5Cleqq+k%27+-+k+%5Cleqq+N-1" 
alt="1 \leqq k' - k \leqq N-1">

同様に, bが0,-N,Nのときだけ0以外になることを利用し, 次のようになる.(時計回りの成分が残る)

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%28l%2Ck%29%3D%5Cfrac%7BNA_%7Bl%2Ck%27%7D%7D%7B2%7Dexp%28-j%5Ctheta_%7Bl%2Ck%27%7D%29" 
alt="y(l,k)=\frac{NA_{l,k'}}{2}exp(-j\theta_{l,k'})">

3 k=0のとき

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%28l%2Ck%29%3D2NA_%7Bl%2Ck%27%7Dcos%28%5Ctheta_%7Bl%2Ck%27%7D%29" 
alt="y(l,k)=2NA_{l,k'}cos(\theta_{l,k'})">

このときは, オイラーの公式からcosの実数に戻すことが可能となる.(位相という概念が意味を持たない成分ということになる.) k=0のときの周波数成分をオフセット成分といったりする. 実用上はこのオフセット成分の振幅を考えることはあまり意味がない. 処理の過程で0と置いてしまっても問題ないことが多い.

4 k=N/2のとき

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cfrac%7BN%7D%7B2%7D+%5Cleqq+k%27+%2B+k+%5Cleqq+N" 
alt="\frac{N}{2} \leqq k' + k \leqq N">

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+-%5Cfrac%7BN%7D%7B2%7D+%5Cleqq+k%27+-+k+%5Cleqq+0" 
alt="-\frac{N}{2} \leqq k' - k \leqq 0">

k=0のときと同様に実数の成分だけが残る.(位相という概念が意味を持たない成分ということになる.)

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+y%28l%2Ck%29%3D2NA_%7Bl%2Ck%27%7Dcos%28%5Ctheta_%7Bl%2Ck%27%7D%29" 
alt="y(l,k)=2NA_{l,k'}cos(\theta_{l,k'})">

いずれのケースも, 短時間フーリエ変換を行うことで得られる複素数y(l,k)からkに相当する周波数の振幅A_l,kと位相θ_l,kを容易に知ることができることを意味している. また負の周波数成分は, 生の周波数成分の複素共役にになっていることがわかる. そのため, 負の周波数成分のフーリエ変換の情報は冗長だということになり, 信号処理の各種モジュールでは, 負の周波数成分を除いた, kが0からN/2までのN/2+1個(ビン)のフーリエ変換の結果を出力することが一般的だ.

### 2.7 音声の可視化

各時間周波数の音声をx_lkとして書き直す.

<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+x_%7Blk%7D%3D%7Cx_%7Blk%7D%7Cexp%28j%7B%5Cphi%7D%28x_%7Blk%7D%29%29" 
alt="x_{lk}=|x_{lk}|exp(j{\phi}(x_{lk}))">

- |x_lk|：振幅
- |φ_lk|：位相

音声の特徴は, 位相よりも主に振幅に現れる.
