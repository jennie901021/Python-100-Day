#中間件是安插在Web應用請求和響應過程之間的組件，它在整個Web應用中扮演了攔截過濾器的角色，通過中間件可以攔截請求和響應，並對請求和響應進行過濾（簡單的說就是執行額外的處理）

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#
#中間件是安插在Web應用請求和響應過程之間的組件，它在整個Web應用中扮演了攔截過
濾器的角色，通過中間件可以攔截請求和響應，並對請求和響應進行過濾（簡單的說就是執行額外的處理）

"""
middlewares.py
"""
from django.http import JsonResponse
from django.shortcuts import redirect

# 需要登录才能访问的资源路径
LOGIN_REQUIRED_URLS = {'/praise/', '/criticize/', '/excel/', '/teachers_data/'}


def check_login_middleware(get_resp):

    def wrapper(request, *args, **kwargs):
        # 请求的资源路径在上面的集合中
        if request.path in LOGIN_REQUIRED_URLS:
            # 会话中包含userid则视为已经登录
            if 'userid' not in request.session:
                # 判断是不是Ajax请求
                if request.is_ajax():
                    # Ajax请求返回JSON数据提示用户登录
                    return JsonResponse({'code': 10003, 'hint': '请先登录'})
                else:
                    backurl = request.get_full_path()
                    # 非Ajax请求直接重定向到登录页
                    return redirect(f'/login/?backurl={backurl}')
        return get_resp(request, *args, **kwargs)

    return wrapper

1.CommonMiddleware - 基礎設置中間件，可以處理以下一些配置參數。
    DISALLOWED_USER_AGENTS - 不被允許的用戶代理（瀏覽器）
    APPEND_SLASH - 是否追加/
    USE_ETAG - 瀏覽器緩存相關
2.SecurityMiddleware - 安全相關中間件，可以處理和安全相關的配置項。
    SECURE_HSTS_SECONDS - 強制使用HTTPS的時間
    SECURE_HSTS_INCLUDE_SUBDOMAINS - HTTPS是否覆蓋子域名
    SECURE_CONTENT_TYPE_NOSNIFF - 是否允許瀏覽器推斷內容類型
    SECURE_BROWSER_XSS_FILTER - 是否啟用跨站腳本攻擊過濾器
    SECURE_SSL_REDIRECT - 是否重定向到HTTPS連接
    SECURE_REDIRECT_EXEMPT - 免除重定向到HTTPS
3.SessionMiddleware - 會話中間件。
4.CsrfViewMiddleware - 通過生成令牌，防範跨請求份偽的造中間件。
5.XFrameOptionsMiddleware - 通過設置請求頭參數，防範點擊劫持攻擊的中間件。