"""
HTML 是用來描述網頁的一種語言，全稱是 Hyper-Text Markup Language，即超文
本標記語言。我們瀏覽網頁時看到的文字、按鈕、圖片、視頻等元素，它們都是通過 HTML 書寫並通過瀏覽器來呈現的。
"""
#結構
"""
    html
        head
            title
            meta
        body
"""
#文本
"""
*標題（heading）和段落（paragraph）
    h1 ~ h6
    p
*上標（superscript）和下標（subscript）
sup
        sub
*空白（白色空間折疊）
*折行（break）和水平標尺（horizontal ruler）
    br
    hr
*語義化標籤
    加粗和強調 - strong
    引用 - blockquote
    縮寫詞和首字母縮寫詞 - abbr / acronym
    引文 - cite
    所有者聯繫信息 - address
    內容的修改 - ins / del
"""
#列表（list）
"""
*有序列表（ordered list）- ol / li
*無序列表（unordered list）- ul / li
*定義列表（definition list）- dl / dt / dd
"""
#鏈接（anchor）
"""
*頁面鏈接
*錨鏈接
*功能鏈接
"""
#圖像（image）
"""
*圖像存儲位置
"""

#面向对象
"""
*对象的概念
*创建对象的字面量语法
*访问成员运算符
*创建对象的构造函数语法
    this关键字
*添加和删除属性
    delete关键字
*标准对象
    Number / String / Boolean / Symbol / Array / Function
    Date / Error / Math / RegExp / Object / Map / Set
    JSON / Promise / Generator / Reflect / Proxy
"""

#BOM
"""
*window对象的属性和方法
*history对象
    forward() / back() / go()
*location对象
*navigator对象
*screen对象
"""
#DOM
"""
*DOM树
*访问元素
    getElementById() / querySelector()
    getElementsByClassName() / getElementsByTagName() / querySelectorAll()
    parentNode / previousSibling / nextSibling / children / firstChild / lastChild
*操作元素
    nodeValue
    innerHTML / textContent / createElement() / createTextNode() / appendChild() / insertBefore() / removeChild()
    className / id / hasAttribute() / getAttribute() / setAttribute() / removeAttribute()
*事件处理
    事件类型
        UI事件：load / unload / error / resize / scroll
        键盘事件：keydown / keyup / keypress
        鼠标事件：click / dbclick / mousedown / mouseup / mousemove / mouseover / mouseout
        焦点事件：focus / blur
        表单事件：input / change / submit / reset / cut / copy / paste / select
    事件绑定
        HTML事件处理程序（不推荐使用，因为要做到标签与代码分离）
        传统的DOM事件处理程序（只能附加一个回调函数）
        事件监听器（旧的浏览器中不被支持）
    事件流：事件捕获 / 事件冒泡
    事件对象（低版本IE中的window.event）
        target（有些浏览器使用srcElement）
        type
        cancelable
        preventDefault()
        stopPropagation()（低版本IE中的cancelBubble）
    鼠标事件 - 事件发生的位置
        屏幕位置：screenX和screenY
        页面位置：pageX和pageY
        客户端位置：clientX和clientY
    键盘事件 - 哪个键被按下了
        keyCode属性（有些浏览器使用which）
        String.fromCharCode(event.keyCode)
    HTML5事件
        DOMContentLoaded
        hashchange
        beforeunload
"""

#JavaScript API
"""
客户端存储 - localStorage和sessionStorage

localStorage.colorSetting = '#a4509b';
localStorage['colorSetting'] = '#a4509b';
localStorage.setItem('colorSetting', '#a4509b');
获取位置信息 - geolocation

navigator.geolocation.getCurrentPosition(function(pos) { 		  
    console.log(pos.coords.latitude)
    console.log(pos.coords.longitude)
})
从服务器获取数据 - Fetch API

绘制图形 - <canvas>的API

音视频 - <audio>和<video>的API
"""
