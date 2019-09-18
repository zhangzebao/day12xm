from selenium.webdriver.common.by import By

# 不更新
no_update = By.ID, "com.yunmall.lc:id/img_close"
# 我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 已有账号去登陆
exists_user = By.ID, "com.yunmall.lc:id/textView1"
# 用户名
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_password = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登陆按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 设置
setting_btn = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 消息推送
message_push = By.ID, "com.yunmall.lc:id/setting_notification"
# 修改密码
modify_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 退出
quit_btn = By.ID, "com.yunmall.lc:id/setting_logout"
# 确认退出
sure_quit = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

"""-----地址管理配置数据------"""
# 地址管理
address_menage = By.ID, "com.yunmall.lc:id/setting_address_manage"
# 新增地址
add_address = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 手机号
address_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 所在地区
address_province = By.ID, "com.yunmall.lc:id/address_province"
# 北京市
address_beijing = By.XPATH, "//*[contains(@text,'北京市')]"
# 第二次北京(普通点击方法)
double_beijing = By.XPATH, "//*[contains(@text,'北京市') and contains(@resource-id, 'com.yunmall.lc:id/area_title')]"
# 昌平区
address_chang_ping = By.XPATH, "//*[contains(@text,'昌平区')]"
# 详细地址
address_detail = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_post = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_send = By.ID, "com.yunmall.lc:id/button_send"
# 编辑
address_edit = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
# 修改(元素定位不到使用了坐标)
# address_modify = By.XPATH, "//*[contains(@text,'修改')]"
# 上海
address_shanghai = By.XPATH, "//*[contains(@text,'上海市')]"
# 长宁区
address_chang_ing = By.XPATH, "//*[contains(@text,'长宁区')]"
# 删除(元素定位不到使用了坐标)
address_delete = By.XPATH, "//*[contains(@text,'删除')]"
# 确认删除地址
sure_delete_address = By.ID, "com.yunmall.lc:id/ymdialog_left_button"

# 新增成功后收件人
add_name_phone = By.ID, "com.yunmall.lc:id/receipt_name"
# 新增成功后地址
"com.yunmall.lc:id/receipt_address"
