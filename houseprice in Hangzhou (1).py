#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests 
import re
import time
import random 
import pandas as pd

def web_url(i):
    web_url='https://hangzhou.anjuke.com/sale/xihu/p%s/#filtersort' %i
    req_header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36','referer': 'https://hangzhou.anjuke.com/sale/?from=navigation','cookie':'aQQ_ajkguid=0451D7D2-ABA0-045C-84A2-1130B026E80B; 58tj_uuid=53758a3e-c239-42ec-acde-dd1c1b7b9e25; als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1558431735; ctid=18; _ga=GA1.2.195202587.1560255209; wmda_uuid=cfae28865505ea8cc5438796992617bb; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; sessid=B5BEDABE-E477-E75F-0393-F70BCB75877E; lps=http%3A%2F%2Fhangzhou.anjuke.com%2Fsale%2F%3Fpi%3Dbaidu-cpc-hz-shantou-sp%26kwid%3D105976943222%7Chttps%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K00000KbUiqGbb95an2eGCUtmYYqiuCCUq8dSPNFd4gVaVajsdtNvC4Vgl8ld_uDbR6b0BL7H5vEf_ICUBkdJa1jFUlqCO586S2wzPv0jv-VZJAm7vvh16xjEbWKw0ExMSp96QH6eeCdNLc7hGkeDnjTelaxCRuvVq4M0_nP-0IEPUJVsVplQe26cpwg1mLfOV9cMuiVuoi89Mg2hf.Db_NR2Ar5Od66Ju1TPH_Zb17-sIJRfw_YRsItUvQvTyj5jW91dTrXrGh26eKMWkqXL6knNvUVOWYeS1Wbzu7PHV2XgZJyAp7BEukzUd0.U1Yk0ZDq8o1yLUXOEP_0TA-W5HD0IjvlEPUIVeStvsKGUHYznWR0u1dEugK1nfKdpHdBmy-bIfKspyfqnHb0mv-b5HRd0AdY5HDknjcsg1DsnH-xnH0kPdtknjD1g1nvnjD0pvbqnfKzIjYkPWD0uy-b5HcvPHc1g1DYnWuxnWDsrjKxnWbkn1NxnWbzn1IxnW6dnH9xnWbsrH-xnWbkn17xnWb1PW-xnW63n1uxnWbznW7xnWbsP1c0mhbqnW0Yg1Ddr0KVm1Y1n7tknj0kg1D3nWRkP16sP17xn10vPjD3P1DYr7ts0Z7spyfqn1c0TyPGujYzrj00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn1f3nHcYrHc0UMus5H08nj0snj0snj00Ugws5H00uAwETjYk0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKGuAnqiDFK0ZwdT1YkPjmdPW0knW61rjb1nWn4nWnvP6Kzug7Y5HDdPWD1n1D1PWRzPWb0Tv-b5yfvmhnzuj-9nj0LnWbzPH00mLPV5HfLP1FDPjfkfHm1rRRvwWD0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn7ts0ZK9I7qhUA7M5Hn0uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KsmgF9Uh_qn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0snans0APzm1YdP1Rzrf%26word%3D%25E6%259D%25AD%25E5%25B7%259E%25E6%2588%25BF%25E4%25BB%25B7%26ck%3D8316.2.103.497.178.538.168.1707%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.307.0%26bc%3D110101; twe=2; wmda_session_id_6289197098934=1561331377126-bb7c3e18-1dcf-77e9; init_refer=https%253A%252F%252Fwww.baidu.com%252Fbaidu.php%253Fsc.K00000KbUiqGbb95an2eGCUtmYYqiuCCUq8dSPNFd4gVaVajsdtNvC4Vgl8ld_uDbR6b0BL7H5vEf_ICUBkdJa1jFUlqCO586S2wzPv0jv-VZJAm7vvh16xjEbWKw0ExMSp96QH6eeCdNLc7hGkeDnjTelaxCRuvVq4M0_nP-0IEPUJVsVplQe26cpwg1mLfOV9cMuiVuoi89Mg2hf.Db_NR2Ar5Od66Ju1TPH_Zb17-sIJRfw_YRsItUvQvTyj5jW91dTrXrGh26eKMWkqXL6knNvUVOWYeS1Wbzu7PHV2XgZJyAp7BEukzUd0.U1Yk0ZDq8o1yLUXOEP_0TA-W5HD0IjvlEPUIVeStvsKGUHYznWR0u1dEugK1nfKdpHdBmy-bIfKspyfqnHb0mv-b5HRd0AdY5HDknjcsg1DsnH-xnH0kPdtknjD1g1nvnjD0pvbqnfKzIjYkPWD0uy-b5HcvPHc1g1DYnWuxnWDsrjKxnWbkn1NxnWbzn1IxnW6dnH9xnWbsrH-xnWbkn17xnWb1PW-xnW63n1uxnWbznW7xnWbsP1c0mhbqnW0Yg1Ddr0KVm1Y1n7tknj0kg1D3nWRkP16sP17xn10vPjD3P1DYr7ts0Z7spyfqn1c0TyPGujYzrj00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn1f3nHcYrHc0UMus5H08nj0snj0snj00Ugws5H00uAwETjYk0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKGuAnqiDFK0ZwdT1YkPjmdPW0knW61rjb1nWn4nWnvP6Kzug7Y5HDdPWD1n1D1PWRzPWb0Tv-b5yfvmhnzuj-9nj0LnWbzPH00mLPV5HfLP1FDPjfkfHm1rRRvwWD0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn7ts0ZK9I7qhUA7M5Hn0uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KsmgF9Uh_qn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0snans0APzm1YdP1Rzrf%2526word%253D%2525E6%25259D%2525AD%2525E5%2525B7%25259E%2525E6%252588%2525BF%2525E4%2525BB%2525B7%2526ck%253D8316.2.103.497.178.538.168.1707%2526shh%253Dwww.baidu.com%2526sht%253Dbaiduhome_pg%2526us%253D1.0.1.0.1.307.0%2526bc%253D110101; new_uv=3; _gid=GA1.2.2038773126.1561331378; new_session=0; ajk_member_captcha=534c05078bd0611268307fa8ba92f139; browse_comm_ids=826608%7C160752; propertys=ssuzq6-ptkryk_stt5sj-ptkrep_; __xsptplus8=8.3.1561331377.1561332623.24%232%7Cwww.baidu.com%7C%7C%7C%25E6%259D%25AD%25E5%25B7%259E%25E6%2588%25BF%25E4%25BB%25B7%7C%23%23jDv1jRlQJMraurHt76h0Hnh5BjD5AQ9M%23'}
    web_page=requests.get(web_url,headers=req_header)
    web_page.encoding='utf8'
    text=web_page.text
    #print(web_url)
    return(text)


# In[101]:


from bs4 import BeautifulSoup
def get_house_infor(text):
    soup=BeautifulSoup(text,'lxml')
    houses=soup.select(".house-title a")
    total_dic = {}
    for i in range(0,60):
        time.sleep(3)
        url=houses[i]['href']
        #print(url)
        infor={}
        req_header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36','referer': 'https://hangzhou.anjuke.com/sale/?from=navigation','cookie':'aQQ_ajkguid=0451D7D2-ABA0-045C-84A2-1130B026E80B; 58tj_uuid=53758a3e-c239-42ec-acde-dd1c1b7b9e25; als=0; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1558431735; ctid=18; _ga=GA1.2.195202587.1560255209; wmda_uuid=cfae28865505ea8cc5438796992617bb; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; sessid=B5BEDABE-E477-E75F-0393-F70BCB75877E; lps=http%3A%2F%2Fhangzhou.anjuke.com%2Fsale%2F%3Fpi%3Dbaidu-cpc-hz-shantou-sp%26kwid%3D105976943222%7Chttps%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.K00000KbUiqGbb95an2eGCUtmYYqiuCCUq8dSPNFd4gVaVajsdtNvC4Vgl8ld_uDbR6b0BL7H5vEf_ICUBkdJa1jFUlqCO586S2wzPv0jv-VZJAm7vvh16xjEbWKw0ExMSp96QH6eeCdNLc7hGkeDnjTelaxCRuvVq4M0_nP-0IEPUJVsVplQe26cpwg1mLfOV9cMuiVuoi89Mg2hf.Db_NR2Ar5Od66Ju1TPH_Zb17-sIJRfw_YRsItUvQvTyj5jW91dTrXrGh26eKMWkqXL6knNvUVOWYeS1Wbzu7PHV2XgZJyAp7BEukzUd0.U1Yk0ZDq8o1yLUXOEP_0TA-W5HD0IjvlEPUIVeStvsKGUHYznWR0u1dEugK1nfKdpHdBmy-bIfKspyfqnHb0mv-b5HRd0AdY5HDknjcsg1DsnH-xnH0kPdtknjD1g1nvnjD0pvbqnfKzIjYkPWD0uy-b5HcvPHc1g1DYnWuxnWDsrjKxnWbkn1NxnWbzn1IxnW6dnH9xnWbsrH-xnWbkn17xnWb1PW-xnW63n1uxnWbznW7xnWbsP1c0mhbqnW0Yg1Ddr0KVm1Y1n7tknj0kg1D3nWRkP16sP17xn10vPjD3P1DYr7ts0Z7spyfqn1c0TyPGujYzrj00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn1f3nHcYrHc0UMus5H08nj0snj0snj00Ugws5H00uAwETjYk0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKGuAnqiDFK0ZwdT1YkPjmdPW0knW61rjb1nWn4nWnvP6Kzug7Y5HDdPWD1n1D1PWRzPWb0Tv-b5yfvmhnzuj-9nj0LnWbzPH00mLPV5HfLP1FDPjfkfHm1rRRvwWD0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn7ts0ZK9I7qhUA7M5Hn0uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KsmgF9Uh_qn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0snans0APzm1YdP1Rzrf%26word%3D%25E6%259D%25AD%25E5%25B7%259E%25E6%2588%25BF%25E4%25BB%25B7%26ck%3D8316.2.103.497.178.538.168.1707%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.307.0%26bc%3D110101; twe=2; wmda_session_id_6289197098934=1561331377126-bb7c3e18-1dcf-77e9; init_refer=https%253A%252F%252Fwww.baidu.com%252Fbaidu.php%253Fsc.K00000KbUiqGbb95an2eGCUtmYYqiuCCUq8dSPNFd4gVaVajsdtNvC4Vgl8ld_uDbR6b0BL7H5vEf_ICUBkdJa1jFUlqCO586S2wzPv0jv-VZJAm7vvh16xjEbWKw0ExMSp96QH6eeCdNLc7hGkeDnjTelaxCRuvVq4M0_nP-0IEPUJVsVplQe26cpwg1mLfOV9cMuiVuoi89Mg2hf.Db_NR2Ar5Od66Ju1TPH_Zb17-sIJRfw_YRsItUvQvTyj5jW91dTrXrGh26eKMWkqXL6knNvUVOWYeS1Wbzu7PHV2XgZJyAp7BEukzUd0.U1Yk0ZDq8o1yLUXOEP_0TA-W5HD0IjvlEPUIVeStvsKGUHYznWR0u1dEugK1nfKdpHdBmy-bIfKspyfqnHb0mv-b5HRd0AdY5HDknjcsg1DsnH-xnH0kPdtknjD1g1nvnjD0pvbqnfKzIjYkPWD0uy-b5HcvPHc1g1DYnWuxnWDsrjKxnWbkn1NxnWbzn1IxnW6dnH9xnWbsrH-xnWbkn17xnWb1PW-xnW63n1uxnWbznW7xnWbsP1c0mhbqnW0Yg1Ddr0KVm1Y1n7tknj0kg1D3nWRkP16sP17xn10vPjD3P1DYr7ts0Z7spyfqn1c0TyPGujYzrj00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn1f3nHcYrHc0UMus5H08nj0snj0snj00Ugws5H00uAwETjYk0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKGuAnqiDFK0ZwdT1YkPjmdPW0knW61rjb1nWn4nWnvP6Kzug7Y5HDdPWD1n1D1PWRzPWb0Tv-b5yfvmhnzuj-9nj0LnWbzPH00mLPV5HfLP1FDPjfkfHm1rRRvwWD0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1Kxn7ts0ZK9I7qhUA7M5Hn0uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KsmgF9Uh_qn0KEIjYs0AqzTZfqnanscznsc10WnansQW0snj0snans0APzm1YdP1Rzrf%2526word%253D%2525E6%25259D%2525AD%2525E5%2525B7%25259E%2525E6%252588%2525BF%2525E4%2525BB%2525B7%2526ck%253D8316.2.103.497.178.538.168.1707%2526shh%253Dwww.baidu.com%2526sht%253Dbaiduhome_pg%2526us%253D1.0.1.0.1.307.0%2526bc%253D110101; new_uv=3; _gid=GA1.2.2038773126.1561331378; new_session=0; ajk_member_captcha=534c05078bd0611268307fa8ba92f139; browse_comm_ids=826608%7C160752; propertys=ssuzq6-ptkryk_stt5sj-ptkrep_; __xsptplus8=8.3.1561331377.1561332623.24%232%7Cwww.baidu.com%7C%7C%7C%25E6%259D%25AD%25E5%25B7%259E%25E6%2588%25BF%25E4%25BB%25B7%7C%23%23jDv1jRlQJMraurHt76h0Hnh5BjD5AQ9M%23'}
        details=requests.get(url,headers=req_header).text
        soup2=BeautifulSoup(details,'lxml')
        house_infor=soup2.select(".houseInfoBox .houseInfo-detail-item")
        #print(house_infor)
        zongjia=soup2.select(".houseInfo")
        for everyprice in zongjia:
            zongjia1=everyprice.text.strip().split('\n')
            zongjiafinal=str(zongjia1[2]).strip()
            infor['总价']=zongjiafinal
        for everyhouse in house_infor:
            temp=everyhouse.text.strip().split('\n')
            if temp[0] =='参考月供 ':
                continue
            #print(temp[0],temp[1:])
            for one_item in temp[1:]:
                one_item=one_item.strip()
                if  not one_item:
                    continue
         
                infor[temp[0]]=one_item
            

    
        for key, value in infor.items():
            if not total_dic.get(key):
                total_dic[key] = [value]
            else:
                total_dic[key].append(value)
    
    #print(total_dic)
    xiaoqu=total_dic.get('所属小区：')
    singleprice=total_dic.get('房屋单价：')
    #print(xiaoqu)

    newsingleprice_list=[]
    for j in singleprice:
        newsingleprice=j.strip('元/m²')
        newsingleprice_list.append(newsingleprice)
    #print(newsingleprice_list)
    
    return(xiaoqu,newsingleprice_list)

    


# In[3]:


import csv 
def main():
    csv_list1=[]
    csv_list2=[]
    for i in range (1,11):
        text=web_url(i)
        return_data=get_house_infor(text)
        xiaoqu=return_data[0]
        csv_list1.append(xiaoqu)
        newsingleprice_list=return_data[1]
        csv_list2.append(newsingleprice_list)

    df1=pd.DataFrame(csv_list1)
    df1.to_csv('test1.csv')
    df2=pd.DataFrame(csv_list2)
    df2.to_csv('test2.csv')
    



# In[4]:


if __name__=='__main__':
    main()


# In[90]:


mingcheng_totallist=[]
danjia_totallist=[]
zidian=[]
f1=open('test1.csv','r',encoding='utf-8')
csvreader1=csv.reader(f1)
for mingcheng in csvreader1:
    mingcheng_totallist.append(mingcheng[1:])
#print(mingcheng_totallist[1])
    
f2=open('test2.csv','r',encoding='utf-8')
csvreader2=csv.reader(f2)
for danjia in csvreader2:
    danjia_totallist.append(danjia[1:])
print(len(danjia_totallist[1]))

key=mingcheng_totallist[1]
value=danjia_totallist[1]
print(key)
print(value)
for i in range(0,60):
    zidian.append((key[i],value[i]))
#print(zidian)
paixu=sorted(zidian,key=lambda x:x[1],reverse=False)
#print(paixu[0:10])
final_list=paixu[0:10]
#print(final_list)

finalx=[]
finaly=[]
for j in final_list:
    finalx.append(j[0])
    finaly.append(j[1])
print(finalx,finaly)


# In[85]:


from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
bar = (
    Bar()
    .add_xaxis(finalx)
    .add_yaxis("单价",finaly)
    .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
            title_opts=opts.TitleOpts(title="房屋单价"),
            yaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(formatter="{value} /元/m²"))
            )
       )

bar.render()

