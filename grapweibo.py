# coding=utf-8
import requests
from urllib.parse import urlencode
from pyquery import PyQuery as pq
import tool;
import time;
timeString = time.time();
import sys

host = 'm.weibo.cn'
userid="1216826604"
refer = 'https://m.weibo.cn/u/%s'%(userid)
container_url = 'https://%s/api/container/getIndex?uid=%s&type=uid&value=%s' % (host,userid,userid)
base_url = 'https://%s/api/container/getIndex?type=uid' % host
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

headers = {
    'Host': host,
    'Referer': refer,
    'User-Agent': user_agent,
	'X-Requested-With': 'XMLHttpRequest'
}
async def getContainerID():
    try:
        response = requests.get(container_url, headers=headers)
        for i in response.json()['data']['tabsInfo']['tabs']:
            if i['tab_type'] == 'weibo':
                conId = i['containerid']
                return conId
    except requests.ConnectionError as e:
        print('抓取错误', e.args)
# time.sleep(3)

# 按页数抓取数据
def get_single_page(page,conId):
    params = {
        'display':0,
        'value':userid,
        'containerid': conId,
        'page': page
    }
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            time.sleep(1)
            return response.json();
    except requests.ConnectionError as e:
        print('抓取错误', e.args)

def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value
		
# 解析页面返回的json数据
def parse_page(json):
    data = json.get('data');
    if data:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            if item:
                data = {
                    'id': item.get('id'),
                    'text': "".join(pq(item.get("text")).text().split()),  # 仅提取内容中的文本
                    'attitudes': item.get('attitudes_count'),
                    'comments': item.get('comments_count'),
                    'reposts': item.get('reposts_count'),
                    '发布日期':item.get('created_at')
                }
                yield data
async def await_coroutine():
    containerID = await getContainerID()
    if __name__ == '__main__':
        objDic = {};
        i=0
        for page in range(1, 1000):  # 抓取的数据
            time.sleep(1)
            json1 = get_single_page(page,containerID)
            results = parse_page(json1)
            for result in results:
                i+=1
                objDic[i] = result
                # print(result)
    tool.saveDicToJson(objDic,'%sweibo.txt'%(timeString))
    
run(await_coroutine())
