# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os


class SfPipeline:
    #因为在open_spider中没有item选项，所以获取不到其中的item信息，无法灵活的切换文件以及文件夹
    #所以，在尝试简化代码方面就失去了意义

    def open_spider(self,spider):
        
        # check_file(item.book_Name)
        # self.f = open(f"{item.book_Name}/{item.chaper_name[0]}.txt","a",encoding = "utf-8")
        self.f = open("book.json","w",encoding = "utf-8")
        # self.f.write(per_name")[0].extract())

    def process_item(self, item, spider):

        # self.f.write("----------------------------------------------------------\n")
        # self.f.write(item.chaper_name[0] + "\n")
        # self.f.write("----------------------------------------------------------\n")
        # for i in item.chaper_text:
        #      self.f.write(i.extract() + "\n")

        return item
     
    def close_process(self,spider):
         self.f.close()
        #  print(f"{item.chaper_name}下载完成")

# def check_file(book_Name):
#         print("解析完成")
#         print("正在检查下载路径")
#         save_path = f".\{book_Name}"
#         if os.path.exists(save_path):
#             print("下载路径正常")
#         else:
#             print("下载路径失效")
#             print("开始创建新的下载路径" + save_path)
#             os.mkdir(save_path)
#             print("即将开始下载")