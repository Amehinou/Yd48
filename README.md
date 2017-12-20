# Yd48
## 批量下载SNH48G 公演

## Install
pip3 install bs4 you-get lxml<br>
git clone https://github.com/Amehinou/Yd48 </br>
cd Yd48 </br>
python3 Yd48.py

## Usage

优酷页面 <a href="http://i.youku.com/i/UMTM4NTM5Nzc4OA==/">snh48club</a>

python3 Yd48.py -t [Team Name] -p [youku playlist Pages number]  </br>

#### -t 搜索关键字
<img src="https://cdn.earture.org/src/t.png">

#### -p 下载页数
<img src="https://cdn.earture.org/src/p.png">

eg. </br>
### 下载BEJ48 TeamE 优酷视频列表第1页的所有公演 </br>

python3 Yd48.py -t TeamE -p 1  </br>

### 下载 20171217 的所有公演 </br>

python3 Yd48.py -t 20171217 -p 1  </br>

### 下载SHY48 优酷视频列表第2页的所有公演 </br>

python3 Yd48.py -t SHY48 -p 2 
