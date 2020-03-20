## upload相关接口   
* [x] <a href='#avatar'>avatar</a>   
* [ ] loginByOpenid   
* [ ] logout   
* [ ] get   

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