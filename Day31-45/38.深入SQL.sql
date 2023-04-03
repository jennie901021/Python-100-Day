#創建畫像標籤表。
create table `tb_tags`
(
`tag_id` int unsigned not null comment '標籤ID',
`tag_name` varchar(20) not null comment '標籤名',
primary key (`tag_id`)
) engine=innodb;

insert into `tb_tags` (`tag_id`, `tag_name`) 
values
    (1, '70後'),
    (2, '80後'),
    (3, '90後'),
    (4, '00後'),
    (5, '愛運動'),
    (6, '高學歷'),
    (7, '小資'),
    (8, '有房'),
    (9, '有車'),
    (10, '愛看電影'),
    (11, '愛網購'),
    (12, '常點外賣');

#查詢按月薪從高到低排在第4到第6名的員工的姓名和月薪。
select * from (
	select 
		`ename`, `sal`,
		row_number() over (order by `sal` desc) as `rank`
	from `tb_emp`
) `temp` where `rank` between 4 and 6;

#JSON類型
"""
很多開發者在使用關係型數據庫做數據持久化的時候，常常感到結構化的存儲缺乏靈活性，因為必須事先設計好所有的列以及對應的數據類型。
在業務發展和變化的過程中，如果需要修改表結構，這絕對是比較麻煩和難受的事情。從 MySQL 5.7 版本開始，MySQL引入了對 JSON 數據類型的支持（MySQL 8.0 解決了 JSON 的日誌性能瓶頸問題）
，用好 JSON 類型，其實就是打破了關係型數據庫和非關係型數據庫之間的界限，為數據持久化操作帶來了更多的便捷。
JSON 類型主要分為 JSON 對象和 JSON數組兩種，如下所示。
"""
#JSON 對象
{"name": "駱昊", "tel": "13122335566", "QQ": "957658"}
#JSON 數組
[1, 2, 3]
[{"name": "駱昊", "tel": "13122335566"}, {"name": "王大錘", "QQ": "123456"}]