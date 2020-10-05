## Use private VOD server for review.

### Install

#### Clone git repo

#git clone https://github.com/loney-liu/docker-vod-server

#git submodule update

#### Build docker image

#cd docker-vod-server

#docker-compose build

#docker-compose up -d

#### Test VOD Server

http://localhost:9999

#### Create Action Menu Item

![AMI](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Action_Menu_Items.jpg)

#### How to use in Asset

![Asset](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Asset.jpg)

![upload](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Uploader.jpg)

#### Data directory

docker-vod-server/www/data/hls

#### Change default language

Edit docker-vod-server/www/i18n.yml