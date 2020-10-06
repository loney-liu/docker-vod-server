# Use private VOD server for review.

## Install

#### Clone git repo

```
$git clone https://github.com/loney-liu/docker-vod-server
```

#### Required submodule [python-api](https://github.com/shotgunsoftware/python-api)

```
$cd docker-vod-server/build/web/python-api
$git submodule init
$git submodule update
```

#### Build docker image

```
$cd docker-vod-server
$sudo docker-compose build
```

#### Start docker image

```
$cd docker-vod-server
$sudo docker-compose up -d
```

#### Stop docker image

```
$cd docker-vod-server
$sudo docker-compose down
```

## Test Web Server

#### http://your_vod_server:5000/en

![Sever Up](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Server_is_up.jpg)


## Test VOD Server

#### Edit docker-vod-server/index.html. Change `localhost` to `your_vod_server_ip`.

```
<source src="http://your_vod_ser_ip:8080/test.mp4" type="video/mp4" />
```

#### http://your_vod_server:9999

![AMI](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Live_Streaming.jpg)

## Create Action Menu Item

```
Title: VOD Server
Entity Type: Asset/Shot/Task
URL: http://your_vod_server_ip:5000/en or http://your_vod_server_ip:5000/cn 
Selection Required: Selected
```

![AMI](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Action_Menu_Items.jpg)

## How to use in Asset

#### It only creates version for Asset/Shot/Task. Other entities are not tested.

*Notice:* If you don't want to use DIY transcoding, please upload mp4 media type only.

![Asset](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Asset.jpg)

![upload](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Uploader.jpg)

## Tested on

#### Screening Room, RV, Create

## Data directory

docker-vod-server/www/data/hls

## Change default language

#### Edit AMI URL

English: http://your_vod_server_ip:5000/en

中文: http://your_vod_server_ip:5000/cn

## Attention

#### If you want to use private VOD server, you are responsible for data security!