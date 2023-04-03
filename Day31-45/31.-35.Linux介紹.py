"""
1.獲取登錄信息 - w / who / last/ lastb
2.查看自己使用的Shell - ps
3.查看命令的說明和位置 - whatis / which / whereis
4.清除屏幕上顯示的內容 - clear
5.查看幫助文檔 - man / info / --help / apropos
6.查看系統和主機名 - uname / hostname
7.時間和日期 - date / cal
8.重啟和關機 - reboot / shutdown
9.出登錄 - exit / logout
10.查看歷史命令 - history
"""

#實用命令
"""
1. 創建/刪除空目錄 - mkdir / rmdir
2.創建/刪除文件 - touch / rm
    touch命令用於創建空白文件或修改文件時間。在Linux系統中一個文件有三種時間：
        更改內容的時間 - mtime。
        更改權限的時間 - ctime。
        最後訪問時間 - atime。
    rm的幾個重要參數：
        -i：交互式刪除，每個刪除項都會進行詢問。
        -r：刪除目錄並遞歸的刪除目錄中的文件和目錄。
        -f：強制刪除，忽略不存在的文件，沒有任何提示。
3.切換和查看當前工作目錄 - cd / pwd
4.查看目錄內容 - ls
        -l：以長格式查看文件和目錄。
        -a：顯示以點開頭的文件和目錄（隱藏文件）。
        -R：遇到目錄要進行遞歸展開（繼續列出目錄下面的文件和目錄）。
        -d：只列出目錄，不列出其他內容。
        -S / -t：按大小/時間排序。
5.查看文件內容 - cat / tac / head / tail / more / less / rev / od
6.拷貝/移動文件 - cp / mv
7.文件重命名 - rename
8.查找文件和查找內容 - find / grep
9.創建鏈接和查看鏈接 - ln / readlink
10.壓縮/解壓縮和歸檔/解歸檔 - gzip / gunzip / xz
11.歸檔和解歸檔 - tar
12.將標準輸入轉成命令行參數 - xargs
"""

#軟件安裝和配置
"""
使用包管理工具
1.yum - Yellowdog Updater Modified。
    yum search：搜索軟件包，例如yum search nginx。
    yum list installed：列出已經安裝的軟件包，例如yum list installed | grep zlib。
    yum install：安裝軟件包，例如yum install nginx。
    yum remove：刪除軟件包，例如yum remove nginx。
    yum update：更新軟件包，例如yum update可以更新所有軟件包，而yum update tar只會更新tar。
    yum check-update：檢查有哪些可以更新的軟件包。
    yum info：顯示軟件包的相關信息，例如yum info nginx。
2.rpm - Redhat Package Manager。
    安裝軟件包：rpm -ivh <packagename>.rpm。
    移除軟件包：rpm -e <packagename>。
    查詢軟件包：rpm -qa，例如可以用rpm -qa | grep mysql來檢查是否安裝了MySQL相關的軟件包。
    下面以Nginx為例，演示如何使用yum安裝軟件。
"""

#Shell編程
"""
之前我們提到過，Shell是一個連接用戶和操作系統的應用程序，它提供了人機交互的界面（接口），用戶通過這個界面訪問操作系
統內核的服務。 Shell腳本是一種為Shell編寫的腳本程序，我們可以通過Shell腳本來進行系統管理，同時也可以通過它進行文件操作。總之，編寫
Shell腳本對於使用Linux系統的人來說，應該是一項標配技能。
"""

