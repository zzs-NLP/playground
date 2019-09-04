#coding=utf-8
import requests
from sign_up import sign
import urllib
import json
from resquest_http import http_get,http_post,http_delete,http_put,ws_sample
from img_base64 import img_base
from PIL import Image
import datetime
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


#创建人脸库
def create_facesets(name,description,extra):
    func_api="/openapi/v1/facesets"
    res=http_post(func_api, 'POST',{"name": name,"description":description,"extra": extra})
    res = json.loads(res)
    logger.debug(res)
    print(res['data'])


#查询人脸库列表
def faceset_list():
    func_api="/openapi/v1/facesets"
    res=http_get(func_api, 'GET')
    #"faceset_id":"5d5ce77a9c81530008b17ce2","name":"face_ciger"
    res = json.loads(res)
    print(res['data'])


#删除人脸库
def del_facesets(faceset_id):
    func_api="/openapi/v1/facesets/"+faceset_id
    res=http_delete(func_api, 'DELETE')
    res = json.loads(res)
    logger.debug(res)
    print(res)
    print(res['data'])


#更新人脸库
def update_facesets(faceset_id,name,description,extra):
    func_api="/openapi/v1/facesets/"+faceset_id
    res=http_put(func_api, 'PUT',{"name": name,"description":description,"extra":extra})
    res = json.loads(res)
    logger.debug(res)
    print(res['data'])

#查询人脸库
def info_faceset(faceset_id):
    func_api="/openapi/v1/facesets/"+faceset_id
    res=http_get(func_api, 'GET')
    res = json.loads(res)
    logger.debug(res)
    print(res['data'])


#注册用户
def registered_user(faceset_id,image_type,img_path,age,gender):
    func_api="/openapi/v1/facesets/"+faceset_id+"/faces"
    base64_img=img_base(img_path)
    body={"images": [{
        "image_type": image_type,
        "image_base64": base64_img,
    },],
    "attributes": {
        "age": age,
        "gender": gender
    }}
    res=http_post(func_api, 'POST',body)
    res = json.loads(res)
    logger.debug(res)
    data=res['data']
    print(res)
    return data


#获取人脸库的用户列表
def user_list(faceset_id):
    func_api="/openapi/v1/facesets/"+faceset_id+"/faces"
    res=http_get(func_api, 'GET')
    res = json.loads(res)
    print(res['data'])


#删除人脸库的用户
def del_user(faceset_id,face_id):
    func_api="/openapi/v1/facesets/"+faceset_id+"/faces/"+face_id
    res=http_delete(func_api, 'DELETE')
    res = json.loads(res)
    logger.debug(res)
    print(res['data'])


#更新人脸库的用户信息
def update_user(faceset_id,face_id):
    func_api="/openapi/v1/facesets/"+faceset_id+"/faces/"+face_id
    body = {
            "images": [{
                "image_type": 0,
                "image_url": "https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=6e23ed544a166d222c7a1dc6274a6292/48540923dd54564ea9808ea6bade9c82d0584f43.jpg"
            }],
            "attributes": {
                "age":20,
                "gender": "male"
            }
        }
    res=http_put(func_api, 'PUT',body)
    res = json.loads(res)
    logger.debug(res)
    print(res['data'])


#获取人脸库的用户信息
def user_info(faceset_id,face_id):
    func_api="/openapi/v1/facesets/"+faceset_id+"/faces/"+face_id
    res=http_get(func_api, 'GET')
    res = json.loads(res)
    print(res['data'])
    return (res['data'])


#人脸更新:向人脸库中指定用户添加人脸特征图片
def user_append_img(faceset_id,face_id,image_type,img_path,age,gender):
    func_api="/openapi/v1/facesets/"+faceset_id+"/faces/"+face_id+"/images_add"
    img_base64=img_base(img_path)
    body = {
        "images": [{
            "image_type": image_type,
            "image_base64": img_base64
        }],
        "attributes": {
            "age": age,
            "gender": gender
        }
    }
    res=http_post(func_api, 'POST',body)
    res = json.loads(res)
    logger.debug(res)
    print(res)
    print(res['data'])


#人脸检测
def detect_face(image_type,img_path):
    func_api="/openapi/v1/faces/detect"
    base64_img=img_base(img_path)
    body = {
        "image_type": image_type,
        "image_base64": base64_img,
        "keypoint": True,
        "quality": True,
        "attributes": "age,gender",
        "max_face_count": 10
    }
    res=http_post(func_api, 'POST',body)
    res = json.loads(res)
    logger.debug(res)
    data=res['data']
    print(data)
    return data

    # img1 = Image.open(img_path)
    #
    # cropped1 = img1.crop((303,361,552,669))
    # cropped2= img1.crop((509,303,544,351))
    #
    # cropped1.save("/home/hensel/Desktop/11_cut.jpg")
    # cropped2.save("/home/hensel/Desktop/22_cut.jpg")

#人脸抠图
def extract_face(image_type,img_path):
    func_api="/openapi/v1/faces/face_extract"
    base64_img=img_base(img_path)
    body ={
    "image_type":image_type,
    "image_base64":base64_img,
    "max_face_count":1
    }
    res=http_post(func_api, 'POST',body)
    res = json.loads(res)
    logger.debug(res)
    print(res['data'])



#人脸比对 1：1
def match_face(path_img1,path_img2):
    func_api="/openapi/v1/faces/match"
    base64_img_1=img_base(path_img1)
    base64_img_2=img_base(path_img2)

    body ={
    "image_type":1,
    "image_base64_1":base64_img_1,
    "face_rect_1":"107,45,183,136",
    "image_base64_2":base64_img_2,
    "face_rect_2":"145,81,312,289"
    }
    res=http_post(func_api, 'POST',body)
    res = json.loads(res)
    logger.debug(res)
    print(res['data'])


    # img1 = Image.open("/home/hensel/Desktop/1.jpeg")
    # img2 = Image.open("/home/hensel/Desktop/2.jpeg")
    #
    # cropped1 = img1.crop((72,18,215,161))
    # cropped2= img2.crop((62,20,393,351))

    # cropped1.save("/home/hensel/Desktop/11_cut.jpg")
    # cropped2.save("/home/hensel/Desktop/22_cut.jpg")


#人脸比对 1：n 可以多个人脸库比对
def search_face(img_path,faceset_ids):
    func_api="/openapi/v1/faces/search"
    base64_img_1=img_base(img_path)

    body ={
    "image_base64":base64_img_1,
    "image_type":1,
    "faceset_ids":faceset_ids}
    res=http_post(func_api, 'POST',body)
    res = json.loads(res)
    # print(res)
    # print(res['data'])
    return res['data']





#创建人脸库 会员 白名单 黑名单
def user_face(space_id):
    func_api="/openapi/v1/analysis_tools/enable"

    body ={
    "space_id":space_id,
    }
    res=http_post(func_api, 'POST',body)
    res = json.loads(res)
    print(res)
    print(res['data'])


#关联人脸库到设备空间
def faceset_space(space_ids,faceset_ids):
    func_api="/openapi/v1/analysis_tools/attach_space"
    body ={
        "space_ids":space_ids,
        "faceset_ids":faceset_ids,
}
    res=http_post(func_api, 'POST',body)
    res = json.loads(res)
    print(res)
    print(res['data'])


#总客流量查询
def count_person(device_sn,start_time,end_time):
    func_api="/openapi/v1/analysis_tools/"+device_sn+"/count"
    params={
        "start_time":start_time,
        "end_time":end_time,
    }
    res=http_get(func_api, 'GET',params)
    res = json.loads(res)
    print(res)
    print(res['data'])

#去重总客流量查询
def person_count_distinct(space_id,device_sns,start_time,end_time):
    func_api="/openapi/v1/analysis_tools/"+space_id+"/person_count"
    params={
        "start_time":start_time,
        "end_time":end_time,
        "filter_whitelist":"true",
        # "cycle":"hour",
        # "only_capture":"true",
        # "device_sns":device_sns,
    }
    res=http_get(func_api, 'GET',params)
    res = json.loads(res)
    print(res)
    print(res['data'])

#查询到店记录
def visitors(device_sn,start_time,end_time):
    func_api="/openapi/v1/analysis_tools/"+device_sn+"/visitors"
    params={
        "start_time":start_time,
        "end_time":end_time,
    }
    res=http_get(func_api, 'GET',params)
    res = json.loads(res)
    # print(res)
    print(res['data'])

#到店记录订阅
def subscription(topic_name,topic_id,client_id):
    func_api = "/openapi/v1/analysis_tools/visitors/sub"
    body = {
        "topic_name":topic_name,
        "topic_id":topic_id,
        "client_id":client_id
    }
    print(body)
    res = http_put(func_api, 'PUT', body)
    res = json.loads(res)
    print(res)
    print(res['data'])

    #{'subscription_id': '8cef6b9f-c95c-11e9-907c-0a58c0a80e02'


#取消到店记录订阅
def del_subscription_id(subscription_id):
    func_api = "/openapi/v1/analysis_tools/visitors/sub/"+subscription_id
    res = http_delete(func_api, 'DELETE')
    res = json.loads(res)
    print(res)
    print(res['data'])

#到店记录的实时推送
# ws_sample(client_id="")



if __name__ == '__main__':

    #人脸库接口
    # create_facesets("smart4s", "smart4s-customer", "customer")
    # faceset_list()
    # del_facesets("5d5fa209ba18560008ba77d6")
    # update_facesets("5d6db70c4e7f1d0008910d5a","cig_test_update", "cig test update faceset", "test")
    # info_faceset("5d65d05cba18560008ba7859")

    #人脸用户管理
    # registered_user("5d5ce700ba18560008ba7789", 1,"/home/hensel/Desktop/horizon/测试接口/2.jpeg",18", "male")
    # user_list("5d65d05cba18560008ba7859")
    # del_user("5d5e078cba18560008ba77b7","5d5f671aba18560008ba77d2")
    # update_user("5d5ce700ba18560008ba7789","5d5dfded9c81530008b17d0f")
    # user_info("5d65d05cba18560008ba7859","5d6e41004e01730008a8b449")
    # user_append_img("5d5e078cba18560008ba77b7",'5d5f67b39c81530008b17d35',1,"/home/hensel/Desktop/horizon/测试接口/2.jpg" ,"18", "male")

    #人脸识别
    # detect_face(1,"/home/hensel/Desktop/horizon/测试接口/7.png")
    # extract_face(1,"/home/hensel/Desktop/horizon/测试接口/7.png")
    # match_face("/home/hensel/Desktop/1.jpeg","/home/hensel/Desktop/2.jpeg")
    # search_face("/home/hensel/Desktop/7.png",["5d5ce700ba18560008ba7789","5d5e078cba18560008ba77b7"])

    #智慧商业客流分析
    # user_face("a55dfe635d4bf67a2f1b487d_NHcXY2YV")
    # faceset_space(["a55dfe635d4bf67a2f1b487d_NHcXY2YV"],["5d5ce700ba18560008ba7789"])
    # count_person("0691A001100112638L","2019-08-22T13:02:16+08:00","2019-08-22T14:00:16+08:00")
    # person_count_distinct("a55dfe635d4bf67a2f1b487d_NHcXY2YV", [], "2019-09-02T14:42:16+08:00","2019-09-02T14:50:16+08:00")
    # visitors("0691A001100112638L","2019-08-23T10:00:16+08:00","2019-08-23T13:47:16+08:00")
    # subscription("device","0691A001100112638L","cig123")
    ws_sample("cig123")
    # del_subscription_id("47b2420b-c942-11e9-907c-0a58c0a80e02")
