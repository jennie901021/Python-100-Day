#基本mySQL知識
"""
我們通常可以將 SQL 分為四類，分別是 DDL（數據定義語言）、DML（數據操作語言）、DQL（數據查詢語言）和 DCL（數據控制語言）。 DDL 主要用於創建、刪除、修改數據庫中的對象，比如創建、刪除和修改二維表，核心的
關鍵字包括create、drop和alter；DML 主要負責數據的插入、刪除和更新，關鍵詞包括insert、delete和update；DQL 負
責數據查詢，最重要的一個關鍵詞是select；DCL 通常用於授予和召回權限，核心關鍵詞是grant和revoke。
"""
"""
1. MySQL目前的版本不支持全外連接，上面我們通過union操作，將左外連接和右外連接的結果求並集實現全外連接的效果。大家可以通過下面的圖來加深對連表操作的認識。
2. MySQL 中支持多種類型的運算符，包括：算術運算符（+、-、*、/、%）、比較運算符（=、<>、<=>、<、<=、>、>=、BETWEEN...AND...、IN、IS NULL、IS NOT NULL、LIKE、RLIKE、REGEXP）、
  邏輯運算符（NOT、AND、OR、XOR）和位運算符（&、|、^、~、>>、<<），我們可以在 DML 中使用這些運算符處理數據。
3. 在查詢數據時，可以在SELECT語句及其子句（如WHERE子句、ORDER BY子句、HAVING子句等）中使用函數，這些函數包括字符串函數、數值函數、時間日期函數、流程函數等，如下面的表格所示。
"""
#執行指令
"""
1. select_type：查詢的類型。
    SIMPLE：簡單 SELECT，不需要使用 UNION 操作或子查詢。
    PRIMARY：如果查詢包含子查詢，最外層的 SELECT 被標記為 PRIMARY。
    UNION：UNION 操作中第二個或後面的 SELECT 語句。
    SUBQUERY：子查詢中的第一個 SELECT。
    DERIVED：派生表的 SELECT 子查詢。
2. table：查詢對應的表。
3. type：MySQL 在表中找到滿足條件的行的方式，也稱為訪問類型，包括：ALL（全表掃描）、index（索引全掃描，只遍歷索引樹）、range（索引範
   圍掃描）、ref（非唯一索引掃描）、eq_ref（唯一索引掃描）、const / system（常量級查詢）、NULL（不需要訪問表或索引）。在所有的訪問類型中，很顯然 ALL 是性能最差的，它代表的全表掃描是指要掃描表中的每一行才能找到匹配的行。
4. possible_keys：MySQL 可以選擇的索引，但是有可能不會使用。
5. key：MySQL 真正使用的索引，如果為NULL就表示沒有使用索引。
6. key_len：使用的索引的長度，在不影響查詢的情況下肯定是長度越短越好。
7. rows：執行查詢需要掃描的行數，這是一個預估值。
8. extra：關於查詢額外的信息。
    Using filesort：MySQL 無法利用索引完成排序操作。
    Using index：只使用索引的信息而不需要進一步查表來獲取更多的信息。
    Using temporary：MySQL 需要使用臨時表來存儲結果集，常用於分組和排序。
    Impossible where：where子句會導致沒有符合條件的行。
    Distinct：MySQL 發現第一個匹配行後，停止為當前的行組合搜索更多的行。
    Using where：查詢的列未被索引覆蓋，篩選條件並不是索引的前導列。
"""