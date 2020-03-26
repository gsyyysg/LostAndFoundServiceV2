## user相关接口   
* [x] <a href='#categories'>categories</a>   
* [x] <a href='#create'>create</a>   
* [x] <a href='#list'>list</a>   
* [x] <a href='#delete'>delete</a>   
* [x] <a href='#update'>update</a>   
* [x] <a href='#apply'>apply</a>   
* [x] <a href='#confirm'>confirm</a>    
* [x] <a href='#reject'>reject</a>    

## 接口文档   
domain=‘http(s)://lostandfoundv2.yiwangchunyu.wang’   
 
请注意！：用户在服务端的唯一标识为user_id，不是opendi or stu_id   

### <a name='categories'>categories</a> 获取类别列表   
url = {domain}/service/dynamic/categories   
method = post   
params:   

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": [
        {
            "id": 1,
            "status": 1,
            "ctime": "2020-03-26 11:34:04",
            "mtime": "2020-03-26 11:34:15",
            "name": "校园卡"
        },
        {
            "id": 2,
            "status": 1,
            "ctime": "2020-03-26 11:34:29",
            "mtime": "2020-03-26 11:34:35",
            "name": "雨伞"
        },
        {
            "id": 3,
            "status": 1,
            "ctime": "2020-03-26 15:18:00",
            "mtime": "2020-03-26 15:18:27",
            "name": "其他"
        }
    ]
}
```

### <a name='create'>create</a> 创建动态   
url = {domain}/service/dynamic/create   
method = post   
params:   


|   名称  | 类型 | 必须 | 备注 |
| :-----| ----: | :----: | :----: |
|user_id | int | Y |  |
|type | int | Y |  |
|category | int | Y |  |
|title | string | Y |  物品名称（保留字段，可传''）|
|desc | string | Y |  物品描述|
|images | json_string | N | 建议先调用接口上传图片(upload/dynamicImg)，成功填此接口；或者先创建，再上传图片，再更新此字段（不建议） |
|location | json_string | N | 地理位置信息 |
|meta | string | N | 捡到校园卡，传校园卡卡号 |

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": []
}
```

### <a name='list'>list</a> 查询动态列表   
url = {domain}/service/dynamic/list   
method = post   
params:   


|   名称  | 类型 | 必须 | 备注 |
| :-----| ----: | :----: | :----: |
|id | int | n |  |
|user_id | int | n |  |
|type | int | n |  |
|category | int | n |  |
|title | string | n |  物品名称（保留字段，可传''）|
|desc | string | n |  物品描述|
|meta | string | n | 捡到校园卡，传校园卡卡号 |
|state | int | n | 1:待申领，2：待确认，3：申领成功 |
|belongsTo | int | n | 申领人 |
|page | int | n | 0 |
|size | int | n | 10 |

我发布的：传user_id
我申领的：传belongsTo

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "cnt": 2,
        "dynamics": [
            {
                "id": 1,
                "status": 1,
                "ctime": "2020-03-26 14:55:20",
                "mtime": "2020-03-26 14:55:28",
                "user_id": 1,
                "type": 1,
                "category": 1,
                "title": "",
                "desc": "丢失",
                "images": [],
                "location": {},
                "meta": null,
                "belongsTo": 1,
                "state": "待申领",
                "user_info": {
                    "id": 1,
                    "status": 1,
                    "ctime": "2020-03-20 08:53:49",
                    "mtime": "2020-03-20 10:49:53",
                    "stu_id": "10152150127",
                    "nick_name": "yiwangchunyu",
                    "name": "汪春雨",
                    "avatar": "http://127.0.0.1:8000/media/avatar/1_20200320184953.jpg",
                    "gender": 1,
                    "phone": "18918053907",
                    "role": 2
                }
            },
            {
                "id": 2,
                "status": 1,
                "ctime": "2020-03-26 16:53:28",
                "mtime": "2020-03-26 16:53:28",
                "user_id": 1,
                "type": 1,
                "category": 1,
                "title": "",
                "desc": "",
                "images": [],
                "location": {},
                "meta": "",
                "belongsTo": 1,
                "state": "待申领",
                "user_info": {
                    "id": 1,
                    "status": 1,
                    "ctime": "2020-03-20 08:53:49",
                    "mtime": "2020-03-20 10:49:53",
                    "stu_id": "10152150127",
                    "nick_name": "yiwangchunyu",
                    "name": "汪春雨",
                    "avatar": "http://127.0.0.1:8000/media/avatar/1_20200320184953.jpg",
                    "gender": 1,
                    "phone": "18918053907",
                    "role": 2
                }
            }
        ]
    }
}
```


### <a name='delete'>delete</a> 删除动态   
url = {domain}/service/dynamic/delete   
method = post   
params:   


|   名称  | 类型 | 必须 | 备注 |
| :-----| ----: | :----: | :----: |
|id | int | Y | 动态id|
|user_id | int | Y |  |

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": []
}
```


### <a name='apply'>update</a> 更新动态   
url = {domain}/service/dynamic/apply   
method = post   
params:   


|   名称  | 类型 | 必须 | 备注 |
| :-----| ----: | :----: | :----: |
|id | int | Y |  |
|user_id | int | N |  |
|type | int | N |  |
|category | int | N |  |
|title | string | N |  物品名称（保留字段，可传''）|
|desc | string | N |  物品描述|
|images | json_string | N | 建议先调用接口上传图片(upload/dynamicImg)，成功填此接口；或者先创建，再上传图片，再更新此字段（不建议） |
|location | json_string | N | 地理位置信息 |
|meta | string | N | 捡到校园卡，传校园卡卡号 |

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": []
}
```

### <a name='apply'>apply</a> 申领   
url = {domain}/service/dynamic/apply   
method = post   
params:   


|   名称  | 类型 | 必须 | 备注 |
| :-----| ----: | :----: | :----: |
|id | int | Y |  |
|user_id | int | Y |  |

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "user_info": {
            "id": 1,
            "status": 1,
            "ctime": "2020-03-20 08:53:49",
            "mtime": "2020-03-20 10:49:53",
            "stu_id": "10152150127",
            "nick_name": "yiwangchunyu",
            "name": "汪春雨",
            "avatar": "http://127.0.0.1:8000/media/avatar/1_20200320184953.jpg",
            "gender": 1,
            "phone": "18918053907",
            "role": 2
        }
    }
}
```

### <a name='confirm'>confirm</a> 确认   
url = {domain}/service/dynamic/confirm   
method = post   
params:   


|   名称  | 类型 | 必须 | 备注 |
| :-----| ----: | :----: | :----: |
|id | int | Y |  |
|user_id | int | Y |  |

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": {
    }
}
```

### <a name='reject'>reject</a> 拒绝   
url = {domain}/service/dynamic/reject   
method = post   
params:   


|   名称  | 类型 | 必须 | 备注 |
| :-----| ----: | :----: | :----: |
|id | int | Y |  |
|user_id | int | Y |  |

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": {
    }
}
```