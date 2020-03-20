##user相关接口   
* [x] <a href='#login'>login</a>   
* [ ] loginByOpenid   
* [ ] logout   
* [ ] get   

##接口文档   
domain=‘http(s)://lostandfoundv2.yiwangchunyu.wang’
###<a name='login'>login</a> 用户登录（无状态登录）
url = {domain}/service/user/login   
method = post   
params:   


|   名称  | 类型 | 必须 | 备注 |   
| :-----| ----: | :----: | :----: |
|openid | string | Y | 可通过getOpenid获取，获取后清缓存到前端当做tocken |   
|stu_id | string| Y | 学工号 |   
|password | string| Y | 学工号密码 |   
|gender | int| Y | 有1说1，没1说0 |   
|phone | string| Y | 手机号，前端请在验证码验证后调此接口 |   
|avatar | string| Y | 头像url（微信头像） |   