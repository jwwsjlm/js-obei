import requests
import re
import grpc
import obei_pb2
import obei_pb2_grpc
import urllib3
urllib3.disable_warnings()
channel = grpc.insecure_channel('localhost:50051')
stub = obei_pb2_grpc.GreeterStub(channel)

def run(str, cookie):
    response = stub.obeiHKIIUU9O618PPTHPM(obei_pb2.jsStr(jscode=str, cookie=cookie))
    return response.message

def get_html():
    import requests

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://qiye.obei.com.cn/web-zone/bwzy/procurement.html',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://qiye.obei.com.cn/web-zone/bwzy/procurement.html', headers=headers, verify=False)
    return response

def getHkJs(urlsrt):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
       'Pragma': 'no-cache',
        'Referer': 'https://qiye.obei.com.cn/web-zone/bwzy/procurement.html',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(urlsrt, headers=headers, verify=False)
    return response


def get_js(urlstr):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://qiye.obei.com.cn/web-zone/bwzy/procurement.html',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get(urlstr, headers=headers, verify=False)
    return response


def postPurchaseList(urlstr, HPM, HKM, csrfToken):
    cookies = {
        'HKIIUU9O618PPTHPM': HPM,
        'HKIIUU9O618PPTHKM': HKM,
        'csrfToken': csrfToken
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
         'Origin': 'https://qiye.obei.com.cn',
        'Pragma': 'no-cache',
        'Referer': 'https://qiye.obei.com.cn/web-zone/bwzy/procurement.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-csrf-token': csrfToken,
    }
    json_data = {
        'code': 'bwzy',
        'noticeType': '1',
        'pageNum': 1,
        'pageSize': 10,
        'pageFlag': 'addSelect',
        'sidx': 'issueDate',
        'sord': 'desc',
    }

    response = requests.post(urlstr, cookies=cookies, headers=headers, verify=False, json=json_data)
    return response


def postProcurement(urlstr, HPM, HKM):
    cookies = {
        'HKIIUU9O618PPTHKM': HKM,
        'HKIIUU9O618PPTHPM': HPM
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
            'Pragma': 'no-cache',
        'Referer': 'https://qiye.obei.com.cn/web-zone/bwzy/procurement.html',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(urlstr, cookies=cookies, headers=headers,verify=False)
    return response


def run_js_HKIIUU(js_str, js_cookie):

    ret = run(js_str, js_cookie)
    return ret


def regex_match(pattern, string):
    matches = re.findall(pattern, string)
    return matches


def main():
    # 获取HTML文本
    response = get_html()
    html = response.text

    # 使用正则表达式匹配HTML文本中的资源链接
    pattern = r'src="([^"]*)"'
    matches = regex_match(pattern, html)

    # 拼接完整URL地址
    urlstr = "https://qiye.obei.com.cn" + matches[0]
    print(urlstr)

    # 访问目标URL并获取JavaScript代码
    html = get_js(urlstr).text

    # 通过正则表达式匹配JavaScript代码中的部分内容，并拼接为新的URL
    mcopssurl = 'https://qiye.obei.com.cn/Mcopss6d6w6EWERuu.js?' + regex_match(r"\.js\?(.*?)';", html)[0]
    # 访问上述URL，并获取响应的cookies
    mcopssret = getHkJs(mcopssurl)
    # 提取cookies中的HKIIUU9O618PPTHPM和HKIIUU9O618PPTHKM字段
    HKIIUU9O618PPTHPM = mcopssret.cookies.get("HKIIUU9O618PPTHPM")
    HKIIUU9O618PPTHKM = mcopssret.cookies.get("HKIIUU9O618PPTHKM")
    print('HKIIUU9O618PPTHKM', HKIIUU9O618PPTHKM)

    # 运行一段JavaScript代码
    ret = run_js_HKIIUU(HKIIUU9O618PPTHKM, "un")
    print("HKIIUU9O618PPTHPM", ret)

    # POST请求一个URL并获取csrfToken
    Procurement = postProcurement('https://qiye.obei.com.cn/web-zone/bwzy/procurement.html', HPM=ret,
                                  HKM=HKIIUU9O618PPTHKM)
    csrfToken = Procurement.cookies.get("csrfToken")
    print('csrfToken', csrfToken)

    # 再次运行JavaScript代码
    ret = run_js_HKIIUU(HKIIUU9O618PPTHKM, "post")

    # POST请求一个URL并获取回应的文本
    mcopssCookie = postPurchaseList('https://qiye.obei.com.cn/web-zone/api/sys/zone/getPurchaseList',
                                    HKM=HKIIUU9O618PPTHKM, HPM=ret, csrfToken=csrfToken)
    print(mcopssCookie.text)



if __name__ == "__main__":
    main()
