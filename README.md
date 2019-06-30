**HaloSet**
---
[![996.icu](https://img.shields.io/badge/link-996.icu-red.svg)](https://996.icu)
>前言:我之所以开发这个部署脚本，一方面是为了我自己使用方便，二方面是为了方便小白用户。
[Halo](https://github.com/halo-dev/halo)是一个很优秀的博客平台，
但是官方提供的启动方式实在是太菜了【-_-】而且重启后无法自动启动...

>然后呢？

>然后我就做了这个

说明：使用本脚本请自觉支持[996.icu](https://996.icu)
###使用说明
使用脚本前请确认您的计算机(服务器)是:
1. 支持apt-get包安装
2. 支持Java运行环境
3. 支持Python3

###总计安装：
`sudo apt install openjdk-8* openjfx python3`
>建议使用tuna的apt源

###启用脚本：
`git clone https://github.com/zzh-blog/HaloSet.git`

`sudo chmod 777 -R HaloSet`

`cd HaloSet`

`python3 Halo.py`
