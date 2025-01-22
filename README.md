# Use private VOD server for review.

## Note: 
1. Safari doesn't work properly. Please use Chrome or Firefox
2. https is required.

## Generate certification for your domain

### HA-Proxy
This is an example to create certification for the test domain "f.ll.tt". Please change it to your domain. And you could use your faviorate tool to configure reversed proxy.

![Create Certificaton for HA-Proxy](https://github.com/loney-liu/docker-vod-server/blob/master/proxy/certs/SelfSignedCACert.txt)

### CopyParty
In this version, the file server is changed to copyparty. 
1. https://your_domain_name will show all files uploaded.
2. Put combined certification into `config/copyparty/cert.pem` *Please don't change `cert.pem`
3. Private key is always on the top of the combined certification.

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

## Configure AMI

#### Setup script user in Shotgun

![Script User](https://github.com/loney-liu/docker-vod-server/blob/master/demo/ScriptUser.jpg)

#### Add script user and key to docker-vod-server/www/configure.xml

```
script_name: your_script_name
script_key: your_application_key
```

## Configure Custom URL

#### Add a URL page to task

![Design PAge](https://github.com/loney-liu/docker-vod-server/blob/master/demo/DesignPage.jpg)
![Custom URL](https://github.com/loney-liu/docker-vod-server/blob/master/demo/CustomURL.jpg)

```

Please replace `your_vod_server_ip` and `your_shotgun_site_url` and keep other parameters.
English: language=en
Chinese: language=cn
```
#### Asset
`https://your_vod_server/task_url?language=cn&sg_url=autodesk-china-training.shotgunstudio.com&user_login={current_user.login}&project_id={project.Project.id}&project_name={project.Project.name}&task_name={content}&task_id={id}&link_id={entity.Asset.id}&link_name={entity.Asset.code}`

#### Shot
`URL: https://your_vod_server/task_url?language=cn&sg_url=autodesk-china-training.shotgunstudio.com&user_login={current_user.login}&project_id={project.Project.id}&project_name={project.Project.name}&task_name={content}&task_id={id}&content={content}&link_id={entity.Shot.id}&link_name={entity.Shot.code}`


#### CustomEntity<Number>
`URL: https://your_vod_server/task_url?language=cn&sg_url=autodesk-china-training.shotgunstudio.com&user_login={current_user.login}&project_id={project.Project.id}&project_name={project.Project.name}&task_name={content}&task_id={id}&content={content}&link_id={entity.Shot.id}&link_name={entity.<CustomEntityNumberß>.code}`


![Add Page](https://github.com/loney-liu/docker-vod-server/blob/master/demo/AddPage.jpg)

## Test 

#### Web Server

https://your_vod_server:5000/en

![Sever Up](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Server_is_up.jpg)


#### VOD Server

Edit docker-vod-server/index.html. Change `localhost` to `your_vod_server_ip`.

```
<source src="https://your_vod_ser_ip/test.mp4" type="video/mp4" />
```

#### https://your_vod_server:9999

![AMI](https://github.com/loney-liu/docker-vod-server/blob/master/demo/Live_Streaming.jpg)

## Create Action Menu Item

```
Title: VOD Server (Or whatever you like)
Entity Type: Asset/Shot/Task
URL: https://your_vod_server_ip:5000/en or http://your_vod_server_ip:5000/cn 
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

English: https://your_vod_server_ip:5000/en

中文: https://your_vod_server_ip:5000/cn

## Attention

#### If you want to use private VOD server, you are responsible for data security!
