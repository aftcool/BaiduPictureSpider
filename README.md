# BaiduPictureSpider
对于爬取百度图片，（ps:针对目前的瀑布式加载）,以关键字“piao bao ying” 为例：
![image](https://github.com/aftcool/BaiduPictureSpider/blob/master/BaiduImgSpider1.png)
由于目前百度图片是动态瀑布式加载，不是老式的分页式。故设计动态爬取..，但作为菜鸟，目前还没有了解！！QAQ
但是当每次动态加载，向后台发送加载信号，然后后台向前台传递一个JSON数据（其中包含了图片的URL），
所以只需要了解，每次的Request URL是否有规律即可...
接下来看网页分析（XHR：即动态加载ajax是请求的数据）：
![image](https://github.com/aftcool/BaiduPictureSpider/blob/master/BaiduImgSpider2.png)
其中的返回的两组Request URL：仅有一个变量是变化的，就是pn
![image](https://github.com/aftcool/BaiduPictureSpider/blob/master/Request01.png)
![image](https://github.com/aftcool/BaiduPictureSpider/blob/master/Request02.png)
辅助Request URL，网页访问，可以看到是一堆JSON数据：
![image](https://github.com/aftcool/BaiduPictureSpider/blob/master/BaiduImgSpider3.png)
（需要注意的是：图片的objRUL才是高清图片，但是百度采用了加密操作，但加密十分简单,容易解码，具体看代码！）
这个时候，应该就知道怎么爬取百度图片了。只需要通过JSON数据获取到每张图片的URL，即可保存到本地..
具体看代码！
