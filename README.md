amazon说明文档
==
介绍
 - 
amazon是一个基于Scrapy-Selenium的爬取amazon个人订单信息的爬虫。由于需要登陆，重写了一个登陆的下载器中间件来获取网页的set-cookie并重新组合成cookies给scrapy，这样就可以爬取需要登陆才能获取的页面了。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0<br>

### 依赖包
* Requests<br>
* Selenium 3.11.0

### 其它
* 主要采用了selenium的get_cookies()方法来获取网页cookie并提供给scrapy。这里采用了模拟浏览器的工具Selenium结合Scrapy框架爬取亚马逊个人账户里的订单信息，爬取的信息很少，仅仅做一个演示和验证功能的爬虫。

爬取结果
-
输出的cookie和订单信息如下截图:<br>
![订单详情截图](https://github.com/lanluyu/jingdong/blob/master/phone.PNG)
