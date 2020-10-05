## Use private VOD server for review.

### Install

#### Clone git repo

# git clone https://github.com/loney-liu/docker-vod-server
# git submodule update

#### Build docker image

# cd docker-vod-server
# docker-compose build
# docker-compose up -d

#### Test VOD Server

http://localhost:9999

#### Create Action Menu Item

#### Data directory

docker-vod-server/www/data/hls

#### Change default language

Edit docker-vod-server/www/i18n.yml