## upload相关接口   
* [x] <a href='#avatar'>avatar</a>   
* [x] <a href='#dynamicImg'>dynamicImg</a>  


## 接口文档   
domain=‘http(s)://lostandfoundv2.yiwangchunyu.wang’
### <a name='avatar'>avatar</a> 上传用户头像   
url = {domain}/service/upload/avatar      
method = post   
params:   

|   名称  | 类型 | 必须 | 备注 |   
| :-----| ----: | :----: | :----: |
|user_id | int| Y | 用户id，用户唯一标识 |     
|avatar | string| Y | 头像url（微信头像） |   

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "avatar": "https:/lostandfoundv2//media/avatar/test.jpg"
    }
}
```

### <a name='dynamicImg'>dynamicImg</a> 上传用户头像   
url = {domain}/service/upload/dynamicImg      
method = post   
params:   

|   名称  | 类型 | 必须 | 备注 |   
| :-----| ----: | :----: | :----: |
|images | file| Y | 可传多个 |     

return:
```json
{
    "code": 0,
    "msg": "success",
    "data": "[\"http://{domain}/media//dynamic/2020/3/27/011216_59730.jpg\", \"http://{domain}/media//dynamic/2020/3/27/011216_89864.jpg\"]"
}
```