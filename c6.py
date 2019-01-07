# 使用原生爬虫爬取电子书信息， 每一本书的信息都需要爬取，
# 包括书名、作者、内容简介...等。
# 参考地址：http://d81fb43e-d.parkone.cn/
import re
from urllib import request

class Spider():
    url = 'http://d81fb43e-d.parkone.cn/page/'
    url1 = 'http://d81fb43e-d.parkone.cn'
    #所有a链接到书的详细信息的父页面
    root_patternn = '<div class="cover">([\s\S]*?)</div>'
    #所有a链接到书的详细信息的后缀
    root_pattern1 = '<a href="([\s\S]*?)" data-toggle="modal" data-target="#bookDetailsModal" data-remote="false">'
    #书名正则
    bname = '<h2>([\s\S]*?)</h2>'
     #作者正则
    root_pattern2 = '<a href="/author/.*"([\s\S]*?)</a>'
    #出版社正则
    root_pattern3 = '<span>出版社:([\s\S]*?)</span>'
    #出版日期正则
    root_pattern4 = '<p>出版日期([\s\S]*?)</p>'
    #简介正则
    root_pattern5 = '<p class="description">([\s\S]*?)</p>'
    
    
    
    def fetch_content(self,surl):
        r = request.urlopen(surl)
        htmls = r.read()
        htmls = str(htmls,encoding='utf-8')
        return htmls

        
        
    
    
    def analysis(self):
        #j表示page后的序号
        j = 1
        #j从1开始每次加1,当url/j的书的正则(root_patternn)能匹配上(长度大于零)就一直循环
        while(len(re.findall(Spider.root_patternn,self.fetch_content(Spider.url+str(j))))>0):
            #url/j返回的html
            html = self.fetch_content(Spider.url+str(j))
            #匹配书的详细信息a链接的上一层<div class="cover">html页面为root
            root = re.findall(Spider.root_patternn,html)
            for i in root:
                #匹配找出书的详细信息a链接后面的字符串，并拼成一个新的url
                a = re.findall(Spider.root_pattern1,i)
                url1 = Spider.url1+str(a[0])
                b = self.fetch_content(url1)
                a1 = re.findall(Spider.bname,b)#书名
                a2 = re.findall(Spider.root_pattern2,b)#作者
                a3 = re.findall(Spider.root_pattern3,b)#出版社
                a4 = re.findall(Spider.root_pattern4,b)#出版日期
                a5 = re.findall(Spider.root_pattern5,b)#简介
                print('书名',a1,'作者',a2,'出版社',a3,'日期',a4,'简介',a5)
            j = j + 1   
            
            

splider = Spider()
splider.analysis()
    



        
       
        
        
            
            
            
            
            
            
               
                
                
               
            
           
                
                 

 
           
            
           
          
    
       
        
           
            

             
    

    
            


           
            
    
   
        

        

        


        
        
    
    
        
       
        
       
        
    

        
        
        
    
            

    
            
        
        

        

       
        
        
            



        
        
       
        
        


