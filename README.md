# Use private VOD server for review.

## Install

### Clone git repo

$git clone https://github.com/loney-liu/docker-vod-server

#### Required submodule python-api

$cd docker-vod-server/build/web/python-api

$git submodule init

$git submodule update

### Build docker image

$cd docker-vod-server

$sudo docker-compose build

### start docker image

$cd docker-vod-server

$sudo docker-compose up -d

### stop docker image

$cd docker-vod-server

$sudo docker-compose down

## Test VOD Server

http://localhost:9999

![AMI](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Live_Streaming.jpg)

## Create Action Menu Item

![AMI](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Action_Menu_Items.jpg)

## How to use in Asset

It only creates version for Asset/Shot/Task. Other entities are not tested.

*Notice:* If you don't want to use DIY transcoding, please upload mp4 media type only.

![Asset](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Asset.jpg)

![upload](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Uploader.jpg)

## Tested on

Screening Room, RV, Create

## Data directory

docker-vod-server/www/data/hls

## Change default language

Edit docker-vod-server/www/i18n.yml

en: English

cn: 中文

## Attention

If you want to use private VOD server, you are responsible for data security!