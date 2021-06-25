import requests,json

headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
domain = 'https://zywxhd02.gxust.edu.cn'

def getRoomInfo(RoomID):
    url = '/Home/GetRoomInfo'
    postData = f'Yzm=123&RoomID={RoomID}'
    Data = requests.post(
        url = domain + url,
        data = postData,
        headers = headers
        )
    Data_json = json.loads(Data.json())
    # print(Data_json)
    return Data_json['component'][1]['Value']

def getRoomTree(roomDepID,level):
    url = '/Home/GetRoomTree'
    postData = f'yzm=123&RoomDepId={roomDepID}&level={level}'
    if level == 1:
        postData = 'yzm=123&Id=000&level=1'
    Data = requests.post(
        url = domain + url,
        headers = headers,
        data = postData
    )
    Data_json = json.loads(Data.json())
    # print(Data_json)
    return Data_json

def getRoomID():
    level = 1
    roomDepID = 1
    IDList = []
    RoomName = ''
    while level < 5:
        data = getRoomTree(roomDepID,level)
        for single in data['component']:
            singleRoomInfo = dict(ID = single['RoomDepId'],name = single['DepName'])
            IDList.append(singleRoomInfo)
            print(str(IDList.index(singleRoomInfo)) + '\t|\t' + singleRoomInfo['name'])
        selectIndex = int(input('Select:'))
        roomDepID = IDList[selectIndex]['ID']
        RoomName += (IDList[selectIndex]['name'] + '-')
        IDList.clear()
        level += 1
    RoomName = RoomName.rstrip('-')
    print(f'\nRoomName:{RoomName}')
    print(f'RoomID:{roomDepID}')
    return roomDepID

print(getRoomInfo(getRoomID()))