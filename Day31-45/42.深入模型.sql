#使用ORM完成模型的CRUD操作
"""
有了Django框架的ORM，我們可以直接使用面向對象的方式來實現對數據的CRUD（增刪改查）操作。我們可以在PyCharm的終端中輸入下面的命令進入到Django項目的交互式環境，然後嘗試對模型的操作。
"""
python manage.py shell
#新增
from polls.models import Subject

subject1 = Subject(name='Python全棧開發', intro='當下最熱門的學科', is_hot=True)
subject1.save()
subject2 = Subject(name='全棧軟件測試', intro='學習自動化測試的學科', is_hot=False)
subject2.save()
subject3 = Subject(name='JavaEE分佈式開發', intro='基於Java語言的服務器應用開發', is_hot=True)
#刪除
subject = Subject.objects.get(no=2)
subject.delete()
#更新
subject = Subject.objects.get(no=1)
subject.name = 'Python全棧+人工智能'
subject.save()
#查詢
Subjects.objects.all()

#利用Django後台管理模型
"""
在創建好模型類之後，可以通過Django框架自帶的後台管理應用（admin應用）實現對模型的管理。雖然實際應用中，這個後
台可能並不能滿足我們的需求，但是在學習Django框架時，我們可以利用admin應用來管理我們的模型，同時也通過它來了解一個項目的後台管理系統需要哪些功能。
"""
#補充內容
"""
Django模型最佳實踐
1.正確的為模型和關係字段命名。
2.設置適當的related_name屬性。
3.用OneToOneField代替ForeignKeyField(unique=True)。
4.通過“遷移操作”（migrate）來添加模型。
5.用NoSQL來應對需要降低範式級別的場景。
6.如果布爾類型可以為空要使用NullBooleanField。
7.在模型中放置業務邏輯。
8.用<ModelName>.DoesNotExists取代ObjectDoesNotExists。
9.在數據庫中不要出現無效數據。
10.不要對QuerySet調用len()函數。
11.將QuerySet的exists()方法的返回值用於if條件。
12.用DecimalField來存儲貨幣相關數據而不是FloatField。
13.定義__str__方法。
14.不要將數據文件放在同一個目錄中。
"""