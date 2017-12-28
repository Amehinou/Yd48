# Yd48
## 批量下载SNH48G 公演

## Install

sudo apt-get install libxml2-dev libxslt-dev python-dev<br>
pip3 install bs4 you-get lxml<br>
git clone https://github.com/Amehinou/Yd48 </br>
cd Yd48 </br>
python3 Yd48.py -t 联合公演 -p 1
```console
air:Yd48 sakura$ python3 Yd48.py -t 特殊公演 -p 1

    
        欢迎使用SNH48G公演批量下载程序 Yd48 ！
                      
    
正在更新数据........
即将为您下载以下公演:
===============================================================
GNZ48 圣诞节慈善夜暨特殊公演 - 826演唱会不忘初心之经典重现（20171224 夜场）
BEJ48 TeamJ《因为喜欢你》第二十场暨怦然心动特殊公演（20171223 夜场）
BEJ48 TeamB&TeamE&TeamJ《月光宝盒》三队联合中秋特殊公演（20171004 夜场）
SHY48 TeamSⅢ《天才少女日记》第二十四场暨中秋特殊公演（20171004 午场）
BEJ48 《乱点鸳鸯谱》三队联合七夕情人节特殊公演（20170827 午场）
SNH48 拉票特殊公演暨第四届总决选中报（20170709 夜场）
SHY48 TeamHⅢ《梦想的旗帜》第二十六场暨穿越时空的爱男装特殊公演（20170521 夜场）
SHY48 TeamHⅢ《梦想的旗帜》第二十五场暨穿越时空的爱男装特殊公演（20170520 午场）
SHY48 《豫珑决》联合特殊公演（下）（20170430 夜场）
SHY48 《豫珑决》联合特殊公演（上）（20170429 夜场）
SHY48 TeamSⅢ《心的旅程》第二十六场暨出道百日纪念特殊公演（20170421 夜场）
BEJ48 TeamE&TeamJ“丝芭偶像节”特殊公演（20170408 午场）
BEJ48 TeamE《奇幻加冕礼》第二十场暨愚人节特殊公演（20170401 夜场）
BEJ48 TeamJ《我们的派对》男装特殊公演（20170326 午场）
SHY48 TeamHⅢ《梦想的旗帜》第八场暨校园季特殊公演（20170319 午场）
SHY48 TeamHⅢ《梦想的旗帜》第七场暨校园季特殊公演（20170318 午场）
BEJ48 TeamJ《白色情人节特殊公演》（20170312 夜场）
SHY48 TeamSⅢ《心的旅程》第七场暨因为喜欢你情人节特殊公演（20170212 午场）
GNZ48 TeamNⅢ&TeamZ《闹元宵》联合特殊公演（20170211 夜场）
SHY48 TeamSⅢ《心的旅程》第六场暨因为喜欢你情人节特殊公演（20170211 夜场）
GNZ48 TeamZ《2017·爱你·一起》跨年特殊公演（20161231 夜场）
===============================================================
确认下载以上公演? (yes/no):
```


## Usage

优酷页面 <a href="http://i.youku.com/i/UMTM4NTM5Nzc4OA==/">snh48club</a>

python3 Yd48.py -t [Team Name] -p [youku playlist Pages number]  </br>

#### -t 搜索关键字

#### -p 下载页数
<img src="https://cdn.earture.org/src/p.png">

eg. </br>
### 下载BEJ48 TeamE 优酷视频列表第1页的所有公演 </br>

```console
python3 Yd48.py -t TeamE -p 1  
```

### 下载 20171217 的所有公演 </br>

```console
python3 Yd48.py -t 20171217 -p 1  
```

### 下载SHY48 优酷视频列表第2页的所有公演 </br>

```console
python3 Yd48.py -t SHY48 -p 2 
```
