簡單的說RESTful架構就是：“每一個URI代表一種資源，客戶端通過四個HTTP動詞，對服務器端資源進行操作，實現資源的表現層狀態轉移”。

我們在設計Web應用時，如果需要向客戶端提供資源，就可以使用REST風格的URI，這是實現RESTful架構的第一步。當然，真正的RESTful架構並不只是URI符合REST風格，更為重要的是“無狀態”和“冪等性”兩個詞，我們在後面的課程中會為大家闡述這兩點。下面的例子給出了一些符合REST風格的URI，供大家在設計URI時參考。

##編寫序列化器
前後端分離的開發需要後端為前端、移動端提供API數據接口，而API接口通常情況下都是返回JSON格式的數據，這就需要對模型對象進行序列化處理。 DRF中封裝了Serializer類和ModelSerializer類用於實現序列化操作，通過繼承Serializer類或ModelSerializer類，我們可以自定義序列化器，用於將對象處理成字典，代碼如下所示。
"""
from rest_framework import serializers 


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = '__all__'
"""

##JWT概述
JSON Web Token通常簡稱為JWT，它是一種開放標準（RFC 7519）。隨著RESTful架構的流行，越來越多的項目使用JWT作為用戶身份認證的方式。 JWT相當於是三個JSON對象經過編碼後，用.分隔並組合到一起，這三個JSON對象分別是頭部（header）、載荷（payload）和簽名（signature）
1. 頭部
其中，alg屬性表示簽名的算法，默認是HMAC SHA256（簡寫成HS256）；typ屬性表示這個令牌的類型，JWT中都統一書寫為JWT。

2. 載荷

載荷部分用來存放實際需要傳遞的數據。 JWT官方文檔中規定了7個可選的字段：

-iss ：簽發人
-exp：過期時間
-sub：主題
-aud：受眾
-nbf：生效時間
-iat：簽發時間
-jti：編號