# -*- coding:utf-8 -*-


class ResourceId(object):
    IP = "192.168.1.122:5555"
    # 首页
    PACKAGE_NAME = "com.cvte.captain.mindlinker"                               # 包名
    MINDLINKER = "com.cvte.captain.mindlinker:id/serverConfigBackdoor"         # 左上角MindLinker字样
    CREATE_MEETING = "com.cvte.captain.mindlinker:id/createMeetingButton"      # 创建会议
    JOIN_MEETING = "com.cvte.captain.mindlinker:id/joinMeetingButton"          # 加入会议
    SCREEN_SHARE = "com.cvte.captain.mindlinker:id/createShareButton"          # 屏幕共享
    EXIT = "com.cvte.captain.mindlinker:id/exitImageButton"                    # 退出
    SERVICE = "com.cvte.captain.mindlinker:id/serviceImageButton"              # 服务
    MORE = "com.cvte.captain.mindlinker:id/moreImageButton"                    # 更多
    DEVICES_NAME = "com.cvte.captain.mindlinker:id/deviceNameTextView"         # 设备名称
    SETTING = "com.cvte.captain.mindlinker:id/settingTextView"                 # 更多里的设置按钮
    FEEDBACK = "com.cvte.captain.mindlinker:id/feedbackTextView"               # 更多里的反馈
    ABOUT = "com.cvte.captain.mindlinker:id/aboutTextView"                     # 更多里的关于
    FEEDBACK_QR = "com.cvte.captain.mindlinker:id/qrcodeImageView"             # 扫描反馈的二维码
    QR_CLOSE = "com.cvte.captain.mindlinker:id/closeButton"                    # 关闭按钮
    CONTACT = "com.cvte.captain.mindlinker:id/contactOpenLayout"               # 通讯录

    # 加入会议
    NUMBER_VIEW = "com.cvte.captain.mindlinker:id/number_input_view"           # 加入会议的整个窗口
    CLOSE_BUTTON = "com.cvte.captain.mindlinker:id/closeButton"                # 关闭按钮
    BLANK_BOX = "com.cvte.captain.mindlinker:id/emptyCodeTextView"             # 会议号输入框
    EDIT_BOX = "com.cvte.captain.mindlinker:id/inputCodeEditText"              # 已输入数字后的输入框
    LAST_CODE = "com.cvte.captain.mindlinker:id/lastCodeTextView"              # 历史会议号
    KEY_ONE = "com.cvte.captain.mindlinker:id/numberOne"                       # 数字键盘的1
    KEY_TWO = "com.cvte.captain.mindlinker:id/numberTwo"                       # 数字键盘的2
    KEY_THREE = "com.cvte.captain.mindlinker:id/numberThree"                   # 数字键盘的3
    KEY_FOUR = "com.cvte.captain.mindlinker:id/numberFour"                     # 数字键盘的4
    KEY_FIVE = "com.cvte.captain.mindlinker:id/numberFive"                     # 数字键盘的5
    KEY_SIX = "com.cvte.captain.mindlinker:id/numberSix"                       # 数字键盘的6
    KEY_SEVEN = "com.cvte.captain.mindlinker:id/numberSeven"                   # 数字键盘的7
    KEY_EIGHT = "com.cvte.captain.mindlinker:id/numberEight"                   # 数字键盘的8
    KEY_NINE = "com.cvte.captain.mindlinker:id/numberNine"                     # 数字键盘的9
    KEY_ZERO = "com.cvte.captain.mindlinker:id/numberZero"                     # 数字键盘的0
    KEY_CLEAR = "com.cvte.captain.mindlinker:id/clearNumber"                   # 数字键盘的清空
    KEY_DELETE = "com.cvte.captain.mindlinker:id/deleteNumber"                 # 数字键盘的清空
    KEY_CAMERA = "com.cvte.captain.mindlinker:id/cameraCheckBox"               # 关闭摄像头勾选框
    KEY_MIC = "com.cvte.captain.mindlinker:id/mircophoneCheckBox"              # 关闭麦克风勾选框
    KEY_CONFIRM = "com.cvte.captain.mindlinker:id/confirmButton"               # 确定按钮

    # 邀请码无效
    DIALOG_TEXT = "com.cvte.captain.mindlinker:id/dialog_content_textview"     # 邀请码无效
    DIALOG_IMAGE = "com.cvte.captain.mindlinker:id/dialog_icon_imageview"      # 感叹号
    DIALOG_CLOSED = "com.cvte.captain.mindlinker:id/dialog_close_imagebutton"  # 退出按钮

    # 会中状态
    SMART = "com.cvte.captain.mindlinker:id/bigVideoHostTip"                   # 主持人
    MEETING_ID = "com.cvte.captain.mindlinker:id/meetingIdTextView"            # 会议号
    MEETING_TIME = "com.cvte.captain.mindlinker:id/meetingDurationTextView"    # 会议时长
    SHARING_STATUS = "com.cvte.captain.mindlinker:id/screenPublishText"        # 共享状态/观看人数

    # 会中菜单栏
    MENU = "com.cvte.captain.mindlinker:id/container_bg"                       # 菜单页
    MEETING_MEMBER = "com.cvte.captain.mindlinker:id/meetingMemberText"        # 会议人数
    WINDOW_INVITOR = "com.cvte.captain.mindlinker:id/windowMeetingInvitor"     # 邀请按钮
    SCREEN_SHARE_LAYOUT = "com.cvte.captain.mindlinker:id/shareScreenLayout"   # 屏幕共享布局
    SCREEN_SHARE_IMAGE = "com.cvte.captain.mindlinker:id/shareScreenImageView" # 屏幕共享图片
    SCREEN_SHARE_TEXT = "com.cvte.captain.mindlinker:id/shareScreenText"       # 屏幕共享文字
    WHITEBOARD_LAYOUT = "com.cvte.captain.mindlinker:id/whiteboardLayout"      # 互动白板布局
    WHITEBOARD_IMAGE = "com.cvte.captain.mindlinker:id/whiteboardImageView"    # 互动白板图片
    WHITEBOARD_TEXT = "com.cvte.captain.mindlinker:id/whiteboardText"          # 互动白板文字
    HANGUP_LAYOUT = "com.cvte.captain.mindlinker:id/windowMeetingLeave"        # 离开按钮布局
    AUDIO_OPTION = "com.cvte.captain.mindlinker:id/windowAudioOption"          # 麦克风按钮布局
    AUDIO_IMAGE = "com.cvte.captain.mindlinker:id/windowAudioImageView"        # 麦克风按钮图片
    VIDEO_OPTION = "com.cvte.captain.mindlinker:id/windowVideoOption"          # 摄像头按钮布局
    VIDEO_IMAGE = "com.cvte.captain.mindlinker:id/windowVideoImageView"        # 摄像头按钮图片
    SETTING_WINDOW = "com.cvte.captain.mindlinker:id/windowSetting"            # 设置按钮布局
    ALERT_CENTER_BUTTON = "com.cvte.captain.mindlinker:id/alertCenterBtn"      # 结束会议按钮
    ALERT_CONFIRM_BUTTON = "com.cvte.captain.mindlinker:id/alertConfirmBtn"    # 离开会议按钮
    ALERT_CANCEL_BUTTON = "com.cvte.captain.mindlinker:id/alertCancelBtn"      # 取消按钮
    ALERT_TITLE = "com.cvte.captain.mindlinker:id/alertTitle"                  # 离开会议时的弹窗文案：离开还是结束
    ALERT_SUB_CONTENT = "com.cvte.captain.mindlinker:id/alertSubContent"       # 离开会议时的弹窗文案：指定主持人

    # 首页-设置
    TAB_VIDEO = "com.cvte.captain.mindlinker:id/setting_tab_video"             # 视频栏按钮
    TAB_AUDIO = "com.cvte.captain.mindlinker:id/setting_tab_audio"             # 音频栏按钮
    SETTING_CLOSE = "com.cvte.captain.mindlinker:id/closeButton"               # 设置关闭按钮
    VIDEO_PREVIEW = "com.cvte.captain.mindlinker:id/previewLayout"             # 视频预览画面
    VIDEO_CONFIG = "com.cvte.captain.mindlinker:id/videoConfigRootView"        # 整个视频配置页
    AUDIO_CONFIG = "com.cvte.captain.mindlinker:id/audioConfigRootView"        # 整个音频配置页
    ONLY_SELF = "com.cvte.captain.mindlinker:id/selfActiveCheckBox"            # 仅显示自己勾选项
    ONLY_TEXT = "com.cvte.captain.mindlinker:id/selfActiveTextView"            # 仅显示自己的文案
    CAMERA_OPTION = "com.cvte.captain.mindlinker:id/itemTextView"              # 仅显示自己的文案
    SPEAKER_CHECK = "com.cvte.captain.mindlinker:id/speakerLayout"             # 扬声器检测按钮
    MICROPHONE = "com.cvte.captain.mindlinker:id/microphoneImageView"          # 麦克风图标
    SPEAKER_TEXT = "com.cvte.captain.mindlinker:id/speakerHeaderTextView"      # 扬声器文案
    SPEAKER_DEVICE_TEXT = "com.cvte.captain.mindlinker:id/speaker_device"      # 扬声器设备文案
    MIC_DEVICE_TEXT = "com.cvte.captain.mindlinker:id/settingMicLayout"        # 麦克风设备文案

    # 首页-关于
    VERSION = "com.cvte.captain.mindlinker:id/versionTextView"                 # 版本号
    SDK = "com.cvte.captain.mindlinker:id/sdkTextView"                         # SDK
    CHECK_UPDATE = "com.cvte.captain.mindlinker:id/checkUpdateLayout"          # 检查更新
    DOWNLOAD = "com.cvte.captain.mindlinker:id/downloadTextView"               # 下载地址
    PRIVACY = "com.cvte.captain.mindlinker:id/privacyTextView"                 # 隐私政策
    PROTO = "com.cvte.captain.mindlinker:id/protocalTextView"                  # 用户协议
    ABOUT_CLOSE = "com.cvte.captain.mindlinker:id/closeButton"                 # 关于的关闭按钮

    # 服务
    SERVICE_MENU = "com.cvte.captain.mindlinker:id/deviceMenuLayout"           # 加入企业的按钮
    SERVICE_CLOSE = "com.cvte.captain.mindlinker:id/closeButton"               # 企业的弹窗
    STATUS_TITLE = "com.cvte.captain.mindlinker:id/deviceStatusTitle"          # 是否已加入企业的标题
    DEVICES_MANAGE = "com.cvte.captain.mindlinker:id/deviceContactManager"     # 请联系管理员的文案
    DEVICES_SN = "com.cvte.captain.mindlinker:id/deviceSN"                     # SN码
    JOIN_ENTERPRISE = "com.cvte.captain.mindlinker:id/deviceTextView"          # 加入企业的文案
    DEVICES_STATUS = "com.cvte.captain.mindlinker:id/deviceStatus"             # 设备是否已加入企业的状态
    ENTERPRISE_NAME = "com.cvte.captain.mindlinker:id/deviceCompanyName"       # 已加入企业的名称
    DOT = "com.cvte.captain.mindlinker:id/deviceStatusDot"                     # 未加入企业小红点

    # 通讯录
    CONTACT_NAME = "com.cvte.captain.mindlinker:id/contactName"                # 通讯录的设备名称
    CONTACT_CHECK_BOX = "com.cvte.captain.mindlinker:id/contactCheckBox"       # 设备名称的勾选框
    SELECT_TITLE = "com.cvte.captain.mindlinker:id/selectTitle"                # 已选的设备数量
    CONTACT_CANCEL = "com.cvte.captain.mindlinker:id/createCancelButton"       # 取消按钮
    CONFIG_BUTTON = "com.cvte.captain.mindlinker:id/createConfirmButton"       # 发起会议按钮,默认不可点击


class Text(object):
    CREATE = "发起会议"
    JOIN = "加入会议"
    SHARE = "屏幕共享"
    ADDRESS = "从通讯录邀请"
    EXIT = "退出"
    SERVICE = "服务"
    MORE = "更多"
    QR_JOIN_MEETING = "使用 MindLinker App 扫码入会"
    FEEDBACK_TXT = "扫码反馈"
    INVITATION_CODE = "邀请码"
    HANGUP = "离开"
    AUDIO = "麦克风"
    VIDEO = "摄像头"
    SETTING = "设置"
    FEEDBACK = "反馈"
    ABOUT = "关于"
    END_SHARING = "结束共享"
    CAMERA = "摄像头"
    PLEASE_USE = "请使用手机扫码提交您的反馈意见"
    RECOMMEND = "(推荐使用MindLinker App扫码)"
    MindLinker = "MindLinker"
    DOES_NOT_BELONG = "设备不属于该企业?"
    CLICK_FEEDBACK = "点击反馈"
    INVITE = "从通讯录邀请"


class Xpath(object):
    windowCode = 'com.cvte.captain.mindlinker:id/window_code_title'
    QR = '//*[@resource-id="com.cvte.captain.mindlinker:id/rightSideLayout"]' \
         '/android.widget.RelativeLayout[1]'
    HANGUP = '//*[@resource-id="com.cvte.captain.mindlinker:id/windowMeetingLeave"]' \
             '/android.widget.ImageView[1]'
    SETTING = '//*[@resource-id="com.cvte.captain.mindlinker:id/windowSetting"]' \
              '/android.widget.ImageView[1]'

    # 坐标请不要直接引用,直接输入
    RIGHT_SIDEBAR = '3790, 1756'                       # 右侧侧边栏坐标
    LEFT_SIDEBAR = '0, 1756'                          # 左侧侧边栏坐标
